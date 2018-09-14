Writeup 2 - OSINT (Open Source Intelligence)
======

Name: Bryan Soriano
Section: 0101
I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Bryan Soriano

## Assignment 2 writeup

### Part 1 (45 pts)

1. kruegster1990's real name is Fred Krueger. I found it on twitter.

2. He is from Silver Spring, MD, and born in 1990. Found on twitter.
   Reddit account with same username.
   Instagram account with same username, has a picture of an airline ticket.
   Email: kruegster@tutanota.com

3. 142.93.118.186 . I used a domain to IP address website.

4. Found /secret by using /robots.txt flag- CMSC389R-{fly_th3_sk1es_w1th_u5}

5. I clicked on the admin page and saw IP: 142.93.117.193 in the URL.

6. I used a website (iplocation.com) to find the location of 142.93.117.193, 
   it told me the ip address was located in Canada.

7. Linux Ubuntu. I used the nmap -O command.

8. \<!-- CMSC389R-{h1dden_fl4g_in_s0urce} -->
"CMSC389R-{dns-txt-rec0rd-ftw}"

### Part 2 (55 pts)

When I was doing the first part of the assignment, I found Mr. Krueger's 
Instagram and noticed the flight ticket. I thought maybe I could scan the
bar code to find a secret but that didn't work. Later on, I read part 2
and saw we needed to use the flight ticket. I used the password to nc
into the admin server, then looked to see if I could find any files. 
I looked into /home/ and saw the flight records folder, and remembered the
flight ticket from before and used it to find the correct txt file.
CMSC389R-{c0rn3rstone-air-27670}

