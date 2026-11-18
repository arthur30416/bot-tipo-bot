import random  # <--- 1. Adicionado aqui para o comando roll funcionar
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Estamos logados como {bot.user}')

@bot.command()
async def oi(ctx):
    await ctx.send(f'Olá! eu sou um bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)


@bot.group()
async def legal(ctx):
    """Says if a user is cool.

    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send(f'No, {ctx.subcommand_passed} is not cool')


@legal.command(name='eu')
async def _bot(ctx):
    await ctx.send('Sim vc,e legal.')

@legal.command(name='friza')
async def _bot(ctx):
    await ctx.send('nao friza,nao e legal.')


@bot.command()
async def repete(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)


@bot.command()
async def roll(ctx, dice: str):
    """Rola um dado no formato NdN (ex: 2d6)."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('O formato deve ser no padrão NdN! (Exemplo: 2d6)')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)


bot.run()
