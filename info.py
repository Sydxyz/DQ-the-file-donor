import re
from os import environ
from Script import script 

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ['API_ID'])
API_HASH = environ['API_HASH']
BOT_TOKEN = environ['BOT_TOKEN']

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))

PICS = (environ.get('PICS', 'https://graph.org/file/0fbca0c54571553e6b677.jpg https://graph.org/file/6d5f1aa50c313eb2e6c5f.jpg https://graph.org/file/e2993dbcba456c8fdd401.jpg https://graph.org/file/12fc5f2761710b5592dc7.jpg https://graph.org/file/c2fabc0db3dac832b4502.jpg https://graph.org/file/9b71714b8e6255c452c1d.jpg https://graph.org/file/c984f1d2e4b178a85688b.jpg https://graph.org/file/d5c89abf2a6ebe8912106.jpg https://graph.org/file/ffb3cb4e40ae0ff7fd013.jpg https://graph.org/file/dc9f6aacbfe27dcfcd5b5.jpg https://graph.org/file/dea2d59ee82a7b967be9c.jpg https://graph.org/file/9d9136767b1cea04dc435.jpg https://graph.org/file/dea2d59ee82a7b967be9c.jpg https://graph.org/file/9a1076b6603e5f574b026.jpg https://graph.org/file/2bb4b51510a706273b11f.jpg https://graph.org/file/8b2b612e19730c3a9d7c3.jpg https://graph.org/file/17861acd359bbe4b98ced.jpg https://graph.org/file/9633c1d6510329007cf31.jpg https://graph.org/file/9434b5bc0f77db797df2f.jpg https://graph.org/file/2bb4b51510a706273b11f.jpg https://graph.org/file/9a1076b6603e5f574b026.jpg https://graph.org/file/ed5a62b08977abe123c35.jpg https://graph.org/file/b3f7a877793d6ddfe71cc.jpg https://graph.org/file/582b30aad797964979186.jpg https://graph.org/file/40850ddfa8f54c1c4f81b.jpg https://graph.org/file/32edfca6d37628faa6c65.jpg https://graph.org/file/42b7f439a001a766dcaa0.jpg https://graph.org/file/11ce92deb96ccfce472b3.jpg https://graph.org/file/871324cfa1e6dfb696312.jpg https://graph.org/file/525c5b1821ab231786b12.jpg https://graph.org/file/5339642869fd8ef095fec.jpg https://graph.org/file/3f803b7732216a7c7a45b.jpg https://graph.org/file/3a404e1a01076e8e443a5.jpg https://graph.org/file/feeb6092bf95acc2272d8.jpg https://graph.org/file/6851314ef223779a4d08b.jpg https://graph.org/file/1a6a6528ed7505cf9a449.jpg https://graph.org/file/5b5929d28023b768a78be.jpg https://graph.org/file/b0815b6ad638be4296127.jpg https://graph.org/file/cbbe85a6053211becf918.jpg https://graph.org/file/1bf03a3fb6df8f5fc74b3.jpg https://graph.org/file/9e8ca9dc0e6bee7b1c18b.jpg https://graph.org/file/40850ddfa8f54c1c4f81b.jpg https://graph.org/file/54be1b314245d9836ce50.jpg https://graph.org/file/3be609fa29df3ecd5db80.jpg https://graph.org/file/c79e3912c7da4185d999f.jpg https://graph.org/file/3471c0d113ca9f03d9f5c.jpg https://graph.org/file/e7c5bcb34a8c59f851748.jpg https://graph.org/file/0614fd746e907cb88b62b.jpg https://graph.org/file/eb4460e25712996da4e62.jpg https://graph.org/file/baaa08f211c749905c6fb.jpg https://graph.org/file/3d265b47cc29c245291a8.jpg https://graph.org/file/43fde3f0c2ad2bd5cae47.jpg https://graph.org/file/787103c7def1de6fa21c6.jpg https://graph.org/file/14d3c49f250741d76037c.jpg https://graph.org/file/bef4370ccae8d51e05835.jpg https://graph.org/file/7868f5dacc0f71553ccd2.jpg https://graph.org/file/8871331e997abde9885ce.jpg https://graph.org/file/81f6f1f0b27b9117afd0a.jpg https://graph.org/file/150c3bf7316a94cffb1dd.jpg https://graph.org/file/205be2966b576fde8fea0.jpg https://graph.org/file/b24227885fb8ed3555871.jpg https://graph.org/file/a029cae4e05b7e45afee4.jpg https://graph.org/file/bd22c125de5c3fb300b48.jpg  https://graph.org/file/80c304101716898063142.jpg https://graph.org/file/d27823791badb5aa37835.jpg https://graph.org/file/30e193f39935af1673cfc.jpg https://graph.org/file/86311bccc20ac5e540f52.jpg https://graph.org/file/9f881fc390b3c5ad069b8.jpg https://graph.org/file/09e9d12dfb1b8b45f0f45.jpg https://graph.org/file/af9878994347f1e6c1ab0.jpg https://graph.org/file/034bcd00e8c55af32cf46.jpg https://graph.org/file/83fe790f8eaab08bf8a42.jpg https://graph.org/file/13d941fda884595eb43e0.jpg https://graph.org/file/9c38f3c50e3050729ed47.jpg https://graph.org/file/eb66c9f2c52ba4820a1bf.jpg https://graph.org/file/9829f8bd4e6a528ca5867.jpg https://graph.org/file/7f4a9e2a88027ca6f945e.jpg https://graph.org/file/b3eaa7cb07f991a56bb6e.jpg https://graph.org/file/600ef9a37616783259840.jpg https://graph.org/file/b086be6d635b73fa54b8a.jpg https://graph.org/file/46ec02065db1afe56d623.jpg https://graph.org/file/1319115951e0526a3b528.jpg')).split()
NOR_IMG = environ.get("NOR_IMG", "https://telegra.ph/file/46443096bc6895c74a716.jpg")
MELCOW_VID = environ.get('MELCOW_VID', 'https://telegra.ph/file/451f038b4e7c2ddd10dc0.mp4').split()
SPELL_IMG = environ.get("SPELL_IMG", "https://telegra.ph/file/5e2d4418525832bc9a1b9.jpg")

# Admins, Channels & Users
support_chat_id = environ.get('SUPPORT_CHAT_ID')
SUPPORT_CHAT_ID = int(support_chat_id) if support_chat_id and id_pattern.search(support_chat_id) else None
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '0').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL')
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None
reqst_channel = environ.get('REQST_CHANNEL_ID')
REQST_CHANNEL = int(reqst_channel) if reqst_channel and id_pattern.search(reqst_channel) else None
SUPPORT_CHAT_ID = int(environ.get('SUPPORT_CHAT_ID'))
NO_RESULTS_MSG = bool(environ.get("NO_RESULTS_MSG", False))
SYD_LINKS = 'https://t.me/+0Zi1FC4ulo8zYzVl'
SYD_SHARE = 'https://t.me/000000000'
# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "")
DATABASE_NAME = environ.get('DATABASE_NAME', "Rajappan")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Others
IS_VERIFY = bool(environ.get('IS_VERIFY', False))
VERIFY2_URL = environ.get('VERIFY2_URL', "mdisklink.link")
VERIFY2_API = environ.get('VERIFY2_API', "4fa150d44b4bf6579c24b33bbbb786dbfb4fc673")
SHORTLINK_URL = environ.get('SHORTLINK_URL', 'gplinks.in')
SHORTLINK_API = environ.get('SHORTLINK_API', 'bae09e598efe918f2a81c4310e461a0ec32b79ec')
IS_SHORTLINK = bool(environ.get('IS_SHORTLINK', False))
DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '0').split()]
MAX_B_TN = environ.get("MAX_B_TN", "5")
MAX_BTN = is_enabled((environ.get('MAX_BTN', "True")), True)
PORT = environ.get("PORT", "8080")
GRP_LNK = environ.get('GRP_LNK', 'https://t.me/+I0u1R3m5zZAzYzBl')
CHNL_LNK = environ.get('CHNL_LNK', 'https://t.me/+0P4lGV1P6VcxYzll')
MSG_ALRT = environ.get('MSG_ALRT', 'Wʜᴀᴛ Aʀᴇ Yᴏᴜ Lᴏᴏᴋɪɴɢ Aᴛ 😊 ? Dᴏɴᴛ ᴛᴏᴜᴄʜ ᴍy ᴩʀɪᴠᴀᴛᴇ ᴩᴀʀᴛ😁')
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', 0))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'Mod_MoviezX')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "False")), False)
IMDB = is_enabled((environ.get('IMDB', "True")), True)
AUTO_FFILTER = is_enabled((environ.get('AUTO_FFILTER', "True")), True)
AUTO_DELETE = is_enabled((environ.get('AUTO_DELETE', "True")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", f"{script.IMDB_TEMPLATE_TXT}")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"
