# Разработай систему управления учетными записями пользователей для небольшой компании. Компания разделяет сотрудников на обычных
# работников и администраторов. У каждого сотрудника есть уникальный идентификатор (ID), имя и уровень доступа. Администраторы,
# помимо обычных данных пользователей, имеют дополнительный уровень доступа и могут добавлять или удалять пользователя из системы.
# Требования:
# 1.Класс `User*: Этот класс должен инкапсулировать данные о пользователе: ID, имя и уровень доступа ('user' для обычных сотрудников).
# 2.Класс `Admin`: Этот класс должен наследоваться от класса `User`. Добавь дополнительный атрибут уровня доступа, специфичный для администраторов
# ('admin'). Класс должен также содержать методы `add_user` и `remove_user`, которые позволяют добавлять и удалять пользователей из списка
# (представь, что это просто список экземпляров `User`).
# 3.Инкапсуляция данных: Убедись, что атрибуты классов защищены от прямого доступа и модификации снаружи. Предоставь доступ к необходимым атрибутам
# через методы (например, get и set методы).


class User():
    def __init__(self, id, name):
        self.__id = id
        self.__name = name
        self.__access_level = 'user'

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name

    def get_access_level(self):
        return self.__access_level

    def info(self):
        return f'ID: {self.__id}, Name: {self.__name}, Access level: {self.__access_level}'


class Admin(User):
    def __init__(self, id, name):
        super().__init__(id, name)
        self.access_level = 'admin'

    def add_user(self, user):
        list_users.append(user)

    def remove_user(self, user):
        list_users.remove(user)


def print_list(list):
    print('Список сотрудников:')
    for user in list:
        print(user.info())

# Создаём объёкты admin и user
admin = Admin(0, 'admin')
user1 = User(1, 'user1')
user2 = User(2, 'user2')
user3 = User(3, 'user3')

# Создаём пустой список
list_users = []

# Добавляем объекты User в список с помощью метода add_user
admin.add_user(user1)
admin.add_user(user2)
admin.add_user(user3)

# Выводим список на экран
print_list(list_users)

# Удаляем из списка объект user2 с помощью метода remove_user
admin.remove_user(user2)

# Выводим список на экран
print_list(list_users)

# Меняем имя user1 на user10
user1.set_name('user10')

# Выводим список на экран
print_list(list_users)

# Получаем ID пользователя user1
print(f'ID пользователя {user1.get_name()}: {user1.get_id()}')