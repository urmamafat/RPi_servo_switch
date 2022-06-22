import time
import telepot 
import RPi.GPIO as GPIO
from telepot.loop import MessageLoop
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton


GPIO.setmode(GPIO.BOARD)
GPIO.setup(5, GPIO.OUT)
GPIO.setwarnings(False)
p = GPIO.PWM(5,50)
p.start(5)

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    if command == '/on':
        print('on')
        p.ChangeDutyCycle(2)
        time.sleep(1)
        p.ChangeDutyCycle(7)
        time.sleep(1)
        p.ChangeDutyCycle(0)
        time.sleep(1)
        bot.sendMessage(chat_id, '/on JOB DONE ')
    elif command == '/off':
        print('off')
        p.ChangeDutyCycle(12)
        time.sleep(1)
        p.ChangeDutyCycle(7)
        time.sleep(1)
        p.ChangeDutyCycle(0)
        time.sleep(1)
        bot.sendMessage(chat_id, '/off JOB DONE ')
    elif command=='/keyboard':
        bot.sendMessage(chat_id, 'here you go!', reply_markup=ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='/on'), KeyboardButton(text='/off')]]))
    else:
        bot.sendMessage(chat_id, '--INVALID COMMOAND--, Valid command are "/on" or "/off"', reply_markup=ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='/on'), KeyboardButton(text='/off')]]))


bot = telepot.Bot(‘<TOKEN>’)
MessageLoop(bot,handle).run_as_thread()


while 1:
    time.sleep(10)