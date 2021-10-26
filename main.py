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
import os
def convert_bytes(num):
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0

def file_size(file_path):
    if os.path.isfile(file_path):
        file_info = os.stat(file_path)
        return convert_bytes(file_info.st_size)


# Main
#------
@app.on_message(filters.command(['start']))
def start(_, msg):
  msg.reply("Send me files to get the file size.")

@app.on_message()
def fileinfo(client,msg):
  rep = msg.reply_text("`Uploading...\nPlease Wait, You\'ll be notified once the process is finished!`", quote = True)
  try:
    dl = msg.download()
    if dl:
      rep.edit(f"`Upload Successfull!\nProcessing...")
      size = file_size(dl)
      rep.delete()
      msg.reply(f"File Size: {size}", quote = True)
    else:
      rep.delete()
      msg.reply("`Some error occured :/`", quote = True)
  except:
    rep.delete()
    msg.reply("`No file found in the message :/`", quote = True)




app.run()
