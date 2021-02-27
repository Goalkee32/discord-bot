import discord
from discord.ext import commands

import random


client = commands.Bot(command_prefix = '')

@client.event
async def on_ready(): 
    print('Online')

@client.command(aliases=['champange', 'alkis'])
async def bubbel(ctx):
    responses = ['https://www.youtube.com/watch?v=7WYwNZMAaKc',
                'https://www.youtube.com/watch?v=PoZYMPOryvA',
                'https://www.youtube.com/watch?v=mFy-tIa61TQ']
                
    await ctx.send(f'Vad gott: {random.choice(responses)}')

@client.command(aliases=['måltid', 'högtid'])
async def hungrig(ctx):
    responses = ['https://www.youtube.com/watch?v=OA-cl9eHE8w',
                'https://www.youtube.com/watch?v=THOmMVHB_3o']
    await ctx.send(f'Det kanske låter gott: {random.choice(responses)}')

@client.command(aliases=['!clear', 'clear'])
async def _clear(ctx, amount=10):
    await ctx.channel.purge(limit=amount)

@client.command(aliases=['!kick', 'kick'])
async def _kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'Kickade {member.mention}')

@client.command(aliases=['!ban', 'ban'])
async def _ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Bannade {member.mention}')

@client.command(aliases=['!unban', 'unban'])
async def _unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users: 
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbannade {user.mention}')
            return


client.run('ODE1MjEwMzUzNTk2MTcwMjUw.YDpFzg.pOOGTP4qiQ4Os2aPUdUh-dB8oIs')
