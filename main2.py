from brary.essentials import *
from brary.economy import *

sword = newItem("Wooden Sword")
plank = newItem("Wooden Plank")
game = Game(Board.setup())
game.board.create("Player")
game.newShop(Shop.setup("Normal Shop"), "u")
game.newInventory()
game.loop()