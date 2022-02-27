from pyrogram import Client, filters ,idle,__version__
from pyrogram.filters import group , new_chat_members , command , chat , text 
from pyrogram.errors import FloodWait, MessageNotModified
from pyrogram.types import Message
from pyrogram.raw.functions.messages import DeleteHistory
from pyrogram.types import ChatPermissions,ChatEventFilter
from pyrogram.raw.all import layer
from time import time
from datetime import datetime
from requests import get
from prettytable import PrettyTable
import wikipedia
import random
from asyncio import exceptions, gather
import asyncio
import jdatetime
from pyrogram.types import InlineKeyboardButton,InlineKeyboardMarkup
from pyrogram.raw.functions.messages import GetStickerSet
from pyrogram.errors import MessageNotModified,FloodWait
from contextlib import suppress
from html import escape
import requests
import os
import sys
from platform import python_version

session_string = "BABhW8W1KdObnFX31t2Esf6DKotj4m_rnR0s0CLRpzKbVmfWeon6dEgXqLyLj1WTmqLnQgU1Sx2owcyfduhO1BI5bIwDVbwuwUq3QxgRnxJvDXswwj3cC1qO5FF2PFTpYtP7a6Hh-803FRivNtOrECFUUT1OId6fkEm6tp5oCzwNRMWKysvTBfru-xnD6v5uDjlbEhsbleC1vEvUssedlVICxUVziiYt5UGNiCwhN3fiwS3bHNXua6-AbZehexq59AFGW7SjZSE_zEiqe4yk71zA9W3cCkxjFUtmeELiuiM5XTzqiPTbhfrQ3-WbsjVejmLSCoo5n0tbzssx8uBgYh7GfTBmRAA"

bot = Client(
    session_string,
    api_id =
    5892086,
    api_hash = "0735af1a9678868ae6ea64c652b813a3"
)

ETELAH = """"
سلام داوش تو که سلفمو ران کردی یه دعایی واسه ما کن
آپدیت سلف اینا هسته 
..
.dice2 Valeu 
.spam2 int | str
.app text search app 
.jok 
.join username 
.country name > info country
.move name > search Movie 
.porn 
.wikifa text > Farsi 
.webs link > screen shoter Site

بمولا مرام و معرفت 🤝
"""


with bot:
    adminbot=bot.get_me().mention
    me=bot.get_me().first_name
    bot.send_message("me", ETELAH)





KIR= """
⣠⡶⠚⠛⠲⢄⡀
⣼⠁      ⠀⠀⠀⠳⢤⣄
⢿⠀⢧⡀⠀⠀⠀⠀⠀⢈⡇
⠈⠳⣼⡙⠒⠶⠶⠖⠚⠉⠳⣄
⠀⠀⠈⣇⠀⠀⠀⠀⠀⠀⠀⠈⠳⣄
⠀⠀⠀⠘⣆       ⠀⠀⠀⠀⠀⠈⠓⢦⣀
⠀⠀⠀⠀⠈⢳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠲⢤
⠀⠀⠀⠀⠀⠀⠙⢦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢧
⠀⠀⠀⠀⠀⠀⠀    ⠓⠦⠀⠀⠀⠀
🚹 ¦ بیا بخورش عشقم 🍆💦
"""


START_TIME = datetime.utcnow()
TIME_DURATION_UNITS = (
    ("y", 60 * 60 * 24 * 7),
    ("d", 60 * 60 * 24),
    ("h", 60 * 60),
    ("m", 60),
    ("s", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{}{}{}".format(amount, unit, "" if amount == 1 else ""))
    return ":".join(parts)


@bot.on_message(filters.me & filters.command(["ping"],prefixes="."))
async def ping3(bot, m: Message):
    start = time.time()
    current_time = datetime.utcnow()
    m_reply = await m.edit_text("⚡")
    await asyncio.sleep(2)
    delta_ping = time.time() - start
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await m_reply.edit(
        f"**<i>Pong!</i>** `{delta_ping * 1000:.3f}` \n **<i>Uptime:</i>** `{uptime}`\n **<i>Bot Of > {adminbot}</i>**"
    )



@bot.on_message(filters.me & filters.command(["dice2"],prefixes="."))
async def dice32(bot, m:Message):
    text = int(m.text.split(None, 1)[1])
    if int(text) >=7:
        await m.edit_text("lol Bro !")
    elif int(text) == 0:
        await m.edit_text("lol Bro !")
        return False
    await m.edit_text(f"""
    <i>Sending Dice Of Value -></i> `{text}`
    """)
    while True:
        try:
            msg = await bot.send_dice(m.chat.id, "🎲")
            if msg.dice.value != text:
                await msg.delete()
                await asyncio.sleep(0.5)
            else:
                break
        except Exception as e :
            await m.edit_text(f"<i>Error, Please select int</i>\n{e}")
            return True


@bot.on_message(filters.me & filters.command(["cr"],prefixes="."))
def Creator(bot, m:Message):
    m.edit_text("""
    🧷📎🧷📎
📎Amir🧷
    📎🧷 「@QinBaz」
    """)




@bot.on_message(filters.me & filters.command(["se"],prefixes="."))
def download_photo(bot,m:Message):
    m.delete()
    m.reply(":)")
    name = 'photo.jpg'
    gsydh = bot.download_media(m.reply_to_message.photo.file_id, name)
    tim = time.strftime("%H:%M:%S")            
    bot.send_photo("me","downloads//photo.jpg", caption=f"<i>{tim} From User {m.reply_to_message.from_user.mention}</i>")
    remove(gsydh)

@bot.on_message(filters.me & filters.command(["kir"],prefixes="."))
def kir(bot, m:Message):
    m.delete()
    bot.send_message(m.chat.id,f"{KIR}")
import psutil
@bot.on_message(filters.me & filters.command(["^[Hh][Ee][Ll][Pp]$"],prefixes="."))
async def help(bot, m:Message):
    start = time.time()
    current_time = datetime.utcnow()
    m_reply = await m.edit_text("<i>Wait...</i>")
    delta_ping = time.time() - start
    uptime_sec = (current_time - START_TIME).total_seconds()
    disk_p = dict(psutil.disk_usage("/")._asdict())["percent"]
    uptime = await _human_time_duration(int(uptime_sec))
    await asyncio.sleep(2)
    await m.edit_text(f"""
    **<i>Welcome to QinUserBot Help</i>**

`.Help F`
`.Help P`
`.Help G`
`.Help O`

<i>Ping</i> > ({delta_ping * 1000:.3f})
<i>Mem Usage</i> > ({disk_p}%)
<i>UpTime</i> > ({uptime})
<i>Version</i> > (v1.0.1)
    """)


@bot.on_message(filters.me & filters.command(["^[Hh]elp [Ff]"],prefixes="."))
async def HELp(bot, m:Message):
    await m.edit_text("""
    **<i>Help Fun :</i>**
`.jok` > **<i>Get Jok</i>**
`.dice` > **<i>Send random dice</i>**
`.dice2` > **<i>(value,1 ta 6)</i>**
`.fun` > **<i>Send random of 🎲🎰🎳🎯🏀⚽️</i>**
`.b` > **<i>Send random number for Bet</i>**
`.tdice` **<i>(on/off) > Diagnosis Stimulus Emoji Game</i>**
`.dog` > **<i>Get dog photo</i>**
`.cat` > **<i>Get cat photo</i>**  
`.qo` > **<i>(Reply To Message) Get Sticker of Replayed To Message</i>**
    """)


@bot.on_message(filters.me & filters.command(["^[Hh]elp [Pp]"],prefixes="."))
async def HELpp(bot, m:Message):
    await m.edit_text("""
    **<i>Help Practical:</i>**
`.weather` > **<i>(City)</i>**
`.info` > **<i>(reply to user) or (username)</i>**
`.id` > **<i>Get id of User or Photo and ...(reply)</i>**
`.py` > **<i>(Code) run python code</i>**
`.telegraph` > **<i>(Reply to any Media) Get Telegraph link of Media</i>**
`.pdf` > **<i>(Reply to .jpg Format Photo) Photo to pdf</i>**
`.dlmusic` > **<i>(link) Download Music of Youtube or SoundCloud</i>**
`.ims` > **<i>(Reply to Sticker) Get Photo of Stickers</i>**
`ims2` > **<i> (Reply to Sticker) Get Vedio of Stickers</i>**
`.v` > **<i>(link) Download or Search Youtube Video</i>**
`.se` > **<i>(Reply to Photo)</i> دانلود عکس زمان دار**
`.profile` > **<i>(fname) Or (lname) Or (bio) Or (rmlname) (text)</i>**
`.rmpfp` > **<i>Delete All Profile Picture</i>**
`.move` > **<i>(text) Search Video </i>**
`.app` > **<i>(text) Search App From GooglePlay</i>**
`.country` > **<i>(text) Info Country</i>**
`.sys` > **<i>Get System Info And Stats Of Self</i>**
    """)


@bot.on_message(filters.me & filters.command(["^[Hh]elp [Gg]"],prefixes="."))
async def HELpg(bot, m:Message):
    await m.edit_text("""
    **<i>Help Group:</i>**
`.ban` > **<i>(Reply To User) or (Id or Username)Ban a User from Chat</i>**
`.unban` > **<i>(Reply To User) or (Id or Username) UnBan User from Chat</i>**
`.mute` > **<i>(Reply To User) or (Id or Username) Mute User from Chat</i>**
`.unmute` > **<i>(Reply To User) or (Id or Username) UnMute User from Chat</i>**
`.dmute` > **<i>(Only Reply To User) Mute User Globaly</i>**
`.undmute` > **<i>(Only Reply To User) UnMute User From Golobaly</i>**
`.cdmute` > **<i>Recovery MuteList</i>**
`.pin` > **<i>(Reply To Message) Pin Message from Chat</i>**
`.unpin` > **<i>(Reply To Pin Messages) UnPin Message from chat</i>**
`.promote` > **<i>(Reply To User) or (Id Or Username) Promote User</i>**
`.del` > **<i>(Reply to Message) Delete Message</i>**
`.lock` > <i>(str)
    `msg`
    `media`
    `sagi` > sticker and animation and game and inlinebot
    `webprev`
    `polls`
    `info`
    `invite`
    `pin`</i>
`.setchatname` > **<i>(text)</i>**
`.setchatpic` > **<i>(reply to photo)</i>**
`.welcome` > **<i>(on/off) Send Message For New Members</i>**
`.leave` > **<i>Left From Chat</i>**
`.join` > **<i>(Username) Join Group And Channel</i>**
    """)
#---------------------

#--------------------



@bot.on_message(filters.me & filters.command(["^[Hh]elp [oO]"],prefixes="."))
async def HELpp(bot, m:Message):
    await m.edit_text("""
    **<i>Help Other:</i>**
`.senemy` > **<i>(Only Reply To User) Add User To Enemy</i>**
`.denemy` > **<i>(Only Reply To User) Delete Of Enemy list</i>**
`.cenemy` > **<i>Recovery Enemy List</i>**
`.ping` > **<i>Get Ping And UpTime Of UserBot</i>**
`.corona` > **<i>(Name Of Country) Get States Corona Of Your Country</i>**
`.corona2` > **<i>Get States Corona Globaly</i>**
`.wiki` > **<i>(text)</i>**
`.wikifa` > **<i>(text)</i>**
`.tag` > **<i>Tag Members Of chat</i>**
`.tag2` > **<i>(text) Tag All Member In One Message</i>**
`.spam` > **<i>(int) (Reply To Message)</i>**
`.spam2` > **<i>(int | str)</i>**
`.typing` > **<i>(bold) Or (copy) For Off Use `.typing off`</i>**
`.ac typing` > **<i>(on/off) Typing Action in Chat or Pv</i>**
`.onlines` > **<i>Get Onlines Chat Member</i>**
`.today` > **<i>Get Time And Day</i>**
`.co` > **<i>(on/off) First Comment</i>** 
`.tname` > **<i>(on/off) Time Name</i>**
`.block` > **<i>(Only Reply To User) Block a User</i>**
`.unblock` > **<i>(Only Reply To User) UnBlock a User</i>**
`.porn` > **<i>Get Porn</i>**
`.webs` > **<i>(Link) Screen Shoter Site</i>**
    """)


STATS_TEXT = (
    "**<i>Status Of QinUserBot</i>**\n"
    "<i>Owner:</i> {}\n"
    "<i>Pyrogram Version:</i> `{} (Layer {})`\n"
    "<i>Python Version:</i> `{}`\n"
    "<i>UserBot Version:</i> `{}`\n"
    "<i>UpTime UserBot:</i> `{}`\n"
    "<i>Dick Info:</i> `{}`\n"
    "<i>Ram Info:</i> `{}`\n"
    "<i>Cpu Usage:</i> `{}%`\n"
    "<i>Cpu Count:</i> `{}`\n"
    "<i>System User:</i> `{}`\n"
)


@bot.on_message(filters.me & filters.command(["spam2"],prefixes="."))
async def spammer(bot, m:Message):
    await m.delete()
    for i in range(int(m.command[1])):
        try:
            await bot.send_message(m.chat.id,str(str(m.text).split('|')[1]))
        except:
            pass
#--------------------------------------------------------------------------
import bs4
@bot.on_message(filters.me & filters.command(["app"],prefixes="."))
async def app(bot,message: Message):
    try:
        await message.edit("<i>Searching...</i>")
        app_name = '+'.join(message.text.split(' '))
        page = requests.get(f"https://play.google.com/store/search?q={app_name}&c=apps")
        soup = bs4.BeautifulSoup(page.content, 'lxml', from_encoding='utf-8')
        results = soup.findAll("div", "ZmHEEd")

        app_name = results[0].findNext('div', 'Vpfmgd').findNext('div', 'WsMG1c nnK0zc').text
        app_dev = results[0].findNext('div', 'Vpfmgd').findNext('div', 'KoLSrc').text
        app_dev_link = "https://play.google.com" + results[0].findNext(
            'div', 'Vpfmgd').findNext('a', 'mnKHRc')['href']
        app_rating = results[0].findNext('div', 'Vpfmgd').findNext(
            'div', 'pf5lIe'
        ).find('div')['aria-label'].replace("Rated ", "⭐️ ").replace(
            " out of ", "/"
        ).replace(" stars", "", 1).replace(" stars", "⭐️").replace("five", "5")
        app_link = "https://play.google.com" + results[0].findNext(
            'div', 'Vpfmgd').findNext('div', 'vU6FJ p63iDd').a['href']
        app_icon = results[0].findNext('div', 'Vpfmgd').findNext('div', 'uzcko').img['data-src']

        app_details = f"[📲]({app_icon}) **{app_name}**\n\n"
        app_details += f"<i>Developer :</i> [{app_dev}]({app_dev_link})\n"
        app_details += f"<i>Rating :</i> {app_rating}\n"
        app_details += f"<i>Features :</i> [View in Play Store]({app_link})"
        await message.edit(app_details, disable_web_page_preview=False)
    except IndexError:
        await message.edit("<i>No Result Found In Search. Please Enter **Valid app name**</i>")
    except Exception as e:
        await message.edit_text(e)









from psutil._common import bytes2human
@bot.on_message(filters.me & filters.command(["sys"],prefixes="."))
async def Stats(bot, m:Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    disk_p = psutil.disk_usage("/")
    info_dick = (f"{bytes2human(disk_p.total)} Total , {bytes2human(disk_p.used)} Used>"f"({disk_p.percent}%)")
    ram_p = psutil.virtual_memory()
    info_ram = info = (f"{bytes2human(ram_p.total)} Total,"f"{bytes2human(ram_p.available)} Available,"f"{bytes2human(ram_p.used)} Used>"f"({bytes2human(ram_p.percent)}%)")
    cpu_p = psutil.cpu_percent()
    cpu_c = psutil.cpu_count()
    sy_p = psutil.users()
    await m.edit_text(
        STATS_TEXT.format(
            adminbot,
            __version__,
            layer,
            python_version(),
            "V1.0.1",
            uptime,
            info_dick,
            info_ram,
            cpu_p,
            cpu_c,
            sy_p
        ),
        disable_web_page_preview=True,
    )




@bot.on_message(filters.me & filters.command(["dog"],prefixes="."))
def woof(bot, m:Message):
    try:
       me = m.edit_text("<i>Wait</i>")
       r = get("https://random.dog/woof.json")
       rj = r.json()
       me.delete()
       m.reply_photo(rj["url"])
    except Exception as e:
        m.edit_text("<i>**Error**\n Sended To Your Saved Message</i>")
        bot.send_message("me",f"**ERROR :**\n{e}")




@bot.on_message(filters.me & filters.command(["cat"],prefixes="."))
def meow(bot, m:Message):
    try:
      me = m.edit_text("<i>Wait</i>")    
      r = get("https://api.thecatapi.com/v1/images/search")
      rj = r.json()
      me.delete()
      m.reply_photo(rj[0]["url"])
    except Exception as e:
        m.edit_text("<i>**Error**\n Sended To Your Saved Message</i>")
        bot.send_message("me",f"**ERROR :**\n{e}")
 

@bot.on_message(filters.me & filters.command(["jok"],prefixes="."))
def jok(bot, m:Message):
    jok = requests.get("https://api.codebazan.ir/jok/")
    m.edit_text(jok.text)






@bot.on_message(filters.me & filters.command(["onlines"],prefixes="."))
def online(bot,m:Message):
    Online_Usr=''
    gp = m.chat.id
    for member in bot.iter_chat_members(gp):
        if member.user.status in ["online", "recently"]:
            Online_Usr += f"|[{member.user.first_name}] {member.user.mention}\n"
    bot.edit_message_text(m.chat.id, m.message_id, f"**<i>Online Members :**</i>\n {Online_Usr}\n Onlines ↬ |{(len(Online_Usr))}|**")

    


#-----------------------------------------------------------
@bot.on_message(filters.me & filters.command(["today"],prefixes="."))
def today(c,m):
  ir=pytz.timezone("Asia/Tehran")
  t = jdatetime.datetime.now(ir).strftime("%H:%M:%S")
  d = jdatetime.datetime.now(ir).strftime("%y/%B/%d")
  text = f"<i>**Today**:</i> `{d}`\n<i>**Time**:</i> `{t}`"
  send =bot.edit_message_text(text=text,
    chat_id=m.chat.id,
    message_id=m.message_id,)
#----------------------------------------------------------
@bot.on_message(filters.me & filters.command(["join"],prefixes="."))
async def join_chat(bot, message: Message):
    """ Join chat """
    replied = message.reply_to_message
    if replied:
        text = replied.text
    else:
        text = message.text.split(None, 1)[1]
    if not text:
        await message.edit(
            "```Bruh, Without chat name, I can't Join... :0```", del_in=3)
        return
    try:
        chat = await bot.get_chat(text)
        await bot.join_chat(text)
        await  bot.send_message(text, f"<i>Joined {chat.title} Successfully...</i>")
        message.delete()
        asyncio.slepp(1.5)
    except Exception as e:
        await message.edit(f"**<i>Error</i>**\n{e}")
        return
    else:
        await message.delete()
        await asyncio.sleep(2)
#-----------------------------------------------------------
from countryinfo import CountryInfo
@bot.on_message(filters.me & filters.command(["country"],prefixes="."))
async def countryinfo(bot, update: Message):
    if " " not in update.text:
        await update.edit_text("Send with country name")
        return
    country = CountryInfo(update.text.split(" ", 1)[1])
    info = f"""**<i>Country Information</i>**
<i>Name</i> : `{country.name()}`
<i>Native Name</i> : `{country.native_name()}`
<i>Capital</i> : `{country.capital()}`
<i>Population</i> : `{country.population()}`
<i>Region</i> : `{country.region()}`
<i>Sub Region</i> : `{country.subregion()}`
<i>Top Level Domains</i> : `{country.tld()}`
<i>Calling Codes</i> : `{country.calling_codes()}`
<i>Currencies</i> : `{country.currencies()}`
<i>Residence</i> : `{country.demonym()}`
<i>Timezone</i> : `{country.timezones()}`
<i>Wiki</i> : {country.wiki()}"""
    try:
        await update.edit_text(text=info, disable_web_page_preview=False)
    except Exception as KeyError:
        await update.edit_text(f"**<i>Error</i>\n{KeyError}**", disable_web_page_preview=True)
#----------------------------------------------------------
from justwatch import JustWatch, justwatchapi
WATCH_COUNTRY = os.environ.get("WATCH_COUNTRY", "IN")
def get_stream_data(query):
    stream_data = {}

    # Cooking Data
    just_watch = JustWatch(country=WATCH_COUNTRY)
    results = just_watch.search_for_item(query=query)
    movie = results['items'][0]
    stream_data['title'] = movie['title']
    stream_data['movie_thumb'] = ("https://images.justwatch.com"
                                  + movie['poster'].replace("{profile}", "") + "s592")
    stream_data['release_year'] = movie['original_release_year']
    try:
        print(movie['cinema_release_date'])
        stream_data['release_date'] = movie['cinema_release_date']
    except KeyError:
        try:
            stream_data['release_date'] = movie['localized_release_date']
        except KeyError:
            stream_data['release_date'] = None

    stream_data['type'] = movie['object_type']

    available_streams = {}
    if movie.get("offers"):
        for provider in movie['offers']:
            provider_ = get_provider(provider['urls']['standard_web'])
            available_streams[provider_] = provider['urls']['standard_web']

    stream_data['providers'] = available_streams

    scoring = {}
    if movie.get("scoring"):
        for scorer in movie['scoring']:
            if scorer['provider_type'] == "tmdb:score":
                scoring['tmdb'] = scorer['value']

            if scorer['provider_type'] == "imdb:score":
                scoring['imdb'] = scorer['value']
    stream_data['score'] = scoring
    return stream_data


@bot.on_message(filters.me & filters.command(["move"],prefixes="."))
async def fetch_watch_sources(bot,message: Message):
    await message.edit("<i>Wait...</i>")
    query = message.text.split(" ", 1)[1]
    streams = get_stream_data(query)
    title = streams['title']
    thumb_link = streams['movie_thumb']
    release_year = streams['release_year']
    release_date = streams['release_date']
    scores = streams['score']
    try:
        imdb_score = scores['imdb']
    except KeyError:
        imdb_score = None

    try:
        tmdb_score = scores['tmdb']
    except KeyError:
        tmdb_score = None

    # type = streams['type']
    stream_providers = streams['providers']
    if release_date is None:
        release_date = release_year

    output_ = f"**<i>Movie:</i>**\n`{title}`\n**<i>Release Date:</i>**\n`{release_date}`"
    if imdb_score:
        output_ = output_ + f"\n**<i>IMDB: </i>**{imdb_score}"
    if tmdb_score:
        output_ = output_ + f"\n**<i>TMDB: </i>**{tmdb_score}"

    output_ = output_ + "\n\n**<i>Available On:</i>**\n"
    for provider, link in stream_providers.items():
        if 'sonyliv' in link:
            link = link.replace(" ", "%20")
        output_ += f"[{pretty(provider)}]({link})\n"

    await bot.send_photo(chat_id=message.chat.id,
                                    photo=thumb_link,
         
                                    caption=output_,
                                    disable_notification=True)
    await message.delete()


# Helper Functions
def pretty(name):
    if name == "play":
        name = "Google Play Movies"
    return name[0].upper() + name[1:]


def get_provider(url):
    url = url.replace("https://www.", "")
    url = url.replace("https://", "")
    url = url.replace("http://www.", "")
    url = url.replace("http://", "")
    url = url.split(".")[0]
    return url

#----------------------------------------------------------

#-----------------------------------------------------------
@bot.on_message(filters.me & filters.command(["ban"],prefixes="."))
async def kick(bot, m:Message):
    chat_id = m.chat.id
    user_id = m.from_user.id
    check_status = await bot.get_chat_member(chat_id=chat_id, user_id=user_id)
    admin_strings = ["creator", "administrator"]
    if check_status.status not in admin_strings:
         await m.edit_text(f"<i>Im Not Admin !</i>")
         await asyncio.sleep(0)
         return False 
    if m.reply_to_message:
        try:
         user = m.reply_to_message.from_user.id
         await bot.ban_chat_member(m.chat.id, user)
         await m.edit_text(f"<i>[User](tg://user?id={m.reply_to_message.from_user.id}) Successfully Banned !</i>")
        except Exception as e:
            await m.edit_text(f"**ERROR :**\n{e}")
    elif m.text is not m.reply_to_message:
        id=(str(m.text[6:]))
        try:
            user= await bot.get_users(int(id))
            await bot.ban_chat_member(m.chat.id,int(id))
            await m.edit_text(f"<i>[User](tg://user?id={user.id}) Successfully Banned !</i>")
        except:
            try:
                user=await bot.get_users(id)
                await bot.ban_chat_member(m.chat.id,id)
                await m.edit_text(f"<i>[User](tg://user?id={user.id}) Successfully Banned !</i>")
            except Exception as e:
                await m.edit_text(f"<i>**ERROR :**</i>\n`{e}`")
    else:
        try:
         m.edit_text("<i>Please Use Username Or Id Or Reply To User</i>")
        except Exception as e:
          await m.edit_text(f"**<i>ERROR :</i>**\n{e}")
    return True



@bot.on_message(filters.me & filters.command(["unban"],prefixes="."))
async def unban(bot, m:Message):
    chat_id = m.chat.id
    user_id = m.from_user.id
    check_status = await bot.get_chat_member(chat_id=chat_id, user_id=user_id)
    admin_strings = ["creator", "administrator"]
    if check_status.status not in admin_strings:
        await m.edit_text(f"<i>Im Not Admin !</i>") 
        await asyncio.sleep(0)
        return False 
    if m.reply_to_message:
        try:
         user = m.reply_to_message.from_user.id
         await bot.unban_chat_member(m.chat.id, user)
         await m.edit_text(f"<i>[User](tg://user?id={m.reply_to_message.from_user.id}) Successfully UnBanned !</i>")
        except Exception as e:
            await m.edit_text(f"**<i>ERROR :</i>**\n`{e}`")
    elif m.text is not m.reply_to_message:
        id=(str(m.text[6:]))
        try:
            user= await bot.get_users(int(id))
            await bot.unban_chat_member(m.chat.id,int(id))
            await m.edit_text(f"<i>[User](tg://user?id={user.id}) Successfully UnBanned !</i>")
        except:
            try:
                user=await bot.get_users(id)
                await bot.unban_chat_member(m.chat.id,id)
                await m.edit_text(f"<i>[User](tg://user?id={user.id}) Successfully UnBanned !</i>")
            except Exception as e:
                await m.edit_text(f"<i>**ERROR :</i>**\n`{e}`")
    else:
        try:
         m.reply("<i>Please Use Username Or Id Or Reply To User</i>")
        except Exception as e:
          await m.reply(f"**<i>ERROR :</i>**\n{e}")
    return True
#-------------------------------------------------------------
@bot.on_message(filters.me & filters.command(["promote"],prefixes="."))
async def Amir(bot, m:Message): 
    chat_id = m.chat.id
    user_id = m.from_user.id
    check_status = await bot.get_chat_member(chat_id=chat_id, user_id=user_id)
    admin_strings = ["creator", "administrator"]
    if check_status.status not in admin_strings:
        await m.edit_text(f"<i>Im Not Admin !</i>") 
        await asyncio.sleep(0)
        return False     
    if m.reply_to_message:
        try:
         user = m.reply_to_message.from_user.id
         await bot.promote_chat_member(m.chat.id, user)
         await m.edit_text(f"<i>[User](tg://user?id={m.reply_to_message.from_user.id}) Successfully Promoted !</i>")
        except Exception as e:
            await m.edit_text(f"**<i>ERROR :</i>**\n`{e}`")
    elif m.text is not m.reply_to_message:
        id= m.text.split(None, 1)[1]
        try:
            user= await bot.get_users(int(id))
            await bot.promote_chat_member(m.chat.id,int(id))
            await m.edit_text(f"<i>[User](tg://user?id={user.id}) Successfully Promoted !</i>")
        except:
            try:
                user=await bot.get_users(id)
                await bot.promote_chat_member(m.chat.id,id)
                await m.edit_text(f"<i>[User](tg://user?id={user.id}) Successfully Promoted !</i>")
            except Exception as e:
                await m.edit_text(f"**<i>ERROR :</i>**\n{e}")
    else:
        try:
         m.edit_text("<i>Please Use Username Or Id Or Reply To User</i>")
        except Exception as e:
          await m.reply(f"**<i>ERROR :</i>**\n{e}")
    return True 

#----------------------------welcome on off-----------------------------
welcome=False
@bot.on_message(filters.me & filters.command(["welcome"],prefixes="."))
def welcome_func(bot, m:Message):
    global welcome
    on_off=str(m.command[1])
    if on_off.lower()=='on':
        welcome=True
        m.edit_text(f"<i>Welcome Is {on_off} Now</i>")
    elif on_off.lower()=='off':
        welcome=False
        m.edit_text(f"<i>Welcome Is {on_off} Now</i>")
    else:
        m.edit_text(":(")



@bot.on_message(~filters.me & filters.new_chat_members)
def New_Gaps(bot,m:Message):
    if welcome==True:
        m.reply(
            f"""
**Hello Dear {m.from_user.mention} 
Welcome to {m.chat.title}
Members of chat : `{m.chat.members_count}`
Your firstname : `{m.from_user.first_name}`
Your username : @{m.from_user.username}
Your id : `{m.from_user.id}`
**
"""
        )


#-----------------------------------------------------------
@bot.on_message(filters.me & filters.command(["qo"],prefixes="."))
async def quotly(bot, m: Message):
    p=0
    if not m.reply_to_message:
        await m.edit_text("Reply To Any Users Text Message")
        return
    await m.edit_text("<i>Making a Quote</i>")
    await m.reply_to_message.forward("@QuotLyBot")
    is_sticker = False
    progress = 0
    while not is_sticker:
        try:
            msg = await bot.get_history("@QuotLyBot", 1)
            check = msg[0]["sticker"]["file_id"]
            is_sticker = True
        except:
            time.sleep(0.5)
            progress += random.randint(0, 10)
            try:
                await m.edit_text(
                    f"```Making a Quote```\nProcessing {progress}%",
                    parse_mode="md",
                )
                if progress >= 100:
                    pass
            except Exception as ef:
                await m.edit_text(f"**<i>ERROR:</i>**\n{ef}")
                p += 1
                if p == 3:
                    break
    await m.edit_text("Complete !" , parse_mode="md")
    msg_id = msg[0]["message_id"]
    await bot.forward_messages(m.chat.id, "@QuotLyBot", msg_id)
    await bot.read_history("@QuotLyBot")
    await m.delete()
#---------------------------------------------------------
@bot.on_message(filters.me & filters.command(["porn"],prefixes="."))
def pornd(bot, m: Message):
    ki = m.edit_text("<i>Wait😈</i>")
    msg =  bot.get_history("@LOKSM2bot",1)
    bot.send_message("@LOKSM2bot","فیلم 👙")
    msg_id = msg[0]["message_id"]
    bot.forward_messages(m.chat.id, "@LOKSM2bot", msg_id)
    bot.read_history("@QuotLyBot")
    ki.delete()
#----------------------------------------------------------
import html
@bot.on_message(filters.me & filters.command(["tag2"],prefixes="."))
async def everyone(bot, m: Message):
    await m.delete()
    if len(m.text.split()) >= 2:
        text = m.text.split(None, 1)[1]
    else:
        text = "hi all"
    kek = bot.iter_chat_members(m.chat.id)
    async for a in kek:
        if not a.user.is_bot:
            text += mention_html(a.user.id, "\u200b")
    await bot.send_message(
        m.chat.id,
        text,
        parse_mode="html",
    )
    return

def mention_html(user_id, name):
    return f'<a href="tg://user?id={user_id}">{html.escape(name)}</a>'
#-----------------------------------------------------------
@bot.on_message(filters.me & filters.command(["leave"],prefixes="."))
def leave(bot,m:Message):
    m.edit_text('Bye Bye !')
    bot.leave_chat(m.chat.id)

#---------------------------------------------------------
@bot.on_message(filters.me & filters.command(["pin"],prefixes="."))
async def pin(bot, m:Message):
    chat_id = m.chat.id
    user_id = m.from_user.id
    check_status = await bot.get_chat_member(chat_id=chat_id, user_id=user_id)
    admin_strings = ["creator", "administrator"]
    if check_status.status not in admin_strings:
        await m.edit_text("<i>Im Not Admin !</i>")
        await asyncio.sleep(0)
        return False
    try:
     await bot.pin_chat_message(m.chat.id,m.reply_to_message.message_id)
     await m.edit_text("<i>Pinned !</i>")
    except Exception as e:
        await m.edit_text(f"**<i>Please Reply To Message</i>**\n**<i>ERROR :</i>**\n`{e}`")    
    return True

@bot.on_message(filters.me & filters.command(["unpin"],prefixes="."))
async def unpin(bot, m:Message):
    chat_id = m.chat.id
    user_id = m.from_user.id
    check_status = await bot.get_chat_member(chat_id=chat_id, user_id=user_id)
    admin_strings = ["creator", "administrator"]
    if check_status.status not in admin_strings:
        await m.edit_text("<i>Im Not Admin !</i>")
        await asyncio.sleep(0)
        return False
    try:
     await bot.unpin_chat_message(m.chat.id,m.reply_to_message.message_id)
     await m.edit_text("<i>UnPinned !</i>")
    except Exception as e:
        await m.edit_text(f"**<i>Please Reply To Pin Message</i>**\n**<i>ERROR :</i>**\n`{e}`")
    return True
# --------------------------------------

@bot.on_message(filters.me & filters.command(["corona"],prefixes="."))
def corona_c(bot, m):
  me = m.edit_text("Wait")
  cmd = m.command
  if not (len(cmd)>=2):
    me.edit('not enough provided')
    time.sleep(3)
  country = cmd[1]
  me.edit("**<i>Getting Corona State For :</i>**"+ country)
  r = get(f"https://corona.lmao.ninja/v2/countries/{country}").json()
  if "cases" not in r:
    me.edit('not available in this country')
    time.sleep(3)
  else:
    last_update = datetime.fromtimestamp(r["updated"]/1000).strftime("%Y-%m-%d %I:%M:%S")
    cc = PrettyTable()
    cc.header = False
    country = r["**<i>CountryInfo</i>**"]["iso3"] if len(r["country"]) > 12 else r["country"]
    cc.title = f"**<i>Corona State In</i>** `{country}`"
    cc.add_row(["**<i>Population</i>**", f"{r['population']:,}"])
    cc.add_row(["**<i>Cases</i>**", f"{r['cases']:,}"])
    cc.add_row(["**<i>Cases Today</i>**", f"{r['todayCases']:,}"])
    cc.add_row(["**<i>Deaths</i>**", f"{r['deaths']:,}"])
    cc.add_row(["**<i>Deaths Today</i>**", f"{r['todayDeaths']:,}"])
    cc.add_row(["**<i>Recovered</i>**", f"{r['recovered']:,}"])
    cc.add_row(["**<i>Active</i>**", f"{r['active']:,}"])
    cc.add_row(["**<i>Critical</i>**", f"{r['critical']:,}"])
    cc.add_row(["**<i>Tests</i>**", f"{r['tests']:,}"])
    cc.align = "l"
    me.edit(f"'''{str(cc)}'''\nLast Updated : `{last_update}`")



@bot.on_message(filters.me & filters.command(["corona2"],prefixes="."))
def corona_All(bot, m:Message):
  me = m.edit_text("Wait")
  try:
    r = get("https://corona.lmao.ninja/v2/all?yesterday=true").json()
    last_update = datetime.fromtimestamp(r["updated"]/1000).strftime("%Y-%m-%d %I:%M:%S")
    ac = PrettyTable()
    ac.header = False
    ac.title = "**<i>Global Statistics</i>**"
    ac.add_row(["<i>Cases</i>", f"{r['cases']:,}"])
    ac.add_row(["<i>Cases Today</i>", f"{r['todayCases']:,}"])
    ac.add_row(["<i>Deaths</i>", f"{r['deaths']:,}"])
    ac.add_row(["<i>Deaths Today</i>", f"{r['todayDeaths']:,}"])
    ac.add_row(["<i>Recovered</i>", f"{r['recovered']:,}"])
    ac.add_row(["<i>Active</i>", f"{r['active']:,}"])
    ac.add_row(["<i>Critical</i>", f"{r['critical']:,}"])
    ac.align = "l"
    me.edit(f"'''{str(ac)}'''\nLast Updated: `{last_update}`")
  except Exception as e:
    me.edit("<i>Api Corona Not Found</i>")
    m.reply(f"`{e}`")
    time.sleep(3)
#---------------------------------------------------------------------
import json
import pytube


@bot.on_message(filters.me & filters.command(["v2"],prefixes="."))
def v2dl(bot, m:Message):
    m.edit_text("<i>Downloading</i>")
    link = m.text.split(None, 1)[1]
    itag = 18
    video = pytube.YouTube(link)
    stream = video.streams.get_by_itag(itag)
    v = stream.download()
    body=f"""
Title: {video.title}
Number of Views: {video.views}
Length of video: {video.length} Secend
Description: {video.description}
Ratings: {video.rating}
"""
    m.edit_text(f"**<i>Successfully Downloaded\n File in Your Directory\n Video Info : `{body}`</i>**")



@bot.on_message(filters.me & filters.command(["v3"],prefixes="."))
async def v2dl11(bot, m:Message):
    path = "w.json"
    await m.edit_text("<i>Downloading</i>")
    link = m.text.split(None, 1)[1]
    yt = pytube.YouTube(link)
    yrs = yt.streams.get_highest_resolution().download()
    await m.reply.video(yrs)







#----------------------------------------------------------------------
from pyrogram.errors import FloodWait
@bot.on_message(filters.me & filters.command(["spam"],prefixes="."))
def spam(bot, m):
    m.delete()
    msgid = m.reply_to_message.message_id
    chatid = m.chat.id
    spam = int(m.text.split(" ")[1])
    time.sleep(0)
    for i in range(spam):
        try:
         bot.forward_messages(
            chat_id=chatid,
            from_chat_id=chatid,
            message_ids=[msgid]
        )
        except Exception as e:
            m.edit_text(f"**<i>Please reply to message</i>**\n**<i>ERROR :</i>**\n`{e}`")
#------------------------------------------------------------------
@bot.on_message(filters.me & filters.command(["block"],prefixes="."))
def Block(bot,m:Message):
    if m.reply_to_message:
        id=m.reply_to_message.from_user.id
        bot.block_user(id)
        m.edit_text(f"<i>User {m.reply_to_message.from_user.mention} Blocked</i>")
    else:
        m.edit_text("<i>Please Reply To User</i>")

@bot.on_message(filters.me & filters.command(["unblock"],prefixes="."))
def Unblock(bot,m:Message):
    if m.reply_to_message:
        id=m.reply_to_message.from_user.id
        bot.unblock_user(id)
        m.edit_text(f"<i>User {m.reply_to_message.from_user.mention} UnBlocked</i>")
    else:
        m.edit_text("<i>Please Reply To User</i>")
#-------------------------------------------------------------------

@bot.on_message(filters.me & filters.command(["wiki"],prefixes="."))
def wikipedia_search(bot,m:Message):
    me = m.edit_text("🔎")
    try:
        text=m.text[6:]
        wikipedia.set_lang('en')
        result = wikipedia.page(text)
        me.edit(result.summary[0:1000])
    except :
        me.edit("**<i>Error Try Another Text !</i>**")


@bot.on_message(filters.me & filters.command(["wikifa"],prefixes="."))
def wikipedia_search_fa(bot, m:Message):
    me = m.edit_text("🔎")
    try:
        text=m.text[8:]
        wikipedia.set_lang('fa')
        result = wikipedia.page(text)
        me.edit(result.summary[0:1000])
    except Exception as e:
        m.edit_text(f"صفحه ایی با این موضوع پیدا نشد! \n **ERROR :**\n{e}")
#---------------------------------------------------------------
mtx="بیا بالا"
speed=0
autotag=0
is_tagging =dict()

def add_istagging(chat_id):
    global is_tagging
    if chat_id not in is_tagging:
        is_tagging.update({chat_id: False})

@bot.on_message(filters.me & filters.command(["tag"],prefixes="."))
def tagge2r(bot, m:Message):
    global is_tagging
    rag=''
    s=0
    chat_id = m.chat.id
    add_istagging(chat_id)
    m.edit_text('Ok')
    if not is_tagging[chat_id]:
        is_tagging[chat_id] = True
        chat_members = bot.iter_chat_members(chat_id=chat_id)
        for usr in chat_members:
            if usr['user']['username']:
                if is_tagging[chat_id]:
                    bot.send_chat_action(chat_id, 'typing')
                    if not usr.user.is_bot:
                        rag+= f"**{(mtx)} {usr.user.mention()} ** \n "
                        s+=5
                        if s==5:
                            bot.send_message(chat_id,rag)
                            rag=''
                            s=0
                else:
                    return
        is_tagging[chat_id] = False
#-------------------------------------------------------------
typei = ["off"]
game = ["off"]
@bot.on_message(filters.me & filters.command(["ac typing"],prefixes=".") , group=3)
async def actyping(bot, m:Message):
    xx = m.message_id
    xxx = m.chat.id
    ff = m.text.split()
    if ff[2] == "on":
        typei.clear()
        game.clear()
        game.append("off")
        typei.append("on")
        await m.edit_text("<i>Typing Action Is On Now!</i>")
    elif ff[2] == "off":
        typei.clear()
        typei.append("off")
        await m.edit_text("<i>Typing Action Now Off!</i>")
    else:
        await m.edit_text(":(")

@bot.on_message(~filters.me ,group=4)
async def actyping2(bot, m:Message):
    if "on" in typei:
        await bot.send_chat_action(m.chat.id, "typing")
#-----------------------------------------------------------
action_type=0
@bot.on_message(filters.me & filters.command(["typing"],prefixes="."))
def copy_Text_func(bot, m:Message):
    global action_type
    text=str(m.command[1])
    if text.lower()=='copy' :
        action_type=1
        m.edit_text("<i>Copy Mode On</i>")

    if text.lower()=='bold' :
        action_type=2
        m.edit_text("<i>Bold Mode On</i>")

    if text.lower()=='off' :
        action_type=0
        m.edit_text("<i>Typing Edit Is Off Now</i>")

Has_Sended=list()

@bot.on_message(filters.me & filters.text)
def My_Msg(bot,m:Message):
    global Has_Sended
    if m.message_id not in Has_Sended:
        Has_Sended=[]
    if action_type==1:
        m.edit_text(f'``` {m.text} ```')
    elif action_type==2:
        m.edit_text(f'** {m.text} **')
#------------------------------------------------------------
import pytz
GALB = ("💝","💘","💖","💗","💓","💞","🤍","🤎","💔","❤️‍🔥","❤️‍🩹","❣️","💕","🖤","💜","💙","💚","💛","🧡","❤️")
@bot.on_message(filters.me & filters.command(["tname on"],prefixes="."), group=24)
async def bio_time(bot,m:Message):
    tname = 1
    await m.edit_text('<i>Time Name Is On</i>')
    while True:
        if tname ==1:
            ir=pytz.timezone("Asia/Tehran")
            time= jdatetime.datetime.now(ir).strftime("%H:%M")
            t = (time)
            await bot.update_profile(last_name=f'|{t} {random.choice(GALB)}')
            await asyncio.sleep(60)

@bot.on_message(filters.me & filters.command(["tname off"],prefixes="."), group=24)
async def bio_time(bot, m:Message):
    tname = 0
    if tname==0:
        await bot.update_profile(last_name="")
        await m.edit_text('<i>Time Name Is Off</i>')
#------------------------------------------------------------
@bot.on_message(filters.me & filters.command(["res"],prefixes="."), group=25)
async def restart(bot, m: Message):
    await m.edit_text("**<i>Restarted ✅</i>**")
    os.execl(sys.executable, sys.executable, *sys.argv)
    quit()
#------------------------------------------------------------
@bot.on_message(filters.me & filters.command(["mute"],prefixes="."),group=15)
async def mute(bot, m):
    chat_id = m.chat.id
    user_id = m.from_user.id
    check_status = await bot.get_chat_member(chat_id=chat_id, user_id=user_id)
    admin_strings = ["creator", "administrator"]
    if check_status.status not in admin_strings:
        await m.edit_text(f"<i>Im Not Admin !</i>")
        await asyncio.sleep(0)
        return False
    if m.reply_to_message:

        try:
           await bot.restrict_chat_member(m.chat.id, m.reply_to_message.from_user.id, ChatPermissions())
           await m.edit_text(f"<i>[User](tg://user?id={m.reply_to_message.from_user.id}) Successfully Muted !</i>")
        except Exception as e:
           await m.edit_text(f"<i>An Error Occured!</i>\n`{e}`") 
    elif m.text is not m.reply_to_message:
        id=(str(m.text[6:]))
        try:
           user= await bot.get_users(int(id))
           await bot.restrict_chat_member(m.chat.id, int(id), ChatPermissions())
           await m.edit_text(f"<i>[User](tg://user?id={user.id}) Successfully Muted !</i>")
        except:
            try:
               user= await bot.get_users(id)
               await bot.restrict_chat_member(m.chat.id, id, ChatPermissions())
               await m.edit_text(f"<i>[User](tg://user?id={user.id}) Successfully Muted !</i>")
            except Exception as e:
                    await m.edit_text(f"<i>An Error Occured!</i>\n`{e}`")
    return True




@bot.on_message(filters.me & filters.command(["unmute"],prefixes="."), group=15)
async def unmute(bot, m: Message):
    user_id = m.from_user.id
    chat_id = m.chat.id
    from_user_id = m.from_user.id
    check_status = await bot.get_chat_member(chat_id=chat_id, user_id=user_id)
    admin_strings = ["creator", "administrator"]
    if check_status.status not in admin_strings:
        await m.edit_text(f"<i>Im Not Admin !</i>") 
        await asyncio.sleep(0)
        return False
    if m.reply_to_message:
        try:
           await m.chat.unban_member(m.reply_to_message.from_user.id)
           await m.edit_text(f"<i>[User](tg://user?id={m.reply_to_message.from_user.id}) Successfully UnMuted !</i>")
        except Exception as e:
              await m.edit_text(f"<i>An Error Occured!</i>\n`{e}`")
    elif m.text is not m.reply_to_message:
        id= m.text.split(None, 1)[1]
        try:
            user= await bot.get_users(int(id))
            await bot.unban_chat_member(m.chat.id,int(id))
            await m.edit_text(f"<i>[User](tg://user?id={user.id}) Successfully UnMuted !</i>")
        except:
            try:
                user=await bot.get_users(id)
                await bot.unban_chat_member(m.chat.id,id)
                await m.edit_text(f"<i>[User](tg://user?id={user.id}) Successfully UnMuted !</i>")
            except Exception as e:
                  await m.edit_text(f"<i>An Error Occured!</i>\n`{e}`")
    return True

mutee=[]
@bot.on_message(filters.me & filters.command(["dmute"],prefixes="."),group=16)
async def dmute(bot, m:Message):
     xxxx = m.reply_to_message.from_user.id
     await m.edit_text(f"<i>[User](tg://user?id={m.reply_to_message.from_user.id}) Successfuly Muted Globaly !</i>")
     mutee.append(xxxx)

@bot.on_message(filters.private)
async def dmute(bot, m:Message):
    user = m.from_user.id
    if user in mutee:       
        xx = m.chat.id
        xxx = m.message_id
        await bot.delete_messages(xx, xxx, revoke=True)
        await asyncio.sleep(0)


@bot.on_message(group )
async def dmute(bot, m:Message):
     user = m.from_user.id
     if user in mutee:       
         xx = m.chat.id
         xxx = m.message_id
         await bot.delete_messages(xx, xxx, revoke=True)
         await asyncio.sleep(0)


@bot.on_message(filters.me & filters.command(["undmute"],prefixes="."),group=16)
async def dmute(bot, m:Message):
    xxxx = m.reply_to_message.from_user.id
    await m.edit_text(f"<i>[User](tg://user?id={m.reply_to_message.from_user.id}) Successfuly UnMuted Globaly !</i>")
    mutee.remove(xxxx)

@bot.on_message(filters.me & filters.command(["cdmute"],prefixes="."),group=16)
async def dmute(bot, m:Message):
    await m.edit_text(f"<i>Successfuly Recovery MuteList !</i>")
    mutee.clear()



enemy2=[]
@bot.on_message(filters.me & filters.command(["senemy"],prefixes=".") ,group=5)
async def enemy(bot, m:Message):
    if m.reply_to_message:
        xxxx = m.reply_to_message.from_user.id
        await m.edit_text(f"<i>[User](tg://user?id={m.reply_to_message.from_user.id}) is Now Enemy !</i>")
        enemy2.append(xxxx)

@bot.on_message(group,group=8)
async def fosh1(bot, m:Message):
    if m.from_user.id in enemy2:
        ry = fosh[random.randrange(len(fosh))]
        await m.reply_text(ry)
        await asyncio.sleep(0)
@bot.on_message(filters.private, group=8)
async def fosh1(bot, m:Message):
    if m.from_user.id in enemy2:
        ry = fosh[random.randrange(len(fosh))]
        await m.reply_text(ry)

@bot.on_message(filters.me & filters.command(["denemy"],prefixes="."), group=6)
async def enemy23(bot, m:Message):
    xxxx = m.reply_to_message.from_user.id
    await m.edit_text(f"<i>[User](tg://user?id={m.reply_to_message.from_user.id}) Deleted From Enemy !</i>")
    enemy2.remove(xxxx)



@bot.on_message(filters.me & filters.command(["cenemy"],prefixes="."), group=6)
async def enemy23(bot, m:Message):
    await m.edit_text(f"<i>Successfuly Recovery EnemyList !</i>")
    enemy2.clear()


#------------------------------------------------------------------------
@bot.on_message(filters.me & filters.command(["del"],prefixes=".") & group, group=9)
async def del_msg(bot, m: Message):
    try:
        if m.reply_to_message:
            await bot.delete_messages(
            chat_id=m.chat.id, message_ids=m.reply_to_message.message_id
        )
        await m.delete()
    except Exception as e:
        await m.reply(f"<i>An Error Occured!\n`{e}`</i>")
#--------------------------------------------------------------
from requests import post
import shutil
import urllib
CARBON_LANG = "Auto"
@bot.on_message(filters.me & filters.command(["carbon"],prefixes="."), group=10)
async def admins(bot, m:Message):
    json = {
        "backgroundColor": "rgba(0, 255, 230, 100)",
        "theme": "Dracula",
        "exportSize": "10x",
    }
    cmd = m.command
    if len(cmd) >= 2:
        await m.edit_text("<i>Carboning Your Code Wait !</i>")
        r = m.text.split(None, 1)[1]
        json["code"] = urllib.parse.quote(r)
    else:
        await m.reply(
            f"Usage: `.carbon` <reply to a code or text>"
        )
    json["language"] = CARBON_LANG
    apiUrl = "http://carbonnowsh.herokuapp.com"
    r = post(apiUrl, json=json, stream=True)
    filename = "carbon.png"
    if r.status_code == 200:
        r.raw.decode_content = True
        with open(filename, "wb") as f:
            shutil.copyfileobj(r.raw, f)
            f.close()
        await bot.send_document(
            m.chat.id,
            filename,
            caption="<i>Qinbaz</i>",
        )
    else:
        m.edit_text
        ("<i>Image Couldn't Be Retreived</i>")
    return
#---------------------------------------------------------------------------
@bot.on_message(filters.me & filters.command(["id"],prefixes=".") & group, group=11)
async def get_id(bot, m: Message):
    file_id = None
    user_id = None

    if m.reply_to_message:
        rep = m.reply_to_message
        if rep.audio:
            file_id = rep.audio.file_id
        elif rep.document:
            file_id = rep.document.file_id
        elif rep.photo:
            file_id = rep.photo.file_id
        elif rep.sticker:
            file_id = rep.sticker.file_id
        elif rep.video:
            file_id = rep.video.file_id
        elif rep.animation:
            file_id = rep.animation.file_id
        elif rep.voice:
            file_id = rep.voice.file_id
        elif rep.video_note:
            file_id = rep.video_note.file_id
        elif rep.contact:
            file_id = rep.contact.file_id
        elif rep.location:
            file_id = rep.location.file_id
        elif rep.venue:
            file_id = rep.venue.file_id
        elif rep.from_user:
            if rep.forward_from:
                user_id = rep.forward_from.id
                if rep.forward_from.last_name:
                    user_name = (
                        rep.forward_from.first_name + " " + rep.forward_from.last_name
                    )
                else:
                    user_name = rep.forward_from.first_name
                username = rep.forward_from.username
            else:
                user_id = rep.from_user.id
                if rep.from_user.last_name:
                    user_name = rep.from_user.first_name + " " + rep.from_user.last_name
                else:
                    user_name = rep.from_user.first_name
                username = rep.from_user.username

    if user_id:
        await m.edit_text(
            "<i>User Short Info:</i>\n**<i>User ID:</i>** `{}`\n**<i>Name:</i>** `{}`\n**<i>Username:</i>** @{}".format(
                user_id, user_name, username
            )
        )
    elif file_id:
        await m.edit_text(f"<i>File's ID:</i> `{file_id}`")
    else:
        await m.edit_text(f"<i>This Chat's ID:</i> `{m.chat.id}`")
#-----------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------
import pyfiglet
@bot.on_message(command('font')& group , group=8)
async def figlet_font(bot, m: Message):
    CMD_FIG = {
        "slant": "slant",
        "3D": "3-d",
        "5line": "5lineoblique",
        "alpha": "alphabet",
        "banner": "banner3-D",
        "doh": "doh",
        "iso": "isometric1",
        "letter": "letters",
        "allig": "alligator",
        "dotm": "dotmatrix",
        "bubble": "bubble",
        "bulb": "bulbhead",
        "digi": "digital",
    }
    input_str = m.text.split(None, 1)[1]
    if "|" in input_str:
        text, font_style = input_str.split("|", maxsplit=1)
    elif input_str is not None:
        font_style = None
        text = input_str
    else:
        await m.reply("`Please add some text to figlet`")
        return
    if font_style is not None:
        try:
            font = CMD_FIG[font_style]
        except KeyError:
            await m.reply("`Font not available`")
            return
        result = pyfiglet.figlet_format(text, font=font)
    else:
        result = pyfiglet.figlet_format(text)
    await m.reply_text(f"‌‌‎`{result}`")
    await m.delete()
    return










#---------------------------------------------------------------------------------------
from pyrogram.filters import linked_channel, edited

comentaval=0
textco = "OK :)"
@bot.on_message(filters.me & filters.command(["co"],prefixes="."), group=19)
def avalqqq(bot,m:Message):
    global comentaval
    text=str(m.command[1])
    if text.lower()=='on' :
        comentaval=1
        m.edit_text("<i>Comment Is On Now</i>")
    elif text.lower()=='off':
        comentaval=0
        m.edit_text("<i>Comment Is Off Now</i>")

COMMENTe = ["🎮","👍","🔎","🎭","🤝","👍🏽","👌🏽","🦾","🍃","🌿","🗿","💻","🦠","💎","🔐","🔎","🔍","❣️","💕","1️⃣","🥇"]
@bot.on_message(linked_channel&~edited, group=18)
def comment1(_, m: Message):
    if comentaval==1:
        m.reply(random.choice(COMMENTe))




@bot.on_message(filters.me & filters.command(["weather"],prefixes="."), group=20)
async def weather(bot, m: Message):
    await m.edit_text("<i>Wait !</i>")
    if len(m.text.split()) == 1:
        await m.reply(
            f"Usage: `.weather <location>`", parse_mode="markdown"
        )
        return
    location = m.text.split(None, 1)[1]
    h = {"user-agent": "httpie"}
    a = requests.get(f"https://wttr.in/{location}?mnTC0&lang=en", headers=h)
    if (
        "**Sorry, we processed more than 1M requests today and we ran out of our datasource capacity.**"
        in a.text
    ):
        await m.reply("<i>Sorry!\nCannot Fetch Info, Api full !</i>")
        return
    weather = f"<code>{escape(a.text)}</code>"
    await m.edit_text(weather, parse_mode="html")
#-----------------------------------------------------------------------
@bot.on_message(filters.me & filters.command(["lock"],prefixes=".") &  group , group=20)
async def lock_perm(bot, m: Message):
    msg = ""
    sagi = ""
    media = ""
    webprev = ""
    polls = ""
    info = ""
    invite = ""
    pin = ""
    perm = ""

    lock_type = m.text.split(None, 1)[1]
    chat_id = m.chat.id

    if not lock_type:
        await m.edit_text("<i>I Can't Lock Nothing!</i>")
        await asyncio.sleep(5)
        return

    get_perm = await bot.get_chat(chat_id)

    msg = get_perm.permissions.can_send_messages
    sagi = get_perm.permissions.can_send_other_messages 
    webprev = get_perm.permissions.can_add_web_page_previews
    polls = get_perm.permissions.can_send_polls
    info = get_perm.permissions.can_change_info
    invite = get_perm.permissions.can_invite_users
    pin = get_perm.permissions.can_pin_messages

    if lock_type == "all":
        try:
            await bot.set_chat_permissions(chat_id, ChatPermissions())
            await m.edit_text(text="<i>🔒 Locked All Permission From This Chat!</i>")
            await asyncio.sleep(5)
            await bot.send_message(
                "me",
                "#LOCK\n\nCHAT: `{}` (`{}`)\nPERMISSIONS: `All Permissions`".format(
                    get_perm.title, chat_id
                ),
            )

        except Exception as e_f:
            await m.edit_text(
                f"<i>I Don't Have Permission To Do That</i>\n**<i>ERROR:</i>** `{e_f}`"
            )
            await asyncio.sleep(5)

        return

    if lock_type == "msg":
        msg = False
        perm = "messages"

    elif lock_type == "media":
        media = False
        perm = "audios, documents, photos, videos, video notes, voice notes"

    elif lock_type == "sagi":
        sagi = False
        perm = "sagi"

    elif lock_type == "webprev":
        webprev = False
        perm = "web page previews"

    elif lock_type == "polls":
        polls = False
        perm = "polls"

    elif lock_type == "info":
        info = False
        perm = "info"

    elif lock_type == "invite":
        invite = False
        perm = "invite"

    elif lock_type == "pin":
        pin = False
        perm = "pin"

    else:
        await m.edit_text("<i>Invalid Lock Type!</i>")
        await asyncio.sleep(5)
        return

    try:
        await bot.set_chat_permissions(
            chat_id,
            ChatPermissions(
                can_send_messages=msg,
                can_send_media_messages=media,
                can_send_other_messages=sagi,
                can_add_web_page_previews=webprev,
                can_send_polls=polls,
                can_change_info=info,
                can_invite_users=invite,
                can_pin_messages=pin,
            ),
        )

        await m.edit_text(text=f"<i>🔒 Locked {perm} For This Chat!</i>")
        await asyncio.sleep(5)
        await bot.send_message(
            "me",
            "#LOCK\n\nCHAT: `{}` (`{}`)\nPERMISSIONS: `{} Permission`".format(
                get_perm.title, chat_id, perm
            ),
        )

    except Exception as e_f:
        await m.edit_text(
            text=r"<i>I Don't Have Permission To Do That!</i>" "\n" f"**<i>ERROR:</i>** \n `{e_f}`"
        )
        await asyncio.sleep(5)
    return



#------------------------------------------------------------------
@bot.on_message(filters.me & filters.command(["setchatpic"],prefixes=".") &  group , group=20)
async def set_picture(bot, m: Message):
    chat_id = m.chat.id
    user_id = m.from_user.id
    check_status = await bot.get_chat_member(chat_id=chat_id, user_id=user_id)
    admin_strings = ["creator", "administrator"]
    if check_status.status not in admin_strings:
        await m.edit_text(f"<i>Im Not Admin !</i>") 
        await asyncio.sleep(2)
        await m.delete()
        return False 
    if m.chat.type in ["group", "supergroup"]:
        await m.edit_text("<i>Tring to Change Group Picture....</i>")
        chat_id = m.chat.id
        try:
            if m.reply_to_message and m.reply_to_message.media:
                file_id = m.reply_to_message.photo.file_id
                await bot.set_chat_photo(m.chat.id, photo=file_id)
                await m.edit_text(f"<i>Picture Has Been Set For This [chat](T.me/{m.chat.username}) !</i>" ,disable_web_page_preview=True)
            else:
                await m.edit_text("`<i>Reply To An Image To Set That As Group Pic</i>`")
        except Exception as ef:
            await m.edit_text(f"<i>Not Change Chat Pic For To:</i>\n`{ef}`")
            return True
    return

#------------------------------------------------------------------------------------
@bot.on_message(filters.me & filters.command(["profile"],prefixes="."),group=20)
async def update_profile(bot, m: Message):
    update = m.text.split(None, 2)
    msgreply = m.reply_to_message
    replytxt = m.reply_to_message

    # Set first_name
    if update[1] == "fname":
        if update[2]:
            try:
                await bot.update_profile(first_name=f"{update[2]}")
                await m.edit_text(f"**<i>Updated First Name To:</i>** `{update[2]}`")
            except Exception as ef:
                await m.edit_text(f"**<i>Error:</i>**\n`{ef}`")
                return
        elif msgreply and not update[2]:
            try:
                await bot.update_profile(first_name=f"{replytxt}")
                await m.edit_text(f"**<i>Updated First Name To:</i>** `{replytxt}`")
            except Exception as ef:
                await m.edit_text(f"**<i>Error:</i>**\n`{ef}`")
                return

    # Set last_name
    elif update[1] == "lname":
        if update[2]:
            try:
                await bot.update_profile(last_name=f"{update[2]}")
                await m.edit_text(f"**<i>Updated Last Name To:</i>** `{update[2]}`")
            except Exception as ef:
                await m.edit_text(f"**<i>Error:</i>**\n`{ef}`")
                return
        elif msgreply and not update[2]:
            try:
                await bot.update_profile(last_name=f"{replytxt}")
                await m.edit_text(f"**</i>Updated Last Name To:</i>** `{replytxt}`")
            except Exception as ef:
                await m.edit_text(f"**<i>Error:</i>**\n`{ef}`")
                return

    # Remove last_name
    elif update[1] == "rmlname":
        try:
            await bot.update_profile(last_name="")
            await m.edit_text(f"**<i>Removed Last Name !</i>**")
        except Exception as ef:
            await m.edit_text(f"**<i>Error:</i>**\n`{ef}`")
            return

    # Set bio
    elif update[1] == "bio":
        if update[2]:
            try:
                await bot.update_profile(bio=f"{update[2]}")
                await m.edit_text(f"**<i>Updated Bio To:</i> `{update[2]}`**")
            except Exception as ef:
                await m.edit_text(f"**<i>Error:</i>**\n`{ef}`")
                return
        elif msgreply and not update[2]:
            try:
                await bot.update_profile(bio=f"{replytxt}")
                await m.edit_text(f"**<i>Updated Bio To:</i>** `{replytxt}`")
            except Exception as ef:
                await m.edit_text(f"**<i>Error:</i>**\n`{ef}`")
    return


@bot.on_message(filters.me & filters.command(["rmpfp"],prefixes="."),group=20)
async def remove_pfp(bot, m: Message):
    photos = bot.get_profile_photos("me")
    try:
        bot.delete_profile_photos([p.file_id for p in photos[1:]])
        await m.edit_text(f"**<i>Removed Profile All Pictures !</i>**")
    except Exception as ef:
        await m.edit_text(f"**<i>Error:</i>**\n{ef}")
    return

#------------------------------------------------------------------------------------



@bot.on_message(filters.me & filters.command(["setchatname"],prefixes=".") &  group , group=20)
async def setchatname(bot, m: Message):
    chat_id = m.chat.id
    user_id = m.from_user.id
    check_status = await bot.get_chat_member(chat_id=chat_id, user_id=user_id)
    admin_strings = ["creator", "administrator"]
    if check_status.status not in admin_strings:
        await m.edit_text(f"<i>Im Not Admin !</i>") 
        await asyncio.sleep(2)
        await m.delete()
        return False 
    await m.edit_text("<i>Trying to Change Chat Name !</i>")
    chat_id = m.chat.id
    chat_title = m.text.split(None, 1)
    if m.reply_to_message:
        chat_title = m.reply_to_message.text
    else:
        chat_title = chat_title[1]
    try:
        await bot.set_chat_title(chat_id, chat_title)
        await m.edit_text(f"<i>Changed Chat Name to:</i> <code>{chat_title}</code>")
    except Exception as ef:
        await m.edit_text(f"<i>Not Change Chat Title For To:</i>\n`{ef}`")
        return True



@bot.on_message(filters.me & filters.command(["invitelink"],prefixes=".") &  group , group=21)
async def invitelink(bot, m: Message):
    try:
        chat_id = m.chat.id
        link = await bot.export_chat_invite_link(chat_id)
        await m.reply(f"<i>Link for Chat:</i>\n`{link}`")
    except Exception as ef:
        await m.edit_text(f"**<i>Error:</i>**\n`{ef}`")
    return
#------------------------------------------------------------------
DICE_E_MOJI = "🎲"
@bot.on_message(
 filters.me & filters.command(["dice"],prefixes="."), group=21
)
async def roll_dice(bot, m: Message):
    await m.delete()
    await bot.send_dice(
        chat_id=m.chat.id,
        emoji=DICE_E_MOJI,
        disable_notification=True,
    )


ADDAD = ("1","2","3","4","5","6")
@bot.on_message(filters.me & filters.command(["b"],prefixes="."), group=21)
async def runs(bot, m: Message):
    run = random.choice(ADDAD)
    if m.reply_to_message:
        await m.reply_to_message.reply_text(f"**Bendaz :** {run}")
        await m.delete()
    else:
        await m.delete()
        await m.reply(f"**Bendaz :** {run}")
    return


TASHKHIS=0
@bot.on_message(filters.me & filters.command(["tdice"],prefixes="."), group=21)
def Tashdice(c,m):
    global TASHKHIS
    text=str(m.command[1])
    if text.lower()=='on':
        TASHKHIS=1
        m.edit_text('<i>Diagnosis Stimulus Emoji Game Is Now On</i>')

    elif text.lower()=='off' :
        TASHKHIS=0
        m.edit_text('<i>Diagnosis Stimulus Emoji Game Is Now Off</i>')

    else:
        m.reply(":(")

    


@bot.on_message(~filters.me , group=22)
async def dice(bot, m:Message):
    if TASHKHIS==1:
        await m.reply_text(f"**<i>Number Of Your Game :</i>** `{m.dice.value}`")




Emogi = ["🎲", "🎯", "🏀", "⚽️", "🎳","🎰"]
@bot.on_message(filters.me & filters.command(["fun"],prefixes="."), group=22)
async def fune(bot, m: Message):
    await m.edit_text(";)")
    run2 = random.choice(Emogi)
    await bot.send_dice(m.chat.id , run2)
#----------------------------------------------------------------------
from telegraph import upload_file
@bot.on_message(filters.me & filters.command(["telegraph"],prefixes="."), group=22)
async def telegraph(bot, m: Message):
    replied = m.reply_to_message
    start_t = datetime.now()
    await m.edit_text("<i>Trying to paste to telegraph...</i>")
    if not replied:
        await m.edit_text("<i>Reply To A Supported Media File</i>")
        return
    if not (
        (replied.photo and replied.photo.file_size <= 5242880)
        or (replied.animation and replied.animation.file_size <= 5242880)
        or (
            replied.video
            and replied.video.file_size <= 5242880
        )
        or (
            replied.document
            and replied.document.file_name.endswith(
                (".jpg", ".jpeg", ".png", ".gif", ".mp4")
            )
            and replied.document.file_size <= 5242880
        )
    ):
        await m.edit_text("<i>Not supported !</i>")
        return
    download_location = await bot.download_media(
        message=m.reply_to_message, file_name="telepyrobot/downloads/"
    )
    await m.edit_text("<i>Pasting to telegraph...</i>")
    try:
        response = upload_file(download_location)
    except Exception as document:
        await m.reply(document)
    else:
        end_t = datetime.now()
        ms = (end_t - start_t).seconds
        await m.edit_text(
            f"<i>Document Passed To [Telegraph](https://telegra.ph{response[0]}) **in __{ms}__ seconds**</i>",
            disable_web_page_preview=True,
        )
    finally:
        os.remove(download_location)
    return
#------------------------------------------------------------------

#------------------------------------------------------------------
import youtube_dl
from urllib.parse import urlparse

def get_file_extension_from_url(url):
    url_path = urlparse(url).path
    basename = os.path.basename(url_path)
    return basename.split(".")[-1]

ydl_opts = {
    'format': 'bestaudio',
    'writethumbnail': True
}

@bot.on_message(filters.me & filters.command(["dlmusic"],prefixes="."), group=22)
async def music(_, message: Message):
    if len(message.command) != 2:
        await message.edit_text("`.dlmusic` <i>Needs A Link As Argument</i>")
        return
    link = message.text.split(None, 1)[1]
    m = await message.edit_text(f"Downloading [Link]({link})",
                                 disable_web_page_preview=True)
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
            # .webm -> .weba
            basename = audio_file.rsplit(".", 1)[-2]
            thumbnail_url = info_dict['thumbnail']
            thumbnail_file = basename + "." + \
                get_file_extension_from_url(thumbnail_url)
            if info_dict['ext'] == 'webm':
                audio_file_weba = basename + ".mp4"
                os.rename(audio_file, audio_file_weba)
                audio_file = audio_file_weba
    except Exception as e:
        await m.reply(str(e))
        return
        # info
    title = info_dict['title']
    webpage_url = info_dict['webpage_url']
    performer = info_dict['uploader']
    duration = int(float(info_dict['duration']))
    caption = f"[{title}]({webpage_url})"
    await m.delete()
    await message.reply_chat_action("upload_document")
    await message.reply_audio(audio_file, caption=caption,
                              duration=duration, performer=performer,
                              title=title, thumb=thumbnail_file)
    os.remove(audio_file)
    os.remove(thumbnail_file)
#---------------------------------------------------------------------------------------
from io import BytesIO
from os import path, remove
from time import time

import img2pdf
from PIL import Image

async def convert(
    main_message: Message,
    reply_messages,
    status_message: Message,
    start_time: float,
):
    m = status_message

    documents = []

    for message in reply_messages:
        if not message.document:
            return await m.edit("<i>Not Document, ABORTED !</i>")

        if message.document.mime_type.split("/")[0] != "image":
            return await m.edit("<i>Invalid Mime Type !</i>")

        if message.document.file_size > 5000000:
            return await m.edit("<i>Size Too Large, ABORTED !</i>")
        documents.append(await message.download())

    for img_path in documents:
        img = Image.open(img_path).convert("RGB")
        img.save(img_path, "JPEG", quality=100)

    pdf = BytesIO(img2pdf.convert(documents))
    pdf.name = "Qinbaz.pdf"

    if len(main_message.command) >= 2:
        pdf.name = main_message.text.split(None, 1)[1]

    elapsed = round(time.time() - start_time, 2)

    await main_message.reply_document(
        document=pdf,
        caption=section(
            "IMG2PDF",
            body={
                "Title": pdf.name,
                "Size": f"{pdf.__sizeof__() / (10**6)}MB",
                "Pages": len(documents),
                "Took": f"{elapsed}s",
            },
        ),
    )

    await m.delete()
    pdf.close()
    for file in documents:
        if path.exists(file):
            remove(file)


@bot.on_message(filters.me & filters.command(["pdf"],prefixes="."), group=23)
async def img_to_pdf(_, message: Message):
    reply = message.reply_to_message
    if not reply:
        return await message.edit_text(
            "<i>Reply to an image (as document) or group of images.</i>"
        )

    m = await message.edit_text("<i>Converting..</i>")
    start_time = time.time()

    if reply.media_group_id:
        messages = await bot.get_media_group(
            message.chat.id,
            reply.message_id,
        )
        return await convert(message, messages, m, start_time)

    return await convert(message, [reply], m, start_time)

#-----------------------------------------------------------------------
#@bot.on_message(text & group & ~filters.edited, group=3)
def reply_text(bot, m:Message):
    for word_lis in ['@','t.me','T.me','com','https','tg'] : 
        if word_lis in m.text:
            bot.delete_messages(
            chat_id=m.chat.id, message_ids=m.message_id
        )       
            m.reply(f" ارسال لینک در گروه ممنوع است  : {m.from_user.mention} ")
        break
#------------------------------------------------------------------
#@bot.on_message(text & group & ~filters.edited, group=1)
def reply_text(bot, m:Message):
    for word_lis in ['salam','سلام','hi','hello'] : 
        if word_lis in m.text:
                m.reply(f"hey")
                break
#-----------------------------------------------------------------

import re


def clear_string(msg: str):
    msg = re.sub(r"\<code\>(.*)\<\/code\>", "\g<1>", msg)
    msg = re.sub(r"\<i\>(.*)\<\/i\>", "\g<1>", msg)
    msg = re.sub(r"\<b\>(.*)\<\/b\>", "\g<1>", msg)
    msg = re.sub(r"\<u\>(.*)\<\/u\>", "\g<1>", msg)
    msg = re.sub(r"\*\*(.*)\*\*", "\g<1>", msg)
    msg = re.sub(r"\_\_(.*)\_\_", "\g<1>", msg)
    msg = re.sub(r"\`(.*)\`", "\g<1>", msg)
    return msg 


import io
from io import BytesIO
import os
import sys
import traceback





@bot.on_message(filters.me & filters.command(["py"],prefixes="."), group=23)
async def eval(bot, m: Message):
    status_m = await m.edit_text("**<i>Processing...</i>**")
    cmd = m.text.split(None, 1)[1]

    reply_to_id = m.message_id
    if m.reply_to_message:
        reply_to_id = m.reply_to_message.message_id

    old_stderr = sys.stderr
    old_stdout = sys.stdout
    redirected_output = sys.stdout = io.StringIO()
    redirected_error = sys.stderr = io.StringIO()
    stdout, stderr, exc = None, None, None

    try:
        await aexec(cmd, bot, m)
    except Exception:
        exc = traceback.format_exc()

    stdout = redirected_output.getvalue()
    stderr = redirected_error.getvalue()
    sys.stdout = old_stdout
    sys.stderr = old_stderr

    evaluation = ""
    if exc:
        evaluation = exc
    elif stderr:
        evaluation = stderr
    elif stdout:
        evaluation = stdout
    else:
        evaluation = "Success"

    final_output = (
        "**<b>CODE</b>: <code>{}</code>\n\n<b>OUTPUT</b>:\n<code>{}</code> \n**".format(
            cmd, evaluation.strip()
        )
    )

    await status_m.edit(final_output)
    return


async def aexec(code, c, m):
    exec(
        f"async def __aexec(bot, m: Message):"
        + "".join(f"\n {l}" for l in code.split("\n"))
    )
    return await locals()["__aexec"](bot, m)
#-------------------------------------------------------------------------------------------
n = "\n"
w = " "


bold = lambda x: f"**{x}:** "
bold_ul = lambda x: f"**--{x}:**-- "

mono = lambda x: f"`{x}`{n}"


def section(
    title: str,
    body: dict,
    indent: int = 2,
    underline: bool = False,
) -> str:

    text = (bold_ul(title) + n) if underline else bold(title) + n

    for key, value in body.items():
        text += (
            indent * w
            + bold(key)
            + ((value[0] + n) if isinstance(value, list) else mono(value))
        )
    return text


async def get_user_info(user, already=False):
    if not already:
        user = await bot.get_users(user)
    if not user.first_name:
        return ["Deleted account", None]
    user_id = user.id
    common_chats = await bot.get_common_chats(user.id)
    username = user.username
    first_name = user.first_name
    mention = user.mention("Link")
    dc_id = user.dc_id
    status = user.status
    scam = user.is_scam
    bot2 = user.is_bot
    veri = user.is_verified
    langcode = user.language_code
    delete = user.is_deleted 
    phone = user.phone_number
    contact = user.is_contact
    photo_id = user.photo.big_file_id if user.photo else None
    body = {
        "<i>ID</i>": user_id,
        "<i>DC</i>": dc_id,
        "<i>Name</i>": [first_name],
        "<i>Username</i>": [("@" + username) if username else "Null"],
        "<i>Mention</i>": [mention],
        "<i>Is Verified<i>": bool(veri),
        "<i>Is Your Contact</i>": bool(contact),
        "<i>Group In Common</i>": len(common_chats),
        "Is Deleted": bool(delete),
        "<i>Status</i>": status,
        "<i>Scam</i>": bool(scam),
        "<i>Is Bot</i>": bool(bot2),
        "<i>User Phone Number</i>" : [("+" + phone) if phone else "Null"]
    }

    caption = section("<i>User info</i>",body)
    return [caption, photo_id]



@bot.on_message(filters.me & filters.command(["info"],prefixes="."), group=24)
async def info_func(_, message: Message):
    if message.reply_to_message:
        user = message.reply_to_message.from_user.id
    elif len(message.command) == 1:
        user = message.from_user.id
    else:
        user = message.text.split(None, 1)[1]

    m = await message.edit_text("<i>Processing...</i>")

    try:
        info_caption, photo_id = await get_user_info(user)
    except Exception as e:
        return await m.edit(str(e))

    if not photo_id:
        return await m.edit(info_caption, disable_web_page_preview=True)
    photo = await bot.download_media(photo_id)

    await message.reply_photo(photo, caption=info_caption, quote=False)
    await m.delete()
    os.remove(photo)
#------------------------------------------------------------------------------------------
@bot.on_message(filters.me & filters.command(["ims"],prefixes=".")& ~filters.edited, group=24)
async def sticker_image(_, message: Message):
    r = message.reply_to_message

    if not r:
        return await message.edit_text("Reply to a sticker.")

    if not r.sticker:
        return await message.edit_text("Reply to a sticker.")

    m = await message.edit_text("<i>Sending...</i>")
    f = await r.download(f"{r.sticker.file_unique_id}.png")

    await gather(
        *[
            message.reply_photo(f),
            message.reply_document(f),
        ]
    )

    await m.delete()
    os.remove(f)




@bot.on_message(filters.me & filters.command(["ims2"],prefixes=".")& ~filters.edited, group=25)
async def sticker_image2(_, message: Message):
    r = message.reply_to_message

    if not r:
        return await message.edit_text("Reply to a sticker.")

    if not r.sticker:
        return await message.edit_text("Reply to a sticker.")

    m = await message.edit_text("<i>Sending...</i>")
    f = await r.download(f"{r.sticker.file_unique_id}.webm")

    await gather(
        *[
            message.reply_video(f),
            message.reply_document(f),
        ]
    )

    await m.delete()
    os.remove(f)






#-------------------------------------------------------------------------------------------
import urllib.parse
import requests
@bot.on_message(filters.me & filters.command(["webs"],prefixes=".")& ~filters.edited, group=27)
async def take_ss(_, message: Message):
       await message.edit_text("<i>Taking ScreenShot ....</i>")
       url2 = message.text.split(None, 1)[1]
       BASE = 'https://mini.s-shot.ru/1024x0/JPEG/1024/Z100/?'
       url = url2
       url = urllib.parse.quote_plus(url)
       print(url)

       path = 'target1.jpg'
       response = requests.get(BASE + url, stream=True)
       if response.status_code == 200:
            with open(path, 'wb') as file:
                for chunk in response:
                    file.write(chunk)
            await message.edit_text("**<i>Uploading</i>**")
            await message.reply_document(path)
            os.remove(path)
            await message.edit_text("<i>Successfully Uploaded</i>")
        
#-------------------------------------------------------------------------------------------
from yt_dlp import YoutubeDL
import asyncio
import math
import os
import time
import aiofiles
import aiohttp
import wget
from youtubesearchpython import SearchVideos
@bot.on_message(filters.me & filters.command(["v"],prefixes="."), group=25)
async def vsong(bot, message: Message):
    text = message.text.split(None, 1)[1]
    pablo = await message.edit_text(f"**<i>Wait (Download or searching)</i>** : `{text}`")
    if not text:
        await pablo.edit("Error!")
        return

    search = SearchVideos(f"{text}", offset=1, mode="dict", max_results=1)
    mi = search.result()
    mio = mi["search_result"]
    mo = mio[0]["link"]
    thum = mio[0]["title"]
    fridayz = mio[0]["id"]
    mio[0]["channel"]
    kekme = f"https://img.youtube.com/vi/{fridayz}/hqdefault.jpg"
    await asyncio.sleep(0.6)
    url = mo
    sedlyf = wget.download(kekme)
    opts = {        "format": "best",        "addmetadata": True,        "key": "FFmpegMetadata",        "prefer_ffmpeg": True,        "geo_bypass": True,        "nocheckcertificate": True,        "postprocessors": [{"key": "FFmpegVideoConvertor", "preferedformat": "mp4"}],        "outtmpl": "%(id)s.mp4",        "logtostderr": False,        "quiet": True,    }
    try:
        with YoutubeDL(opts) as ytdl:
            ytdl_data = ytdl.extract_info(url, download=True)
    except Exception as e:
        await message.edit_text(f"**Downloading** \n `{str(e)}`")
        return
    c_time = time.time()
    file_stark = f"{ytdl_data['id']}.mp4"
    capy = f"""
**<i>Vedio Name(link):</i>** [{thum}]({mo})
**[Qinbaz](t.me/Qinbaz)**
"""
    await bot.send_video(        message.chat.id,        video=open(file_stark, "rb"),        duration=int(ytdl_data["duration"]),        file_name=str(ytdl_data["title"]),        thumb=sedlyf,        caption=capy,        supports_streaming=True,        progress=progress,        progress_args=(            pablo,            c_time,            f"**Downloading :** `{text}`",            file_stark,        ),    )
    await pablo.delete()
    for files in (sedlyf, file_stark):
        if files and os.path.exists(files):
            os.remove(files)

def humanbytes(size):
    if not size:
        return ""
    power = 2 ** 10
    raised_to_pow = 0
    dict_power_n = {0: "", 1: "Ki", 2: "Mi", 3: "Gi", 4: "Ti"}
    while size > power:
        size /= power
        raised_to_pow += 1
    return str(round(size, 2)) + " " + dict_power_n[raised_to_pow] + "B"

async def progress(current, total, message, start, type_of_ps, file_name=None):
    now = time.time()
    diff = now - start
    if round(diff % 10.00) == 0 or current == total:
        percentage = current * 100 / total
        speed = current / diff
        elapsed_time = round(diff) * 1000
        if elapsed_time == 0:
            return
        time_to_completion = round((total - current) / speed) * 1000
        estimated_total_time = elapsed_time + time_to_completion
        progress_str = "{0}{1} {2}%\n".format(            "".join("🔴" for i in range(math.floor(percentage / 10))),            "".join("🔘" for i in range(10 - math.floor(percentage / 10))),            round(percentage, 2),        )

        tmp = progress_str + "{0} of {1}\nETA: {2}".format(            humanbytes(current), humanbytes(total), time_formatter(estimated_total_time)        )
        if file_name:
            try:
                await message.edit(                    "{}\n**Filename:** `{}`\n{}".format(type_of_ps, file_name, tmp)                )
            except FloodWait as e:
                await asyncio.sleep(e.x)
            except MessageNotModified:
                pass
        else:
            try:
                await message.edit("{}\n{}".format(type_of_ps, tmp))
            except FloodWait as e:
                await asyncio.sleep(e.x)
            except MessageNotModified:
                pass
def get_user(message: Message, text: str):
    asplit = None if text is None else text.split(" ", 1)
    user_s = None
    reason_ = None
    if message.reply_to_message:
        user_s = message.reply_to_message.from_user.id
        reason_ = text or None
    elif asplit is None:
        return None, None
    elif len(asplit[0]) > 0:
        user_s = int(asplit[0]) if asplit[0].isdigit() else asplit[0]
        if len(asplit) == 2:
            reason_ = asplit[1]
    return user_s, reason_
def get_readable_time(seconds: int) -> int:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]
    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)
    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "
    time_list.reverse()
    ping_time += ":".join(time_list)
    return ping_time
def time_formatter(milliseconds: int) -> str:
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = (        ((str(days) + "Day(s), ") if days else "")        + ((str(hours) + "houre(s), ") if hours else "")        + ((str(minutes) + "Minute(s), ") if minutes else "")        + ((str(seconds) + " Secend(s), ") if seconds else "")        + ((str(milliseconds) + " MicroSecend(s), ") if milliseconds else "")    )
    return tmp[:-2]
def get_file_extension_from_url(url):
    url_path = urlparse(url).path
    basename = os.path.basename(url_path)
    return basename.split(".")[-1]
async def download_song(url):
    song_name = f"{randint(6969, 6999)}.mp3"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status == 200:
                f = await aiofiles.open(song_name, mode="wb")
                await f.write(await resp.read())
                await f.close()
    return song_name

is_downloading = False
def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60 ** i for i, x in enumerate(reversed(stringt.split(":"))))



 #-------------------------------------------------------------------------------------------
#@bot.on_message(text)
def delete_message(bot, m:Message):
    for word_list in ['کص','ننت','WTF','کون','کونی','کیر','fuck','دالگت','کس','خر','shit','جنده']:
     if word_list in m.text:
        bot.delete_messages(m.chat.id , m.message_id)
        bot.send_message(m.chat.id, f"بی ادب {m.from_user.mention}")
        break







print("im update")
bot.run()

