## Выполнили: Бодрова Юлия, Константинова Елена, Михтеева Эвелина. Студентки 26 группы.

# Игра Тайный Санта.

# Описание:
В проекте реализована возможность регистрации и авторизации с помощью JWT-токена на сайте, а также через телеграм-бот. Имеется возможность заполнять анкету пользлователя (имя, возраст, пол, почтовый адрес, хобби) и добавлять фотографию участника в профиль. Также пользователь может удалить свою учетную запись.

Для участников с ролью администратора (по умолчаню роль назначается USER, для создания пользователя с ролью администратора необходимо зарегистрировать пользователя, указав email: Admin) достпуна функция "сгенерировать пары", которая назначает каждому пользователю другого пользователя, которому необходимо подарить подарок, после чего пользователю-дарителю становится доступна для просмотра анкета пользователя-получателя. Анкеты остальных пользователей (до генерации пар анкеты всех пользователей) для просмотра закрыты.

На главной странице отображаются правила игры и 9 случайных фотографий участников. В разделе "участники" отображаются фото участников с именами по 12 штук на странице (страницы переключаются), реализован поиск по имени.

# Стек технологий
## backend

Node JS, Express, PosgreSQL, Sequelize

## fronend

Node JS, React JS, React bootstrap, Axios, React-router-do, Mobx

## telegram-bot

Использовались библиотеки aiogram, requests для Python

# Домены
Доступ к сайту: http://localhost:3000/

Доступ к серверу: http://localhost:5000/

Телеграм бот: https://telegram.me/SecretSanta26Bot

Имя бота: @SecretSanta26Bot

# Запуск

## Для запуска сервера и клиентской части

В корневой папке приложения выполнить команду

### docker-compose up --build

Команда для запуска сервера:

### npm run dev

Команда для запуска клиентской части:

### npm start

## Для запуска бота

Необходимо активировать его виртуальное окружение командами

## cd venv
## Scripts/activate

Для связи бота с сервером требуется использование утилиты ngrok, создающей туннели на локальный компьютер пользователя (для имитации резервируется публичный адрес, все обращения по которому пробрасываются на локальный порт).

Команда после запуска ngrok.exe:

### ngrok http -region=ap 5000

После чего будет присвоен публичный адрес, который необходимо скопировать и вставить в файл createBot.py (присвоить переменной webhook_url).

Для создания вебхука необходимо в терминале ввести команду:

### curl https://api.telegram.org/bot5021941924:AAGwoickulSzKu3mk0ZQlkI93rbHBGudopM/setWebhook?url={webhook_url}

Где вместо {webhook_url} необходимо вставить адрес, полученный в ngrok.

Запуск бота производится с помощью файла telegramBot_run.bat

# Команды бота
Основные команды реализованы с помощью кнопок (регистрация, удаление пользователя, обновление анкеты, получение анкеты пользователя, которому должен подарить подарок, правила игры, ссылка на сайт)

/отмена - отмена текущего действия