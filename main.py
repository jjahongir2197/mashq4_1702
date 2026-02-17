class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Auth:
    def __init__(self):
        self.users = []

    def register(self, u, p):
        self.users.append(User(u, p))

    def login(self, u, p):
        for user in self.users:
            if user.username == u and user.password == p:
                print("Kirish OK")
                return True
        print("Login yoki parol xato")
        return False

def run():
    auth = Auth()

    while True:
        print("\n1. Ro‘yxat\n2. Login\n3. Chiqish")
        c = input("Tanlang: ")

        if c == "1":
            auth.register(input("User: "), input("Pass: "))
        elif c == "2":
            auth.login(input("User: "), input("Pass: "))
        else:
            break

run()
