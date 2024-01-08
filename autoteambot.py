import discord
from discord.ext import commands
import random

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)
TOKEN = 'YOUR_TOKEN'


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("!팀생성"))

@bot.command(name='팀생성')
async def create_teams(ctx, team_size: int):
    # 음성 채널에 접속되어 있는 멤버들 가져오기
    channel = ctx.author.voice.channel
    members = channel.members
    
    # 멤버들을 무작위로 섞기
    random.shuffle(members)
    
    # 팀 생성
    teams = [members[i:i+team_size] for i in range(0, len(members), team_size)]
    
    # 팀 출력
    for i, team in enumerate(teams, start=1):
        team_names = ', '.join([member.display_name for member in team])
        await ctx.send(f'Team {i}: {team_names}')
        
bot.run(TOKEN)
