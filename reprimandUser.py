import random
from sys import maxsize

mentionStrings = [
    'Also wirklich mal, {usr}!',
    '{usr}, was fällt dir ein?!',
    'Falls du es nicht mitbekommen hast, {usr}...',
    'Ey, {usr}!',
    'Sag doch auch mal was, {usr}!'
]

notTalkingStrings = [
    'Mich interessiert nicht, was du mir sagst, rede mit anderen !',
    'Kümmere dich um deinen Kram, {usr}!',
    'Hey {usr}, warum sollte ich mit mir selbst reden?!'
]


def buildmessage(username):
    random.seed()
    randstring = mentionStrings[
        random.randint(0, maxsize) % len(mentionStrings)]
    message = randstring.format(usr=username)
    return message


def noBotMessage(user):
    random.seed()
    randstring = notTalkingStrings[
        random.randint(0, maxsize) % len(notTalkingStrings)]
    message = randstring.replace('{usr}', user.name)
    return message
