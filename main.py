from brary.essentials import *

board = Board.setup()
piston = board.new(Piston)
player = board.create("Player")
game: Game = board.new(Game)
while game.loop(lambda: False): ...