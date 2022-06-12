import os
import sys
import tabulate

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


def make_white(mess):
    return WHITE + mess + END


def make_purple(mess):
    return PURPLE + mess + END


def make_cyan(mess):
    return CYAN + mess + END


def make_darkcyan(mess):
    return DARKCYAN + mess + END


def make_blue(mess):
    return BLUE + mess + END


def make_green(mess):
    return GREEN + mess + END


def make_yellow(mess):
    return YELLOW + mess + END


def make_red(mess):
    return RED + mess + END


def make_bold(mess):
    return BOLD + mess + END


def make_underline(mess):
    return UNDERLINE + mess + END


def get_com(mss=()):
    if mss:
        rtval = input(
            DARKCYAN + "$" + END + " [" + GREEN + mss[1].ip + END + ":" + RED + str(
                mss[1].port) + END + "] ")
    else:
        rtval = input(DARKCYAN + "$" + END + " ")
    rtval = rtval.rstrip(" ").lstrip(" ")
    return rtval


def print_green(mess):
    print(make_green(mess))


def print_blue(mess):
    print(make_blue(mess))


def print_red(mess=""):
    print(make_red(mess))


def help_c_current():
    headers = (BOLD + 'Command' + END, BOLD + 'Description' + END)
    lister = [
        ('help', 'Shows manual for commands'),
        ('sessions', 'Show all connected clients to the server'),
        ('connect', 'Connect to a Specific Client'),
        ('disconnect', 'Disconnect from Current Client'),
        ('keylogger', 'KeyLogger Module'),
        ('exit', 'Exit')
    ]
    sys.stdout.write("\n")
    print(tabulate.tabulate(lister, headers=headers))
    sys.stdout.write("\n")


def help_c_general():
    headers = (BOLD + 'Command' + END, BOLD + 'Description' + END)
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

def help_c_sessions():
    sys.stdout.write("\n")
    print("Info       : Display connected sessions to the server!")
    print("Arguments  : None")
    print("Example    : \n")
    print("$ sessions")
    sys.stdout.write("\n")

def help_c_connect():
    sys.stdout.write("\n")
    print("Info       : Connect to an available session!")
    print("Arguments  : Session ID")
    print("Example    : \n")
    print("$ connect 56\n")
    headers = (
        BOLD + 'Argument' + END, BOLD + 'Type' + END, BOLD + 'Description' + END)
    lister = [
        ('ID', 'integer', 'ID of the sessions from the list')
    ]
    print(tabulate.tabulate(lister, headers=headers))
    sys.stdout.write("\n")

def help_c_disconnect():
    sys.stdout.write("\n")
    print("Info       : Disconnect current session!")
    print("Arguments  : None")
    print("Example    : \n")
    print("$ disconnect")
    sys.stdout.write("\n")

def help_c_keylogger():
    sys.stdout.write("\n")
    print("Info       : Keylogger Module!")
    print("Arguments  : on, off, dump")
    print("Example    : \n")
    print("$ keylogger on")
    print("$ keylogger off")
    print("$ keylogger dump\n")
    headers = (BOLD + 'Argument' + END, BOLD + 'Description' + END)
    lister = [
        ('on', 'Turn Keylogger on'),
        ('off', 'Turn Keylogger off'),
        ('dump', 'Dump keylogs')
    ]
    print(tabulate.tabulate(lister, headers=headers))
    sys.stdout.write("\n")
