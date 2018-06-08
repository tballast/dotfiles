#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Use in i3wm with:
Save as screeshot.py somewhere into your PATH
bindsym --release Print exec --no-startup-id screenshot.py
"""


import os
from subprocess import Popen, PIPE
import time

SCREENSHOT_UTILITY = '/usr/bin/scrot -s'  # /usr/bin/import
NOTIFY_UTILITY = '/usr/bin/notify-send'
NOTIFY_TITLE = '"Took Sweet Screenshot!"'


def feed_xclipboard(str):
    pipe = Popen("xclip -sel clip", shell=True, stdin=PIPE).stdin
    pipe.write(str)
    pipe.close()


def import_screenshot():
    suffix = '.png'
    prefix = 'Screenshot_from_'
    date_string = time.strftime("%Y-%m-%d_%H:%M:%S")
    dir_name = os.path.expanduser('~/Pictures/')
    filename = dir_name + prefix + date_string + suffix

    p = Popen(SCREENSHOT_UTILITY + " " + filename, shell=True)
    sts = os.waitpid(p.pid, 0)[1]
    # cmdline = [NOTIFY_UTILITY, "-i", filename + " Saved to: file://" + filename]
    cmdline = NOTIFY_UTILITY + " -i " + filename + \
        " " + NOTIFY_TITLE + " " + filename
    # p = Popen([NOTIFY_UTILITY, "shit"], shell=True)
    os.system(cmdline)
    # sts = os.waitpid(p.pid, 0)[1]

    os.system("/usr/bin/sxiv " + filename)
    return filename


if __name__ == '__main__':
    screenshot = import_screenshot()
    feed_xclipboard(screenshot)
