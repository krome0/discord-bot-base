from discord.ext import commands
import discord


class EventHandler(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self) -> None:  # on bot is ready
        print(f'bot is ready!')

    @commands.Cog.listener()
    async def on_command_error(self, ctx: commands.Context, exception: discord.DiscordException) -> None:
        if isinstance(exception, commands.CommandNotFound):  # if there is no command -> pass
            pass

        elif isinstance(exception, commands.UserInputError):
            await ctx.send('Argument Error')

        else:
            await ctx.send('Unexpected Error')

        # you can add exception and handle errors
        # you can find more exception type in discord.py docs
        # https://discordpy.readthedocs.io/en/latest/ext/commands/api.html#exceptions


async def setup(bot: commands.Bot):
    await bot.add_cog(EventHandler(bot))
