from discord import app_commands 
from random import randint
from colorama import Fore, Back

import discord
import os
import random
import time

os.system("cls")
os.system("title Birdy Bot - Attempting to Connect . . .")

Current_Time = time.strftime("%H:%M:%S", time.localtime())

Green = Back.GREEN

class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents = discord.Intents.all())
        self.synced = False 

    async def on_ready(self):
        await self.wait_until_ready()

        if not self.synced: 
            await tree.sync()
            self.synced = True

        os.system("cls")
        print(f"[{Green}Successfully logged in as{Back.RESET}]: {Fore.RESET}{self.user}")
        os.system("title Birdy Bot - Online")

client = aclient()
tree = app_commands.CommandTree(client)


@tree.command(name = "towers", description="🗼Towers gamemode for Bloxflip")
async def towers(interaction: discord.Interaction, height:int):
    start_time = time.time()
    grid = [["🟥","🟥","🟥"],["🟥","🟥","🟥"],["🟥","🟥","🟥"],["🟥","🟥","🟥"],["🟥","🟥","🟥"],["🟥","🟥","🟥"],["🟥","🟥","🟥"],["🟥","🟥","🟥"]]

    count = 0
    while count < height:
        a = randint(0,2)
        grid[count][a] = "🟩"
        count += 1

    chance = randint(45,95)
    if height < 4:
            chance = chance - 15

    em = discord.Embed(color=0x0025ff)

    em.add_field(name="🔎Birdy Bot Prediction", value="```"+grid[7][0]+grid[7][1]+grid[7][2]+"\n"+grid[6][0]+grid[6][1]+grid[6][2]+"\n"+grid[5][0]+grid[5][1]+grid[5][2]+"\n"+grid[4][0]+grid[4][1]+grid[4][2] +"\n"+ \
         grid[3][0]+grid[3][1]+grid[3][2] + "\n" + grid[2][0]+grid[2][1]+grid[2][2] + "\n" + grid[1][0]+grid[1][1]+grid[1][2] + "\n" + grid[0][0]+grid[0][1]+grid[0][2] + "```" \
            + f"**Accuracy**\n```{chance}%```")
        
    await interaction.response.send_message(embed=em)
    print(f"{Current_Time}[{Green}BirdyBot{Back.RESET}]: Executed command - Towers")



@tree.command(name = "mines", description="⛏Mines gamemode for Bloxflip")
async def mines(interaction: discord.Interaction, tiles: int):
    start_time = time.time()
    grid = ["🟥","🟥","🟥","🟥","🟥","🟥","🟥","🟥","🟥","🟥","🟥","🟥","🟥","🟥","🟥","🟥","🟥","🟥","🟥","🟥","🟥","🟥","🟥","🟥","🟥"]
    already_used = []

    count = 0
    while tiles > count:
        a = random.randint(0, 24)

        if a in already_used:
            continue

        already_used.append(a)
        grid[a] = "🟩"
        count += 1
        
    chance = random.randint(45,95)
    if tiles < 4:
        chance = chance - 15

    em = discord.Embed(color=0x0025ff)

    em.add_field(name="🔎Birdy Bot Prediction", value="\n" + "```"+grid[0]+grid[1]+grid[2]+grid[3]+grid[4]+"\n"+grid[5]+grid[6]+grid[7]+grid[8]+grid[9]+"\n"+grid[10]+grid[11]+grid[12]+grid[13]+grid[14]+"\n"+grid[15]+grid[16]+grid[17] \
        +grid[18]+grid[19]+"\n"+grid[20]+grid[21]+grid[22]+grid[23]+grid[24] + "```\n" + f"**Accuracy**\n```{chance}%```\n")

    em.set_footer(text="**Educated guess for Mines**")
    await interaction.response.send_message(embed=em)
    print(f"{Current_Time}[{Green}BirdyBot{Back.RESET}]: Executed command - Mines")






# **** DO NOT GO BELOW THIS POINT **** #






















client.run("OTk4MjYwNzM2MDc1NzYzNzkz.GHJhF1.4uLKzgXNK8vxc8FKNFRBLx9qXRLTJflERLVwvY")