# login_page.py
#
# Log in window for Account.py
#
# Yeonjae Kim  /  Minsu Song
#
from constant import *
import json
class Model:
    def __init__(self):
        pass

    def read_userinfo(self):
        with open(USER_INFO_FILE, 'r') as file:
            user_dict = json.loads(file.read())

        print(user_dict)

    def read_log(self):
        pass

    def read_userpassword(self):
        pass