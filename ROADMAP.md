# brary roadmap

## important:
- fossil heavily advises not to use WIP versions for production.
  - WIP stands for unfinished release, which means bugs and unfinished features.
- use WIP releases to test, check out what's coming in the next full release, or contribute to it.
- **you have been warned**

## info:
1. items marked with `(-)` are already present in FOSSIL's `py3kit` and will be/were ported and reworked to `brary`
2. items marked with `(+)` are completely new ideas not present in any other FOSSIL products.
3. items marked with `(/)` are present in `py3kit` but in a different way. a note will be present after this tag to explain the differences.
4. `nfr` means not finalized release (not recommended for personal use or production)
5. `pbr` means public release (ready for production)
6. look for public releases [here](https://github.com/fossil-org/brary/releases)

## brary pbr1 (11.3.2025)
- game loop (-)
- colors (+)
- scripts (/): in brary, everything is hosted in scripts rather than just blocks of code
- pistons (-)
- players (-)
- handbook (+)

## brary nfr2 (28.3.2025)
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

## brary nfr3 (29.3.2025)
- this release is **experimental** and **unfinished**
- economy script handler support (+)
- `.setup` initializers to every economy class (+)
- player inventory accessible with the `i` command in-game (+)
- - player inventory also shows balance
- - add a player inventory with `game.player.inventory = ItemInventory.setup()`
- - enable/disable viewing the inventory with `game.player.inventory_enabled` (disabled by default but enabled once you add an inventory)
- bug fixes

# brary nfr4 (2.4.2025)
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

# brary pbr5 (2.4.2025)
- bug fixes (-)
- more testing (-)
- ansi colors with `Color.ansi<codes>m` (+)
- `Color.brown` (+)
- - more colors will be added in the future (+)

# brary pbr6 (2.4.2025)
- fixed ansi colors (+)
- added sign and color to item listings (+)
- other bug fixes (-)

# brary pbr7 (6.4.2025)
- bots (-)
- future planning (+)
- quality of life (+)
- improved collisions (+)
- fixed most internal errors (+)

## planned:
- tax pay missed penalty (+)
- debt (+)
- income (+)
- ways to earn money (+)
- game loop commands (-)
- game loop output (-)
- hp (+)
- stamina (+)
- moves (+)
- fights (+)
- weapons (+)
- pve battles (+)
- status effects (+)
- leveling (+)
- xp (+)
- skill points (+)
- skill tree (+)
- randomly generated shops (+)
- missions (+)
- dungeons (+)
- different move sets (+)
- pvp (+)