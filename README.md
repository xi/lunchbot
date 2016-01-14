# lunchbot project based on errbot

This project consists of a simple [errbot](http://errbot.io/) config and a
plugin that makes errbot announce where to go for lunch.

## installation

    $ pip install errbot
    $ errbot -c config.py

## choose chatroom

By default, lunchbot will join the `#test_lunchbot` channel on freenote (IRC).
It can also be run in debug mode (`errbot -c config.py -T`) or on jabber
(adjust `config.py`).
