import re

names = re.compile(r'(?:^|\s)(@\w+)')
droggelbecher = re.compile(r'(?:^|\s)[Dd]roggelbecher').search

message = 'Droggelbecher? ... Droggelbecher!\n\nhttps://youtu.be/6V3eESJ66Nk'


def get_mentions(message):
    return {x.group(1) for x in names.finditer(message)}


def has_droggelbecher(bot_stuff):
    if droggelbecher(bot_stuff['message']) is not None:
        bot_stuff['sendMessage'](chat_id=bot_stuff['chat_id'],
                                 text=message)
        return True
    return False
