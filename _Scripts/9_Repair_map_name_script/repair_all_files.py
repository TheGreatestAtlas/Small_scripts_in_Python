import os

katalog = "."  

for nazwa in os.listdir(katalog):
    sciezka_stara = os.path.join(katalog, nazwa)

    if os.path.isfile(sciezka_stara):
        
        baza, ext = os.path.splitext(nazwa)

        nowa_baza = baza.replace(".", "_").replace(",", "_").replace("!","")

        nowa_nazwa = nowa_baza + ext
        sciezka_nowa = os.path.join(katalog, nowa_nazwa)

        if sciezka_nowa != sciezka_stara:
            print(f"Renaming: {nazwa} -> {nowa_nazwa}")
            os.rename(sciezka_stara, sciezka_nowa)
