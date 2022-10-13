
// Хеш-таблица с открытой адресацией (открытое хеширование)
// Это реализация хеш-таблицы с открытой адресацией, которая использует линейное пробирование 
// для разрешения коллизий. Линейное пробирование - это метод, при котором при возникновении
// коллизии, мы просто переходим к следующему элементу в массиве и проверяем его наличие.
// Открытая адресация - это метод, при котором мы храним элементы в массиве, а не в списке.

#include <iostream>

using namespace std;

// Класс хеш-таблицы
class HashTable
{
private:
    // Массив для хранения элементов
    int *array;

    // Максимальный размер хеш-таблицы
    int capacity;

    // Текущий размер хеш-таблицы
    int size;

    // Вспомогательная функция, которая возвращает хеш-код для заданного ключа
    int hash(int key)
    {
        return key % capacity;
    }

public:
    // Конструктор
    HashTable(int capacity)
    {
        // Инициализируем размер хеш-таблицы
        this->capacity = capacity;
        size = 0;

        // Выделяем память для массива
        array = new int[capacity];

        // Инициализируем все элементы массива как -1
        for (int i = 0; i < capacity; i++)
            array[i] = -1;
    }

    // Деструктор
    ~HashTable()
    {
        delete[] array;
    }

    // Функция для добавления элемента в хеш-таблицу
    void insert(int key)
    {
        // Если размер хеш-таблицы больше или равен ее ёмкости, то она заполнена
        if (size >= capacity)
            return;

        // Получаем хеш-код для ключа
        int hashIndex = hash(key);

        // Пока ячейка занята, мы будем искать другую позицию с помощью линейного пробирования
        while (array[hashIndex] != -1 && array[hashIndex] != -2 && array[hashIndex] != key)
        {
            hashIndex++;
            hashIndex %= capacity;
        }

        // Если ячейка свободна, то вставляем ключ
        if (array[hashIndex] == -1 || array[hashIndex] == -2)
            size++;
        array[hashIndex] = key;
    }

    // Функция для удаления элемента из хеш-таблицы
    void remove(int key)
    {
        // Получаем хеш-код для ключа
        int hashIndex = hash(key);

        // Пока ячейка занята, мы будем искать другую позицию с помощью линейного пробирования
        while (array[hashIndex] != -1)
        {
            // Если элемент найден, то удаляем его
            if (array[hashIndex] == key)
            {
                array[hashIndex] = -2;
                size--;
                return;
            }
            hashIndex++;
            hashIndex %= capacity;
        }
    }

    // Функция для поиска элемента в хеш-таблице
    bool search(int key)
    {
        // Получаем хеш-код для ключа
        int hashIndex = hash(key);

        // Пока ячейка занята, мы будем искать другую позицию с помощью линейного пробирования
        while (array[hashIndex] != -1)
        {
            // Если элемент найден, то возвращаем true
            if (array[hashIndex] == key)
                return true;
            hashIndex++;
            hashIndex %= capacity;
        }

        // Если элемент не найден, то возвращаем false
        return false;
    }

    // Функция для отображения хеш-таблицы
    void display()
    {
        for (int i = 0; i < capacity; i++)
        {
            if (array[i] != -1 && array[i] != -2)
                cout << i << " --> " << array[i] << endl;
        }
    }
};

int main()
{
    // Создаем хеш-таблицу с размером 7
    HashTable hashTable(7);

    // Вставляем ключи в хеш-таблицу
    hashTable.insert(49);
    hashTable.insert(56);
    hashTable.insert(72);

    // Отображаем хеш-таблицу
    hashTable.display();

    // Удаляем элемент из хеш-таблицы
    hashTable.remove(56);

    // Отображаем хеш-таблицу
    hashTable.display();

    // Ищем элемент в хеш-таблице
    if (hashTable.search(56) == true)
        cout << "Элемент найден" << endl;
    else
        cout << "Элемент не найден" << endl;

    return 0;
}
