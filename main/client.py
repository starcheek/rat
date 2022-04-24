import base64
import threading


class CLIENT:

    STATUS = "Active"
    MESSAGE = ""
    KEY     = ")J@NcRfU"

    def __init__(self, sock, addr):
        self.sock    = sock
        self.ip      = addr[0]
        self.port    = addr[1]

    def acceptor(self):
        data = ""
        chunk = ""

        while True:
            chunk = self.sock.recv(4096)
            if not chunk:
                self.STATUS = "Disconnected"
                break
            data += chunk.decode('utf-8')
            if self.KEY.encode('utf-8') in chunk:
                try:
                    self.MESSAGE = base64.decodebytes(data.rstrip(self.KEY).encode('utf-8')).decode('utf-8')
                except UnicodeDecodeError:
                    self.MESSAGE = base64.decodebytes(data.rstrip(self.KEY).encode('utf-8'))
                if not self.MESSAGE:
                    self.MESSAGE = " "
                data = ""

    def engage(self):
        t = threading.Thread(target=self.acceptor)
        t.daemon = True
        t.start()

    def send_data(self, val):
        self.sock.send(base64.encodebytes(val.encode('utf-8')) + self.KEY.encode('utf-8'))

    def recv_data(self):
        while not self.MESSAGE:
            try:
                pass
            except KeyboardInterrupt:
                break
        rtval = self.MESSAGE
        self.MESSAGE = ""
        return rtval