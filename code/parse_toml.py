import os
import tomllib
import argparse


def read_toml(path):
    with open(path,'rb') as f:
        return tomllib.load(f)


def search_nested_dict(d, key):
    ''' Seach value for specified key `key` in nested dictionary `d`
    '''
    match_items = []
    stack = [d]
    while stack:
        curr_dict = stack.pop()
        for k, v in curr_dict.items():
            if isinstance(v, dict):
                stack.append(v)
            if k == key:
                match_items.append(v)
    return match_items


def main():
    ''' Main function'''
    parser = argparse.ArgumentParser(
        description="Search for specified key elements in a toml file."
    )
    parser.add_argument(
        '-p', '--path', required=True, help="Path to the toml file."
    )
    parser.add_argument(
        '-k','--key', required=True, help="Key to search."
    )

    args = parser.parse_args()
    path = args.path
    key = args.key

    if not os.path.isfile(path):
        print(f'Error: \'{path}\' is not a valid file.')
        return

    try:
        toml_d = read_toml(path)
    except tomllib.TOMLDecodeError:
        print('Invalid tomal file.')
        return

    math_items = search_nested_dict(toml_d, key)

    if not math_items:
        print(f'No matching elements for the \'{key}\' key.')
        return

    for item in math_items:
        print(item)


if __name__ == '__main__':
    main()
