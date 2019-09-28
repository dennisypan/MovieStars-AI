# MovieStars-AI
A chatbot that describes which movie celebrities are in the photo image.  You simply enter URL of an image to the bot, and the bot will reply you a message describing which movie stars are in the image.

|


This repository contains:
1) bot.py (Python program that analyzes image from an URL, to determine which movie stars are in the image)
2) Temp.jpg (When bot.py access image from URL, it will save the image as "Temp.jpg" to the local directory)
3) index.html (the html page hosted web-chat window of STARS-AI, so user can talk to bot)
4) background.PNG (the background image of index.html)

|


NOTE: 
1) for bot.py at lines 18 - 21, you have to creat your own "aws_access_key_id" and "aws_secret_access_key" via your own AWS account.  After you got the 2 keys from AWS, fill the blanks ("aws_access_key_id" and "aws_secret_access_key") on the bot.py file.  
2) for index.html at lines 15 - 18, "channelId" and "token" are all fake, for cybersecurity reason.  Once you got your own webchat script from CAI, replace everything in lines 15 - 18 with your own webchat script from CAI.
