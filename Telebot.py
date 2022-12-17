import telebot

TOKEN = "5957442226:AAHMG7V5KEDbLTnYpDNS1TTfxg1tRq_jr5g"

bot = telebot.TeleBot(TOKEN)
@bot.message_handler(filter)
def function_name(message):
    bot.reply_to(message, "This is a message handler")