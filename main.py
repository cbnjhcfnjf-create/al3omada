import os
import discord
from discord.ext import commands

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
        await message.channel.send('العمدة مشغول الان يجيك')

    await bot.process_commands(message)

@bot.command(name='نبض')
async def ping(ctx):
    latency = round(bot.latency * 1000)
    await ctx.send(f'🟢 البوت شغال ومتصل! سرعة الاستجابة: {latency}ms')

@bot.command(name='مساعدة')
async def help_command(ctx):
    help_text = (
        "**قائمة الأوامر المتاحة:**\n"
        "• `/نبض` - للتأكد من اتصال البوت وسرعة الاستجابة.\n"
        "• `/مساعدة` - لعرض هذه القائمة.\n"
        "• كتابة كلمة **العمدة** في الشات للرد التلقائي."
    )
    await ctx.send(help_text)

TOKEN = os.getenv("DISCORD_BOT_TOKEN")

if TOKEN:
    bot.run(TOKEN)
else:
    print("❌ خطأ: لم يتم العثور على DISCORD_BOT_TOKEN!")
