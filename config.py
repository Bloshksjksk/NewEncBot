import os, time, re

id_pattern = re.compile(r'^.\d+$') 


class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "4682685")  # ⚠️ Required
    API_HASH  = os.environ.get("API_HASH", "3eba5d471162181b8a3f7f5c0a23c307") # ⚠️ Required
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5658651338:AAGN4uc4bzEH7cYpjMWdekxV4P94HDFJ5oU") # ⚠️ Required
    FORCE_SUB = os.environ.get('FORCE_SUB', '-1001678093514') # ⚠️ Required
    AUTH_CHANNEL = int(FORCE_SUB) if FORCE_SUB and id_pattern.search(
    FORCE_SUB) else None
   
    # database config
    DB_URL  = os.environ.get("DB_URL", "mongodb+srv://misoc51233:O7KeKHeGuye685YM@cluster0.luylexo.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")  # ⚠️ Required
    DB_NAME  = os.environ.get("DB_NAME","SnowEncoderBot") 

    # Other Configs 
    ADMIN = int(os.environ.get("ADMIN", "945284066")) # ⚠️ Required
    LOG_CHANNEL = int(os.environ.get('LOG_CHANNEL', '-1001629153349')) # ⚠️ Required
    BOT_UPTIME = BOT_UPTIME  = time.time()
    START_PIC = os.environ.get("START_PIC", "https://th.bing.com/th/id/OIG2.F4kFpmzg7gXzdIWqrUF6?pid=ImgGn")

    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))
    PORT = int(os.environ.get("PORT", "8080"))


    caption = """
**File Name**: {0}

**Original File Size:** {1}
**Encoded File Size:** {2}
**Compression Percentage:** {3}

__Downloaded in {4}__
__Encoded in {5}__
__Uploaded in {6}__

𝚃𝚑𝚊𝚗𝚔𝚜 𝙵𝚘𝚛 𝚄𝚜𝚒𝚗𝚐 𝙼𝚎🤘🏻
"""
