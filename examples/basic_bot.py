import os

from disdata import Database, Config  # import database class
from dotenv import load_dotenv
from disnake.ext import commands

bot = commands.Bot(command_prefix="?")
bot.load_extension(
    "disnake-debug"
)  # this is not necessary, however the eval pairs nicely with the database
bot.db = Database(
    database_server=938485141616070696  # discord server to use for the database
)


@bot.event
async def on_ready():
    config = Config.from_dict(
        {
            "lock_database": True,  # defaults to False
            "force_lock": True,  # defaults to False
            "allowed_members": [],  # defaults to None
        }
    )

    # you can also do it like this:
    # config.lock_database = True # kicks any members that join the server
    # config.force_lock = True # [warning]: will kick all the members in the database_server
    # config.allowed_members = [298043305927639041] # wont kick these members

    # you can also just pass Config to keep defaults
    await bot.db.start(bot, config=config)  # config is a required argument


if __name__ == "__main__":
    load_dotenv()
    bot.run(os.environ["TOKEN"])
