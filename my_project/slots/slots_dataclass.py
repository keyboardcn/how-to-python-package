from dataclasses import dataclass

@dataclass(slots=True)
class User:
    id : int
    first_name : str
    joined : str
    __dict__: dict = None  # Allow dynamic attributes

@dataclass(slots=True)
class AdminUser(User):
    admin_level : int = 5


if __name__ == "__main__":
    data = [1, "John", "2023-10-01", {}]
    user = User(*data)
    print(user.id)
    print(user.first_name)
    print(user.joined)
    user.last_name = "Doe"
    print(user.last_name)
    print(user.__dict__)
    print(user.__slots__)
    print(User.__slots__)

    print("---- Admin User ----")
    admin_data = [2, "Alice", "2022-05-15", {}, 5]
    admin_user = AdminUser(*admin_data)
    print(admin_user.__slots__)
    print(admin_user) 
    print(admin_user.__dict__)
