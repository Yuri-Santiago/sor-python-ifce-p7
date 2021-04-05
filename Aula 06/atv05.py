"""
5. Encontre todos as contas do Instagram indicadas no texto do link.
https://www.businessinsider.com/instagram-top-10-people-2017-2017-11
"""

import re

link = """
Here are the 10 most-followed Instagram accounts in 2017

Selena Gomez is the queen of Instagram for the second year in a row.
Instagram released its 2017 Year in Review on Wednesday, which highlights the most-liked posts, top hashtags, and 
most-used filters from the past year.
Gomez is the most-followed celebrity on Instagram for 2017, holding onto her title from last year and adding 24 million
new followers in the process. 
Besides Gomez, several members of the Kardashian-Jenner clan, as well as Dwayne Johnson and soccer player Cristiano 
Ronaldo, top the list. 
Here are the most-followed accounts on Instagram this year:

10. Kendall Jenner
Jenner's account, @kendalljenner, has more than 84.8 million followers.

9. Justin Bieber
Bieber's account, @justinbieber, has more than 93.9 million followers.

8. Dwayne Johnson
Johnson's account, @therock, has more than 96 million followers.

7. Kylie Jenner
Jenner's account, @kyliejenner, has more than 99.5 million followers.

6. Taylor Swift
Swift's account, @taylorswift, has more than 104 million followers.

5. Kim Kardashian West
West's account, @kimkardashian, has more than 104 million followers.

4. Beyoncé
Beyoncé's account, @beyonce, has more than 108 million followers.

3. Ariana Grande
Grande's account, @arianagrande, has more than 115 million followers.

2. Cristiano Ronaldo
Ronaldo's account, @cristiano, has more than 116 million followers.

1. Selena Gomez
Gomez's account, @selenagomez, has more than 130 million followers.
"""

padrao = re.compile('@.*,')
arrobas = re.findall(padrao, link)
print(arrobas)
