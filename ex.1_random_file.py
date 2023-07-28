# Лекція 10: Context Manager. Files

import random


def gen_number():
    return random.randint(1, 100)


def create_file():
    for char in range(ord('A'), ord('Z')+1):
        file_name = chr(char) + '.txt'
        with open(file_name, 'a') as file:
            random_number = gen_number()
            file.write(str(random_number) + '\n')


def sum_file():
    with open('summary.txt', 'w') as summary_file:
        for char in range(ord('A'), ord('Z') + 1):
            file_name = chr(char) + '.txt'
            with open(file_name, 'r') as file:
                random_number = file.read().strip()
                summary_file.write(f"{file_name}: {random_number}\n")


if __name__ == "__main__":
    create_file()
    sum_file()
