import os
from pathlib import Path

basepath = Path('/home/eliasheinzen/aprendizado-maquina/python/images/krusty')
files_in_basepath = sorted(entry for entry in basepath.iterdir() if entry.is_file())
i = 1
for item in files_in_basepath:
    # print('krusty (' + str(i) + ').png')
    os.rename(item, '/home/eliasheinzen/aprendizado-maquina/python/images/krusty/krusty (' + str(i) + ').jpg')
    i = i + 1
    # print(a)