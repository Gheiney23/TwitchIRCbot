# Utility Functions for main bot file

import Config


# Function: chat
# Send a chat message to the server
# Parameters
# socket -- the socket over which to send the message
#  msg -- The message to send

def chat(socket, msg):
    socket.send('PRIVMSG {} :{}\r\n'.format(Config.CHAN, msg).encode())

# Will be adding timeout features here
