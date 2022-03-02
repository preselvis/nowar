# Для нетехнічних котиків і киць
Інструкція як шкварити сайти хуйловської пропаганди:
1. Встановіть Python3 за цим посиланням:
    https://www.python.org/downloads/
2. Встановіть і увімкніть VPN
3. Запустіть термінал:
    http://xn--j1a5b.dp.ua/yak-vidkriti-komandnij-ryadok-v-windows-10/
4. Перейдіть у папку з проєктом за допомогою команди cd повний_путь та запустіть наступну команду
    pip3 install -r requirements.txt
5. Відкрийте builds/windows/app.exe та натісніть кнопку Start
6. Це не зупинити!!!

Слава Україні! Смерть ворогам!


# Run from CLI/sources
Python 3.10

```
git clone https://github.com/nanabanano/runner.git
cd runner
pip3 install pyinstaller
pip3 install -r requirements.txt

# mac
pyinstaller app.py --collect-all dns --add-data="headers.txt:." --add-data="DRipper.py:." --onefile

# win
pyinstaller --collect-all dns --add-data "headers.txt;." --add-data "DRipper.py;." --onefile app.py

# cli
python3 app.py
```

- [or]

```
chmod +x app.py
./app.py
```

see dist folder
