import discord 
from discord.ext import commands
from discord.utils import get 
import os

PREFIX = '/'
client = commands.Bot(command_prefix = PREFIX)
bad_words = ['пидор', 'хуйло' , 'блять','пиздец','ахуеть', 'нихуя', 'сука', 'нихуя', 'пидорас',
 'гондон', 'гандон', 'чмо', 'ебать', 'вахуе', 'в ахуе', 'ска', 'ебаный в рот', 'хули']
csgome = ['го кс', 'гокс', 'gocs', 'go cs', 'cs', 'кс', 'катать', '']


#/help
@client.event 
async def on_ready():
	print ('BOT connected')
	await client.change_presence(status = discord.Status.online, activity = discord.Game('Discord'))

#clear message
@client.command(pass_context = True)
@commands.has_permissions(administrator = True)
async def clear (ctx, amount = 2):
	await ctx.channel.purge(limit = amount)

#Kick 
@client.command( pass_context = True)
@commands.has_permissions(administrator = True)
async def kick (ctx, member: discord.Member, *, reason = 'No reason'):
	await ctx.channel.purge( limit = 1)
	await member.kick(reason = reason)
	await ctx.send(f'kick user{member.mention}')


#callplayincsgo
@client.command( pass_context = True)
async def csgo( ctx, arg ):
	await ctx.channel.purge( limit = 1)
	emb = discord.Embed(title = 'СS:GO')
	emb.add_field (name = 'Прекрастный человек <<'+ ctx.author.name +'>> зовет играть ', value = f'Дорогой {arg} заходи катать в CSGO')
	emb.set_image(url = 'https://avatars.mds.yandex.net/get-zen_doc/1602486/pub_5d98b2e73d873600b14f6859_5d9a6fda1d656a00ad1fe6b3/scale_1200')
	await ctx.send(f'{arg}')
	await ctx.send(embed = emb)

#callplayingta5
@client.command( pass_context = True)
async def gta5( ctx,arg ):
	await ctx.channel.purge( limit = 1)
	emb = discord.Embed(title = 'GTA 5')
	emb.add_field (name = 'Прекрастный человек <<'+ ctx.author.name +'>> зовет играть ', value = f'Дорогой {arg} заходи чилить в GTA 5')
	emb.set_image(url = 'https://b1.gmbox.ru/c/1092.jpg')
	await ctx.send(f'{arg}')
	await ctx.send(embed = emb)

#call of minecraft
@client.command( pass_context = True)
async def minecraft( ctx, arg ):
	await ctx.channel.purge( limit = 1)
	emb = discord.Embed(title = 'Minecraft')
	emb.add_field (name = 'Прекрастный человек <<'+ ctx.author.name +'>> зовёт играть ', value = f'Дорогой {arg} заходи чилить в Minecraft')
	emb.set_image(url = 'https://img1.akspic.ru/image/128271-voda-otrazhenie-vodnyj_put-utro-majnkraft-3840x2160.jpg')
	await ctx.send(f'{arg}')
	await ctx.send(embed = emb)


#callmoders
@client.command( pass_context = True)
@commands.has_permissions(administrator = True)
async def moders( ctx ):
	await ctx.channel.purge( limit = 1)
	arg = "<@703160584442609785>"
	emb = discord.Embed(title = 'Призыв долбоебов')
	emb.add_field (name = 'Прекрастный <<ДОЛБОЕБ>> <<'+ ctx.author.name +'>> зовёт вас поговорить', value = f'Дорогие'+arg+' заходи <<СУКА>> в ГОЛОСОВОЙ ВАС ЖДУТ АДМЭНЫ')
	emb.set_image(url = 'https://d1hlpam123zqko.cloudfront.net/907/601/456/1280003015-1s8tc0e-im5arjdh3321h6k/original/file.jpg')
	await ctx.send('НУКА НАХУЙ ЗАШЛИ'+arg)
	await ctx.send(embed = emb)

#filterchat
@client.event
async def on_message(message):
	await client.process_commands( message )
	msg = message.content.lower()
	if msg in bad_words:
		await message.delete()
		await message.author.send(f'{message.author.name}, слушай не пиши такие сообщения иначе бан!')
	elif msg in csgome:
		arg = "<@435609317727797249>"
		await message.send(arg)

#join
@client.command()
async def join(ctx):
	await ctx.channel.purge( limit = 1)
	global voice
	channel = ctx.message.author.voice.channel
	voice = get(client.voice_clients, guild = ctx.guild)
	if voice and voice.is_connected():
		await voice.move_to(channel)
	else:
		voice = await channel.connect()
		await ctx.send (f'Бот присоединился к каналу:{channel}')

#leave
@client.command()
async def leave(ctx):
	await ctx.channel.purge( limit = 1)
	channel = ctx.message.author.voice.channel
	voice = get(client.voice_clients, guild = ctx.guild)
	if voice and voice.is_connected():
		await voice.disconnect()
	else:
		voice = await channel.connect()
		await ctx.send (f'Бот отключился от канала:{channel}')

#Connect
token = os.environ.get('BOT_GET')
client.run( str(token) )
