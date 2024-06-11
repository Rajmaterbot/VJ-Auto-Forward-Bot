from os import getenv

class Config(object):
      API_HASH = getenv("API_HASH", "01fd2c9e36d0754b9fd24f15359fe22e")
      API_ID = int(getenv("API_ID", "24120186"))
      AS_COPY = True if getenv("AS_COPY", True) == "`{file_name}`" else True
      BOT_TOKEN = getenv("BOT_TOKEN", "7252797686:AAF_xw2oBKsYes_xfEX_1kMQXID3AuhSb8s")
      CHANNEL = list(x for x in getenv("CHANNEL_ID", "-1001688659594:-1002243504787").replace("\n", " ").split(' '))


# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
