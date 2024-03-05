class Node:
    def __init__(self, directory_name, file_name, specification, day, month, year, file_size):
        self.directory_name = directory_name
        self.file_name = file_name
        self.specification = specification
        self.day = day
        self.month = month
        self.year = year
        self.file_size = file_size

    def print_node(self):
        print(f'\nИмя каталога {self.directory_name}')
        print(f'Имя файла {self.file_name}')
        print(f'Спецификация {self.specification}')
        print(f'День создания {self.day}')
        print(f'Месяц создания {self.month}')
        print(f'Год создания {self.year}')
        print(f'Размер файла {self.file_size}')


class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity

    def _hash(self, key):
        return hash(key) % self.capacity

    def insert(self, directory_name, file_name, specification, day, month, year, file_size):
        key = directory_name + file_name
        index = self._hash(key) #формируется ключ key

        if self.table[index] is None: # если none то создается новый узел с переменными
            self.table[index] = Node(directory_name, file_name, specification, day, month, year, file_size)
            self.size += 1
        else:
            for i in range(self.capacity): # если есть узел, то квад. проб.
                index = (index + i * i) % self.capacity
                if self.table[index] is None:
                    self.table[index] = Node(directory_name, file_name, specification, day, month, year, file_size)
                    self.size += 1

    def search(self, directory_name, file_name):
        key = directory_name + file_name
        index = self._hash(key)

        if self.table[index].directory_name + self.table[index].file_name == key: #ычисляется хэш по ключу, кот. нужно проверить
            return index
        else: #если проверка не пройдена(нету), то квад. проб. и возвращает индекс этого узла по ключу
            for i in range(self.capacity):
                index = (index + i * i) % self.capacity
                if self.table[index].directory_name + self.table[index].file_name == key:
                    return index


    def remove(self, directory_name, file_name):
        self.table[self.search(directory_name, file_name)] = None
        self.size -= 1


    def __len__(self):
        return self.size

    def __contains__(self, directory_name, file_name):
        try:
            self.table[self.search(directory_name, file_name)]
            return True
        except AttributeError:
            return False

    def print_all(self):
        for i in range(self.capacity):
            if self.table[i]:
                self.table[i].print_node()


# Driver code
if __name__ == '__main__':
    ht = HashTable(10)
    choice = 0
    while choice != 5:
        print("\nВыберите: \n1) Добавить каталог и файл; \n2) Удалить каталог и файл; \n3) Печать; \n4) Проверить наличие каталога в таблице; \n5) Выйти.")
        choice = int(input())
        if choice == 1:
            directory_name = input("Введите имя каталога: ")
            file_name = input("Введите имя файла: ")
            specification = input("Введите спецификацию: ")
            day = int(input("Введите день создания: "))
            month = int(input("Введите месяц создания: "))
            year = int(input("Введите год создания: "))
            file_size = int(input("Введите размер файла: "))

            ht.insert(directory_name, file_name, specification, day, month, year, file_size)
        elif choice == 2:
            directory_name = input("Введите имя каталога: ")
            file_name = input("Введите имя файла: ")
            ht.remove(directory_name, file_name)
        elif choice == 3:
            print(f'\nКоличество объектов в хэш-таблице: {ht.__len__()}')
            print("\nХэш-таблица:")
            ht.print_all()
        elif choice == 4:
            directory_name = input("Введите имя каталога: ")
            file_name = input("Введите имя файла: ")
            if ht.__contains__(directory_name, file_name):
                print('\nТакой каталог есть в таблице.')
            else:
                print('\nТакого каталога нет в таблице.')
        elif choice == 5:
            break
        else:
            print("Ошибка.")
