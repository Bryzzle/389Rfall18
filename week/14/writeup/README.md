Writeup 10 - Crypto II
=====

Name: Bryan Soriano
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Bryan Soriano

## Assignment 10 Writeup

### Part 1 (70 Pts)
The first thing that I tried was looking for somewhere on the website that took in input (like a textbox or something). I did not find this, but I noticed that the url had "id=" in it and had either the values 0, 1, or 2. I guessed that the SQL statement the server runs was probably something like "SELECT * FROM table WHERE id='x'" (where x is 0, 1, or 2). I had never done SQL injection through the URL, so I looked it up and found a website to encode my SQL statement https://meyerweb.com/eric/tools/dencoder/ . The SQL injection statement that I encoded was "' or 1=1-- ". The first single quote replaces the single quote in the SQL statement, then the "or 1=1" will make the server retrieve all data from the table, finally the "-- " comments out the rest of the server's command. When it was encoded, it became "%27or%201%3D1--%20". I inserted this after the "id=" in the URL to get the flag CMSC38R-{y0U-are_the_5ql_n1nja}.


### Part 2 (30 Pts)

1. The prompt said that "user input is directly included in the page without proper escaping", so I made the user input the alert javascript code, "<script> alert("") </script>". As the prompt stated, the code was put into the page upon searching and executed.

1. The first thing I noticed in the 2nd level is that, there was a pink word, which showed that the website was still accepting HTML tags from user input. I tried using the script command from the first part, but that did not work at all. I looked at the hints to see that the onerror attribute was what I needed to use. I looked it up on google and saw that it can be used to trigger events on errors. I did <img src="askdlfja" onerror="alert('')"/> to make the exploit happen.
