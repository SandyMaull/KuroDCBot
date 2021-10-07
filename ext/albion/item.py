import discord
from discord.ext import commands
from ext.db_module import fetch
import json
import os

def checkdata():
    albion_db = fetch.one("config", 'name', 'ALBION')
    albion_data = json.loads(albion_db)
    if albion_data['value'] == 'TRUE':
        return True
    else:
        return False

def remove_containdata(data, lists):
    res = [ele for ele in lists if(ele in data)]
    res = ''.join(res)
    res = "{}".format(res)
    return res

class music(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def albion_item(self, ctx, *item):
        if checkdata():
            enchantment_list = ['#1', '#2', '#3']
            tier_list = ['T1', 'T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'T8']
            item = list(item)
            try:
                tier_res = remove_containdata(item, tier_list)
                item.remove(tier_res)
            except:
                await ctx.send("Please Declare the Tier!, i.e: `T4 Light Crossbow #2`")
                return
            try:
                enchan_res = remove_containdata(item, enchantment_list) 
                item.remove(enchan_res)
                print(tier_res)
                print(item)
                print(enchan_res)
            except:
                print(tier_res)
                print(item)

            embed = discord.Embed(
                title = 'This is Title',
                description = 'This is Descriptions',
                colour = discord.Colour.red()
            )
            embed.set_footer(text="This is Footer")
            embed.set_image(url='https://render.albiononline.com/v1/item/T4_MAIN_1HCROSSBOW@3')
            embed.set_thumbnail(url='https://render.albiononline.com/v1/item/T4_MAIN_1HCROSSBOW@3')
            embed.set_author(name="T4 Light Crossbow Enchantment 3",
            icon_url='https://render.albiononline.com/v1/item/T4_MAIN_1HCROSSBOW@3')
            embed.add_field(name="Field Name 1", value="Field Value 1", inline=False)
            embed.add_field(name="Field Name 2", value="Field Value 2", inline=True)
            embed.add_field(name="Field Name 3", value="Field Value 3", inline=True)
            await ctx.send(embed=embed)
        else:
            return

def setup(client):
    client.add_cog(music(client))