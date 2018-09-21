Writeup 3 - OSINT II, OpSec and RE
======

Name: Bryan Soriano
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Bryan Soriano

## Assignment 3 Writeup

### Part 1 (100 pts)

* **Vulnerability 1: Weak Password**

  One vulnerability that I found was Fred's use of a weak password. Fred's weak password allowed me to use the rockyou.txt wordlist to brute force his password, which allowed me to access the admin server. If Fred was using a stronger password, I would not have been able to brute force access. To make a stronger password, Fred should avoid using words which can be found in a dictionary, and also avoid words/numbers that someone can guess by viewing his social media profile/knowing more about him (pokemon on instagram, birthday numbers, etc.). Fred should make a password with at least 16 characters in length, which uses A-Z, a-z, 0-9 and symbols. [This would ensure a high level of entropy within his password.](http://rumkin.com/tools/password/passchk.php)

* **Vulnerability 2: Exposed Ports**

  Another vulnerability I found was Fred keeping unnecessary ports open (ports not needed for his website to function). Since port 1337 was open, I was able to interface with his admin server. By closing port 1337 and any other unneccesary ports, Fred will be able to block attackers from interfacing with the closed ports. [This will minimize the attack surface, reducing security risk, making it more difficult for someone to hack into his servers.](https://www.tripwire.com/state-of-security/featured/understanding-constitutes-attack-surface-2/) Fred should close these ports through his router settings, or by using a firewall.
  
* **Vulnerability 3: Robots.txt**

  Fred uses the robots.txt file to try to hide the /secret/ directory from users/attackers. This is a security risk, since [robots.txt does not enforce any access control over any of the directories that it hides.](https://portswigger.net/kb/issues/00600600_robots-txt-file) An attacker's bot may see that /secret/ is hidden, and try to access it anyways. Fred's website would grant the attacker's bot access to the hidden directory. In order [to handle this vulnerability, Fred should configure basic authorization](http://www.robotstxt.org/faq/nosecurity.html), requiring a secure password to access any directories which he does not want others to have access to. 
