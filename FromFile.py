import keyboard  # pip install keyboard
import os
import pyperclip # pip install pyperclip
import time 

while True:
    
    
    file_txt = [f for f in os.listdir() if f.endswith('.txt')]
    print("\n Wszystkie pliki  w folderze : ")


    for i, plik in enumerate(file_txt, start=1):
        print(f"  {i}. {plik}")
    
    numer = int(input("\nWybierz numer pliku: "))
    userinput = file_txt[numer - 1]  

   
    print("\nMożliwe separatory:")
    print("  , - przecinek")
    print("  ; - średnik")
    print("  | - pionowa kreska")
    print("  tab - tabulator")
    print("  enter - nowa linia")
    input_t = input("Wybierz separator: ")

    
    if input_t.lower() == 'tab':
        separator = '\t'
    elif input_t.lower() == 'enter':
        separator = '\n'
    else:
        separator = input_t

    
    
    with open(userinput, 'r') as f:
        strings = f.read().split(separator)
        
    print(strings) 

    print("\n Kliknij na 1 atrybut kolumny i kliknij f1 żeby zacząć wpisywać dane")
    keyboard.wait('f1')

    
    for string in strings:
        keyboard.press_and_release('f2')
        time.sleep(0.05)
        pyperclip.copy(string) 
        time.sleep(0.1)           
        keyboard.press_and_release('ctrl+v')
        time.sleep(0.05)
        keyboard.press_and_release('enter')
        time.sleep(0.05)

    print("Wszystkie dane z pliku wpisane w excelu")




    
    choice = input("\n Wciśnij n aby wypisac kolejny plik, q aby zakończyć: ").lower()
    if choice == 'q':
        break
