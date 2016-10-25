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
            'Azzam/Shitty Chicken': 8,
            'Tung Long (stinki)': 9,
            'Imren': 3,
            'Thai Boddinstraße': 2,
            'Jasmin': 4,
            'Pizza': 4,
            'Gözleme': 3 ,
            'Go be creative and try out something new!': 1
        }

        if date.today().weekday() == 2:
            location = 'Tschüsch'
        else:
            location = choice(locations)

        self.broadcast(u'Peeps, we are hungry! Today we are going to %s!' % location)

    def auto_announce_lunch(self):
        now = datetime.now()
        if now.weekday() < 5 and now.hour == 12:
            if self.get('last_announced') != date.today():
                self.announce_lunch()

    def activate(self):
        super(Lunch, self).activate()
        self.start_poller(10, self.auto_announce_lunch)
