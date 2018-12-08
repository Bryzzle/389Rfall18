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

1. The first thing I noticed in the 2nd level is that, there was a pink word, which showed that the website was still accepting HTML tags from user input. I tried using the script command from the first part, but that did not work at all. I looked at the hints to see that the onerror attribute was what I needed to use. I looked it up on google and saw that it can be used to trigger events on errors. I did \<img src="askdlfja" onerror="alert('')"/\> to make the exploit happen.

1. For this one, I noticed that depending on what image is chosen, a number in the URL after a # is changed to a 1, 2, or 3. This reminded me of the previous SQL injection in part 1, so I tried to do the same thing. I replaced the 1 with \<img src="askdlfja" onerror="alert('')"/\> from the previous question. This didn't cause the alert to happen, but it replaced the img with the "missing image" icon, so I knew it was being executed at least partly. I tried inserting \<img src="askdlfja" onerror="alert('')"/\> again after the \<img src="askdlfja" onerror="alert('')"/\> I had already inserted in the URL and this caused the alert to happen.

1. I looked at the hint to see that "startTimer('{{ timer }}');" was the source of the issue. After seeing the hint about trying just a single quote to see what happens, I saw the error console said "Invalid or unexpected token". I guessed that maybe the single quote was being interpreted as part of the command instead of as user input. I tried thinking about this problem like SQL injection as well, so I did the command " '); alert('')" which I thought would be interpreted as "startTimer(''); alert('')". However, it threw an error and the console showed me that it was interpreted as "startTimer(''); alert('')');" To solve this, I removed the "')" from my input, to make the line be interpreted as "startTimer(''); alert('');" and it worked. Solution: " '); alert('"

1. For this one, I noticed that once you click sign up, the URL becomes "next=confirm", so I tried putting "alert('')" in place of confirm. This did not work, so I went to the hints and saw the document that said you could do "javascript:doSomething()". So I did "javascript:alert('')", and then clicked the next button which caused the alert to come up.

1. I noticed that I could change the "gadget" that was loaded by changing the name of the js file in the URL. I didn't know where to go from here, so I looked at the hints and saw that I could call external js using google's api. I tried putting "https://www.google.com/jsapi?callback=alert", but it did not work so I inspected the source code. From there I saw that the regex "url.match(/^https?:\/\//" was used to stop the "https" portion of the external js from being called. This doesnt work since it is case sensitive, so I just changed my input to be "HTTPs://www.google.com/jsapi?callback=alert".


