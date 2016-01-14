from datetime import date, datetime

from errbot import BotPlugin, botcmd


class Lunch(BotPlugin):
    def broadcast(self, text):
        for room in self.rooms():
            r = getattr(room, 'room', getattr(room, '_name', None))  # HACK
            self.send(r, text, message_type='groupchat')

    def announce_lunch(self):
        self['last_announced'] = date.today()
        self.broadcast('We are going to Tschuesch, as always!')  # TODO

    def auto_announce_lunch(self):
        if datetime.now().hour == 12:
            if self['last_announced'] != date.today():
                self.announce_lunch()

    def activate(self):
        super(Lunch, self).activate()
        self.start_poller(10, self.auto_announce_lunch)

    @botcmd
    def lunch(self, mess, args):
        """Automatically select a place to have lunch and announce it.

        This command is automatically executed at 12 each day. You can
        trigger it manually if you are hungry already.
        """
        self.announce_lunch()
