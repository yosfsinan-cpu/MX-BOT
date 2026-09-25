import datetime
import os
import telebot

# لێرە تـۆکنێ بۆتێ خۆ دانی (یان ل Railway وەک Environment Variable دانە)
TOKEN = os.getenv("BOT_TOKEN", "LERA_TOKEN_XWE_DANE")
bot = telebot.TeleBot(TOKEN)


# **1. فەرمانا Start و خێرھاتنێ (ب کوردی بادینی)**
@bot.message_handler(commands=['start'])
def send_welcome(message):
  user_id = message.from_user.id
  first_name = message.from_user.first_name
  username = (
      message.from_user.username
      if message.from_user.username
      else "نەدیار"
  )

  # دەم و روژا نها
  now = datetime.datetime.now()
  date_time = now.strftime("%Y-%m-%d | %H:%M:%S")

  # پەیاما خێرئاتنێ و نیشاندانا زانیاریێن کەسی
  welcome_text = (
      f"سلاڤ و رێز، بەڕێز **{first_name}**!\n\n"
      "بەخێر هات بۆ بۆتا **MX BOT**. ئەز ل ڤێرەم دا خزمەتا تە بکەم.\n\n"
      "📌 **زانیاریێن تە یێن تۆمارکری:**\n"
      f"🆔 **ID:** `{user_id}`\n"
      f"👤 **Username:** @{username}\n"
      f"📅 **دەمێ تێگەهشتنێ:** {date_time}\n\n"
      "بۆت نوکە ئامادەیە و کاردکەت!"
  )

  bot.reply_to(message, welcome_text, parse_mode="Markdown")

  # ئەگەر تە بڤێت هەر کەسەک /start لێدەت، بۆتە دۆسە یان ئاگەهداریەکێ بۆ تە (وەک خودانێ بۆتی) بنێرێت:
  # admin_id = 123456789  <- ژمارا ID یا خۆ لێرە دانە
  # bot.send_message(admin_id, f"کاربەرەکێ نوی /start لێدا:\n🆔 ID: {user_id}\n👤 Nav: {first_name}")


# **2. چاڤدێریا گروپان، کەناڵان و پەیامان (ID, Nav, Date)**
@bot.message_handler(
    func=lambda message: True,
    content_types=['text', 'photo', 'video', 'document'],
)
def track_everything(message):
  user_id = message.from_user.id
  first_name = message.from_user.first_name
  chat_type = message.chat.type  # (private, group, supergroup, channel)

  now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

  # دیارکرنا کو پەیام ژ کیڤە هاتیە (تایبەت، گروپ یان کەناڵ)
  if chat_type == 'private':
    place = 'چاتێ تایبەت (Private)'
  elif chat_type in ['group', 'supergroup']:
    place = f"گروپ: {message.chat.title} (ID: {message.chat.id})"
  else:
    place = f"کەناڵ/دیتر: {message.chat.title}"

  # لێرە د کۆنصۆلێ (Terminal) دا زانیاریێن هەر پەیامەکێ دەرئێخە
  print(
      f"[{now}] پەیام هات -> کاربەر: {first_name} (ID: {user_id}) | جهـ: {place}"
  )


if __name__ == '__main__':
  print('MX BOT دەست ب کار بوو...')
  bot.infinity_polling()
