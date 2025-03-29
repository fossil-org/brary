import time

from typing import Callable, Any
from colorama import Style, Fore

from .essentials import ScriptHandler

# economy:

class Currency:
    def __init__(self, name: str, sign: str, color: "ColorObject") -> None:
        self.name: str = name
        self.sign: str = sign
        self.color: "ColorObject" = color
    @classmethod
    def setup(cls, name: str) -> "Currency":
        sh: ScriptHandler = ScriptHandler()
        currency: object = sh.create_class(name)
        return cls(name, currency.S, currency.C)
    def apply(self, number: float, *, name: bool = False, sign: bool = True, color: bool = True) -> str:
        return (self.color.apply if color else str)(f"{self.sign if sign else ''}{number}{' '+self.name if name else ''}")

class TaxSystem:
    def __init__(self, name: str, description: str, amount: str, color: "ColorObject", hidden: bool = False, every_x_ticks: int = 1, times_effective: int = -1):
        self.name: str = name
        self.description: str = description
        self.amount: str = f"round({amount})"
        self.color: "ColorObject" = color
        self.hidden: bool = hidden
        self.every_x_ticks: int = every_x_ticks
        self.times_effective: int = times_effective
    @classmethod
    def setup(cls, name: str) -> "TaxSystem":
        sh: ScriptHandler = ScriptHandler()
        tax_system: object = sh.create_class(name)
        return cls(name, tax_system.D, tax_system.A, tax_system.C, tax_system.H, tax_system.X, tax_system.F)

class OneTimePayment(TaxSystem):
    def __init__(self, listing: "ShopItemListing") -> None:
        super().__init__(f"purchased {listing.item.name}", listing.item.description, listing.price, listing.color, times_effective=1)

class Wallet:
    def __init__(self, currency: Currency, amount: float, taxes: list[TaxSystem] | None = None) -> None:
        self.currency: Currency = currency
        self.amount: float = amount
        self.taxes: list[list[TaxSystem, int, int]] = [] # [tax, tick, times_applied]
        if taxes:
            for tax in taxes:
                self.add_tax(tax)
    @classmethod
    def setup(cls, name: str) -> "Wallet":
        sh: ScriptHandler = ScriptHandler()
        wallet: object = sh.create_class(name)
        return cls(Currency.setup(wallet.V), wallet.A, [TaxSystem.setup(i) for i in wallet.T])
    def deposit(self, amount: float) -> None:
        self.amount += amount
    def withdraw(self, amount: float) -> bool:
        if amount <= self.amount:
            self.amount -= amount
            return True
        else:
            return False
    def round(self) -> None:
        self.amount = round(self.amount)
    def tick(self) -> None:
        remove: list[int] = []
        for i, (tax, tick, times_applied) in enumerate(self.taxes):
            if tax.times_effective == times_applied:
                remove.append(i)
                continue
            if tick == tax.every_x_ticks:
                self.tax(tax)
                self.taxes[i][1] = 1
                self.taxes[i][2] += 1
            else:
                self.taxes[i][1] += 1
        for i in remove:
            self.taxes.pop(i)
    def tax(self, tax: TaxSystem) -> None:
        x = self.amount
        amount = eval(tax.amount)
        if self.amount < amount:
            raise ValueError("insufficient funds")
        self.withdraw(amount)
        tick = 1
        if not tax.hidden:
            print(tax.color.apply(f"-{self.currency.apply(amount, color=False)}, ({tax.name}: {tax.description})"))
            time.sleep(1)
    def add_tax(self, tax: TaxSystem) -> None:
        self.taxes.append([tax, 1, 0])
    def __str__(self, **kwargs: Any) -> str:
        return self.currency.apply(self.amount, **kwargs)

# item:

class Item:
    def __init__(self, name: str, description: str, effect: Callable) -> None:
        self.name: str = name
        self.description: str = description
        self.effect: Callable = effect
    @classmethod
    def setup(cls, name: str) -> "Item":
        sh: ScriptHandler = ScriptHandler()
        item: object = sh.create_class(name)
        return cls(name, listing.D, listing.E)
    def use(self) -> None:
        self.effect()
class ItemInventory:
    def __init__(self, wallet: Wallet, items: list[Item] | None = None) -> None:
        self.wallet: Wallet = wallet
        self.items: list[Item] = items or []
    @classmethod
    def setup(cls) -> "ItemInventory":
        sh: ScriptHandler = ScriptHandler()
        player: object = sh.create_class("Player")
        return cls(Wallet.setup(player.W), [Item.setup(i) for i in player.I])
    def get(self, name: str, if_not_found: Callable | None = None) -> Item:
        for item in self.items:
            if item.name.lower().replace("_", " ") == name.lower().replace("_", " "):
                return item
        if if_not_found:
            return if_not_found
        raise ValueError(f"no item named '{name}' found in the inventory.")
    def add(self, item: Item) -> None:
        print(f"{Fore.MAGENTA}new item received: {item.name}{Style.RESET_ALL}")
        time.sleep(1)
        self.items.append(item)
    def remove(self, item: Item) -> None:
        for i, l_item in enumerate(self.items):
            if l_item.name == item.name:
                self.items.pop(i)
                return
class ShopItemListing:
    def __init__(self, item: Item, price: Wallet, color: "ColorObject") -> None:
        self.item: Item = item
        self.price: Wallet = price
        self.color: "ColorObject" = color
    @classmethod
    def create_item(cls, name: str, description: str, effect: Callable, price: float, color: "ColorObject") -> "ShopItemListing":
        return cls(Item(name, description, effect), price, color)
    @classmethod
    def from_function(cls, price: float, color: "ColorObject") -> Callable:
        def wrapper1(function: Callable) -> "ShopItemListing":
            return cls.create_item(function.__name__.replace("_", " "), function.__doc__, function, price, color)
        return wrapper1
    @classmethod
    def setup(cls, name: str) -> "ShopItemListing":
        sh: ScriptHandler = ScriptHandler()
        listing: object = sh.create_class(name)
        return cls.create_item(name, listing.D, listing.E, listing.P, listing.C)

    def __str__(self) -> str:
        return (f"{self.color.apply(self.item.name)}"
                f"- {'\n- '.join(self.item.description.split('\n'))}"
                f"- costs: {self.wallet}")
    def buy(self, inventory: ItemInventory, amount: int = 1) -> None:
        otp: OneTimePayment = OneTimePayment(self)
        inventory.wallet.add_tax(otp)
        try:
            inventory.wallet.tick()
        except ValueError:
            print(f"{Fore.RED}insufficient funds!{Style.RESET_ALL}")
            time.sleep(1)
            inventory.wallet.taxes.pop()
            return
        inventory.wallet.taxes.pop()
        inventory.add(self.item)