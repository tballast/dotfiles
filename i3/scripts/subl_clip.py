#!/usr/bin/python

import sys
import os
import subprocess

GIT_REPO_LOCATION = "YOUR GIT REPO FOLDER HERE"
TEMP_FILE = "/tmp/SHIT"

NOTIFY_UTILITY = '/usr/bin/notify-send'
NOTIFY_TITLE = '" File Not Found..."'


def ParseOutput(out):
    components = out.split()
    if "line" in components and ("warning" in components or "error" in components):
        file = out.split(",")[0].strip().replace('"', "")
        if file.startswith("/src/"):
            file = file.replace("/src/", "", 1)
        else:
            file = "app/" + file

        line = components[2][:-1]

        with open(TEMP_FILE) as f:
            GIT_REPO_LOCATION = f.read()
            f.closed

        file = GIT_REPO_LOCATION + "/" + file
        file = os.path.abspath(file)
        if not os.path.exists(file):
            # print("HERE1")
            cmdline = NOTIFY_UTILITY + " " + NOTIFY_TITLE
            os.system(cmdline)
            return
        else:
            # print("HERE2")
            file = file + ":" + line
            # print("Opening File: ", file)
            process = subprocess.Popen(['subl', file], stdout=subprocess.PIPE)
            out, err = process.communicate()
    elif "error:" in components or "warning:" in components:
        # TCU SHIT
        the_good_shit = components[0]

        file = out.split(":")[0].strip()
        if file.startswith("YOUR FOLDER PREFIX"):
            file = file.replace("YOUR FOLDER PREFIX", "SHORTENED PREFIX", 1)

        line_components = the_good_shit.split(':')
        line = line_components[1]

        with open(TEMP_FILE) as f:
            GIT_REPO_LOCATION = f.read()
            f.closed

        file = GIT_REPO_LOCATION + "/" + file
        file = os.path.abspath(file)
        if not os.path.exists(file):
            # print("HERE1")
            cmdline = NOTIFY_UTILITY + " " + NOTIFY_TITLE
            os.system(cmdline)
            return
        else:
            # print("HERE2")
            file = file + ":" + line
            # print("Opening File: ", file)
            process = subprocess.Popen(['subl', file], stdout=subprocess.PIPE)
            out, err = process.communicate()


process = subprocess.Popen(
    ['xclip', '-out', '-selection', 'primary'], stdout=subprocess.PIPE)
out, err = process.communicate()

ParseOutput(out)
# ParseOutput(shit)
