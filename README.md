# Excel Typer

Prosty program w Pythonie, który automatycznie wpisuje dane z pliku `.txt` do kolumny w Excelu (lub dowolnej innej aplikacji obsługującej wklejanie). Kopiuje wartości oddzielone przecinkami i wkleja je po kolei, schodząc w dół po kolumnie.

## Funkcje

- Skanuje folder w poszukiwaniu plików `.txt`
- Wyświetla listę dostępnych plików z numerami do wyboru
- Wczytuje wartości oddzielone przecinkami z wybranego pliku
- Czeka na sygnał użytkownika (klawisz F1) zanim zacznie wpisywać
- Wkleja wartości przez schowek systemowy (szybkie, niezawodne, działa z polskimi znakami)
- Po zakończeniu pyta czy uruchomić ponownie z innym plikiem

## Wymagania

- Python 3.6 lub nowszy
- System Windows (na Linux/Mac wymaga modyfikacji)
- Uprawnienia administratora (wymagane przez bibliotekę `keyboard`)

## Instalacja

Sklonuj repozytorium:

```bash
git clone https://github.com/twoj-username/excel-typer.git
cd excel-typer
```

Zainstaluj wymagane biblioteki:

```bash
pip install keyboard pyperclip
```

## Użycie

1. Przygotuj plik `.txt` z wartościami oddzielonymi przecinkami, np.:

   ```
   abc,def,ghi,jkl,mno
   ```

2. Umieść plik w tym samym folderze co skrypt.

3. Uruchom program **jako administrator**:

   ```bash
   python pyth.py
   ```

4. Wybierz numer pliku z listy.

5. Przełącz się do Excela i kliknij na komórkę, od której chcesz zacząć wpisywanie.

6. Wciśnij **F1** — program zacznie wklejać wartości po kolei, schodząc w dół po kolumnie.

7. Po zakończeniu wybierz `n` aby uruchomić ponownie z innym plikiem lub `q` aby zakończyć.

## Przykład działania

```
Wszystkie pliki w folderze:
  1. random_strings.txt
  2. produkty.txt
  3. dane.txt

Wybierz numer pliku: 2
['mleko', 'chleb', 'jajka', 'ser', 'masło']

Kliknij na 1 atrybut kolumny i kliknij F1 żeby zacząć wpisywać dane
[czeka na F1]
Wszystkie dane z pliku wpisane w excelu

Wciśnij N aby wypisać kolejny plik, Q aby zakończyć: q
```

## Kompilacja do .exe

Aby utworzyć samodzielny plik wykonywalny (bez konieczności posiadania zainstalowanego Pythona):

```bash
pip install pyinstaller
pyinstaller --onefile --uac-admin pyth.py
```

Gotowy plik `.exe` znajdziesz w folderze `dist/`. Flaga `--uac-admin` automatycznie żąda uprawnień administratora przy uruchomieniu.

## Jak to działa

Program używa dwóch bibliotek do automatyzacji:

- **`pyperclip`** — kopiuje aktualną wartość do schowka systemowego
- **`keyboard`** — symuluje skróty klawiaturowe (`Ctrl+V` żeby wkleić, `Enter` żeby zatwierdzić i przejść do następnej komórki)

Wklejanie przez schowek jest dużo szybsze niż wpisywanie znak po znaku i radzi sobie z polskimi znakami oraz znakami specjalnymi.

## Znane ograniczenia

- Wymaga uprawnień administratora (ograniczenie biblioteki `keyboard` na Windows)
- Działa tylko jeśli Excel (lub inna aplikacja) jest aktywnym oknem podczas wciśnięcia F1
- Nadpisuje zawartość schowka systemowego
- Wartości w pliku muszą być oddzielone przecinkami (bez spacji w samych wartościach)

## Możliwe rozszerzenia

- Wsparcie dla innych separatorów (średnik, tabulator, nowa linia)
- Pobieranie danych bezpośrednio z bazy MySQL/PostgreSQL/SQLite
- Wpisywanie do wiersza zamiast kolumny (Tab zamiast Enter)
- Interfejs graficzny (tkinter / PyQt)
- Wybór konkretnego zakresu wartości do wpisania

## Licencja

MIT — można używać i modyfikować dowolnie.

## Autor

Stworzone na własny użytek do automatyzacji wpisywania danych do Excela.
