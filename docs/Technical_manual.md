# Техническое руководство по созданию телеграм-бота

## Что такое Telegram-бот и зачем он нужен?
Telegram-бот — это автоматизированный аккаунт, который может взаимодействовать с пользователями через сообщения, команды и другие события. Боты широко используются для автоматизации задач, предоставления информации, игр и многого другого.

## Что потребуется для начала?
- Учетная запись в Telegram
- Установленный Python (рекомендуется версия 3.7 или выше)
- Библиотека pyTelegramBotAPI (обычно импортируется как telebot)

Загрузка [Python](https://www.python.org/downloads/)

Гайд по установке ['pyTelegramBotAPI'](https://pytba.readthedocs.io/en/latest/install.html)

## Регистрация бота в Telegram

### Шаг 1: Создайте нового бота через BotFather
1. Откройте Telegram и найдите бота [@BotFather](https://t.me/BotFather).
2. Начните диалог и отправьте команду `/start`.
3. Создайте нового бота командой `/newbot`.
4. Следуйте инструкциям:
   - Введите имя для вашего бота (например, "БыкиИКоровы").
   - Введите уникальное имя пользователя для бота (например, `Bulls_And_Cows_bot`), которое должно заканчиваться на `_bot`.
5. После успешной регистрации вы получите токен API — длинную строку вида `123456789:ABCdefGHIjklMNOpqrSTUvwxYZ`.

**Важно:** Этот токен — секретный ключ, его нельзя показывать другим.


## Установка библиотеки

Откройте терминал или командную строку и выполните команду:

```bash
pip install pyTelegramBotAPI
```

или

```bash
pip install telebot
```

## Создание простого бота на Python

Создайте файл, например, `bot.py`, и вставьте следующий код:

```python
import telebot

# Вставьте сюда ваш токен
TOKEN = 'ВАШ_ТОКЕН_ЗДЕСЬ'

# Создаем экземпляр бота
bot = telebot.TeleBot(TOKEN)

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.reply_to(message, 'Привет! Я ваш первый бот на Python с помощью telebot.')

# Запуск polling
if __name__ == '__main__':
    bot.polling()
```

**Обратите внимание:** замените `'ВАШ_ТОКЕН_ЗДЕСЬ'` на токен, который вы получили от BotFather.


## Запуск бота

В терминале перейдите в папку с файлом `bot.py` и выполните:

```bash
python bot.py
```

Если всё сделано правильно, бот запустится и начнет слушать входящие сообщения.

## Проверка работы бота

1. Откройте Telegram.
2. Найдите вашего бота по имени пользователя (например, `@my_first_bot`).
3. Напишите команду `/start`.
4. Бот должен ответить: "Привет! Я ваш первый бот на Python."

## Расширение функционала

Теперь вы можете добавлять новые команды или обрабатывать сообщения по вашему желанию.

### Пример: команда /help

Добавьте обработчик:

```python
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Доступные команды:\n/start - начать общение\n/help - помощь')

# В функции main() добавьте:
app.add_handler(CommandHandler('help', help_command))
```

### Обработка текстовых сообщений

```python
from telegram.ext import MessageHandler, filters

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    await update.message.reply_text(f'Вы сказали: {text}')

# В функции main() добавьте:
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
```

## Полезные советы

- Храните токен в отдельном файле или переменной окружения для безопасности.
- Используйте декораторы `@bot.message_handler()` для обработки команд и сообщений.
- Для более сложных сценариев изучайте документацию [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI).


## Итог:
Вы создали своего первого Telegram-бота на Python с помощью библиотеки `telebot`. Теперь можно расширять его функционал — добавлять новые команды, обрабатывать разные типы сообщений или интегрировать внешние сервисы.

