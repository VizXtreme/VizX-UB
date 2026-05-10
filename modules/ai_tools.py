import aiohttp
import os
import base64
from pyrogram import Client, filters
from pyrogram.types import Message

from utils import modules_help, prefix
from utils.config import gemini_key

async def ask_gemini(prompt: str, image_path: str = None) -> str:
    if not gemini_key:
        return "❌ <b>GEMINI_KEY is not configured!</b>"

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={gemini_key}"
    
    parts = [{"text": prompt}]
    
    if image_path:
        with open(image_path, "rb") as f:
            b64_img = base64.b64encode(f.read()).decode("utf-8")
        parts.append({
            "inline_data": {
                "mime_type": "image/jpeg",
                "data": b64_img
            }
        })
        
    payload = {
        "contents": [{"parts": parts}],
        "generationConfig": {"temperature": 0.7}
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=payload) as resp:
            if resp.status == 200:
                data = await resp.json()
                try:
                    return data["candidates"][0]["content"]["parts"][0]["text"]
                except KeyError:
                    return "❌ <b>AI returned an unexpected response format.</b>"
            else:
                return f"❌ <b>API Error {resp.status}:</b> {await resp.text()}"


@Client.on_message(filters.command(["tldr"], prefix) & filters.me)
async def tldr_cmd(client: Client, message: Message):
    if not message.reply_to_message or not message.reply_to_message.text:
        return await message.edit(f"<b>[VizX]</b> ❌ <code>Reply to a text message to summarize it.</code>")
    
    await message.edit("<b>[VizX]</b> ⏳ <code>Summarizing...</code>")
    text_to_summarize = message.reply_to_message.text
    prompt = f"Please summarize the following text into 3 concise bullet points:\n\n{text_to_summarize}"
    
    response = await ask_gemini(prompt)
    await message.edit(f"📘 <b>VizX-UB</b> │ <code>TL;DR</code>\n\n{response}")


@Client.on_message(filters.command(["tr"], prefix) & filters.me)
async def tr_cmd(client: Client, message: Message):
    if not message.reply_to_message or not message.reply_to_message.text:
        return await message.edit(f"<b>[VizX]</b> ❌ <code>Reply to a text message to translate it.</code>")
        
    lang = "English"
    if len(message.command) > 1:
        lang = " ".join(message.command[1:])
        
    await message.edit(f"<b>[VizX]</b> ⏳ <code>Translating to {lang}...</code>")
    text_to_translate = message.reply_to_message.text
    prompt = f"Translate the following text to {lang}. Only return the translation, no other text:\n\n{text_to_translate}"
    
    response = await ask_gemini(prompt)
    await message.edit(f"<b>[VizX]</b> 🌐 <code>Translation ({lang})</code>\n\n{response}")


@Client.on_message(filters.command(["vision", "ask"], prefix) & filters.me)
async def vision_cmd(client: Client, message: Message):
    prompt = "Describe this image in detail."
    if len(message.command) > 1:
        prompt = " ".join(message.command[1:])
        
    await message.edit("<b>[VizX]</b> ⏳ <code>Thinking...</code>")
    
    image_path = None
    if message.reply_to_message and message.reply_to_message.photo:
        await message.edit("<b>[VizX]</b> ⏳ <code>Downloading image...</code>")
        image_path = await message.reply_to_message.download()
    elif not message.reply_to_message and len(message.command) < 2:
        return await message.edit(f"<b>[VizX]</b> ❌ <code>Provide a prompt or reply to an image!</code>")
        
    response = await ask_gemini(prompt, image_path)
    
    if image_path and os.path.exists(image_path):
        os.remove(image_path)
        
    await message.edit(f"🤖 <b>[VizX AI]</b>\n\n{response}")


modules_help["ai_tools"] = {
    "tldr [reply]": "Summarize a long message",
    "tr [lang] [reply]": "Translate a message (defaults to English)",
    "ask [prompt]": "Ask the AI a question",
    "vision [prompt] [reply to image]": "Ask the AI about an image",
}
