from telegram import Updater
import json
import os


def getToken():
    token = []
    if not os.path.exists(file_path):
        token.append(input('Insert Token here: '))
        with open('token.json', 'w') as f:
            json.dump(token, f)
    else:
        with open("token.json") as f:
            token = json.load(f)
    return token[0]


def main():
    token = getToken()
    print(token)


if __name__ == '__main__':
    main()
