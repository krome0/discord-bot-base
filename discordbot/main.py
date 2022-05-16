import json
import asyncio
import discord
from discord.ext import commands


class DiscordBot(commands.Bot):
    def __init__(self):
        config = self.config
        self.token = config['token']
        self.prefix = config['prefix']
        self.presence = config['presence']
        self.cogs_to_load = config['cogs']
        self.description = config['description']

        activity = discord.Game(name=self.presence)
        super().__init__(command_prefix=self.prefix,
                         intents=self.allowed_intent,
                         activity=activity,
                         description=self.description)  # Due to PEP8 and pretty code

        asyncio.run(self.load_cogs())

    @property
    def config(self):
        with open('config.json', 'r', encoding='UTF-8') as json_file:
            config = json.load(json_file)

        return config

    @property  # used @property to make code pretty... It can be erased. But you should use self.allowed_intent()
    def allowed_intent(self) -> discord.Intents:
        intents = discord.Intents.none()       # every Intents are disabled
        # intents = discord.Intents.default()  # every Intents are enabled except presences, members, and message_content
        # intents = discord.Intents.all()      # every Intents are enabled

        intents.message_content = True  # you have to turn on at discord dev application site
        intents.guild_messages = True

        # you can add Intents when you need
        # you can find more intents on discord.py docs
        # https://discordpy.readthedocs.io/en/latest/api.html#discord.Intents

        return intents

    async def load_cogs(self) -> None:  # load cogs(collections of commands)
        for cog in self.cogs_to_load:
            try:
                await self.load_extension(cog)  # changed to Asynchronous at discord.py 2.0
                print(f'Loaded {cog}')
            except Exception as exception:  # when error occurred
                print(f'Error Loading {cog} | {exception}')


def main():
    bot = DiscordBot()
    bot.run(bot.token)


if __name__ == '__main__':
    main()
