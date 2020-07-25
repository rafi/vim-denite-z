# denite-z neo/vim plugin

> Filter and browse [z] / [z.lua] / [zoxide] (jump around) data file with
> this [denite.nvim] plugin for Neovim or Vim.

## Features

- Detect and use [zoxide], or fallback to original [rupa/j2] implementation
- Custom Denite sorter
- Manual command option

## Installation

Use your favorite plugin manager, mine is [dein.vim].

### Requirements

- Python 3.4 or later
- Vim or Neovim
- [denite.nvim]
- **One** of z's variants:
    - [zoxide]
    - [z.lua]
    - [rupa/z]

## Usage

```viml
:Denite z[:query[:order]]
```

- **query** can be any string to filter candidates
- **order** must be one of: `rank`, `recent` (default), `frecent`
  _(Doesn't work when zoxide is used)_

Examples:

- To list all entries: `:Denite z`
- Query to filter results: `:Denite z:acme`
- To list all entries with the _rank_ order: `:Denite z::rank`

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
- [rupa/j2] - included python implementation of z

This plugin is maintained by Rafael Bodill.

Pull requests are welcome.

[z]: https://github.com/rupa/z
[rupa/z]: https://github.com/rupa/z
[zoxide]: https://github.com/ajeetdsouza/zoxide
[z.lua]: https://github.com/skywind3000/z.lua
[rupa/j2]: https://github.com/rupa/j2
[denite.nvim]: https://github.com/Shougo/denite.nvim
[dein.vim]: https://github.com/Shougo/dein.vim
