import logging

CHATROOM_FN = 'Err'
CHATROOM_PRESENCE = ('#test_lunchbot',)
BACKEND = 'IRC'
BOT_IDENTITY = {
    # XMPP (Jabber) mode
    # 'username': 'err@localhost',  # The JID of the user you have created for the bot
    # 'password': 'changeme',       # The corresponding password for this user
    # 'server': ('host.domain.tld', 5222), # server override

    ## IRC mode (Comment the others above if using this mode)
    'nickname' : 'err-chatbot',
    'server' : 'irc.freenode.net',
}

BOT_PREFIX = '!'
DIVERT_TO_PRIVATE = ()
BOT_ADMINS = ()

BOT_LOG_LEVEL = logging.INFO
BOT_DATA_DIR = 'data'
BOT_LOG_FILE = 'data/err.log'

BOT_EXTRA_PLUGIN_DIR = 'plugins'
BOT_ASYNC = True
AUTOINSTALL_DEPS = True
CHATROOM_RELAY = {}
REVERSE_CHATROOM_RELAY = {}

BOT_LOG_SENTRY = False
SENTRY_DSN = ''
SENTRY_LOGLEVEL = BOT_LOG_LEVEL
