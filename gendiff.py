import argparse


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('file1')
    parser.add_argument('file2')
    parser.parse_args()


if __name__ == '__main__':
    main()
