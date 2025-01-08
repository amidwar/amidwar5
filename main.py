from telegram.ext import Updater, CommandHandler
from pycoingecko import CoinGeckoAPI

# إنشاء كائن CoinGecko
cg = CoinGeckoAPI()

# دالة الترحيب
def start(update, context):
    update.message.reply_text('مرحبًا! أنا بوت العملات الرقمية. استخدم /price لمعرفة سعر البيتكوين.')

# دالة الحصول على سعر البيتكوين
def get_price(update, context):
    price = cg.get_price(ids='bitcoin', vs_currencies='usd')
    update.message.reply_text(f"سعر البيتكوين الحالي: ${price['bitcoin']['usd']}")

# الدالة الرئيسية
def main():
    # ضع التوكن الخاص بك هنا بين علامات الاقتباس
    token = "8166763619:AAHfd3_oAPNbiuaqcqfEPR7yJDRvAqo6bVM" 
 # استبدل بالتوكن الخاص بك
    updater = Updater(token, use_context=True)
    dp = updater.dispatcher

    # إضافة الأوامر
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("price", get_price))

    # بدء البوت
    updater.start_polling()
    updater.idle()

# تشغيل الدالة الرئيسية
if __name__ == "__main__":