import re

names = re.compile(r'(@\w+)')


def get_mentions(message):
    result = [x for x in names.finditer(message)]
    print(len(result))
    results = []
    for mention in result:
        if mention not in results:
            results.append(mention.group(0))
    return results
