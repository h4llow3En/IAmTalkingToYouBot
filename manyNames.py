import re

names = re.compile(r'(?:^|\s)(@\w+)')
mm = re.compile(r'(?:^|\s)MM(?:$|\s)').search
herzog = re.compile(r'(?:^|\s)Alexander Herzog(?:$|\s)').search
droggelbecher = re.compile(
    r'droggelbecher', flags=re.IGNORECASE).search

message = 'Droggelbecher? ... Droggelbecher!\n\nhttps://youtu.be/6V3eESJ66Nk'


def get_mentions(message):
    return {x.group(1) for x in names.finditer(message)}


def has_droggelbecher(bot_stuff):
    if droggelbecher(bot_stuff['message']) is not None:
        bot_stuff['sendMessage'](chat_id=bot_stuff['chat_id'],
                                 text=message)
        return True
    return False


def is_mm(bot_stuff):
    realy = 'Och ne, wirklich? {}?'
    has_mm = True if mm(bot_stuff['message']) is not None else False
    has_herz = True if herzog(bot_stuff['message']) is not None else False
    if has_mm or has_herz:
        if has_mm != has_herz:
            bot_stuff['sendMessage'](chat_id=bot_stuff['chat_id'],
                                     text=realy.format(
                                     'MM' if has_mm else 'Alexander Herzog'))
        else:
            bot_stuff['sendMessage'](chat_id=bot_stuff['chat_id'],
                                     text=realy.format(
                                     'MM und Alexander Herzog'))
