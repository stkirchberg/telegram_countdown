# telegram_countdown
A message with a constantly running countdown that you can pin and thus always have a live countdown.


HOW TO USE:

Save the code on your computer!

First, change the date to the desired time on the desired day. This can be done in line 9.
TARGET_DATE = datetime(2025, 6, 14, 18, 0, 0)
-> It is structured as follows: (Year, Month, Day, Hour, Minute, Second)
For example, if you want to select August 8, 2028 at 8:18 a.m., you would enter it as follows: (2028, 8, 8, 8, 18, 0)

Now you need to create a bot.
To do this, go to "BotFather" (this is a bot that allows you to create other bots; simply search for it in the Telegram search bar). Now you can create a new bot using the /newbot command. You will need this to send messages (regardless of your account).
The chat history will look like this:
You: /newbot
BotFather: Alright, a new bot. How are we going to call it? Please choose a name for your bot.
You: Countdown Bot (But you can choose your own name).
BotFather: Good. Now let's choose a username for your bot. It must end in `bot`. Like this, for example: TetrisBot or tetris_bot.
You: tetris_bot (Please choose your own, unique name here!)
BotFather: Done! Congratulations on your new bot. You will find it at t.me/tetris_bot. You can now add a description, about section and profile picture for your bot, see /help for a list of commands. By the way, when you've finished creating your cool bot, ping our Bot Support if you want a better username for it. Just make sure the bot is fully operational before you do this.
Use this token to access the HTTP API:
123456789:AAAbbbCCCdddFFFgggHHH
Keep your token secure and store it safely, it can be used by anyone to control your bot.
For a description of the Bot API, see this page: https://core.telegram.org/bots/api

Now you need your tokens.
You enter them in the code on line 7. Currently, there's a placeholder fake token there.
TOKEN = "123456789:AAAbbbCCCdddEEEfffGGG"
-> Enter it there behind TOKEN = "

Let's move on to the last point you need to change in the code.
In line 8, change the placeholder (testchannel123) to your actual channel ID.
CHANNEL_ID = "@testchannel123"

NOTE: For (private) groups, a numeric ID is used directly. This is negative and can be determined, for example, using the @RawDataBot bot, which you add to the group.
This line of code would then look something like this:
CHANNEL_ID = -1001234567890

Now invite the bot to your server. Sometimes (depending on your settings) it needs admin rights.


Now for the good part. 
First, we need to quickly enter the following command in CMD to make all parts of the code usable:
pip install python-telegram-bot --upgrade
To be on the safe side, we'll install requests:
pip install requests
In case of errors: Check if you have Python installed and are otherwise an admin (or simply run the things as an admin)

Now go to the CMD. From there, navigate to the folder containing the file. Run it with:
python telegramcountdown.py
or, if that doesn't work, with: py telegramcountdown.py

NOTE: Do not close the CMD command now, otherwise the script will terminate.
You can also run the script on sites like pythonanywhere.com.
