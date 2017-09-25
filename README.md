________________________________
# telegram_bot-python-flooded-
________________________________

### Ubuntu (mate) LTS 16.04 (armhf)

    # тестирование именно на этой платформе показалось успешным
    # работал на Raspberry PI 3
    # проект временно заморожен, так как на Raspberry PI 3 сейчас Retropie (ретро-игровая консоль)
________________________________

### планы на будущее:

    # допилить функцию отправки медиа в чат 
    # скомпилировать с Makefile, бибилотеками, блэкджеком и ш..енщинами
________________________________
### для успешного запуска потребуется:

    wget https://www.python.org/ftp/python/3.6.0/Python-3.6.0.tar.xz
    tar -xpJf Python-3.6.0.tar.xz
    cd Python-3.6.0
    ./configure
    make
    make install
    ln -s /usr/local/bin/python3 /usr/bin/python3
    pip3 install python-telegram-bot --upgrade

    ссылка для тех кто собирается использовать на сервере для видеонаблюдения http://ash-yes.livejournal.com/52421.html

________________________________
### добавляем в автозагрузку

    # пихаем telegram-bot.service в /etc/systemd/system/
    # задаем права chmod + X /etc/systemd/system/telegram-bot.service
    # запускаем systemctl start telegram-bot.service
    # добавляем в автозагрузку systemctl enable telegram-bot.service
    # проверяем статус приложения systemctl status telegram-bot.service
________________________________
