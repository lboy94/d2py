''' Join and say things in battle.net chat channels.
'''
#
# Modifiers:
#
def join(name):
    ''' Joins a specific chat channel.

ARGUMENTS: string
REQUIRES: Connected to battle.net, character selected, not in a game.
EFFECTS: If not in chat, joins it and enters the specified chat channel.
    Channel will be properly exited if a game is joined. If allready in a
    channel, previous channel is left and new one joined.
    '''
    
def chat(msg):
    ''' Says something in chat.

ARGUMENTS: string
REQUIRES: In a battle.net chat channel.
EFFECTS: Says msg in the chat channel.
    '''