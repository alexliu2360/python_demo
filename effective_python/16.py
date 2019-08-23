# -*- coding: utf-8 -*-

res = []


def index_words_iter(text):
    if text:
        yield 0
    for index, letter in enumerate(text):
        if letter == ' ':
            yield index + 1


def index_file(handle):
    offset = 0
    for line in handle:
        if line:
            yield offset
        for letter in line:
            offset += 1
            if letter == '':
                yield offset


if __name__ == '__main__':
    # address = 'aa bb cc dd eee s'
    # res = list(index_words_iter(address))
    # print(res)
    #
    # with open('./data/address.txt', 'r') as f:
    #     it = index_file(f)
    #     # results = slice(it, 0, 3)
    #     # print(results)
    #     print(it)
    a = 1
    print('%r' %a)
