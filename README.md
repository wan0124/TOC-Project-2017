# TOC-Project-2017

Template Code for TOC Project 2017  
A telegram bot based on a finite state machine  

## Setup

What you need:
  1.Flask  
  2.transitions  
  3.pygraphviz  
  4.python-telegram-bot  
 You can install this by yourself or do the following code  
 
<pre><code>pip3 install -r requirements.txt</code></pre>

(In my ububtu , I must use pip3 instead pip)  

## Get your own bot

  1.Download Telegram  
  2.Find BotFather  
  3.Use command "/newbot" to get your own bot  
  4.When you finish the following steps , you can get your bot's API , it will be use in your code  
  <pre><code>bot=telegram.Bot(token='XXXXX:XXXXXXXXXXXXX')</code></pre>
## Ngrok

  <pre><code>ngrok https 5000</code></pre>
  use this command , then you'll get https://xxxxxxxx.ngrok.io ,it will also be used in your code  
  <pre><code>status=bot.set_webhook('https://xxxxxxxx.ngrok.io/hook')</code></pre>
  
## Run the server

  <pre><code>python3 test.py</code></pre>
  
## Get Fsm
 
  Search 'https://xxxxxxxx.ngrok.io/show-fsm' in your internet explorer  
  Of course you have to run your server first  
  
## What can you do with my bot ?  

  1.You can use 'Hello' , 'Hi', '/start' to wake my bot  
  2.My bot can do two things , chat with you or do something for you  
  3.Enter '1' or 'chat' to chat with my bot  
  4.Enter '2' or 'help' to get some help from my bot  
  5.In chat function , you can choose one of three object that my bot is interesting to , but for now ,thew functions is not perfect  
  6.In help function , you can ask my bot google something for you or find the songs you want to listen to on youtube  
  7.After my bot finishes searching , you can choose to search another thing , or change to another type of help (google<->youtube)    
  8.Anytime you enter 'bye' , it means that you say bye to my bot , then my bot will fall asleep , you can wake it again by 'Hello' ,'Hi'  

## Fsm of my bot

![](/show-fsm.png)
