import base64
import time
import sqlite3
from sqlite3 import Error
import os


def quit():
    while True:
        print(" \n Type ""w"" for yes or ""q"" for no")
        question = input(" \n Would you like to quit the program? ")
        if question == "w":
            r_num()
        if question == "q":
            exit()


def r_num():
    while True:
        prompt = input(" \n Enter a record number between 1 and 24:  ")
        try:
            check = int(prompt)
        except ValueError:
            print(" \n Please only enter a number.".format(prompt))
            continue
        print("\n", "You have chosen record {}".format(check))
        time.sleep(1)
        quit()


r_num()


def Main():
    con = None
    try:
        path = os.chdir('C:/Users/Mohamed/Downloads')
        print(os.getcwd())
        con = sqlite3.connect("week5.db")
        cur = con.cursor()
        cur.execute('SELECT SQLITE_VERSION()')
        data = cur.fetchone()
        print(data)
    except Error as e:
        print(e)
    return con


def select_all_tasks(con):
    cur = con.cursor()

    cur.execute("SELECT Link FROM week5")

    rows = (cur.fetchall())

    for row in rows:
        print(row)


def decode():
    cur = con.cursor()
    for row in cur.execute("SELECT Link FROM week5"):
        print(base64.b64decode(ascii(row)))


import webbrowser


def browser():
    cur = con.cursor()

    cur.execute("SELECT Link FROM week5")

    rows = cur.fetchall()
    webbrowser.open_new_tab(str(rows))


if __name__ == '__main__':
    con = Main()
    select_all_tasks(con)
    decode()
    browser()
