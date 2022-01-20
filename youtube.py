import json
import requests
import re
from discord.ext import commands, tasks
from datetime import datetime

def getTime():
  timeFormat = "%d-%m-%Y %H:%M:%S %Z%z"
  time1 = datetime.now()
  time2 = time1.strftime(timeFormat)
  return time2

class Youtube(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.Cog.listener()
  async def on_ready(self):
      self.checkforvideos.start()
    
  @tasks.loop(seconds=60)
  async def checkforvideos(self):
    with open("data/youtubedata.json", "r") as f:
      data=json.load(f)

    with open("data/youtube_searches.txt", "a+") as ytData:
      ytData.write(f"Searched at - {getTime()}\n")
      
    for youtube_channel in data:
      channel = f"https://www.youtube.com/channel/{youtube_channel}"
      html = requests.get(channel+"/videos").text
  
      try:
        latest_video_url = "https://www.youtube.com/watch?v=" + re.search('(?<="videoId":").*?(?=")', html).group()
      except:
        continue
  
      if not str(data[youtube_channel]["latest_video_url"]) == latest_video_url:

        data[str(youtube_channel)]['latest_video_url'] = latest_video_url
  
        with open("data/youtubedata.json", "w") as f:
          json.dump(data, f, indent=4)
  
        discord_channel_id = data[str(youtube_channel)]['notifying_discord_channel']
        discord_channel = self.client.get_channel(int(discord_channel_id))

        if {data[str(youtube_channel)]['channel_name']} == "SP1KE":
          toPing = "<@931240187386802246>"
        elif {data[str(youtube_channel)]['channel_name']} == "DRags":
          toPing = "<@931240279854436355>"
          
        msg = f"{toPing}\n\n**{data[str(youtube_channel)]['channel_name']} Just Uploaded a new Video**\n*Go check it out here!*\n{latest_video_url}"
        
        await discord_channel.send(msg)
  
  @commands.command()
  @commands.has_role("Community Managers")
  async def stop_notifying(self, ctx):
    self.checkforvideos.stop()
    await ctx.send("<@852800494791294976> Stopped Notifying")
  
  @commands.command()
  @commands.has_role("Community Managers")
  async def start_notifying(self, ctx):
    try:
      self.checkforvideos.start()
      await ctx.send("<@852800494791294976> Now Notifying")
    except RuntimeError:
      pass
          
def setup(client):
  client.add_cog(Youtube(client))
