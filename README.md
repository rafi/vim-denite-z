# denite-z

Filter and browse [Z] (jump around) data file with this Denite source.

## Features

- Uses original python Z implementation
- Custom Denite sorter
- Manual command option

## Installation

Use your favorite plugin manager, mine is [dein.vim].

### Requirements

- Vim or Neovim
- [denite.nvim]
- Python 3.4 or later

## Usage

```viml
:Denite z[:filter:order]
```

- _**filter**_ can be any string to filter candidates
- _**order**_ must be one of: rank, recent, frecent

Usage examples:

- To list all entries: `:Denite z`
- Filter down results: `:Denite z:acme`
- To list all entries with rank order: `:Denite z::rank`

### Configuration

You can set the order option globally:

```viml
call denite#custom#var('z', 'order', 'frecent')
```

Sort candidates by Z ranking:

```viml
call denite#custom#source('z', 'sorters', ['sorter_z'])
```

Create a short-cut command: (Usage: `:Z foo`)

```viml
command! -nargs=+ -complete=command Z
  \ call denite#start([{'name': 'z', 'args': [<q-args>]}])
```

## Credits & Contribution

- [rupa/z] - wonderful utility
- [rupa/j2] - python version of z

This plugin is maintained by Rafael Bodill.

Pull requests are welcome.

[Z]: https://github.com/rupa/z
[rupa/z]: https://github.com/rupa/z
[rupa/j2]: https://github.com/rupa/j2
[denite.nvim]: https://github.com/Shougo/denite.nvim
[dein.vim]: https://github.com/Shougo/dein.vim
