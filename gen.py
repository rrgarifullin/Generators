import hashlib


def user_input():
    path = input('Введите путь до файла: ')
    return path


def hash_string(path):
    with open(path, 'r', encoding='utf-8') as f:
        while True:
            string = f.readline()
            if '\n' in string:
                string = string.rstrip()
                hashing_string = hashlib.md5(string.encode())
                yield hashing_string
            else:
                break


def main():
    path = user_input()
    for string in hash_string(path):
        print(string.hexdigest())


if __name__ == '__main__':
    main()