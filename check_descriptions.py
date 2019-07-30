import glob
import os
import sys

names_without_description_blocks = []
for name in glob.glob('source/**/**.rst', recursive=True):
    if os.path.basename(name).startswith('_'):
        # Included file, never mind
        continue
    with open(name, 'r') as fh:
        content = fh.read()
    if ':description: ' not in content:
        names_without_description_blocks.append(name)

if names_without_description_blocks:
    print('Files missing `:description:` blocks:\n', file=sys.stderr)
    for name in sorted(names_without_description_blocks):
        print(name)
    print('', file=sys.stderr)
    sys.exit(1)
