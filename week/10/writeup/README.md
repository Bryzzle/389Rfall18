Writeup 10 - Crypto II
=====

Name: Bryan Soriano
Section: 0101

I pledge on my honor that I have not given or received anyunauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Bryan Soriano

## Assignment 10 Writeup

### Part 1 (70 Pts)

I started out this assignment similarly to the previous assignment. I manually nc'd into the server, so I could see the output that would be produced, and the input the server's program was waiting for. I then added the socket commands that would mirror this manual input.

Crafting the payload was the hardest part of this assignment. At first, to make the little endian string I hard coded the length of the message, "\0x78\0x00\0x00\0x00\0x00\0x00\0x00\0x00". This was not working for two reasons. For one, it was adding an extra byte to the end of the string (I am not sure why). To solve this problem I found the struct.pack() function so that I would not have to manually make the string, and it got rid of the extra byte. Another thing that took me a while to realize is that the little endian value needed to change on each iteration, since it is actually supposed to be the length of the message + the length of the secret, not just the length of the message. Once I fixed this problem, I was able to retrieve the flag:

CMSC389R-{i_still_put_the_M_between_the_DV}

### Part 2 (30 Pts)


