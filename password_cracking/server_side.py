import random
import string
import json
import time


class Server:
    def __init__(self):
        self.login: str = self.create_login()
        self.password: str = self.create_password()

    def create_login(self) -> str:
        """
            Generating login
            return: str    
        """
        with open("logins.txt", 'r', encoding='utf-8-sig') as file:
            lines = file.readlines()

        self.login = random.choice(lines).strip()
        return self.login

    def create_password(self) -> str:
        """
            Generating password
            return: str
        """
        password = ""
        length = random.randint(4, 10)
        for _ in range(length):
            password += random.choice(list(string.ascii_letters + string.digits))

        self.password = password
        return self.password

    def send_request(self, request_file: str) -> dict:
        """
            Getting and responding to requests from clients
            request_file: str - Commands from client side
            return: dict
        """
        time.sleep(0.01)

        request_data = json.loads(request_file)

        data_password = request_data["password"]
        data_login = request_data["login"]

        if data_login != self.login:
            return {"result": "Wrong login!"}
        if len(self.password) > len(data_password) and \
                self.password[:len(data_password)] == data_password and len(data_password) > 0:
            return {"result": "Exception happened during login"}
        if data_password != self.password:
            return {"result": "Wrong password!"}
        if data_login == self.login and data_password == self.password:
            return {"result": "Connection success!"}
        return {"result": "Bad request"}

    def get_login(self) -> str:
        """
            Getter of login
            return: str
        """
        return self.login

    def get_password(self) -> str:
        """
            Getter of password
            return: str
        """
        return self.password

