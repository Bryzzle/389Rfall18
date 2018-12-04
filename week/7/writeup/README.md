Writeup 7 - Forensics I
======

Name: Bryan Soriano
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Bryan Soriano

## Assignment 7 writeup

### Part 1 (40 pts)

1. JPEG file

2. John Hancock Center in Chicago, Illinois

3. 2018:08:22 11:33:24

4. iPhone 8 camera

5. 539.5 m

6. CMSC389R-{look_I_f0und_a_str1ng} and CMSC389R-{abr@cadabra}

### Part 2 (55 pts)

The first thing I tried was running the binary file to see what happened. This only returned the message "Where is your flag?" The next thing I tried was using the command "strings ./binary", to see if there were any strings that could hint towards the flag, or even just be the flag. I did not see any hints here, but I did see that fopen, puts, fclose, and fwrite were possibly being used by the program. These are all functions that deal with writing/reading to files. I tried to look and see if there were any hidden files put in the week 7 directory using "ls -a", but I did not find anything. 

Next, I tried using the binwalk command on the binary file to make sure that there were not any hidden files. Binwalk did not find anything either. I decided to try and see whether I could use gdb to find where the function calls were writing data to. To do this, I first put a breakpoint at main using the command "b main". Next, I ran the program and used the command "si" while looking for the calls to the file reading/writing functions. I never found the calls to these functions, because I instead saw that the program put "/tmp/.stego" onto the stack. I then went to this directory and found the .stego file.

Once I found the file, I ran binwalk on it to see if there were any hidden files within it, and I found that there was a JPG file in it after 1 byte. I removed the first byte using a hex editor, then I saw that it was a picture of a stegosaurus. I tried using the "strings" command again, but no helpful strings came up, so I downloaded steghide and tried using that instead. I guessed the password stegosaurus since it was a picture of one, and it worked. I used the less command on the output file to find the flag: CMSC389R-{dropping_files_is_fun} .