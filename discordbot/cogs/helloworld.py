from discord.ext import commands


class HelloWorld(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='hello')
    async def hello(self, ctx: commands.Context):
        await ctx.send(f'Hello {ctx.author.name}!')

    @commands.command()  # you can delete name='' if command name is same with function name
    async def helloworld(self, ctx: commands.Context):
        await ctx.send(f'Hello World')


async def setup(bot: commands.Bot):
    await bot.add_cog(HelloWorld(bot))
