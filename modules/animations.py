import asyncio
from datetime import datetime
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait

from utils import modules_help, prefix

@Client.on_message(filters.command(["type"], prefix) & filters.me)
async def typewriter_cmd(client: Client, message: Message):
    if len(message.command) < 2:
        return await message.edit(f"<b>[VizX]</b> ❌ <code>Usage: {prefix}type [text]</code>")

    text = message.text.split(maxsplit=1)[1]
    typing_symbol = "▒"
    current_text = ""

    for char in text:
        current_text += char
        try:
            await message.edit(f"<b>[VizX]</b> <code>{current_text}{typing_symbol}</code>")
            await asyncio.sleep(0.1)
        except FloodWait as e:
            await asyncio.sleep(e.value)
        except Exception:
            pass

    # Final edit without the typing symbol
    try:
        await message.edit(f"<b>[VizX]</b> <code>{current_text}</code>")
    except Exception:
        pass


@Client.on_message(filters.command(["ghost"], prefix) & filters.me)
async def ghost_cmd(client: Client, message: Message):
    if len(message.command) < 3:
        return await message.edit(f"<b>[VizX]</b> ❌ <code>Usage: {prefix}ghost [seconds] [text]</code>")

    try:
        seconds = int(message.command[1])
    except ValueError:
        return await message.edit(f"<b>[VizX]</b> ❌ <code>Seconds must be an integer!</code>")

    text = message.text.split(maxsplit=2)[2]
    
    await message.edit(f"👻 <b>[Ghost Message]</b>\n\n{text}\n\n<i>(Self-destructing in {seconds}s...)</i>")
    
    await asyncio.sleep(seconds)
    await message.delete()


@Client.on_message(filters.command(["aping"], prefix) & filters.me)
async def aping_cmd(client: Client, message: Message):
    start = datetime.now()
    
    bars = ["▒▒▒▒▒▒▒", "█▒▒▒▒▒▒", "███▒▒▒▒", "█████▒▒", "███████"]
    
    for bar in bars:
        try:
            await message.edit(f"<b>[VizX]</b> <code>PINGING</code> {bar}")
            await asyncio.sleep(0.2)
        except FloodWait as e:
            await asyncio.sleep(e.value)
        except Exception:
            pass
            
    end = datetime.now()
    latency = round((end - start).microseconds / 1000, 2)
    
    await message.edit(f"<b>[VizX]</b> <code>PING</code> → <b>{latency}ms</b> ⚡\n<i>(Animated)</i>")


modules_help["animations"] = {
    "type [text]": "Typewriter effect for your message",
    "ghost [seconds] [text]": "Send a self-destructing message",
    "aping": "Animated ping command",
}
