________________________________
# telegram_bot-python-flooded-
________________________________

### Ubuntu (mate) LTS 16.04 (armhf)
    # тестирование именно на этой платформе показалось успешным
    # работал на Raspberry PI 3
    # проект временно заморожен, так как на Raspberry PI 3 сейчас Retropie (ретро-игровая консоль)
________________________________
### добавляем в автозагрузку
    # пихаем "telegram-bot.service" в /etc/systemd/system/
    # задаем права "chmod + X /etc/systemd/system/telegram-bot.service"
    # запускаем "systemctl start telegram-bot.service"
    # добавляем в автозагрузку "systemctl enable telegram-bot.service"
    # проверяем статус приложения "systemctl status telegram-bot.service"
________________________________

### планы на будущее:
    # допилить функцию отправки медиа в чат 
    # скомпилировать с Makefile, бибилотеками, блэкджеком и ш..енщинами
________________________________
