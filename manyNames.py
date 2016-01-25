import re

names = re.compile(r'(@\w+)')


def get_mentions(message):
    result = names.finditer(message)
    results = {}
    for mention in result:
        results.apppend(mention.group(0))
    return results
