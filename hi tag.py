from DAXXMUSIC import app 
import asyncio
import random
from pyrogram import Client, filters
from pyrogram.enums import ChatType, ChatMemberStatus
from pyrogram.errors import UserNotParticipant
from pyrogram.types import ChatPermissions

spam_chats = []

EMOJI = [ "🦋🦋🦋🦋🦋",
          "🧚🌸🧋🍬🫖",
          "🥀🌷🌹🌺💐",
          "🌸🌿💮🌱🌵",
          "❤️💚💙💜🖤",
          "💓💕💞💗💖",
          "🌸💐🌺🌹🦋",
          "🍔🦪🍛🍲🥗",
          "🍎🍓🍒🍑🌶️",
          "🧋🥤🧋🥛🍷",
          "🍬🍭🧁🎂🍡",
          "🍨🧉🍺☕🍻",
          "🥪🥧🍦🍥🍚",
          "🫖☕🍹🍷🥛",
          "☕🧃🍩🍦🍙",
          "🍁🌾💮🍂🌿",
          "🌨️🌥️⛈️🌩️🌧️",
          "🌷🏵️🌸🌺💐",
          "💮🌼🌻🍀🍁",
          "🧟🦸🦹🧙👸",
          "🧅🍠🥕🌽🥦",
          "🐷🐹🐭🐨🐻‍❄️",
          "🦋🐇🐀🐈🐈‍⬛",
          "🌼🌳🌲🌴🌵",
          "🥩🍋🍐🍈🍇",
          "🍴🍽️🔪🍶🥃",
          "🕌🏰🏩⛩️🏩",
          "🎉🎊🎈🎂🎀",
          "🪴🌵🌴🌳🌲",
          "🎄🎋🎍🎑🎎",
          "🦅🦜🕊️🦤🦢",
          "🦤🦩🦚🦃🦆",
          "🐬🦭🦈🐋🐳",
          "🐔🐟🐠🐡🦐",
          "🦩🦀🦑🐙🦪",
          "🐦🦂🕷️🕸️🐚",
          "🥪🍰🥧🍨🍨",
          " 🥬🍉🧁🧇",
        ]

TAGMES = [ " **➠ बेबी कहा हो। 🤗** ",
           " **➠ ओए सो गए क्या, ऑनलाइन आओ ।😊** ",
           " **➠ ओए वीसी आओ बात करते हैं । 😃** ",
           " **➠ खाना खाया कि नही। 🥲** ",
           " **➠ घर में सब कैसे हैं। 🥺** ",
           " **➠ पता है बहुत याद आ रही आपकी। 🤭** ",
           " **➠ और बताओ कैसे हो।..?? 🤨** ",
           " **➠ मेरी भी सैटिंग करवा दो प्लीज..?? 🙂** ",
           " **➠ आपका नाम क्या है।..?? 🥲** ",
           " **➠ नाश्ता हो गया..?? 😋** ",
           " **➠ मुझे अपने ग्रूप में ऐड कर लो। 😍** ",
           " **➠ आपका दोस्त आपको बुला रहा है। 😅** ",
           " **➠ मुझसे शादी करोगे ..?? 🤔** ",
           " **➠ सोने चले गए क्या 🙄** ",
           " **➠ अरे यार कोई AC चला दो 😕** ",
           " **➠ आप कहा से हो..?? 🙃** ",
           " **➠ हेलो जी नमस्ते 😛** ",
           " **➠ BABY क्या कर रही हो..? 🤔** ",
           " **➠ क्या आप मुझे जानते हो .? ☺️** ",
           " **➠ आओ baby Ludo खेलते है .🤗** ",
           " **➠ चलती है क्या 9 से 12... 😇** ",
           " **➠ आपके पापा क्या करते है 🤭** ",
           " **➠ आओ baby बाजार चलते है गोलगप्पे खाने। 🥺** ",
           " **➠ अकेली ना बाजार जाया करो, नज़र लग जायेगी। 😶** ",
           " **➠ और बताओ BF कैसा है ..?? 🤔** ",
           " **➠ गुड मॉर्निंग 😜** ",
           " **➠ मेरा एक काम करोगे। 🙂** ",
           " **➠ DJ वाले बाबू मेरा गाना चला दो। 😪** ",
           " **➠ आप से मिलकर अच्छा लगा।☺** ",
           " **➠ मेरे बाबू ने थाना थाया।..? 🙊** ",
           " **➠ पढ़ाई कैसी चल रही हैं ? 😺** ",
           " **➠ हम को प्यार हुआ। 🥲** ",
           " **➠ Nykaa कौन है...? 😅** ",
           " **➠ तू खींच मेरी फ़ोटो ..? 😅** ",
           " **➠ Phone काट मम्मी आ गई क्या। 😆** ",
           " **➠ और भाबी से कब मिल वा रहे हो । 😉** ",
           " **➠ क्या आप मुझसे प्यार करते हो 💚** ",
           " **➠ मैं तुम से बहुत प्यार करती हूं..? 👀** ",
           " **➠ बेबी एक kiss दो ना..?? 🙉** ",
           " **➠ एक जॉक सुनाऊं..? 😹** ",
           " **➠ vc पर आओ कुछ दिखाती हूं  😻** ",
           " **➠ क्या तुम instagram चलते हो..?? 🙃** ",
           " **➠ whatsapp नंबर दो ना अपना..? 😕** ",
           " **➠ आप की दोस्त से मेरी सेटिंग करा दो ..? 🙃** ",
           " **➠ सारा काम हो गया हो तो ऑनलाइन आ जाओ।..? 🙃** ",
           " **➠ कहा से हो आप 😊** ",
           " **➠ जा तुझे आज़ाद कर दिया मैंने मेरे दिल से। 🥺** ",
           " **➠ मेरा एक काम करोगे, ग्रूप मे कुछ मेंबर ऐड कर दो ..? ♥️** ",
           " **➠ मैं तुमसे नाराज़ हूं 😠** ",
           " **➠ आपकी फैमिली कैसी है..? ❤** ",
           " **➠ क्या हुआ..? 🤔** ",
           " **➠ बहुत याद आ रही है आपकी 😒** ",
           " **➠ भूल गए मुझे 😏** ",
           " **➠ झूठ क्यों बोला आपने मुझसे 🤐** ",
           " **➠ इतना भाव मत खाया करो, रोटी खाया करो कम से कम मोटी तो हो जाओगी 😒** ",
           " **➠ ये attitude किसे दिखा रहे हो 😮** "
           " **➠ हेमलो कहा busy ho 👀** ",
           " **➠ आपके जैसा दोस्त पाकर मे बहुत खुश हूं। 🙈** ",
           " **➠ आज मन बहुत उदास है ☹️** ",
           " **➠ मुझसे भी बात कर लो ना 🥺** ",
           " **➠ आज खाने में क्या बनाया है 👀** ",
           " **➠ क्या चल रहा है 🙂** ",
           " **➠ ᴄʜᴀᴛᴛɪɴɢ ᴋᴀʀ ʟᴏ ɴᴀ..🥺** ",
           " **➠ ᴍᴇ ᴍᴀsᴏᴏᴍ ʜᴜ ɴᴀ 🥺** ",
           " **➠ ᴋᴀʟ ᴍᴀᴊᴀ ᴀʏᴀ ᴛʜᴀ ɴᴀ 😅** ",
           " **➠ ɢʀᴏᴜᴘ ᴍᴇ ʙᴀᴀᴛ ᴋʏᴜ ɴᴀʜɪ ᴋᴀʀᴛᴇ ʜᴏ 😕** ",
           " **➠ ᴀᴀᴘ ʀᴇʟᴀᴛɪᴏᴍsʜɪᴘ ᴍᴇ ʜᴏ..? 👀** ",
           " **➠ ᴋɪᴛɴᴀ ᴄʜᴜᴘ ʀᴀʜᴛᴇ ʜᴏ ʏʀʀ 😼** ",
           " **➠ ᴀᴀᴘᴋᴏ ɢᴀɴᴀ ɢᴀɴᴇ ᴀᴀᴛᴀ ʜᴀɪ..? 😸** ",
           " **➠ ɢʜᴜᴍɴᴇ ᴄʜᴀʟᴏɢᴇ..?? 🙈** ",
           " **➠ ᴋʜᴜs ʀᴀʜᴀ ᴋᴀʀᴏ 🤞** ",
           " **➠ ʜᴀᴍ ᴅᴏsᴛ ʙᴀɴ sᴀᴋᴛᴇ ʜᴀɪ...? 🥰** ",
           " **➠ ᴋᴜᴄʜ ʙᴏʟ ᴋʏᴜ ɴʜɪ ʀᴀʜᴇ ʜᴏ.. 🥺** ",
           " **➠ ᴋᴜᴄʜ ᴍᴇᴍʙᴇʀs ᴀᴅᴅ ᴋᴀʀ ᴅᴏ 🥲** ",
           " **➠ sɪɴɢʟᴇ ʜᴏ ʏᴀ ᴍɪɴɢʟᴇ 😉** ",
           " **➠ ᴀᴀᴏ ᴘᴀʀᴛʏ ᴋᴀʀᴛᴇ ʜᴀɪɴ 🥳** ",
           " **➠ ʙɪᴏ ᴍᴇ ʟɪɴᴋ ʜᴀɪ ᴊᴏɪɴ ᴋᴀʀ ʟᴏ 🧐** ",
           " **➠ ᴍᴜᴊʜᴇ ʙʜᴜʟ ɢʏᴇ ᴋʏᴀ 🥺** ",
           " **➠ ʏᴀʜᴀ ᴀᴀ ᴊᴀᴏ @THE_FRIENDZ ᴍᴀsᴛɪ ᴋᴀʀᴇɴɢᴇ 🤭** ",
           " **➠ ᴛʀᴜᴛʜ ᴀɴᴅ ᴅᴀʀᴇ ᴋʜᴇʟᴏɢᴇ..? 😊** ",
           " **➠ ᴀᴀᴊ ᴍᴜᴍᴍʏ ɴᴇ ᴅᴀᴛᴀ ʏʀʀ 🥺** ",
           " **➠ मेरा ग्रुप भी join कर लो ना 🤗** ",
           " **➠ मैने तेरा नाम Dil rakh diya 😗** ",
           " **➠ तुमारे सारे दोस्त कहा गए 🥺** ",
           " **➠ my cute owner @RoY_EdiTX 🥰** ",
           " **➠ किसकी याद मे खोए हो जान 😜** ",
           " **➠ गुड नाईट जी बहुत रात हो गई 🥰** ",
           ]

VC_TAG = [ "**➠ ᴏʏᴇ ᴠᴄ ᴀᴀᴏ ɴᴀ ᴘʟs 😒**",
         "**➠ ᴊᴏɪɴ ᴠᴄ ғᴀsᴛ ɪᴛs ɪᴍᴀᴘᴏʀᴛᴀɴᴛ 😐**",
         "**➠ ʙᴀʙʏ ᴄᴏᴍᴇ ᴏɴ ᴠᴄ ғᴀsᴛ 🙄**",
         "**➠ ᴄʜᴜᴘ ᴄʜᴀᴘ ᴠᴄ ᴘʀ ᴀᴀᴏ 🤫**",
         "**➠ ᴍᴀɪɴ ᴠᴄ ᴍᴇ ᴛᴜᴍᴀʀᴀ ᴡᴀɪᴛ ᴋʀ ʀʜɪ 🥺**",
         "**➠ ᴠᴄ ᴘᴀʀ ᴀᴀᴏ ʙᴀᴀᴛ ᴋʀᴛᴇ ʜᴀɪ ☺️**",
         "**➠ ʙᴀʙᴜ ᴠᴄ ᴀᴀ ᴊᴀɪʏᴇ ᴇᴋ ʙᴀʀ 🤨**",
         "**➠ ᴠᴄ ᴘᴀʀ ʏᴇ ʀᴜssɪᴀɴ ᴋʏᴀ ᴋᴀʀ ʀʜɪ ʜᴀɪ 😮‍💨**",
         "**➠ ᴠᴄ ᴘᴀʀ ᴀᴀᴏ ᴠᴀʀɴᴀ ʙᴀɴ ʜᴏ ᴊᴀᴏɢᴇ 🤭**",
         "**➠ sᴏʀʀʏ ʙᴀʙʏ ᴘʟs ᴠᴄ ᴀᴀ ᴊᴀᴏ ɴᴀ 😢**",
         "**➠ ᴠᴄ ᴀᴀɴᴀ ᴇᴋ ᴄʜɪᴊ ᴅɪᴋʜᴀᴛɪ ʜᴜ 😮**",
         "**➠ ᴠᴄ ᴍᴇ ᴄʜᴇᴄᴋ ᴋʀᴋᴇ ʙᴀᴛᴀɴᴀ ᴋᴏɴ sᴀ sᴏɴɢ ᴘʟᴀʏ ʜᴏ ʀʜᴀ ʜᴀɪ.. 💫**",
         "**➠ ᴠᴄ ᴊᴏɪɴ ᴋʀɴᴇ ᴍᴇ ᴋʏᴀ ᴊᴀᴛᴀ ʜᴀɪ ᴛʜᴏʀᴀ ᴅᴇʀ ᴋᴀʀ ʟᴏ ɴᴀ 😇**",
         "**➠ ᴊᴀɴᴇᴍᴀɴ ᴠᴄ ᴀᴀᴏ ɴᴀ ʟɪᴠᴇ sʜᴏᴡ ᴅɪᴋʜᴀᴛɪ ʜᴏᴏɴ.. 😵‍💫**",
         "**➠ ᴏᴡɴᴇʀ ʙᴀʙᴜ ᴠᴄ ᴛᴀᴘᴋᴏ ɴᴀ... 😕**",
         "**➠ ʜᴇʏ ᴄᴜᴛɪᴇ ᴠᴄ ᴀᴀɴᴀ ᴛᴏ ᴇᴋ ʙᴀᴀʀ... 🌟**",
         "**➠ ᴠᴄ ᴘᴀʀ ᴀᴀ ʀʜᴇ ʜᴏ ʏᴀ ɴᴀ... ✨**",
         "**➠ ᴠᴄ ᴘᴀʀ ᴀᴀ ᴊᴀ ᴠʀɴᴀ ɢʜᴀʀ sᴇ ᴜᴛʜᴡᴀ ᴅᴜɴɢɪ... 🌝**",
         "**➠ ʙᴀʙʏ ᴠᴄ ᴘᴀʀ ᴋʙ ᴀᴀ ʀʜᴇ ʜᴏ. 💯**",
        ]


@app.on_message(filters.command(["tagall", "tagmember" ], prefixes=["/", "@", "#"]))
async def mentionall(client, message):
    chat_id = message.chat.id
    if message.chat.type == ChatType.PRIVATE:
        return await message.reply("๏ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴏɴʟʏ ғᴏʀ ɢʀᴏᴜᴘs.")

    is_admin = False
    try:
        participant = await client.get_chat_member(chat_id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("๏ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀᴅᴍɪɴ ʙᴀʙʏ, ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴛᴀɢ ᴍᴇᴍʙᴇʀs. ")

    if message.reply_to_message and message.text:
        return await message.reply("/tagall ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ ᴛʏᴘᴇ ʟɪᴋᴇ ᴛʜɪs / ʀᴇᴘʟʏ ᴀɴʏ ᴍᴇssᴀɢᴇ ɴᴇxᴛ ᴛɪᴍᴇ ʙᴏᴛ ᴛᴀɢɢɪɴɢ...")
    elif message.text:
        mode = "text_on_cmd"
        msg = message.text
    elif message.reply_to_message:
        mode = "text_on_reply"
        msg = message.reply_to_message
        if not msg:
            return await message.reply("/tagall ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ ᴛʏᴘᴇ ʟɪᴋᴇ ᴛʜɪs / ʀᴇᴘʟʏ ᴀɴʏ ᴍᴇssᴀɢᴇ ɴᴇxᴛ ᴛɪᴍᴇ ғᴏᴛ ᴛᴀɢɢɪɴɢ...")
    else:
        return await message.reply("/tagall ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ ᴛʏᴘᴇ ʟɪᴋᴇ ᴛʜɪs / ʀᴇᴘʟʏ ᴀɴʏ ᴍᴇssᴀɢᴇ ɴᴇxᴛ ᴛɪᴍᴇ ʙᴏᴛ ᴛᴀɢɢɪɴɢ...")
    if chat_id in spam_chats:
        return await message.reply("๏ ᴘʟᴇᴀsᴇ ᴀᴛ ғɪʀsᴛ sᴛᴏᴘ ʀᴜɴɴɪɴɢ ᴍᴇɴᴛɪᴏɴ ᴘʀᴏᴄᴇss...")
    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.get_chat_members(chat_id):
        if not chat_id in spam_chats:
            break
        if usr.user.is_bot:
            continue
        usrnum += 1
        usrtxt += f"[{usr.user.first_name}](tg://user?id={usr.user.id}) "

        if usrnum == 1:
            if mode == "text_on_cmd":
                txt = f"{usrtxt} {random.choice(TAGMES)}"
                await client.send_message(chat_id, txt)
            elif mode == "text_on_reply":
                await msg.reply(f"[{random.choice(EMOJI)}](tg://user?id={usr.user.id})")
            await asyncio.sleep(4)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass


@app.on_message(filters.command(["vctag"], prefixes=["/", "@", "#"]))
async def mention_allvc(client, message):
    chat_id = message.chat.id
    if message.chat.type == ChatType.PRIVATE:
        return await message.reply("๏ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴏɴʟʏ ғᴏʀ ɢʀᴏᴜᴘs.")

    is_admin = False
    try:
        participant = await client.get_chat_member(chat_id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("๏ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀᴅᴍɪɴ ʙᴀʙʏ, ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴛᴀɢ ᴍᴇᴍʙᴇʀs. ")
    if chat_id in spam_chats:
        return await message.reply("๏ ᴘʟᴇᴀsᴇ ᴀᴛ ғɪʀsᴛ sᴛᴏᴘ ʀᴜɴɴɪɴɢ ᴍᴇɴᴛɪᴏɴ ᴘʀᴏᴄᴇss...")
    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.get_chat_members(chat_id):
        if not chat_id in spam_chats:
            break
        if usr.user.is_bot:
            continue
        usrnum += 1
        usrtxt += f"[{usr.user.first_name}](tg://user?id={usr.user.id}) "

        if usrnum == 1:
            txt = f"{usrtxt} {random.choice(VC_TAG)}"
            await client.send_message(chat_id, txt)
            await asyncio.sleep(4)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass



@app.on_message(filters.command(["cancel", "stop"]))
async def cancel_spam(client, message):
    if not message.chat.id in spam_chats:
        return await message.reply("๏ ᴄᴜʀʀᴇɴᴛʟʏ ɪ'ᴍ ɴᴏᴛ ᴛᴀɢɢɪɴɢ ʙᴀʙʏ.")
    is_admin = False
    try:
        participant = await client.get_chat_member(message.chat.id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("๏ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀᴅᴍɪɴ ʙᴀʙʏ, ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴛᴀɢ ᴍᴇᴍʙᴇʀs.")
    else:
        try:
            spam_chats.remove(message.chat.id)
        except:
            pass
        return await message.reply("๏ ᴍᴇɴᴛɪᴏɴ ᴘʀᴏᴄᴇss sᴛᴏᴘᴘᴇᴅ ๏")
