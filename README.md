________________________________
# telegram_bot-python-flooded-
________________________________

### Ubuntu (mate) LTS 16.04 (armhf)

    # тестирование именно на этой платформе показалось успешным
    # работал на Raspberry PI 3
   # проект начал пилить.. но пока в основном коде бота. потом буду городить костыли. #
________________________________

### планы на будущее:

    # допилить функцию отправки медиа в чат   #уже начал пилить.#
    # скомпилировать с Makefile, бибилотеками, бл..дж и шл..
________________________________
### для запуска на платформах armhf и amd64 потребуется:
    wget https://www.python.org/ftp/python/3.6.0/Python-3.6.0.tar.xz
    tar -xpJf Python-3.6.0.tar.xz
    cd Python-3.6.0
    ./configure
    make
    sudo make install
    ln -s /usr/local/bin/python3 /usr/bin/python3
    pip3 install python-telegram-bot --upgrade
    pip install --upgrade pip

    ссылка для тех кто собирается использовать на сервере для видеонаблюдения http://ash-yes.livejournal.com/52421.html
________________________________
### чтобы не танцевать с бубном на i386
    sudo apt-get install build-essential
    sudo apt-get install libssl-dev
    sudo apt-get install make build-essential libssl-dev zlib1g-dev libbz2-dev libsqlite3-dev
    wget https://www.python.org/ftp/python/3.5.0/Python-3.5.0.tar.xz (если 3.6.0 не устанавливается в i386)
    tar -xpJf Python-3.5.0.tar.xz
    cd Python-3.5.0
    ./configure
    make
    sudo make install
    ln -s /usr/local/bin/python3 /usr/bin/python3
    sudo apt-get install python3-pip
    pip3 install python-telegram-bot --upgrade
    pip install --upgrade pip
________________________________
### добавляем в автозагрузку

    # пихаем telegram-bot.service в /etc/systemd/system/
    # задаем права chmod + X /etc/systemd/system/telegram-bot.service
    # запускаем systemctl start telegram-bot.service
    # добавляем в автозагрузку systemctl enable telegram-bot.service
    # проверяем статус приложения systemctl status telegram-bot.service
________________________________
