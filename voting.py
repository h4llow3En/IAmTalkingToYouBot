import re

re_upvote = re.compile('(?:^|\s)\+(\d+)').match
re_downvote = re.compile('(?:^|\s)\-(\d+)').match

message = '{name} gefällt das{times}{nicht}.'


def check_vote(bot_stuff):
    match_up = re_upvote(bot_stuff['message'])
    match_down = re_downvote(bot_stuff['message'])
    if match_up is not None:
        create_vote_message(up=True, count=int(
            match_up.group(1)), bot_stuff=bot_stuff)
    elif match_down is not None:
        create_vote_message(up=False, count=int(
            match_down.group(1)), bot_stuff=bot_stuff)


def create_vote_message(bot_stuff, up=True, count=0):
    if count == 0:
        return
    else:
        bot_stuff['sendMessage'](chat_id=bot_stuff['chat_id'],
                                 text=message.format(name=bot_stuff['username'],
                                                     times='\
' if count == 1 else ' {}-fach'.format(count), nicht='' if up else ' nicht'))
