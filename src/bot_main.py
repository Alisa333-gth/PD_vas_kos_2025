import telebot
import random
from telebot import types

# Замените 'YOUR_TOKEN' на полученный от BotFather токен
TOKEN = '7285559383:AAE5sC3yZV-K-T7olg1SgOGXMGZPZ5L74Dw'
bot = telebot.TeleBot(TOKEN)

# Словарь для хранения состояния игры для каждого пользователя
games = {}


def generate_number():
    """Генерирует 4-значное число с уникальными цифрами"""
    digits = list(range(10))
    random.shuffle(digits)
    return ''.join(map(str, digits[:4]))  # Преобразуем в строку для удобства сравнения


def count_bulls_and_cows(secret, guess):
    """Подсчет быков и коров"""
    bulls = sum(s == g for s, g in zip(secret, guess))
    cows = sum(g in secret for g in guess) - bulls
    return bulls, cows


@bot.message_handler(commands=['start', 'game'])
def start_game(message):
    """Начало новой игры"""
    chat_id = message.chat.id
    games[chat_id] = {
        'secret': generate_number(),
        'attempts': 0,
        'history': []
    }

    text = (
        "🐮🐂 Игра 'Быки и коровы' началась!\n"
        "Я загадал 4-значное число с уникальными цифрами.\n"
        "Присылай свои варианты, и я скажу сколько быков и коров!\n"
        "Чтобы сдаться, напиши /stop"
    )
    bot.send_message(chat_id, text)


@bot.message_handler(commands=['stop'])
def stop_game(message):
    """Остановка текущей игры"""
    chat_id = message.chat.id
    if chat_id in games:
        secret = games[chat_id]['secret']
        del games[chat_id]
        bot.send_message(chat_id, f"Игра остановлена. Загаданное число было: {secret}")
    else:
        bot.send_message(chat_id, "Сейчас нет активной игры. Начни новую через /game")


@bot.message_handler(func=lambda message: True)
def handle_guess(message):
    """Обработка догадки пользователя"""
    chat_id = message.chat.id
    guess = message.text.strip()

    # Проверка активной игры
    if chat_id not in games:
        bot.send_message(chat_id, "Сначала начни игру через /game")
        return

    # Валидация ввода
    if not guess.isdigit() or len(guess) != 4 or len(set(guess)) != 4:
        bot.send_message(chat_id, "Некорректный ввод! Нужно 4 уникальные цифры (например: 1234)")
        return

    game = games[chat_id]
    secret = game['secret']
    game['attempts'] += 1

    # Подсчет быков и коров
    bulls, cows = count_bulls_and_cows(secret, guess)

    # Проверка победы
    if bulls == 4:
        del games[chat_id]
        bot.send_message(chat_id, f"🎉 Победа! Ты угадал число {secret} за {game['attempts']} попыток!")
        return

    # Добавление в историю
    game['history'].append(f"{guess} - 🐂{bulls} 🐮{cows}")

    # Формирование ответа
    response = [
                   f"Результат: 🐂{bulls} 🐮{cows}",
                   f"Попытка №{game['attempts']}",
                   "История попыток:"
               ] + game['history'][-3:]  # Показываем последние 3 попытки

    bot.send_message(chat_id, "\n".join(response))


if __name__ == '__main__':
    bot.polling(none_stop=True)
