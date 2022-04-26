import os
import sys

from common.output import *
from common.constants import HELP_OVERALL, HELP_BIND, HELP_GENERATE


class PARSER:
    COMMANDS = ['bind', 'generate']

    def __init__(self, prs):
        self.mode = self.v_mode(prs.mode, prs.help)
        self.help = self.v_help(prs.help)

        if self.mode == "bind":
            self.address = self.v_address(prs.address)
            self.port = self.v_port(prs.port)
        elif self.mode == "generate":
            self.address = self.v_address(prs.address)
            self.port = self.v_port(prs.port)
            self.output = self.v_output(prs.output)
            self.source = prs.source
            self.persistence = prs.persistence

    def v_help(self, hl):
        if hl:
            if not self.mode:
                print(HELP_OVERALL)
            else:
                if self.mode == "bind":
                    print(HELP_BIND)
                elif self.mode == "generate":
                    print(HELP_GENERATE)
                else:
                    help()
            sys.exit()

    def v_address(self, str):
        return str

    def v_port(self, port):
        if not port:
            print_red("You need to Supply a Valid Port Number")

        if port <= 0 or port > 65535:
            print_red("Invalid Port Number")

        return port

    def v_mode(self, val, hl):
        if val:
            if val in self.COMMANDS:
                return val
            else:
                print_red("No such command found in database")
        else:
            if not hl:
                print_red("Invalid Syntax. Refer to the manual!")

    def v_output(self, val):
        if val:
            if os.path.isdir(os.path.dirname(val)):
                return val
            else:
                print_red("Directory doesn't exist!")
        else:
            print_red("You must provide an output Path!")
