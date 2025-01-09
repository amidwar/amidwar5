from telegram.ext import Updater, CommandHandler
import requests

# إعداد التوكن الخاص بالبوت
TELEGRAM_TOKEN = "8166763619:AAHfd3_oAPNbiuaqcqfEPR7yJDRvAqo6bVM"  # استبدل بالتوكن الخاص بك

# دالة الترحيب
def start(update, context):
    update.message.reply_text('مرحبًا! أنا بوت العملات الرقمية. استخدم /price لمعرفة سعر البيتكوين.')

# دالة جلب سعر البيتكوين من CoinGecko API
def get_price(update, context):
    try:
        url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true"
        response = requests.get(url)
        data = response.json()

        if 'bitcoin' in data:
            bitcoin_data = data['bitcoin']
            update.message.reply_text(
                f"بيانات البيتكوين:\n"
                f"السعر: ${bitcoin_data['usd']}\n"
                f"التغيير (24h): {bitcoin_data['usd_24h_change']:.2f}%\n"
                f"القيمة السوقية: ${bitcoin_data['usd_market_cap']:,.2f}\n"
                f"حجم التداول (24h): ${bitcoin_data['usd_24h_vol']:,.2f}"
            )
        else:
            update.message.reply_text("تعذر جلب البيانات. حاول لاحقًا.")
    except Exception as e:
        update.message.reply_text(f"حدث خطأ: {e}")

# الدالة الرئيسية
def main():
    updater = Updater(TELEGRAM_TOKEN, use_context=True)
    dp = updater.dispatcher

    # إضافة الأوامر
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("price", get_price))

    # بدء البوت
    updater.start_polling()
    updater.idle()

# تشغيل الدالة الرئيسية
if __name__ == "__main__":
    main()