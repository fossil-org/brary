# brary roadmap

## important:
- fossil heavily advises not to use EX versions for production.
- EX stands for experimental, which means bugs and unfinished features.
- use EX releases to test, check out what's coming in the next full release, or contribute to it.
- **you have been warned**

## info:
1. items marked with `(-)` are already present in FOSSIL's `py3kit` and will be/were ported and reworked to `brary`
2. items marked with `(+)` are completely new ideas not present in any other FOSSIL products.
3. items marked with `(/)` are present in `py3kit` but in a different way. a note will be present after this tag to explain the differences.
4. `MJ` means major update
5. `MN` means minor update
6. `PT` means tiny patch update
7. `EX` means experimental update
8. `PR` means public release (ready for production)
9. `NS` means not significant: not worth migrating versions in production just yet

## 1.0: MJ PR - first public release (11.3.2025)
- game loop (-)
- colors (+)
- scripts (/): in brary, everything is hosted in scripts rather than just blocks of code
- pistons (-)
- players (-)
- handbook (+)

## 1.1: MJ EX - experimental economy update part 1/? (28.3.2025)
- this release is **experimental** and **unfinished**
- `GamePlayerManager` is now `ScriptHandler` (-)
- new `brary.economy` module (beta) (+)
- (usable) items (+)
- item inventories (+)
- item shop listings (+)
- currencies (+)
- wallets (+)
- one-time payments (`otp`) (+)
- taxes (+)

## 1.2: MJ EX - experimental economy update part 2/? (29.3.2025)
- this release is **experimental** and **unfinished**
- economy script handler support (+)
- `.setup` initializers to every economy class (+)
- player inventory accessible with the `i` command in-game (+)
- - player inventory also shows balance
- - add a player inventory with `game.player.inventory = ItemInventory.setup()`
- - enable/disable viewing the inventory with `game.player.inventory_enabled` (disabled by default but enabled once you add an inventory)
- bug fixes

# 1.3: MJ EX - experimental economy update part 3/? (2.4.2025)
- this release is **experimental** and **unfinished**
- a lot of testing (-)
- `new_item()` function in `brary.economy` links to `ShopItemListing.setup()` (+)
- `(game.)new_inventory()` method in `brary.essentials:Game` links to `game.player.inventory = ItemInventory.setup()` (+) 
- item shops (+)
- tax priority levels
- - example: a wallet with tax priority (tp) 3 does not pay taxes with tp 2 and lower, but does pay 3 and higher.
- - default level would be 0, wallet tp can be -1 for infinite tp (will not pay any taxes except -1 tp taxes)) (+)
- `Sm@` values for board size (+)
- learn about board size in `HANDBOOK.md` (+)

## planned:
- `ECONOMY.md` file with a tutorial and help to create/configure the economy in your game
- tax pay missed penalty (+)
- debt (+)
- income (+)
- ways to earn money (+)
- economy integrated in the `essentials` module (game) (+)
- bots (-)
- game loop commands (-)
- score (+)
- game loop output (-)