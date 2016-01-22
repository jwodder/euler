#!/usr/bin/python
from   collections import defaultdict
import imp
import json
import os
import os.path
import re
import sys
import yaml

tagParents = defaultdict(set)

def addtags(tag, parents, children):
    synonyms = [tag] + (children or {}).get("__synonyms__", [])
    implies = parents.union(synonyms)
    for t in synonyms:
        assert t not in tagParents
        tagParents[t] = implies
    if children is not None:
        for child, grandchildren in children.iteritems():
            if not child.startswith('__'):
                addtags(child, implies, grandchildren)

if sys.path[0]:
    os.chdir(sys.path[0])

if sys.argv[1:] == ['-H']:
    with open('tags.yml') as fp:
        tags = yaml.safe_load(fp)
    for tag, children in tags.iteritems():
        addtags(tag, set(), children)

taggings = {}

sys.dont_write_bytecode = True
for dirpath, dirnames, files in os.walk('.'):
    for baddir in ('.git', 'dev'):
        try:
            dirnames.remove(baddir)
        except ValueError:
            pass
    for fname in files:
        if re.search(r'^euler\d+\.py$', fname):
            src = imp.load_source(fname[:-3], os.path.join(dirpath, fname))
            srctags = set()
            for tag in getattr(src, '__tags__', []):
                srctags.add(tag)
                srctags.update(tagParents[tag])
            taggings[fname] = list(sorted(srctags))
            ### Unload `src` somehow?

print json.dumps(taggings, sort_keys=True, indent=4, separators=(',', ': '))
