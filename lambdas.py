from constants import *


def creator_command(m):
    return m.from_user.id != creator_id


def reply_command(m):
    return m.reply_to_message

def argument_command(m):
    return m.text.count(' ')
