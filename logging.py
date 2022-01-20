import discord
from datetime import datetime
from discord.ext import commands

class Logging(commands.Cog):
    def __init__(self, client):
      self.client = client

    @commands.Cog.listener()
    async def on_user_update(self, before, after):
      if before.name != after.name:
        embed=discord.Embed(title="**Name Change**", description=f"**Before:** {before.name}\n**After:** {after.name}", color=0x35ABEE)
        embed.set_author(name=f'{after.name}#{after.discriminator}', icon_url=after.avatar_url)
        embed.timestamp = datetime.utcnow()
        embed.set_thumbnail(url=after.avatar_url)
        await self.client.get_channel(929447421438746624).send(embed=embed)
        
      if before.discriminator != after.discriminator:
        embed=discord.Embed(title="**Discriminator Change**", description=f"**Before:** {before.discriminator}\n**After:** {after.discriminator}", color=0x35ABEE)
        embed.timestamp = datetime.utcnow()
        embed.set_author(name=f'{after.name}#{after.discriminator}', icon_url=after.avatar_url)
        embed.set_thumbnail(url=after.avatar_url)
        await self.client.get_channel(929447421438746624).send(embed=embed)
  
      if before.avatar_url != after.avatar_url:
        embed=discord.Embed(title="**Avatar Change**", description=f"{after.mention}", color=0x35ABEE)
        embed.timestamp = datetime.utcnow()
        embed.set_author(name=f'{after.name}#{after.discriminator}', icon_url=after.avatar_url)
        embed.set_thumbnail(url=after.avatar_url)
        await self.client.get_channel(929447421438746624).send(embed=embed)

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
      if before.display_name != after.display_name:
        embed=discord.Embed(title="**Nickname Change**", description=f"**Before:** {before.display_name}\n**After:** {after.display_name}", color=0x35ABEE)
        embed.set_author(name=f'{after.name}#{after.discriminator}', icon_url=after.avatar_url)
        embed.timestamp = datetime.utcnow()
        embed.set_thumbnail(url=after.avatar_url)
        await self.client.get_channel(929447421438746624).send(embed=embed)      

      if before.status != after.status:
        if after.name == "Countr#3266" and after.status == "offline":
          channel = await self.client.get_channel(931920178244112434)
          role = await self.client.get_role(847725257716138005)
          overwrites = channel.overwrites_for(role)
          overwrites.send_messages = False
          await channel.set_permissions(role, overwrite=overwrites)
          await channel.send('As <@467377486141980682> is offline the channel will be locked.')
          
        if after.name == "Countr#3266" and before.status == "offline" and after.status == "online":
          channel = await self.client.get_channel(931920178244112434)
          role = await self.client.get_role(847725257716138005)
          overwrites = channel.overwrites_for(role)
          overwrites.send_messages = True
          await channel.set_permissions(role, overwrite=overwrites)
          b = await channel.send('As <@467377486141980682> is online the channel will be unlocked.')
          await b.delete()
          
        #embed=discord.Embed(title="**Status Change**", description=f"**Before:** {before.status}\n**After:** {after.status}", color=0x35ABEE)
        #embed.set_author(name=f'{after.name}#{after.discriminator}', icon_url=after.avatar_url)
        #embed.timestamp = datetime.utcnow()
        #embed.set_thumbnail(url=after.avatar_url)
        #await self.client.get_channel(929447421438746624).send(embed=embed)      
        
      if len(before.roles) < len(after.roles):
        embed=discord.Embed(title="**Roles Added**", description=", ".join([role.mention for role in after.roles if role not in before.roles]), color=0x35ABEE)
        embed.set_author(name=f'{after.name}#{after.discriminator}', icon_url=after.avatar_url)
        embed.timestamp = datetime.utcnow()
        embed.set_thumbnail(url=after.avatar_url)
        await self.client.get_channel(929447421438746624).send(embed=embed)      

      elif len(before.roles) > len(after.roles):
        embed=discord.Embed(title="**Roles Removed**", description=", ".join([role.mention for role in before.roles if role not in after.roles]), color=0x35ABEE)
        embed.set_author(name=f'{after.name}#{after.discriminator}', icon_url=after.avatar_url)
        embed.timestamp = datetime.utcnow()
        embed.set_thumbnail(url=after.avatar_url)
        await self.client.get_channel(929447421438746624).send(embed=embed)      
    
    @commands.Cog.listener()
    async def on_message_edit(self, before,after):
      if before.content != after.content:
        embed=discord.Embed(title=f"**Message Edited in {before.channel.mention}**", description=f"**Before:** {before.content}\n**After:** {after.content}", color=0x35ABEE)
        embed.set_author(name=f'{after.author.name}#{after.author.discriminator}', icon_url=after.author.avatar_url)
        embed.timestamp = datetime.utcnow()
        embed.set_thumbnail(url=after.author.avatar_url)
        await self.client.get_channel(929447421438746624).send(embed=embed)      
        
    @commands.Cog.listener()
    async def on_message_delete(self, message):
        embed = discord.Embed(title=f"**Message Deleted in {message.channel.mention}**", description=f"{message.content}",color=0xF54C47)
        embed.set_author(name=message.author, icon_url=message.author.avatar_url)
        embed.timestamp = message.created_at       
        await self.client.get_channel(929447421438746624).send(embed=embed)      

def setup(client):
  client.add_cog(Logging(client))