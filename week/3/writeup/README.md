Writeup 3 - OSINT II, OpSec and RE
======

Name: Bryan Soriano
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Bryan Soriano

## Assignment 3 Writeup

### Part 1 (100 pts)

* **Vulnerability 1: Weak Password**

  One vulnerability that I found was Fred's use of a weak password. Fred's weak password allowed me to use the rockyou.txt wordlist
  to brute force his password, which allowed me to access the admin server. If Fred was using a stronger password, I would not have
  been able to brute force access. To make a stronger password, Fred should avoid using words which can be found in a dictionary,
  and also avoid words/numbers that someone can guess by viewing his social media profile/knowing more about him (pokemon on instagram,
  birthday numbers, etc.). Fred should make a password with at least 16 characters in length, which uses A-Z, a-z, 0-9 and symbols. This
  would ensure a high level of entropy within his password.
