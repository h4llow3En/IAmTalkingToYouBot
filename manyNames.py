import re

names = re.compile(r'(@\w+)')


def get_mentions(message):
    result = [x for x in names.finditer(message)]
    results = set()
    for mention in result:
        results.add(mention.group(0))
    return results
