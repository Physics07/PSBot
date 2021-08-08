import asyncio, discord
import random
import requests
import json
import urllib
import math
import urllib.request as req
from bs4 import BeautifulSoup
from openpyxl import load_workbook
from openpyxl import Workbook
from discord.ext import commands
client=discord.Client()
tokenfind=open("d:/bot/bottoken.txt", "r")
token=tokenfind.readline()
tokenfind.close()
game=discord.Game("%help 로 도움말 받기")
bot=commands.Bot(command_prefix="%", status=discord.Status.online, activity=game)
bot.remove_command('help')
creator=client.get_user(744736415111446650)
tiercolor=[0x2d2d2d, 0xad5600, 0x435f7a, 0xec9a00, 0x27e2a4, 0x00b4fc, 0xff0062, 0x87e5ff]
tiername=["Unrated", "Bronze V", "Bronze IV", "Bronze III", "Bronze II", "Bronze I", "Silver V", "Silver IV", "Silver III", "Silver II", "Silver I", "Gold V", "Gold IV", "Gold III", "Gold II", "Gold I", "Platinum V", "Platinum IV", "Platinum III", "Platinum II", "Platinum I", "Diamond V", "Diamond IV", "Diamond III", "Diamond II", "Diamond I", "Ruby V", "Ruby IV", "Ruby III", "Ruby II", "Ruby I", "Master"]
levellist=["https://cdn.discordapp.com/attachments/873605368507404378/873763022236188692/0.png", "https://cdn.discordapp.com/attachments/873605368507404378/873763040091308112/1.png", "https://cdn.discordapp.com/attachments/873605368507404378/873763051797643284/2.png", "https://cdn.discordapp.com/attachments/873605368507404378/873763064321818694/3.png", "https://cdn.discordapp.com/attachments/873605368507404378/873763093660983296/4.png", "https://cdn.discordapp.com/attachments/873605368507404378/873763121355960381/5.png", "https://cdn.discordapp.com/attachments/873605368507404378/873763145783590912/6.png", "https://cdn.discordapp.com/attachments/873605368507404378/873763159243120670/7.png", "https://cdn.discordapp.com/attachments/873605368507404378/873763171117187192/8.png", "https://cdn.discordapp.com/attachments/873605368507404378/873763182060113971/9.png", "https://cdn.discordapp.com/attachments/873605368507404378/873763195054088212/10.png", "https://cdn.discordapp.com/attachments/873605368507404378/873763205736955924/11.png", "https://cdn.discordapp.com/attachments/873605368507404378/873763219443945493/12.png", "https://cdn.discordapp.com/attachments/873605368507404378/873763231439671356/13.png", "https://cdn.discordapp.com/attachments/873605368507404378/873763259390496808/14.png", "https://cdn.discordapp.com/attachments/873605368507404378/873763271197458472/15.png", "https://cdn.discordapp.com/attachments/873605368507404378/873763288301842532/16.png", "https://cdn.discordapp.com/attachments/873605368507404378/873763549539864596/17.png", "https://cdn.discordapp.com/attachments/873605368507404378/873763573480947762/18.png", "https://cdn.discordapp.com/attachments/873605368507404378/873763586252603473/19.png", "https://cdn.discordapp.com/attachments/873605368507404378/873763597690482738/20.png", "https://cdn.discordapp.com/attachments/873605368507404378/873763610411810836/21.png", "https://cdn.discordapp.com/attachments/873605368507404378/873763622973759539/22.png", "https://cdn.discordapp.com/attachments/873605368507404378/873763636949159966/23.png", "https://cdn.discordapp.com/attachments/873605368507404378/873763649079115826/24.png", "https://cdn.discordapp.com/attachments/873605368507404378/873763660806381568/25.png", "https://cdn.discordapp.com/attachments/873605368507404378/873763674790182912/26.png", "https://cdn.discordapp.com/attachments/873605368507404378/873763686693601322/27.png", "https://cdn.discordapp.com/attachments/873605368507404378/873763701344317500/28.png", "https://cdn.discordapp.com/attachments/873605368507404378/873763714665435146/29.png", "https://cdn.discordapp.com/attachments/873605368507404378/873763729412603924/30.png", "https://cdn.discordapp.com/attachments/873605368507404378/873763742763065344/31.png"]
@bot.event
async def on_ready():
    print("봇 시작")
@bot.event
async def on_message(msg):
    if msg.content=="마자효": 
        await msg.channel.send("마자효\n1104")
    else: 
        await bot.process_commands(msg)
@bot.command()
async def help(ctx):
    embed=discord.Embed(title="ps봇", color=0xec9a00)
    embed.add_field(name="%help", value="도움말을 표시합니다.", inline=False)
    embed.add_field(name="%p <problem number>", value="번호에 해당되는 백준 문제를 보여줍니다.", inline=False)
    embed.add_field(name="%search <query>", value="쿼리에 맞는 백준 문제를 검색하여 최대 5개까지 보여줍니다.", inline=False)
    embed.add_field(name="%profile <site> <handle>", value="그 핸들의 유저를 보여줍니다.", inline=False)
    await ctx.send(embed=embed)
@bot.command()
async def profile(ctx, arg):
    if arg=="boj":
        try:
            res=req.urlopen('https://solved.ac/api/v3/user/show?handle='+ctx.message.content.split()[2]).read().decode('utf-8')
        except urllib.error.HTTPError:
            await ctx.send("해당 유저가 없습니다.")
            return
        resjson=json.loads(res)
        embed=discord.Embed(title=resjson.get('handle'), url="https://solved.ac/profile/"+resjson.get('handle'), color=tiercolor[math.ceil(resjson.get('tier')/5)])
        if resjson.get('profileImageUrl')!=None:
            embed.set_thumbnail(url=resjson.get('profileImageUrl'))
        else:
            embed.set_thumbnail(url=levellist[resjson.get('tier')])
        embed.add_field(name="Ranking", value=resjson.get('rank'), inline=False)
        embed.add_field(name="AC Rating", value="{} ({})".format(resjson.get('rating'), tiername[resjson.get('tier')]), inline=False)
        userclass="{}".format(resjson.get('class'))
        if resjson.get('classDecoration')=="gold":
            userclass+="++"
        elif resjson.get('classDecoration')=="silver":
            userclass+="+"
        embed.add_field(name="Class", value=userclass, inline=False)
        await ctx.send(embed=embed)
@bot.command()
async def p(ctx, arg):
    try:
        res=req.urlopen(f'https://solved.ac/api/v3/problem/show?problemId='+arg).read().decode('utf-8')
    except urllib.error.HTTPError:
        await ctx.send("해당 번호의 문제가 없습니다.")
        return
    resjson=json.loads(res)
    embed=discord.Embed(title='boj {} : {}'.format(resjson.get('problemId'), resjson.get('titleKo')), url="https://acmicpc.net/problem/{}".format(int(arg)), color=tiercolor[math.ceil(resjson.get('level')/5)])
    embed.set_thumbnail(url=levellist[resjson.get('level')])
    embed.add_field(name="Average Try", value=resjson.get('averageTries'))
    embed.add_field(name="Solved", value=resjson.get('acceptedUserCount'))
    if len(resjson.get('tags'))!=0:
        tagstring=''
        for i in range(0, len(resjson.get('tags'))):
            taglist=resjson.get('tags')[i]
            enkolist=taglist.get('displayNames')
            tagstring+=enkolist[1].get('name')
            if i==len(resjson.get('tags'))-1:
                tagstring+="({})".format(enkolist[0].get('name'))
            else:
                tagstring+="({}), ".format(enkolist[0].get('name'))
        embed.add_field(name="Tag", value="||{}||".format(tagstring), inline=False)
    else:
        embed.add_field(name="Tag", value="None", inline=False)
    await ctx.send(embed=embed)
@bot.command()
async def search(ctx):
    queryarg=''
    mslist=ctx.message.content.split()
    for i in range(1, len(mslist)):
        queryarg+=mslist[i]
        if i!=len(mslist)-1:
            queryarg+=" "
    try:
        res=req.urlopen("http://solved.ac/api/v3/search/suggestion?query="+urllib.parse.quote(queryarg)).read().decode('utf-8')
    except urllib.error.HTTPError:
        await ctx.send("그런거 없습니다.")
        return
    resjson=json.loads(res)
    problemlist=resjson.get('problems')
    if len(problemlist)==0:
        await ctx.send("만족하는 문제가 없습니다.")
        return
    for problem in problemlist:
        prores=req.urlopen('https://solved.ac/api/v3/problem/show?problemId={}'.format(problem.get('id'))).read().decode('utf-8')
        projson=json.loads(prores)
        embed=discord.Embed(title='boj {} : {}'.format(projson.get('problemId'), projson.get('titleKo')), url="https://acmicpc.net/problem/{}".format(projson.get('problemId')), color=tiercolor[math.ceil(projson.get('level')/5)])
        embed.set_thumbnail(url=levellist[projson.get('level')])
        embed.add_field(name="Average Try", value=projson.get('averageTries'))
        embed.add_field(name="Solved", value=projson.get('acceptedUserCount'))
        if len(projson.get('tags'))!=0:
            tagstring=''
            for i in range(0, len(projson.get('tags'))):
                taglist=projson.get('tags')[i]
                enkolist=taglist.get('displayNames')
                tagstring+=enkolist[1].get('name')
                if i==len(projson.get('tags'))-1:
                    tagstring+="({})".format(enkolist[0].get('name'))
                else:
                    tagstring+="({}), ".format(enkolist[0].get('name'))
            embed.add_field(name="Tag", value="||{}||".format(tagstring), inline=False)
        else:
            embed.add_field(name="Tag", value="None", inline=False)
        await ctx.send(embed=embed)
@bot.command()
async def levels(ctx, arg):
    embed=discord.Embed(title='level : {}'.format(arg), color=0xffffff)
    embed.set_image(url=levellist[int(arg)])
    await ctx.send(embed=embed)
bot.run(token)