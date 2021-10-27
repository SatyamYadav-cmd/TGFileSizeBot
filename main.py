# Replace the following variable with your own bot token.

token = "YOUR_BOT_TOKEN_HERE"


# Don't Edit the following code (Line 8-15)
#==========================================
apiid = 6
apihash = "eb06d4abfb49dc3eeb1aeb98ae0f581e"
#------------------------------------------
from pyrogram import Client, filters
app = Client(":memory:",
bot_token=token,
api_id=apiid,
api_hash=apihash)
#==========================================


# Functions
#----------

def convert_bytes(num):
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0

types = ["animation", "audio", "photo", "video", "document", "sticker"]

def get_bytes(msg):
  typ=None
  for x in types:
    if x in msg:
      typ = x
      break
  return msg[typ]['file_size'] if typ else typ


# Main
#------
@app.on_message(filters.command(['start']))
def start(_, msg):
  msg.reply("Send me files to get the file size.")

@app.on_message()
def fileinfo(client,msg):
  rep = msg.reply("Processing...", quote = 1)
  msgS = str(msg).replace("True", "true").replace("False", "false")
  msgD = eval(msgS)
  try:rep.edit(f"File Size: {convert_bytes(get_bytes(msgD))}")
  except: rep.edit("`ERROR: No file found in the message.`")



app.run()
