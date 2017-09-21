#!/usr/bin/python
import config #файл с настройками
import telegram
import os
import subprocess
import sys
import shlex
import datetime
from subprocess import Popen, PIPE
from telegram.ext import CommandHandler
from imp import reload #модуль для перезагрузки (обновления) других модулей

from datetime import datetime
from telegram.ext import Updater
updater = Updater(token=config.token)
dispatcher = updater.dispatcher

#выполнение команды shell и вывод результата в телеграмм
def run_command(command):
    process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE)
    global textoutput
    textoutput = ''
    while True:
        global output
        output = process.stdout.readline()
        output = output.decode('utf8')
        if output == '' and process.poll() is not None:
            break
        if output:
            print (output.strip())
        textoutput = textoutput + '\n' + output.strip()
    rc = process.poll()
    return rc
# кака..
#def sendPhoto(photo, id):
 # for photo in photo:
    #bot.sendPhoto(id, photo)
    
#функция команады старт
def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Raspberry_pi3 готов к работе, отправьте команду /help")

#функция команады help
def help(bot, update):
    reload(config)
    bot.sendMessage(chat_id=update.message.chat_id, text='''список доступных команд: 
    /id - id пользователя
    /ip - внешний ip адрес
    /ifconfig - сетевые настройки
    /weather - погода
    /free - информация о памяти
    /reboot - перезагрузка
    /shutdown - выключение
    /faq - сведенья о системе
    /camon - включение видеопотока
    /camoff - выключение видеопотока
    /w - информация о пользователях вошедших в систему
    /dir1 - объем папки''' + config.dir1 + '''
    
    ''')

#функция команады id
def myid(bot, update):
    userid = update.message.from_user.id
    bot.sendMessage(chat_id=update.message.chat_id, text=userid)
    
#функция команады camon
def camon(bot, update):
    reload(config) 
    user = str(update.message.from_user.id)
    if user in config.admin: #если пользовательский id в списке admin то команда выполняется
        run_command("/home/ignat/bot_serv/scriptcamon.sh")
      
#______________________________
# хмм.. и почему же оно не работает мать твою...
  # photo = '/media/root/server/motion/{:%d-%b-%Y-%R}.jpg'.format(datetime.now())
       # bot.sendPhoto(chat_id, open(photo, 'rb'))
#______________________________
        
        bot.sendMessage(chat_id=update.message.chat_id, text=textoutput)
   
     # как раз таки этот блок нуждается в обработке.. возможно напишу отдельный демон для отслеживания появления новых файлов
# примерно так:
#--------------------------------------------------------------------
# import telegram

# bot = telegram.Bot('TOKEN')

# def main():
    # Тут должно быть отслеживание нового файла и вызов коллбэка


# def on_new_file_created(new_file_name):
 #   photo = '/media/root/server/motion/{}.jpg'.format(new_file_name)
  #  bot.sendPhoto(chat_id, open(photo, 'rb'))


# if __name__ == '__main__':
  #  main()
#--------------------------------------------------------------------        

#функция команады camoff
def camoff(bot, update):
    reload(config) 
    user = str(update.message.from_user.id)
    if user in config.admin: #если пользовательский id в списке admin то команда выполняется
        run_command("service motion stop")
        bot.sendMessage(chat_id=update.message.chat_id, text=textoutput)

#функция команады ifconfig
def ifconfig(bot, update):
    reload(config) 
    user = str(update.message.from_user.id)
    if user in config.admin: #если пользовательский id в списке admin то команда выполняется
        run_command("ifconfig")
        bot.sendMessage(chat_id=update.message.chat_id, text=textoutput)

#функция команады ip
def ip(bot, update):
    reload(config) 
    user = str(update.message.from_user.id)
    if user in config.admin: #если пользовательский id в списке admin то команда выполняется
        run_command("wget -O - -q icanhazip.com")
        bot.sendMessage(chat_id=update.message.chat_id, text=textoutput)

#функция команады faq
def faq(bot, update):
    reload(config) 
    user = str(update.message.from_user.id)
    if user in config.admin: #если пользовательский id в списке admin то команда выполняется
        run_command("cat /home/ignat/bot_serv/faq.txt")
        bot.sendMessage(chat_id=update.message.chat_id, text=textoutput)

#функция команады reboot
def reboot(bot, update):
    reload(config) 
    user = str(update.message.from_user.id)
    if user in config.admin: #если пользовательский id в списке admin то команда выполняется
        run_command("shutdown -r 00")
        bot.sendMessage(chat_id=update.message.chat_id, text=textoutput)

#функция команады shutdown
def shutdown(bot, update):
    reload(config) 
    user = str(update.message.from_user.id)
    if user in config.admin: #если пользовательский id в списке admin то команда выполняется
        run_command("shutdown -h now")
        bot.sendMessage(chat_id=update.message.chat_id, text=textoutput)

#функция команады weather
def weather(bot, update):
    reload(config) 
    user = str(update.message.from_user.id)
    if user in config.admin: #если пользовательский id в списке admin то команда выполняется
        run_command("wget -O - wttr.in/Barnaul -q")
        bot.sendMessage(chat_id=update.message.chat_id, text=textoutput)

#функция команады free
def free(bot, update):
    reload(config) 
    user = str(update.message.from_user.id)
    if user in config.admin: #если пользовательский id в списке admin то команда выполняется
        run_command("free -m")
        bot.sendMessage(chat_id=update.message.chat_id, text=textoutput)

#функция команады w
def w(bot, update):
    reload(config) 
    user = str(update.message.from_user.id)
    if user in config.admin: #если пользовательский id в списке admin то команда выполняется
        run_command("w")
        bot.sendMessage(chat_id=update.message.chat_id, text=textoutput)

#функция команады dir1
def dir1(bot, update):
    reload(config) 
    user = str(update.message.from_user.id)
    if user in config.admin: #если пользовательский id в списке admin то команда выполняется
        dir1_command = "du -sh "+ config.dir1
        run_command(dir1_command)
        bot.sendMessage(chat_id=update.message.chat_id, text=textoutput)
        

    
    
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

camoff_handler = CommandHandler('camoff', camoff)
dispatcher.add_handler(camoff_handler)

camon_handler = CommandHandler('camon', camon)
dispatcher.add_handler(camon_handler)

ifconfig_handler = CommandHandler('ifconfig', ifconfig)
dispatcher.add_handler(ifconfig_handler)

ip_handler = CommandHandler('ip', ip)
dispatcher.add_handler(ip_handler)

faq_handler = CommandHandler('faq', faq)
dispatcher.add_handler(faq_handler)

weather_handler = CommandHandler('weather', weather)
dispatcher.add_handler(weather_handler)

free_handler = CommandHandler('free', free)
dispatcher.add_handler(free_handler)

w_handler = CommandHandler('w', w)
dispatcher.add_handler(w_handler)

reboot_handler = CommandHandler('reboot', reboot)
dispatcher.add_handler(reboot_handler)

shutdown_handler = CommandHandler('shutdown', shutdown)
dispatcher.add_handler(shutdown_handler)

dir1_handler = CommandHandler('dir1', dir1)
dispatcher.add_handler(dir1_handler)

myid_handler = CommandHandler('id', myid)
dispatcher.add_handler(myid_handler)

help_handler = CommandHandler('help', help)
dispatcher.add_handler(help_handler)


updater.start_polling()
