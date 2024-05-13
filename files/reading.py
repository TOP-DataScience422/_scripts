from pathlib import Path
from sys import path


script_dir = Path(path[0])
data_path = script_dir / 'data.txt'
log_path = script_dir / 'log'


# >>> filein = open(data_path)
# >>>
# >>> type(filein)
# <class '_io.TextIOWrapper'>
# >>>
# >>> filein
# <_io.TextIOWrapper name='...\\files\\data.txt' mode='r' encoding='cp1251'>
# >>>
# >>>
# >>> filein.readline()
# 'РїРµСЂРІР°СЏ СЃС‚СЂРѕС‡РєР°\n'
# >>>
# >>> filein.read()
# 'РІС‚РѕСЂР°СЏ СЃС‚СЂРѕС‡РєР°\nС‚СЂРµС‚СЊСЏ СЃС‚СЂРѕС‡РєР°\n'
# >>>
# >>>
# >>> filein = open(data_path, encoding='utf-8')
# >>>
# >>> filein.readline()
# 'первая строчка\n'
# >>>
# >>> filein.read()
# 'вторая строчка\nтретья строчка\n'
# >>>
# >>> filein.close()


# >>> filein = open(r'c:\git\license.txt')
# >>>
# >>> lines = filein.readlines()
# >>> type(lines)
# <class 'list'>
# >>> len(lines)
# 360
# >>>
# >>> lines[0]
# '\n'
# >>> lines[-1]
# 'Public License instead of this License.\n'
# >>>
# >>> filein.close()


if __name__ == '__main__':
    
    with open(log_path, encoding='utf-8') as filein:
        dates = filein.readlines()
    
    print(dates)
    
    from datetime import datetime as dt
    
    dates = [
        dt.strptime(line.rstrip(), '%Y/%m/%d - %H:%M:%S')
        for line in dates
    ]
    print(dates)


# >>> data_path
# WindowsPath('D:/G-Doc/TOP Academy/Data Science/422/scripts/files/data.txt')
# >>>
# >>> data_path.read_text()
# 'РїРµСЂРІР°СЏ СЃС‚СЂРѕС‡РєР°\nРІС‚РѕСЂР°СЏ СЃС‚СЂРѕС‡РєР°\nС‚СЂРµС‚СЊСЏ СЃС‚СЂРѕС‡РєР°\n'
# >>>
# >>> data_path.read_text(encoding='utf-8')
# 'первая строчка\nвторая строчка\nтретья строчка\n'

