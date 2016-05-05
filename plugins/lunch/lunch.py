# -*- encoding: utf-8 -*-

from datetime import date, datetime
import random

from errbot import BotPlugin, botcmd


def choice(d):
    l = []
    for key, weight in d.items():
        for i in range(weight):
            l.append(key)
    return random.choice(l)


class Lunch(BotPlugin):
    def broadcast(self, text):
        for room in self.rooms():
            self.send(room, text)
            for occupant in room.occupants:
                self.send(occupant, text)

    def announce_lunch(self):
        self['last_announced'] = date.today()
        locations = {
            'Tschüsch': 1,
            'Sahara': 8,
            'Alassil': 8,
            'Tung Long (stinki)': 10,
            'Imren': 1,
            'Thai Boddinstraße': 1,
            'Jasmin': 4,
            'Pizza': 3,
            'Gözleme': 1,
        }

        if date.today().weekday() == 1:
            location = 'Tschüsch'
        else:
            location = choice(locations)

        self.broadcast(u'Peeps, we are hungry! Today we are going to %s!' % location)

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
