import hashlib


def hash(path):
    l = hashlib.md5()
    print(f'l =  {l}')

    with open(path, encoding='utf-8') as file:
        while True:
            row = file.readline()
            if not row:
                break
            l.update(row.encode('utf-8'))
            yield l.hexdigest()

gen = hash('countries_links.txt')

if __name__ == '__main__':
    for item in gen:
        print(item)