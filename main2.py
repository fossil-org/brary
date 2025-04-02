from brary.essentials import *
from brary.economy import *

sword = new_item("Wooden Sword")
plank = new_item("Wooden Plank")
game = Game(Board.setup())
game.board.create("Player")
game.new_inventory()
game.loop()