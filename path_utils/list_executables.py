#!/usr/bin/env python3
"""
Author : Xinyuan Chen <45612704+tddschn@users.noreply.github.com>
Date   : 2023-03-18
Purpose: List all executables in $PATH
"""

import argparse

# from pathlib import Path
import os
from .utils import find_executables_in_path


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='List all executables in $PATH',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        '-p',
        '--path',
        help='Paths to search, defaults to $PATH',
        metavar='path',
        type=str,
    )

    parser.add_argument(
        '-C',
        '--commands-only',
        help='Only list command names instead of full paths',
        action='store_true',
    )

    parser.add_argument('-s', '--sort', help='Sort the output', action='store_true')

    parser.add_argument(
        '-d', '--dedup', help='Deduplicate the output', action='store_true'
    )

    return parser.parse_args()


def main():
    """Make a jazz noise here"""

    args = get_args()
    executables_full_paths = find_executables_in_path(args.path)
    if args.commands_only:
        executables_commands = [
            x.rsplit(os.sep, maxsplit=1)[-1] for x in executables_full_paths
        ]
        final_list = executables_commands
    else:
        final_list = executables_full_paths

    if args.dedup:
        final_list = list(set(final_list))

    if args.sort:
        final_list.sort()

    print('\n'.join(final_list))


if __name__ == '__main__':
    main()
