import discord
from discord.ext import commands

class testCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @discord.app_commands.command(name='hello', description='say hello')
    async def hello(self, interaction: discord.Interaction):
        await interaction.response.send_message(f'Hi, {interaction.user.mention}!')

async def setup(bot):
    await bot.add_cog(testCog(bot))
