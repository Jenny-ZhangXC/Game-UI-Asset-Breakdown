#!/usr/bin/env python3
"""Read-only PNG/manifest validation and optional ZIP delivery packaging."""
import argparse
import json
from pathlib import Path
import sys
import zipfile


def check(root):
    try:
        from PIL import Image
    except ImportError:
        raise ValueError('Pillow is required; use an available Python runtime with Pillow.')
    manifest = json.loads((root / 'manifest.json').read_text(encoding='utf-8'))
    assets = manifest.get('assets')
    if not isinstance(assets, list) or not assets:
        raise ValueError('manifest.assets must be a non-empty list')
    errors, seen, files = [], set(), set()
    for a in assets:
        try:
            for key in ('id', 'file', 'name', 'methods', 'transparent', 'width', 'height'):
                if key not in a:
                    raise ValueError('missing field ' + key)
            if not isinstance(a['id'], str) or not a['id'] or a['id'] in seen:
                raise ValueError('empty or duplicate id')
            seen.add(a['id'])
            rel = Path(a['file'])
            if rel.is_absolute() or '..' in rel.parts:
                raise ValueError('unsafe relative file path')
            path = (root / rel).resolve()
            if root not in path.parents or path in files:
                raise ValueError('external or duplicate file')
            files.add(path)
            if not a['methods'] or not isinstance(a['methods'], list) or any(
                m not in {'extracted', 'inpainted', 'reconstructed', 'new'} for m in a['methods']
            ):
                raise ValueError('invalid methods')
            if type(a['transparent']) is not bool:
                raise ValueError('transparent must be boolean')
            with Image.open(path) as im:
                im.load()
                if im.format != 'PNG':
                    raise ValueError('asset must be PNG')
                if list(im.size) != [a['width'], a['height']]:
                    raise ValueError('size differs from manifest')
                if a['transparent']:
                    if 'A' not in im.getbands() and 'transparency' not in im.info:
                        raise ValueError('no transparency')
                    lo, hi = im.convert('RGBA').getchannel('A').getextrema()
                    if lo == 255:
                        raise ValueError('alpha is fully opaque')
                    if hi == 0:
                        raise ValueError('image is fully invisible')
        except (ValueError, TypeError, KeyError, OSError) as exc:
            errors.append(str(a.get('id', '?')) + ': ' + str(exc))
    for name in ('README.md', 'layout.json', 'texts.json'):
        path = root / name
        if not path.is_file():
            errors.append('missing ' + name)
        elif name.endswith('.json'):
            try:
                json.loads(path.read_text(encoding='utf-8'))
            except (ValueError, OSError) as exc:
                errors.append(name + ': ' + str(exc))
    if errors:
        raise ValueError('\n'.join(errors))
    return len(assets)


def package(root, target):
    if target == root or root in target.parents:
        raise ValueError('ZIP must be outside the delivery directory')
    if target.exists():
        raise ValueError('ZIP already exists; choose a versioned filename')
    entries = []
    for path in sorted(root.rglob('*')):
        if path.is_symlink():
            raise ValueError('symlinks are not packaged: ' + str(path))
        if path.is_file():
            rel = path.relative_to(root)
            if any(part.startswith('.') or part == '__pycache__' for part in rel.parts):
                continue
            if path.suffix.lower() in {'.pem', '.key'}:
                raise ValueError('unexpected credential-like file: ' + str(rel))
            entries.append((path, rel))
    target.parent.mkdir(parents=True, exist_ok=True)
    try:
        with zipfile.ZipFile(target, 'w', zipfile.ZIP_DEFLATED) as archive:
            for path, rel in entries:
                archive.write(path, root.name + '/' + rel.as_posix())
        with zipfile.ZipFile(target) as archive:
            if archive.testzip() is not None:
                raise ValueError('ZIP integrity check failed')
    except Exception:
        if target.exists():
            target.unlink()
        raise


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('directory', type=Path, help='Delivery directory containing manifest.json, README.md, layout.json, and texts.json')
    p.add_argument('--zip', type=Path, help='Output ZIP outside the delivery directory; must not already exist')
    args = p.parse_args()
    try:
        root = args.directory.resolve()
        count = check(root)
        if args.zip:
            package(root, args.zip.resolve())
        print(json.dumps({'valid': True, 'assets': count, 'zip': str(args.zip) if args.zip else None}))
    except (ValueError, OSError, TypeError) as exc:
        print(str(exc), file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
