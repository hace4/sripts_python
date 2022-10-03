import sqlite3
from unittest import result

class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()
    
    def add_user(self, user_id):
        with self.connection:
            self.cursor.execute("INSERT INTO `user` (`user_id`) VALUES (?)", (user_id,))
    def user_exist(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM `user` WHERE `user_id` = ?", (user_id,)).fetchall()
            return bool(len(result))
    def set_nickname(self, user_id, nickname):
        with self.connection:
            return self.cursor.execute("UPDATE `user` SET `nickname` = ? WHERE `user_id` = ?", (nickname, user_id,))
    def get_nick_name(self, user_id):
        result = self.cursor.execute("SELECT `nickname` FROM `user` WHERE `user_id` = ?", (user_id,)).fetchall()
        for row in result:
            nickname = str(row[0])
            return nickname