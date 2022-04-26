import os
import sys
import tabulate


class OUT:
    WHITE = '\033[1m\033[0m'
    PURPLE = '\033[1m\033[95m'
    CYAN = '\033[1m\033[96m'
    DARKCYAN = '\033[1m\033[36m'
    BLUE = '\033[1m\033[94m'
    GREEN = '\033[1m\033[92m'
    YELLOW = '\033[1m\033[93m'
    RED = '\033[1m\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
    LINEUP = '\033[F'

    def __init__(self):
        if not self.support_colors:
            self.win_colors()

    def support_colors(self):
        plat = sys.platform
        supported_platform = plat != 'Pocket PC' and (plat != 'win32' or 'ANSICON' in os.environ)
        is_a_tty = hasattr(sys.stdout, 'isatty') and sys.stdout.isatty()
        if not supported_platform or not is_a_tty:
            return False
        return True

    def win_colors(self):
        self.WHITE = ''
        self.PURPLE = ''
        self.CYAN = ''
        self.DARKCYAN = ''
        self.BLUE = ''
        self.GREEN = ''
        self.YELLOW = ''
        self.RED = ''
        self.BOLD = ''
        self.UNDERLINE = ''
        self.END = ''

    def make_white(self, mess):
        return self.WHITE + mess + self.END

    def make_purple(self, mess):
        return self.PURPLE + mess + self.END

    def make_cyan(self, mess):
        return self.CYAN + mess + self.END

    def make_darkcyan(self, mess):
        return self.DARKCYAN + mess + self.END

    def make_blue(self, mess):
        return self.BLUE + mess + self.END

    def make_green(self, mess):
        return self.GREEN + mess + self.END

    def make_yellow(self, mess):
        return self.YELLOW + mess + self.END

    def make_red(self, mess):
        return self.RED + mess + self.END

    def make_bold(self, mess):
        return self.BOLD + mess + self.END

    def make_underline(self, mess):
        return self.UNDERLINE + mess + self.END

    def get_com(self, mss=()):
        if mss:
            rtval = input(
                self.DARKCYAN + "$" + self.END + " [" + self.GREEN + mss[1].ip + self.END + ":" + self.RED + str(
                    mss[1].port) + self.END + "] ")
        else:
            rtval = input(self.DARKCYAN + "$" + self.END + " ")
        rtval = rtval.rstrip(" ").lstrip(" ")
        return rtval

    def print_green(self, mess):
        print(self.make_green(mess))

    def print_blue(self, mess):
        print(self.make_blue(mess))

    def print_red(self, mess=""):
        print(self.make_red(mess))

    def help_c_current(self):
        headers = (self.BOLD + 'Command' + self.END, self.BOLD + 'Description' + self.END)
        lister = [
            ('help', 'Shows manual for commands'),
            ('sessions', 'Show all connected clients to the server'),
            ('connect', 'Connect to a Specific Client'),
            ('disconnect', 'Disconnect from Current Client'),
            ('clear', 'Clear Screen'),
            ('shell', 'Launch a New Terminal/Shell.'),
            ('keylogger', 'KeyLogger Module'),
            ('sysinfo', 'Dump System, Processor, CPU and Network Information'),
            ('screenshot', 'Take Screenshot on Target Machine and Save on Local'),
            ('exit', 'Exit from SillyRAT!')
        ]
        sys.stdout.write("\n")
        print(tabulate.tabulate(lister, headers=headers))
        sys.stdout.write("\n")

    def help_c_general(self):
        headers = (self.BOLD + 'Command' + self.END, self.BOLD + 'Description' + self.END)
        lister = [
            ('help', 'Shows manual for commands'),
            ('sessions', 'Show all connected clients to the server'),
            ('connect', 'Connect to a Specific Client'),
            ('disconnect', 'Disconnect from Current Client'),
            ('clear', 'Clear Screen'),
            ('exit', 'Exit from SillyRAT!')
        ]
        sys.stdout.write("\n")
        print(tabulate.tabulate(lister, headers=headers))
        sys.stdout.write("\n")

    def help_c_sessions(self):
        sys.stdout.write("\n")
        print("Info       : Display connected sessions to the server!")
        print("Arguments  : None")
        print("Example    : \n")
        print("$ sessions")
        sys.stdout.write("\n")

    def help_c_connect(self):
        sys.stdout.write("\n")
        print("Info       : Connect to an available session!")
        print("Arguments  : Session ID")
        print("Example    : \n")
        print("$ connect 56\n")
        headers = (
            self.BOLD + 'Argument' + self.END, self.BOLD + 'Type' + self.END, self.BOLD + 'Description' + self.END)
        lister = [
            ('ID', 'integer', 'ID of the sessions from the list')
        ]
        print(tabulate.tabulate(lister, headers=headers))
        sys.stdout.write("\n")

    def help_c_disconnect(self):
        sys.stdout.write("\n")
        print("Info       : Disconnect current session!")
        print("Arguments  : None")
        print("Example    : \n")
        print("$ disconnect")
        sys.stdout.write("\n")

    def help_c_clear(self):
        sys.stdout.write("\n")
        print("Info       : Clear screen!")
        print("Arguments  : None")
        print("Example    : \n")
        print("$ clear")
        sys.stdout.write("\n")

    def help_c_shell(self):
        sys.stdout.write("\n")
        print("Info       : Launch a shell against client!")
        print("Arguments  : None")
        print("Example    : \n")
        print("$ shell")
        sys.stdout.write("\n")

    def help_c_keylogger(self):
        sys.stdout.write("\n")
        print("Info       : Keylogger Module!")
        print("Arguments  : on, off, dump")
        print("Example    : \n")
        print("$ keylogger on")
        print("$ keylogger off")
        print("$ keylogger dump\n")
        headers = (self.BOLD + 'Argument' + self.END, self.BOLD + 'Description' + self.END)
        lister = [
            ('on', 'Turn Keylogger on'),
            ('off', 'Turn Keylogger off'),
            ('dump', 'Dump keylogs')
        ]
        print(tabulate.tabulate(lister, headers=headers))
        sys.stdout.write("\n")

    def help_c_sysinfo(self):
        sys.stdout.write("\n")
        print("Info       : Gathers system information!")
        print("Arguments  : None")
        print("Example    : \n")
        print("$ sysinfo")
        sys.stdout.write("\n")

    def help_c_screenshot(self):
        sys.stdout.write("\n")
        print("Info       : Screenshot the current screen and save it on server!")
        print("Arguments  : None")
        print("Example    : \n")
        print("$ screenshot")
        sys.stdout.write("\n")


output = OUT()
