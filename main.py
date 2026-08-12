import os
import discord
from discord.ext import commands
from flask import Flask
from threading import Thread

# --- خادم وهمي لمنع Render من المطالبة ببطاقة دفع ---
app = Flask('')

@app.route('/')
def home():
    return "Bot is Alive!"

def run():
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = Thread(target=run)
    t.start()

# --- إعدادات البوت ---
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'✅ تم تسجيل الدخول بنجاح باسم البوت: {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if 'العمدة' in message.content:
        await message.channel.send('الان يجيك!')
        
    await bot.process_commands(message)

@bot.command(name='نبض')
async def ping(ctx):
    latency = round(bot.latency * 1000)
    await ctx.send(f'🏓 سرعة الاستجابة: {latency}ms')

# تشغيل الخادم الوهمي ثم البوت
keep_alive()
TOKEN = os.environ.get('DISCORD_BOT_TOKEN')
if TOKEN:
    bot.run(TOKEN)
