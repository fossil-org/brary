from brary.essentials import *
from brary.economy import *

currency = Currency("USD", "$", Color.green)
@ShopItemListing.from_function(300, Color.yellow)
def Sword_of_Life():
    """A sword that gives life!"""
    print("You have received 100 life!")
general_tax = TaxSystem("General 3-Roundly Tax", "standard tax system, takes place every 3 rounds", "max(5, x / 50)", Color.red, every_x_ticks=3)
wallet = Wallet(currency, 26000, taxes=[general_tax])
inventory = ItemInventory(wallet)
while True:
    Sword_of_Life.buy(inventory)
    print(inventory.items)
    inventory.get("Sword of Life").use()
    print("current balance:", wallet)
    input()