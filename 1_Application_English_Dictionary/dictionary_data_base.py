import mysql.connector
from myconfig import *

con = mysql.connector.connect(user = USER, password = PASSWORD, host = HOST,
        database = DATABASE)
cursor = con.cursor()

def get_all_words_in_dictionary():
    query = cursor.execute("SELECT Expression FROM Dictionary")
    word_list = cursor.fetchall()
    return [word[0] for word in word_list]

def get_possible_definitions(word):
    query = cursor.execute("SELECT Definition FROM Dictionary WHERE Expression = '%s'"
            % word)
    definition_list = cursor.fetchall()
    return [definition[0] for definition in definition_list]
