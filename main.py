from brary.essentials import *
from brary.economy import *

sword = ShopItemListing.setup("Sword of Life")
exit_tool = ShopItemListing.setup("Exit Tool")
board = Board.setup()
piston = board.new(Piston)
player = board.create("Player")
game: Game = board.new(Game)
game.player.inventory = ItemInventory.setup()
sword.buy(game.player.inventory)
marketplace = Shop.setup("Marketplace").send(game)
special_shop = Shop.setup("Special Marketplace").send(game, "sm")
while game.loop(lambda: False): ...