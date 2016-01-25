from telegram import Updater
import json


def getToken():
    with open("token.json") as f:
        token = json.load(f)
    return token


def main():
    token = getToken()
    print(token)


if __name__ == '__main__':
    main()
