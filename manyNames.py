import re

names = re.compile(r'(?:^|\s)(@\w+)')


def get_mentions(message):
    return {x.group(1) for x in names.finditer(message)}
