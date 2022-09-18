#!/usr/bin/env python3


def main():
    with open('output.txt', 'w') as output_file:
        with open('input.txt', 'r') as input_file:
            for i, line in enumerate(input_file, 1):
                output_file.write(f'{i}) {line}')


if __name__ == '__main__':
    main()
