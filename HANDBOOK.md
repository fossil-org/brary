# brary handbook

## script shorthands:
### space shorthands:
- `X` - x location on the board
- `Y` - y location on the board
- `T` - space texture
- `C` - space color
### board shorthands:
- `W` - board max x position (width)
- `H` - board max y position (height)
- `T` - background texture
- `C` - background color
### player shorthands:
- `S` - player speed
- `W` - wallet
- `I` - inventory
### economy shorthands:
- `N` - name
- `D` - item description
- `E` or `def E(_, game):` - item effect
- `P` - listing price
- `C` - color
- `S` - sign (symbol before a value, e.g. $, £, etc.)
- `A` - amount
- `H` - hidden
- `X` - every x ticks
- `F` - times effective
- `T` - taxes
- `V` - currency
- `I` - items
### bot shorthands:
- `F` - from (location)
- `P` - point/to (location)
- `S` - speed
- `T` - texture
- `C` - color

## board size

### how to use `Sm@`
- board size can be set manually or with a single `Sm@` value
- `Sm@` is a custom measurement created for brary to create square boards
- to use an `Sm@` value, use the `Sm@` prefix in your script: `W, H = Sm@<value>`
- - replace `<value>` with an integer or float
- - **important!** always define `W` first, then `H` like this: `W, H = ...` when using `Sm@`
- - example: `Sm@12 = (12, 6)`, `Sm@14.5 = (15, 7)`
- - we recommend using `Sm@` to create nice square boards.


### suggested board size
- brary developers suggest these board sizes for the purposes:
- - for general use: `Sm@16` (`w18h9`)
- - for larger boards: `Sm@32` (`w32h16`)
- - for smaller boards (e.g. dungeon levels): `Sm@12` (`w8h4`)
- it is generally not recommended to make board size over `Sm@64`