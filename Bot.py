# The code and main file for our bot

import Config
import Utils
import socket
import re
import time
from time import sleep


class Bot:

    def __init__(self, _pass, nick, chan):
        self._pass = _pass
        self.nick = nick
        self.chan = chan

    @staticmethod
    def main():
        # Networking functions

        s = socket.socket()
        s.connect((Config.HOST, Config.PORT))
        s.send('PASS {}\r\n'.format(Config.PASS).encode('utf-8'))
        s.send('NICK {}\r\n'.format(Config.NICK).encode('utf-8'))
        s.send('JOIN {} \r\n'.format(Config.CHAN).encode('utf-8'))
        connected = True

        Utils.chat(s, 'Hey dudes!')

        while connected:
            response = s.recv(1024).decode('utf-8')
            if response == 'PING :tmi.twitch.tv\r\n':
                s.send('PONG :tmi.twitch.tv\r\n'.encode())
            else:
                username = re.search(r'\w+', response).group(0)
                message = Config.CHAT_MSG.sub('', response)
                print(response)

                # Custom Commands
                if message.find('!time\r\n') != -1:
                    Utils.chat(s, 'It is currently ' + time.strftime('%I:%M %p %Z on %A, %B %d, %Y.'))
                if message.find('!schedule\r\n') != -1:
                    Utils.chat(s, '<schedule link>')
                if message.find('!coco\r\n') != -1:
                    Utils.chat(s, '<picture of my dog>')
                if message.find('!discord\r\n') != -1:
                    Utils.chat(s, 'Discord <discord channel link>')
                if message.find('!social\r\n') != -1:
                    Utils.chat(s, '<social links>')
            sleep(1)


Bot('<oauth>', '<botname>', '<channel name>')
Bot.main()
