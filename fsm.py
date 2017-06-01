from transitions.extensions import GraphMachine
import time

name=None
google=None
youtube=None

class TocMachine(GraphMachine):

	def __init__(self,**machine_configs):
		self.machine=GraphMachine(model=self,**machine_configs)
	
	def is_going_to_hello(self,update):
		text=update.message.text
		if (text.lower() == 'hello') or (text.lower() == 'hi') or (text.lower() == '/start'):
			return True

	def is_going_to_hello_again(self,update):
		text=update.message.text
		if (text.lower() == 'hello') or (text.lower() == 'hi') or (text.lower() == '/start'):
			return True

	def is_going_to_ask_question(self,update):
		global name
		name=update.message.text
		return True

	def is_going_to_chat_state_1(self,update):
		text=update.message.text
		if (text.find("1") != -1) or (text.find("chat") != -1):
			return True			

	def is_going_to_food_state_1(self,update):
		text=update.message.text
		if (text.find("1") != -1) or (text.find("food") != -1):
			return True

	def is_going_to_weather_state_1(self,update):
		text=update.message.text
		if (text.find("2") != -2) or (text.find("weather") != -1):
			return True

	def is_going_to_traffic_state_1(self,update):
		text=update.message.text
		if (text.find("3") != -1) or (text.find("traffic") != -1):
			return True

	def is_going_to_food_state_2(self,update):
		text=update.message.text
		if (text.find("1") != -1) or (text.find("food") != -1):
			return True

	def is_going_to_help_state_1(self,update):
		text=update.message.text
		if (text.find("2") != -1) or (text.find("help") != -1):
			return True	

	def is_going_to_google_state_1(self,update):
		text=update.message.text
		if (text.find("1") != -1) or (text.find("google") != -1):
			return True	

	def is_going_to_google_state_2(self,update):
		global google
		text=update.message.text
		google=text
		return True	

	def is_going_to_youtube_state_1(self,update):
		text=update.message.text
		if (text.find("2") != -1) or (text.find("song") != -1):
			return True	

	def is_going_to_youtube_state_2(self,update):
		global youtube
		text=update.message.text
		youtube=text
		return True	

	def is_going_to_go_back_to_google(self,update):
		text=update.message.text
		if (text.find("1") != -1) or (text.find("google") != -1):
			return True

	def is_going_to_go_back_to_youtube(self,update):
		text=update.message.text
		if (text.find("1") != -1) or (text.find("youtube") != -1):
			return True

	def is_going_to_go_back_to_help(self,update):
		text=update.message.text
		if (text.find("2") != -1) or (text.find("help") != -1):
			return True

	def is_going_to_go_back_to_user(self,update):
		text=update.message.text
		if text.lower()=='bye':
			return True

	def on_enter_hello(self, update):
        	update.message.reply_text("Hi! What's your name?")

	def on_enter_hello_again(self, update):
		global name
		update.message.reply_text("Hi! "+name+"! Welcome back! What do you want me to do for you?\n 1.Chat with you? \n 2.Help you to do something?")

	def on_enter_ask_question(self,update):
		global name
		update.message.reply_text("Hi "+name+"! What do you want me to do for you?\n 1.Chat with you? \n 2.Help you to do something?")

	def on_enter_chat_state_1(self,update):
		global name
		update.message.reply_text("OK "+name+" ! What do you want to talk about?\n 1.Food \n 2.Weather \n 3.Traffic")

	def on_enter_food_state_1(self,update):
		update.message.reply_text("About food? OK! ")
		self.go_to_food_state_2(update)

	def on_enter_weather_state_1(self,update):
		update.message.reply_text("About weather? OK! ")

	def on_enter_traffic_state_1(self,update):
		update.message.reply_text("About traffic? OK! ")

	def on_enter_food_state_2(self,update):
		now_time=time.strftime("%H")
		if '6'<now_time and now_time<'11':
			update.message.reply_text("I think you should eat breakfast right now!")
		elif '10'<now_time and now_time<'13':
			update.message.reply_text("I think you should eat lunch right now!")
		elif '17'<now_time and now_time<'21':
			update.message.reply_text("I think you should eat dinner right now!")
		else:
			update.message.reply_text("Are you KIDDIND me? NOW? COME ON MAN?")

	def on_enter_help_state_1(self,update):
		global name
		update.message.reply_text("OK "+name+" ! What can I help you? 1.Google something for you? 2.Find some songs for you?")

	def on_enter_google_state_1(self,update):
		update.message.reply_text("What do you want me to google for you?")

	def on_enter_google_state_2(self,update):
		global google
		update.message.reply_text("The result is here : https://www.google.com.tw/?gws_rd=ssl#q="+google+"\n Do you want to 1.google another thing or 2.want me to help you about other thing?")

	def on_enter_youtube_state_1(self,update):
		update.message.reply_text("What song do you want to listen ?")

	def on_enter_youtube_state_2(self,update):
		global youtube
		update.message.reply_text("The result is here : https://www.youtube.com/results?search_query="+youtube+"\n Do you want to 1.find another song or 2.want me to help you about other thing?")

	def on_enter_go_back_to_google(self,update):
		self.back_to_google(update)

	def on_enter_go_back_to_youtube(self,update):
		self.back_to_youtube(update)
		
	def on_enter_go_back_to_help(self,update):
		self.back_to_help(update)

	def on_enter_go_back_to_user(self, update):
        	update.message.reply_text("Bye~")
        	self.go_back(update)

	def on_exit_hello(self, update):
        	print('Leaving hello')

	def on_exit_hello_again(self, update):
        	print('Leaving hello')

	def on_exit_ask_question(self,update):
		print('Leaving ask_question')

	def on_exit_chat_state_1(self,update):
		print('Leaving chat_state_1')

	def on_exit_food_state_1(self,update):
		print('Leaving chat_state_1')

	def on_exit_weather_state_1(self,update):
		print('Leaving chat_state_1')

	def on_exit_traffic_state_1(self,update):
		print('Leaving chat_state_1')

	def on_exit_food_state_2(self,update):
		print('Leaving chat_state_1')

	def on_exit_help_state_1(self,update):
		print('Leaving help_state_1')

	def on_exit_google_state_1(self,update):
		print('Leaving google_state_1')

	def on_exit_google_state_2(self,update):
		print('Leaving google_state_2')

	def on_exit_youtube_state_1(self,update):
		print('Leaving youtube_state_1')

	def on_exit_youtube_state_2(self,update):
		print('Leaving youtube_state_2')

	def on_exit_go_back_to_google(self,update):
		print('Leaving go_back_to_google')

	def on_exit_go_back_to_youtube(self,update):
		print('Leaving go_back_to_toutube')
		
	def on_exit_go_back_to_help(self,update):
		print('Leaving go_back_to_help')

	def on_exit_go_back_to_user(self, update):
		print('Leaving go_back_to_user')
