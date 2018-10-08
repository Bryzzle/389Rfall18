Writeup 5 - Binaries I
======

Name: Bryan Soriano
Section: 0101

I pledge on my honor that I havie not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Bryan Soriano

## Assignment 5 Writeup

  For this assignment, the first thing I had to learn how to do was make loops in this version of assembly. In the example file fib.S, I saw the loop "help:". I did not understand how the loop was functioning at first, since I did not see any explicit incrementing/decrementing going on. So I looked up the "loop" assembly command, and learned that this command automatically decrements the command stored in rcx. I saw that the fib.S file moved the counter into rcx, so I did the same for my program, and now had a functioning loop.
  
  The next thing I had to figure out was how to dereference the pointer passed by one of the arguments, so that I could change its value. I figured out I could do mov [rdi] to accomplish this, but I was having errors because of the size of the second operand. I figured out that the second register/operand had to match the size of the what the first register is asking for (a byte). I used mov [rdi], sil and it worked since sil is only one byte. 
  
  The last thing I had to figure out was how to get the register to move by one, so that the letter I was copying in would shift along the string. I had to thing about how I would move a pointer in C. In C you would just do p++. So I incremented the register, rdi, by 1, and it worked.
  
  The second function, was mostly the same idea except I had to first store the value of [rsi] into a temporary variable, since the program would not compile if I did mov [rdi], [rsi].
