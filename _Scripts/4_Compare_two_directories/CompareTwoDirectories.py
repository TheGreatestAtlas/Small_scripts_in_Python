import os
import filecmp

# Ścieżki do folderów
folder1 = 'C:/Users/Test/Desktop/e2150_moon_project/compileTEX/__TEX'
folder2 = 'C:/Users/Test/Desktop/e2150_moon_project/decompileTEX/__TEX'

files1 = sorted([f for f in os.listdir(folder1) if os.path.isfile(os.path.join(folder1, f))])
files2 = sorted([f for f in os.listdir(folder2) if os.path.isfile(os.path.join(folder2, f))])

if files1 != files2:
    print("Pliki w folderach roznia sie nazwami lub liczba.")
else:
    for filename in files1:
        path1 = os.path.join(folder1, filename)
        path2 = os.path.join(folder2, filename)
        
        if filecmp.cmp(path1, path2, shallow=False):
            print(f"{filename} - OK")
        else:
            print(f"{filename} - ROZNI SIE!")
