import argparse

from gendiff.scripts.generate_diff import generate_diff


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('file1')
    parser.add_argument('file2')
    parser.add_argument(
        '-f',
        '--format',
        default='stylish',
        help='set format of output',
    )

    args = parser.parse_args()
    print(generate_diff(args.file1, args.file2, args.format))


if __name__ == '__main__':
    main()
