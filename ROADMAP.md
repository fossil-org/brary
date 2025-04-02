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
4. mfv means multiple-flow versioning
5. `MJ` means major update
6. `MN` means minor update
7. `PT` means tiny patch update
8. `EX` means experimental update
9. `PR` means public release (ready for production)
10. `NS` means not significant: not worth migrating versions in production just yet

## current mfv flows: `economy.bots`

## MJ PR 1 - first public release (11.3.2025)
- game loop (-)
- colors (+)
- scripts (/): in brary, everything is hosted in scripts rather than just blocks of code
- pistons (-)
- players (-)
- handbook (+)

## MJ EX 1.1 - experimental economy update part 1/4 (28.3.2025)
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

## MJ EX 1.2 - experimental economy update part 2/4 (29.3.2025)
- this release is **experimental** and **unfinished**
- economy script handler support (+)
- `.setup` initializers to every economy class (+)
- player inventory accessible with the `i` command in-game (+)
- - player inventory also shows balance
- - add a player inventory with `game.player.inventory = ItemInventory.setup()`
- - enable/disable viewing the inventory with `game.player.inventory_enabled` (disabled by default but enabled once you add an inventory)
- bug fixes

# MJ EX 1.3 - experimental economy update part 3/4 (2.4.2025)
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

# MJ PR 2 - public release 2: the economy update (aka: experimental economy update part 4/4) (2.4.2025)
- `MJ EX 1.1`
- `MJ EX 1.2`
- `MJ EX 1.3`
- bug fixes
- more testing
- ansi colors with `Color.ansi<codes>m` and `Color.brown`

# MN PR 2.1 - public release 2.1
- fixed ansi colors
- added sign and color to item listings
- other bug fixes

## planned:
- tax pay missed penalty (+)
- debt (+)
- income (+)
- ways to earn money (+)
- bots [coming next update!] (-)
- game loop commands (-)
- score (+)
- game loop output (-)