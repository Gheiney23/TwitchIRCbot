# Setting up the configuration for the bot
import re

HOST = 'irc.twitch.tv'
PORT = 6667
PASS = 'oauth:<enter oauth>'
NICK = '<bot name>'
CHAN = '#<channel name>'
RATE = (20/30)
CHAT_MSG = re.compile(r'^:\w!\w+@\w+\.tmi\.twitch\.tv PRIVMSG #\w+ :')
