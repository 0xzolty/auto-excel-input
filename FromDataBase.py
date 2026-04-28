import keyboard  # pip install keyboard
import os
import pyperclip # pip install pyperclip
import time 
import mysql.connector # pip install mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='test'
)
cursor1 = conn.cursor()
cursor2 = conn.cursor()




while True:
    
    input_rc =input("\nChcesz wpisać kolumny = k ,czy wiersze = w: ")
    if input_rc.lower() == 'k':
        cursor1.execute("SHOW COLUMNS FROM produkty")
        col1 = [str(row[0]).replace(" ", "") for row in cursor1.fetchall()]
        print(col1)
    elif input_rc.lower() == 'w':
        cursor2.execute(f"SELECT {colselect} FROM produkty ")
        row = [str(row[0]).replace(" ", "") for row in cursor2.fetchall()]
        print(row)
    
    
    print("\n Kliknij na 1 atrybut kolumny i kliknij f1 żeby zacząć wpisywać dane")
    keyboard.wait('f1')

    
    for string in strings:
       
        keyboard.press_and_release('f2')
        time.sleep(0.1)
        pyperclip.copy(string) 
        time.sleep(0.1)           
        keyboard.press_and_release('ctrl+v')
        time.sleep(0.1)
        keyboard.press_and_release(f'{rc}')
        time.sleep(0.1)

    print("Wszystkie dane z pliku wpisane w excelu")
    
    choice = input("\n Wciśnij n aby wypisac kolejny plik, q aby zakończyć: ").lower()
    if choice == 'q':
        
        conn.close()
        break
