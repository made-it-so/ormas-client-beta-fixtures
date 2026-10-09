import sys

from textkit.slug import slugify

print(slugify(' '.join(sys.argv[1:])))
