# kt4.
class User:
    count = 0

    def __init__(self, name, login, password, grade):
        self._name = name
        self._login = login
        self._password = password
        self._grade = grade
        User.count += 1

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def login(self):
        return self._login

    @login.setter
    def login(self, value):
        print("Невозможно изменить логин!")

    @property
    def password(self):
        return "*" * 8

    @password.setter
    def password(self, value):
        self._password = value

    def show_info(self):
        print(f"Name: {self.name}, Login: {self.login}")

    def __getattr__(self, name):
        if name == 'grade':
            return "Неизвестное свойство grade"
        raise AttributeError(f"'{type(self).__name__}' object has no attribute '{name}'")

    def __setattr__(self, name, value):
        if name == 'grade':
            print("Неизвестное свойство grade")
        else:
            super().__setattr__(name, value)

    def __lt__(self, other):
        return self._grade < other._grade

    def __gt__(self, other):
        return self._grade > other._grade

    def __eq__(self, other):
        return self._grade == other._grade


class SuperUser(User):
    count = 0

    def __init__(self, name, login, password, role, grade):
        super().__init__(name, login, password, grade)
        self._role = role
        SuperUser.count += 1
        User.count -= 1

    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, value):
        self._role = value

    def show_info(self):
        print(f"Name: {self.name}, Login: {self.login}, Role: {self.role}")


if __name__ == "__main__":
    user1 = User('Paul McCartney', 'paul', '1234', 3)
    user2 = User('George Harrison', 'george', '5678', 2)
    user3 = User('Richard Starkey', 'ringo', '8523', 3)
    admin = SuperUser('John Lennon', 'john', '0000', 'admin', 5)

    user1.show_info()
    admin.show_info()
    print("-" * 30)

    print(f'Всего обычных пользователей: {User.count}')
    print(f'Всего супер-пользователей: {SuperUser.count}')
    print("-" * 30)

    print(f"user1 < user2: {user1 < user2}")
    print(f"admin > user3: {admin > user3}")
    print(f"user1 == user3: {user1 == user3}")
    print("-" * 30)

    user3.name = 'Ringo Starr'
    user1.password = 'Pa$$w0rd'
    
    print(f"Имя user3: {user3.name}")
    print(f"Пароль user2: {user2.password}")
    print(f"Логин user2: {user2.login}")

    user2.login = 'geo'
    print(user1.grade)
    admin.grade = 10
