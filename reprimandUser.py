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
    'Mich interessiert nicht, was du mir sagst, rede mit anderen!',
    'Kümmere dich um deinen Kram, {usr}!',
    'Hey {usr}, warum sollte ich mit mir selbst reden?!'
]

selfMentionStrings = [
    'Sag mal {usr}, brauchst du eigentlich viel Aufmerksamkeit?',
    '{usr}, warum musst du dich immer selbst hervorheben?',
    'Du willst Aufmerksamkeit? Hier: {usr}',
    'Ich muss schon sagen, {usr}, du brauchst ziemlich viel Aufmerksamkeit...',
    'Willst du, dass auch mal jemand mit dir schreibt und du erwähnst dich \
deshalb selbst, {usr}?',
    '{usr}, bitte. Ich brauche dich nicht erinnern, dass du mit DIR redest...'
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


def selfMention(user):
    random.seed()
    randstring = selfMentionStrings[
        random.randint(0, maxsize) % len(selfMentionStrings)]
    message = randstring.format(usr=user.name)
    return message
