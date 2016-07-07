import re

re_pi = re.compile(r'(?:^|\s)(((P|p)i)|(π)|(3(\.|,)14\d*))').search

message = "@{name}, eigentlich is π ja 3.1415926535897932384626433832795028841971693\
9937510582097494... aber rechne lieber mit 3, das ist wesentlich einfacher!"


def check_pi(bot_stuff):
    match = re_pi(bot_stuff['message'])
    print(match)
    if match is not None:
        bot_stuff['sendMessage'](chat_id=bot_stuff['chat_id'],
                                 text=message.format(
            name=bot_stuff['username']))
