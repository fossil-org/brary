from brary.essentials import *
from brary.economy import *

sword = ShopItemListing.setup("Sword of Life")
board = Board.setup()
piston = board.new(Piston)
player = board.create("Player")
game: Game = board.new(Game)
game.player.inventory = ItemInventory.setup()
sword.buy(game.player.inventory)
while game.loop(lambda: False): ...