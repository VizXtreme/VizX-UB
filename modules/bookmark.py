from pyrogram import Client, filters
from pyrogram.types import Message

from utils import modules_help, prefix

@Client.on_message(filters.command(["sv", "mark"], prefix) & filters.me)
async def bookmark_cmd(client: Client, message: Message):
    if not message.reply_to_message:
        return await message.edit(f"<b>[VizX]</b> ❌ <code>Reply to a message to save it.</code>")

    tag = ""
    if len(message.command) > 1:
        tag = " ".join(message.command[1:])
        if not tag.startswith("#"):
            tag = f"#{tag}"

    await message.edit("<b>[VizX]</b> ⏳ <code>Saving...</code>")
    
    # Forward the message to Saved Messages ("me")
    fwd_msg = await message.reply_to_message.forward("me")
    
    if tag:
        # Send the tag as a reply to the forwarded message in Saved Messages
        await client.send_message(
            "me", 
            f"🔖 <b>Saved via VizX-UB</b>\n{tag}", 
            reply_to_message_id=fwd_msg.id
        )
        
    await message.edit(f"<b>[VizX]</b> ✅ <code>Message saved to bookmarks!</code> {tag}")


modules_help["bookmark"] = {
    "sv [tag]": "Save replied message to Saved Messages",
    "mark [tag]": "Save replied message to Saved Messages",
}
