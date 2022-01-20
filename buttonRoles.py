from discord.ext import commands
#from discord.ui import Button, View

class ButtonRoles(commands.Cog):
  def __init__(self, client):
    self.client = client
    
  #@commands.command()
  #@commands.is_owner()
  #async def roles(self, ctx):
 #   button = Button(label="Be Pog now!", style=discord.ButtonStyle.red, emoji="😎")
  #  view = View()
   # view.add_item(button)
    #await ctx.send("Do you want to be pog?", view=view)

    
def setup(client):
  client.add_cog(ButtonRoles(client))
    