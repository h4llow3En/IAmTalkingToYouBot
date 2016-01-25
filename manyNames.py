import re

names = re.compile(r'(@\w+)')


def get_mentions(message):
    result = [x for x in names.finditer(message)]
    print(len(result))
    for mention in result:
        results.append(mention.group(0))
    return results
