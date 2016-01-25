import random
from sys import maxsize

strings = [
    'Also wirklich mal, {usr}!',
    '{usr}, was fällt dir ein?!',
    'Falls du es nicht mitbekommen hast, {usr}...',
    'Ey, {usr}!',
    'Sag doch auch mal was, {usr}!'
]


def buildmessage(username):
    random.seed()
    randstring = strings[random.randint(0, maxsize) % len(strings)]
    message = randstring.format(usr=username)
    return message
