from telegram import Updater
import json
import os


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
    bot.sendMessage(chat_id=update.message.chat_id, text=update.message.text)


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
