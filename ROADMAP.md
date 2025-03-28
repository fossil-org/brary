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

## planned:
- tax pay missed penalty (+)
- debt (+)
- tax priority levels (a wallet with tax priority (tp) 3 does not pay taxes with tp 2 and lower, but does pay 3 and higher. default level for wallets would be 0, and for taxes would be 1, wallet tp can be -1 for infinite tp (will not pay any taxes except -1 tp taxes)) (+)
- income (+)
- ways to earn money (+)
- board render can show current balance (+)
- item shops (+)
- economy script handler support (+)
- economy integrated in the `essentials` module (game) (+)
- advanced support in handbook
- expand handbook (+)
- bots (-)
- game loop commands (-)
- score (+)
- game loop output (-)