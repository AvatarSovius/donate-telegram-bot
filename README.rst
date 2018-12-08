Donate Telegram Bot
==========

Donate Telegram Bot создан и модифицируется в течение обучения в `Learn Python`_ .


Цель проекта
------------

Donate Telegram Bot создан для сбора донатов.

Настройка
---------

Создайте файл settings.py и добавьте туда следующие настройки:

.. code-block:: python

    PROXY = {'proxy_url': 'socks5://ВАШ_SOCKS5_ПРОКСИ:1080',
            'urllib3_proxy_kwargs': {'username': 'ЛОГИН', 'password': 'ПАРОЛЬ'}}

    API_KEY = 'API ключ, который вы получили у BotFather'


Необходимо установить библиотеки telegram-bot, OpenCV и Clarifai.

Запуск
------

В активированном виртуальном окружении выполните:

.. code-block:: text

    python3 bot.py


Отправьте сообщение боту:

.. code-block:: text

    /start


.. _Learn Python: https://learn.python.ru/
