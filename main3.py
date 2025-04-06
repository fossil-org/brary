from brary.essentials import *
from brary.bots import *
from brary.space import *

game = Game(Board.setup())
game.board.create("Player")
game.board.create("Bot1")
bot = Bot.withService(simpleTracker("Player")).setup(
    game,
    "Bot1"
)
game.nto(bot)
game.loop()