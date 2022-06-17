from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from config import BOT_USERNAME, BOT_NAME as bot
from helpers.filters import command, other_filters2
# EfsaneMusicVaves tarafından düzenlendi. 

@Client.on_message(command(["start", f"start@{BOT_USERNAME}"]))
async def start(_, message: Message):
                await message.reply_photo(
                "https://te.legra.ph//file/7da0b633df3bd002a4e5a.jpg",
                caption=(f"""**👋🏻Salam {message.from_user.mention} 🎵 \n Mənim adım {bot}! \n \n ℹ️Mən Səsli Söhbətlərdə Musiqi Oxuya Bilən Bir Botam \n \n ✅Botun istifadə qaydasını öyrənmək üçün /help əmrindən istifadə edin \n \n 🧔🏻Sahibim  [𝐆Ξ𝐍𝐂Ξ𝐋𝐈🥃🧊](https://t.me/o2o_GenCeLi)**"""),
         reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✅ Add me to your Group ✅", url=f"https://t.me/LegendMucisRobot?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🧔🏻Sahib", url="https://t.me/o2o_GenCeLi"
                    ),
                    InlineKeyboardButton(
                        "🇦🇿Rəsmi Kanal", url="https://t.me/SecretMMC"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "💡 Əmrlər" , callback_data= "cbhelp"
                    ),
                    InlineKeyboardButton(
                        "🇦🇿Rəsmi Group", url=f"https://t.me/SecretMMC"
                    )
                ]
                
           ]
        ),
    )
  


@Client.on_message(command(["help", f"help@{BOT_USERNAME}"]))
async def help(_, message: Message):
      await message.reply_text(" Səsli söhbətdə Musiqi oxuması üçün /play əmrindən istifadə edə bilərsiniz ⤵️ \n \n Məsələn: \n \n 1. `/play Ayaz Babayev - Sən Mənlə` \n 2. `/play https://youtu.be/qLXUa89Q5WI` \n \n /alive - Botun işlək olduğunu yoxlamaq üçün əmrdir. Yalnız Bot sahibi istifadə edə bilər. \n \n ⚠️ Botun qruplarda işləyə bilməsi üçün admin olmalıdır !", 
      reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "ℹ️ User Əmrləri", callback_data="herkes")
                 ],[                     
                     InlineKeyboardButton(
                         "✅ Admin əmrləri", callback_data="admin")
                 ],[
                     InlineKeyboardButton(
                         "Geri 🔄", callback_data="start")
                 ],[
                     InlineKeyboardButton(
                         "🧔🏻Sahib", url="https://t.me/o2o_GenCeLi")
                 ]
             ]
         )
    )


@Client.on_callback_query(filters.regex("cbhelp"))
async def cbbilgi(_, query: CallbackQuery):
    await query.edit_message_text(" Səsli söhbətdə Musiqi oxuması üçün /play əmrindən istifadə edə bilərsiniz ⤵️ \n \n Məsələn: \n \n 1. `/play Ayaz Babayev - Sən Mənlə` \n 2. `/play https://youtu.be/qLXUa89Q5WI` \n \n /alive - Botun işlək olduğunu yoxlamaq üçün əmrdir. Yalnız Bot sahibi istifadə edə bilər. \n \n ⚠️ Botun qruplarda işləyə bilməsi üçün admin olmalıdır !", 
    reply_markup=InlineKeyboardMarkup(
      [
        [
          InlineKeyboardButton(
            "ℹ️ User əmrləri", callback_data ="herkes")
        ],
        [
          InlineKeyboardButton(
            "✅ Admin əmrləri",callback_data ="admin")
        ],
        [
          InlineKeyboardButton(
            "🔄 Geri", callback_data="start")
        ],
        [
          InlineKeyboardButton(
            "🧔🏻Sahib", url="https://t.me/o2o_GenCeLi")
        ]
      ]
     ))


@Client.on_callback_query(filters.regex("herkes"))
async def herkes(_, query: CallbackQuery):
    await query.edit_message_text(f"""<b>Salam {query.from_user.mention}!\nBu botun hərkəs üçün əmr menyusu 😉\n\n ▶️ /play - Musiqi oxutmaq üçün youtube url'sinə vəya musiqi dosyasına yanıt verin\n ▶️ /play <song name> - İstədiyiniz musiqi oxut\n 🔴 \n 🎵 /song <song name> - İstədiyiniz musiqi sürətli bir şəkildə axtarın\n 🎵 /vbul - İstədiyiniz videoları sürətli bir şəkildə axtarın\n 🔍 /video <query> - Youtube'da olan videoları axtarın\n\n</b>""",
    reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "🧔🏻Sahib", url="https://t.me/o2o_GenCeLi")
                 ],
                 [
                     InlineKeyboardButton(
                         "️🔄 Geri", callback_data="cbhelp")
                 ] 
             ]
         )
         )


@Client.on_callback_query(filters.regex("admin"))
async def admin(_, query: CallbackQuery):
    await query.edit_message_text(f"""<b>Salam {query.from_user.mention}! \n Bu botun adminlər üçün əmr menyusu ✅ \n \n ▶️ /resume - Musiqi oxutmağa davam et\n ⏸️ /pause - Oxuyan musiqini dayandır \n 🔄 /skip - Sıraya alınmış musiqiyə keç\n ⏹ /end - Musiqi oxumanı dayandır \n 🔼 /promote - Botun sadəcə yönətici üçün olan əmrlərini istifadə üçün istifadəçiyə yetki ver \n 🔽 /demote - Botun yönətici əmrlərini istifadə edən istifadəçinin yetkisini al \n \n ⚪ /asistan - Musiqi asistanı qrupunuza qoşulur. \n \n </b>""",
    reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "🧔🏻Sahib", url="https://t.me/o2o_GenCeLi")
                 ],
                 [
                     InlineKeyboardButton(
                         "️🔄 Geri", callback_data="cbhelp")
                 ] 
             ]
         )
         )


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(f"""**👋🏻Salam {message.from_user.mention} 🎵 \n Mənim adım {bot}! \n \n ℹ️Mən Səsli Söhbətlərdə Musiqi Oxuya Bilən Bir Botam \n \n ✅Botun istifadə qaydasını öyrənmək üçün /help əmrindən istifadə edin \n \n 🧔🏻Sahibim  [𝐆Ξ𝐍𝐂Ξ𝐋𝐈🥃🧊](https://t.me/o2o_GenCeLi)**""",
         reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✅ Add me to your Group ✅", url=f"https://t.me/LegendMucisRobot?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🧔🏻Sahib", url="https://t.me/o2o_GenCeLi"
                    ),
                    InlineKeyboardButton(
                        "🇦🇿Rəsmi Kanal", url="https://t.me/SecretMMC"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "💡 Əmrlər", callback_data= "cbhelp"
                    ),
                    InlineKeyboardButton(
                        "🇦🇿Rəsmi Group", url=f"https://t.me/SecretMMC"
                    )
                ]
                
           ]
        ),
    )
