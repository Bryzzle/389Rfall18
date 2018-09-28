Writeup 3 - Pentesting I
======

Name: Bryan Soriano
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Bryan Soriano

## Assignment 4 Writeup

### Part 1 (45 pts)

This is the flag that I found: CMSC389R-{p1ng_as_a_$erv1c3}. The first thing I did was search "Command Injection Attack" on Google. From there, I found a [link](https://www.netsparker.com/blog/web-security/command-injection-vulnerability/) which had examples of command injection attacks. The first example on that website used the ping command as an example, with the IP address provided by user input (just like Fred's server was doing). It said it may be possible to add commands after the IP address with semicolons. The first command I tried was "127.0.0.1;ls". This command allowed me to see the filesystem. I then tried just ";ls" to see if it would still show me the filesystem, and it did. After seeing the filesystem, I guessed that the flag was probably in the home folder so I used the command ";cd home ls". However, this did not work and only returned a blank line. I had to google how to make sucessive commands on the command line, and found out that you can just keep putting semicolons after every command. After learning this, I then reconnected and used the command ";cd home;ls". This showed me the flag.txt file. Finally, I reconnected and used the command ";cd home;cat flag.txt" to display the flag. 

After doing this, I went looking for the script that Fred was using to see if I could find ways to prevent the vulnerability. I used the command ";cd opt;ls" to see if it was in the opt folder. I found the script there, so I reconnected to the server and issued the command ";cd opt;cat container_startup.sh". I then manually copy and pasted the result into a text file so I could read it. Once I had the file open, I tried to look for where the ping command was being issued, since it was probably using user input. I found the line "cmd="ping -w 5 -c 2 $input"", where $input is a variable which is the users input. This is the vulnerability since a user can input anything they want. There are a couple things that Fred could do to make sure that user input does not result in a vulnerability. He can use regex to make sure that the user input follows the IP address format "###.###.###.###" (aka validate input). He could also use regex to make sure that the user input does not include ";" since it allows users to submit multiple commands. Another thing he could do is escape characters with a \\.

### Part 2 (55 pts)

For the stub.py code, I replicated the manual inputs that I gave in part 1. For example, I knew that every command sent through the socket needed to have the ";" at the beginning of it, so I added a semi colon to the start of every command sent to my execute_cmd function. 

The hardest shell command to simulate was "cd" since I needed to keep track of the current path. At first, I was going to split the user input (when they used cd), and save the path they went to. I realized that I could make the server do the work by simply appending ";pwd" to any user input with "cd" in it. This would make the server return the current working directory. I saved this into a path variable, and then used it in any further commands. I appended "cd " + path + ";" to the start of any command passed in, and then sent this to the server. 

Once I got this working, I got to working on the pull command. At first I tried seeing if there were any commands that would download the file to my local computer. I eventually thought about how when I was testing "cat", the server would return the text, and my code would print it. So for my pull, I essentially used the same idea. I called cat on the remote path given, and then saved the result into a variable. I then wrote this variable to the local path given, and it worked!
