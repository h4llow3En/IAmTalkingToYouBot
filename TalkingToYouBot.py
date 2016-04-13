from telegram import Updater
import json
import os
import manyNames
import reprimandUser
import time
import voting


def getToken():
    token = []
    if not os.path.exists('token.json'):
        token.append(input('Insert Token here: '))
        with open('token.json', 'w') as f:
            json.dump(token, f)
    else:
        with open("token.json") as f:
            token = json.load(f)
    return token[0]


def echo(bot, update):
    '''
    Simple function that echos every received message back to the user.
    '''
    if update.message.text is not None and update.message.text != '':
        bot_stuff = {'sendMessage': bot.sendMessage,
                     'chat_id': update.message.chat_id,
                     'username': update.message.from_user.username,
                     'message': update.message.text}
        voting.check_vote(bot_stuff)
        print('Message received: "{msg}" from {usr}'.format(
            msg=update.message.text,
            usr=update.message.from_user.username))
        usersToMention = manyNames.get_mentions(update.message.text)
        time.sleep(2)
        if len(usersToMention) > 0:
            for username in usersToMention:
                msg = ''
                if username in ('@{}'.format(bot.first_name), bot.name):
                    msg = reprimandUser.noBotMessage(update.message.from_user)
                elif username == '@{}'.format(
                        update.message.from_user.username):
                    msg = reprimandUser.selfMention(update.message.from_user)
                else:
                    msg = reprimandUser.buildmessage(username)
                bot.sendMessage(chat_id=update.message.chat_id, text=msg)
    '''
    elif update.message.sticker is not None:
        print("{}".format(update.message.sticker))
        bot.sendSticker(chat_id=update.message.chat_id,
                        sticker='BQADAQADLgEAArED5ATHstrectuzrwI')'''


def main():
    token = getToken()
    print('''
       .. ..
     .'  `  `.
   .'_.-...-._`.   Hey, I am talking to you!
    `.       .'
      `-...-'
''')
    print("Starting Bot...")

    # Start the Bot with the token
    updater = Updater(token=token)
    dispatcher = updater.dispatcher

    # Add the echo-Message Handler to the Dispatcher
    dispatcher.addTelegramMessageHandler(echo)

    # Make the bot listen for commands
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
