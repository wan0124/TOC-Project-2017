import sys
from io import BytesIO

import telegram
from flask import Flask,request,send_file

from fsm import TocMachine

app=Flask(__name__)
bot=telegram.Bot(token='392346552:AAEzivok_ZCSYrhOhwdLR5ZJ6bW4NmbIZVY')
machine=TocMachine(
	states=[
		'user',
		'user_again',
		'hello',
		'hello_again',
		'ask_question',
		'chat_state_1',
		'food_state_1',
		'food_state_2',
		'weather_state_1',
		'traffic_state_1',
		'help_state_1',
		'google_state_1',
		'google_state_2',
		'youtube_state_1',
		'youtube_state_2',
		'go_back_to_google',
		'go_back_to_youtube',
		'go_back_to_help',
		'go_back_to_user'
	],
	transitions=[
		{
			'trigger':'advance',
			'source':'user',
			'dest':'hello',
			'conditions':'is_going_to_hello'
		},
		{
			'trigger':'advance',
			'source':'user_again',
			'dest':'hello_again',
			'conditions':'is_going_to_hello_again'
		},
		{
			'trigger':'advance',
			'source':'hello',
			'dest':'ask_question',
			'conditions':'is_going_to_ask_question'
		},
		{
			'trigger':'advance',
			'source':['ask_question','hello_again'],
			'dest':'chat_state_1',
			'conditions':'is_going_to_chat_state_1'
		},
		{
			'trigger':'advance',
			'source':'chat_state_1',
			'dest':'food_state_1',
			'conditions':'is_going_to_food_state_1'
		},
		{
			'trigger':'advance',
			'source':'chat_state_1',
			'dest':'weather_state_1',
			'conditions':'is_going_to_weather_state_1'
		},
		{
			'trigger':'advance',
			'source':'chat_state_1',
			'dest':'traffic_state_1',
			'conditions':'is_going_to_traffic_state_1'
		},
		{
			'trigger':'go_to_food_state_2',
			'source':'food_state_1',
			'dest':'food_state_2',
		},
		{
			'trigger':'advance',
			'source':['ask_question','hello_again'],
			'dest':'help_state_1',
			'conditions':'is_going_to_help_state_1'
		},
		{
			'trigger':'advance',
			'source':'help_state_1',
			'dest':'google_state_1',
			'conditions':'is_going_to_google_state_1'
		},
		{
			'trigger':'advance',
			'source':'help_state_1',
			'dest':'youtube_state_1',
			'conditions':'is_going_to_youtube_state_1'
		},
		{
			'trigger':'advance',
			'source':'google_state_1',
			'dest':'google_state_2',
			'conditions':'is_going_to_google_state_2'
		},
		{
			'trigger':'advance',
			'source':'google_state_2',
			'dest':'go_back_to_google',
			'conditions':'is_going_to_go_back_to_google'
		},
		{
			'trigger':'advance',
			'source':'google_state_2',
			'dest':'go_back_to_help',
			'conditions':'is_going_to_go_back_to_help'
		},
		{
			'trigger':'advance',
			'source':'youtube_state_1',
			'dest':'youtube_state_2',
			'conditions':'is_going_to_youtube_state_2'
		},
		{
			'trigger':'advance',
			'source':'youtube_state_2',
			'dest':'go_back_to_youtube',
			'conditions':'is_going_to_go_back_to_youtube'
		},
		{
			'trigger':'advance',
			'source':'youtube_state_2',
			'dest':'go_back_to_help',
			'conditions':'is_going_to_go_back_to_help'
		},
		{
			'trigger':'back_to_google',
			'source':'go_back_to_google',
			'dest':'google_state_1',
		},
		{
			'trigger':'back_to_youtube',
			'source':'go_back_to_youtube',
			'dest':'youtube_state_1',
		},
		{
			'trigger':'back_to_help',
			'source':'go_back_to_help',
			'dest':'help_state_1',
		},
		{
			'trigger':'advance',
			'source':[
					'hello',
					'hello_again',
					'ask_question',
					'chat_state_1',
					'food_state_1',
					'food_state_2',
					'weather_state_1',
					'traffic_state_1',
					'help_state_1',
					'google_state_1',
					'google_state_2',
					'youtube_state_1',
					'youtube_state_2'
				],
			'dest':'go_back_to_user',
			'conditions':'is_going_to_go_back_to_user'
		},
		{
			'trigger':'go_back',
			'source':'go_back_to_user',
			'dest':'user_again'
		}
	],
	initial='user',
	auto_transitions=False,
	show_conditions=True,
)



def _set_webhook():
	status=bot.set_webhook('https://270b2caa.ngrok.io/hook')
	if not status:
		print('Webhook setup failed')
		sys.exit(1);
	else:
		print('Your URL IS')

@app.route('/hook',methods=['POST'])

def webhook_handler():
	update=telegram.Update.de_json(request.get_json(force=True),bot)
	machine.advance(update)
	return 'OK'

@app.route('/show-fsm',methods=['GET'])
def show_fsm():
	byte_io=BytesIO()
	machine.graph.draw(byte_io,prog='dot',format='png')
	byte_io.seek(0)
	return send_file(byte_io,attachment_filename='fsm.png',minetype='image/png')


if __name__=="__main__":
	_set_webhook()
	app.run()
