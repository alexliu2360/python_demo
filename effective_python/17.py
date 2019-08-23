# -*- coding: utf-8 -*-
def normalize(numbers):
    if iter(numbers) is iter(numbers):
        raise TypeError('Must be a container')
    total = sum(numbers)
    return [value * 100 / total for value in numbers]


def read_visits(path):
    with open(path, 'r') as f:
        for line in f:
            yield int(line)


class ReadVisits:
    def __init__(self, path):
        self.path = path

    def __iter__(self):
        with open(self.path, 'r') as f:
            for line in f:
                yield int(line)


if __name__ == '__main__':
    visits = ReadVisits('./data/visits.txt')
    l = normalize(visits)
    print(visits)

    it = read_visits('./data/visits.txt')

