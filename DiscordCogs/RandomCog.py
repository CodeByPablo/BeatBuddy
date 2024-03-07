from random import randint, random
from BeatBuddy.BeatBuddyBot import BeatBuddyBot
from discord.ext.commands import Cog, Context, command
from Config.Helper import Helper
from Config.Embeds import BEmbeds

helper = Helper()

class RandomCog(Cog):
    def __init__(self, bot: BeatBuddyBot):
        self.__embeds = BEmbeds()

    @command(name='random', help=helper.HELP_RANDOM, description=helper.HELP_RANDOM_LONG, aliases=['rand'])
    async def random(self, ctx: Context, arg: str) -> None:
        try:
            arg = int(arg)
        except:
            embed = self.__embeds.ERROR_NUMBER()
            await ctx.send(embed=embed)
            return None
        if arg < 1:
            a = arg
            b = 1
        else:
            a = 1
            b = arg
        x = randint(a, b)
        embed = self.__embeds.RANDOM_NUMBER(a, b, x)
        await ctx.send(embed=embed)

    @command(name='fac', help=helper.HELP_FAC, description=helper.HELP_FAC_LONG, aliases=['flip_a_coin'])
    async def fac(self, ctx: Context) -> None:
        x = random()
        if x < 0.5:
            result = 'heads'
        else:
            result = 'tails'

        embed = self.__embeds.FAC(result)
        await ctx.send(embed=embed)

    @command(name='choose', help=helper.HELP_CHOOSE, description=helper.HELP_CHOOSE_LONG, aliases=['pick'])
    async def choose(self, ctx, *args: str) -> None:
        try:
            user_input = " ".join(args)
            items = user_input.split(sep=',')

            index = randint(0, len(items)-1)

            embed = self.__embeds.CHOSEN_THING(items[index])
            await ctx.send(embed=embed)
        except:
            embed = self.__embeds.BAD_CHOOSE_USE()
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(RandomCog(bot))
