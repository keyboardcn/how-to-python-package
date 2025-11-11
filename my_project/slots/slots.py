from dataclasses import dataclass

class User:
    __slots__ = ['id', 'first_name', 'joined', '__dict__']
    def __init__(self, id: int, first_name: str, joined: str):
        self.id = id
        self.first_name = first_name
        self.joined = joined

    def __repr__(self):
        return f"User(id={self.id}, first_name={self.first_name}, joined={self.joined})"

class AdminUser(User):
    __slots__ = ['admin_level']
    def __init__(self, id: int, first_name: str, joined: str, admin_level: int):
        super().__init__(id, first_name, joined)
        self.admin_level = admin_level

    def __repr__(self):
        return f"AdminUser(id={self.id}, first_name={self.first_name}, joined={self.joined}, admin_level={self.admin_level})"

if __name__ == "__main__":
    data = [1, "John", "2023-10-01"]
    user = User(*data)
    print(user.id)
    print(user.first_name)
    print(user.joined)
    user.last_name = "Doe"
    print(user.last_name)
    print(user.__dict__)
    print(user.__slots__)
    print(User.__slots__)
    print('*', User.__dict__)

    print("---- Admin User ----")
    admin_data = [2, "Alice", "2022-05-15", 5]
    admin_user = AdminUser(*admin_data)
    print(admin_user.__slots__)
    print(admin_user) 
    print(AdminUser.__dict__)   
