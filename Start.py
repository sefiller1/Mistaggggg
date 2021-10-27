import os, logging, asyncio
from telethon import Button
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins



@client.on(events.NewMessage(pattern="^/start$"))
async def start(event):
  await event.reply("**Etiketleme Botu**, Grup veya kanaldaki neredeyse tüm üyelerden bahsedebilir ★\nDaha fazla bilgi için **/help**'i tıklayın.",
                    buttons=(
                      [Button.url('🌟 Beni Bir Gruba Ekle', 'https://t.me/MissTagBot?startgroup=a'),
                      Button.url('Müzik Botu', 'https://t.me/missmusicsbot'),
                      Button.url('👮‍♂️ Sahibim', 'https://t.me/MissKraL')]
                    ),
                    link_preview=False
                   )
@client.on(events.NewMessage(pattern="^/help$"))
async def help(event):
  helptext = """**Miss Tag Bot'un Yardım Menüsü**\n\nKomut: /Toplan \n  Bu komutu, başkalarına bahsetmek istediğiniz metinle birlikte kullanabilirsiniz. \n`Örnek: /Toplan Günaydın!`  \nBu komutu yanıt olarak kullanabilirsiniz. herhangi bir mesaj Bot, yanıtlanan iletiye kullanıcıları etiketleyerek ve /bitir yazarak etiketleme işlemi biter.
\nAdminleri etiketlemek için ise /admin \n komutunu kullanabilirsiniz sevgiler"""
  await event.reply(helptext,
                    buttons=(
                      [Button.url('🌟 Beni Bir Gruba Ekle', 'https://t.me/MİSStagBot?startgroup=a'),
                       Button.url('📣 Support', 'https://t.me/MissMusicSupport'),
                      Button.url('👮‍♂️ Sahibim', 'https://t.me/MissKraL')]
                    ),
                    link_preview=False
                   )
