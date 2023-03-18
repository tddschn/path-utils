# $PATH Utilities

Created for personal use.


- [$PATH Utilities](#path-utilities)
  - [Available commands](#available-commands)
    - [`list-executables`](#list-executables)
  - [Installation](#installation)
    - [pipx](#pipx)
    - [pip](#pip)
  - [Develop](#develop)

## Available commands

### `list-executables`

```
$ list-executables --help

usage: list-executables [-h] [-p path] [-C] [-s] [-d]

List all executables in $PATH

options:
  -h, --help            show this help message and exit
  -p path, --path path  Paths to search, defaults to $PATH (default: None)
  -C, --commands-only   Only list command names instead of full paths (default: False)
  -s, --sort            Sort the output (default: False)
  -d, --dedup           Deduplicate the output (default: False)
```

## Installation

I am not able to upload this package under the name `path-utils` to PyPI, probably because it's too similar to an existing package `path-util` on PyPI.

Please install from `git+https://github.com/tddschn/path-utils.git` until this issues is resolved.

### pipx

This is the recommended installation method.

```bash
# pipx install path-utils
pipx install git+https://github.com/tddschn/path-utils.git
```

### [pip](https://pypi.org/project/path-utils/)

```bash
# pip install path-utils
pip install git+https://github.com/tddschn/path-utils.git
```

## Develop

```
$ git clone https://github.com/tddschn/path-utils.git
$ cd path-utils
$ poetry install
```