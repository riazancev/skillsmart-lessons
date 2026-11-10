# Задание 2

## 2.1 Дизайн LinkedList

```
abstract class LinkedList<T>

    public const int HEAD_NIL = 0;
    public const int HEAD_OK = 1;
    public const int HEAD_ERR = 2; 

    public const int TAIL_NIL = 0;
    public const int TAIL_OK = 1;
    public const int TAIL_ERR = 2; 

    public const int RIGHT_NIL = 0;
    public const int RIGHT_OK = 1;
    public const int RIGHT_ERR = 2; 

    public const int PUT_RIGHT_NIL = 0;
    public const int PUT_RIGHT_OK = 1;
    public const int PUT_RIGHT_ERR = 2; 

    public const int PUT_LEFT_NIL = 0;
    public const int PUT_LEFT_OK = 1;
    public const int PUT_LEFT_ERR = 2; 

    public const int REMOVE_NIL = 0;
    public const int REMOVE_OK = 1;
    public const int REMOVE_ERR = 2; 

    public const int ADD_TO_EMPTY_NIL = 0;
    public const int ADD_TO_EMPTY_OK = 1;
    public const int ADD_TO_EMPTY_ERR = 2; 

    public const int REPLACE_NIL = 0;
    public const int REPLACE_OK = 1;
    public const int REPLACE_ERR = 2; 

    public const int FIND_NIL = 0;
    public const int FIND_OK = 1;
    public const int FIND_ERR = 2; 

    public const int GET_NIL = 0;
    public const int GET_OK = 1;
    public const int GET_ERR = 2; 


    // постусловие: создан пустой список, курсор не установлен
    public LinkedList<T> LinkedList();


    // команды

    // предусловие: список не пуст
    // постусловие: курсор установлен на первый узел
    public void head();

    // предусловие: список не пуст
    // постусловие: курсор установлен на последний узел
    public void tail();

    // предусловие: список не пуст и курсор не на последнем узле
    // постусловие: курсор сдвинут на один узел вправо
    public void right();

    // предусловие: список не пуст
    // постусловие: следом за текущим узлом вставлен узел с заданным значением;
    public void put_right(T value);

    // предусловие: список не пуст
    // постусловие: перед текущим узлом вставлен узел с заданным значением;
    public void put_left(T value);

    // предусловие: список не пуст
    // постусловие: текущий узел удалён;
    // курсор смещён к правому соседу, если он есть, иначе к левому соседу, если он есть, иначе список пуст и курсор не установлен
    public void remove();

    // постусловие: список пуст, курсор не установлен
    public void clear();

    // предусловие: список пуст
    // постусловие: в списке ровно один узел с заданным значением, курсор указывает на него
    public void add_to_empty(T value);

    // постусловие: новым хвостом стал узел с заданным значением;
    // если список был пуст, курсор указывает на этот узел, иначе курсор указывает на прежний хвост
    public void add_tail(T value);

    // предусловие: список не пуст
    // постусловие: значение текущего узла заменено на заданное
    public void replace(T value);

    // предусловие: список не пуст
    // постусловие: курсор указывает на ближайший узел справа с заданным значением
    public void find(T value);

    // постусловие: узлов с заданным значением в списке нет;
    // если текущий узел не удалён, курсор остаётся на нём;
    // если удалён, курсор переходит на ближайший справа оставшийся узел, иначе на ближайший слева оставшийся узел, иначе курсор не установлен
    public void remove_all(T value);


    // запросы

    // предусловие: список не пуст
    public T get();

    public int size();

    public bool is_head();
    public bool is_tail();
    public bool is_value();


    // статусы

    public int get_head_status();
    public int get_tail_status();
    public int get_right_status();
    public int get_put_right_status();
    public int get_put_left_status();
    public int get_remove_status();
    public int get_add_to_empty_status();
    public int get_replace_status();
    public int get_find_status();
    public int get_get_status();
```

## 2.2 Почему эффективная операция tail не сводима к другим

Операция tail может быть реализована с помощью head, right и is_tail, но ее сложность была бы O(n).  
Сложность отдельной операции tail O(1).

## 2.3 Почему не нужна операция поиска всех узлов

Операция поиска всех узлов с заданным значением возвращала бы набор узлов.  
В случае курсора нет самого понятия узла.

Пользователь с помощью курсора может сам найти все узлы по заданному критерию.
