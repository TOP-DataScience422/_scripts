path1 = 'c:\\users\\username\\documents\\journal.log'
print(len(path1), path1)

path2 = r'd:\new_project\data\logs'
print(len(path2), path2, end='\n\n')


from pathlib import Path

# current working directory — текущий рабочий каталог
path3 = Path.cwd()
print(path3)

# D:\G-Doc\TOP Academy\Data Science\422\scripts\files > python paths.py
# D:\G-Doc\TOP Academy\Data Science\422\scripts\files

# D:\G-Doc\TOP Academy\Data Science\422 > python scripts\files\paths.py
# D:\G-Doc\TOP Academy\Data Science\422

path4 = Path(r'c:\windows')
print(path4)

from sys import path

path5 = Path(path[0])
print(path5)

# конструирование путей
path6 = path5 / 'data.txt'
path7 = path5 / 'log'
path8 = path7 / 'journal.log'
print(path6, path7, path8, sep='\n', end='\n\n')

# обращение к файловой системе
# >>> path5.exists()
# True
# >>> path5.is_file()
# False
# >>> path5.is_dir()
# True
# >>>
# >>> path6.exists()
# True
# >>> path6.is_file()
# True
# >>> path6.is_dir()
# False
# >>>
# >>> path7.exists()
# True
# >>> path7.is_file()
# True
# >>> path7.is_dir()
# False
# >>>
# >>> path8.exists()
# False
# >>> path8.is_file()
# False
# >>> path8.is_dir()
# False


# >>> path5.name
# 'files'
# >>> path6.name
# 'data.txt'
# >>> path7.name
# 'log'
# >>>
# >>> path5.suffix
# ''
# >>> path6.suffix
# '.txt'
# >>> path7.suffix
# ''
# >>>
# >>> path5.stem
# 'files'
# >>> path6.stem
# 'data'
# >>> path7.stem
# 'log'


# >>> path5
# WindowsPath('D:/G-Doc/TOP Academy/Data Science/422/scripts/files')
# >>>
# >>> path5.parent
# WindowsPath('D:/G-Doc/TOP Academy/Data Science/422/scripts')
# >>>
# >>> path6
# WindowsPath('D:/G-Doc/TOP Academy/Data Science/422/scripts/files/data.txt')
# >>>
# >>> path6.parent
# WindowsPath('D:/G-Doc/TOP Academy/Data Science/422/scripts/files')
# >>>
# >>> path5 == path6.parent
# True

# >>> print(*path6.parents, sep='\n')
# D:\G-Doc\TOP Academy\Data Science\422\scripts\files
# D:\G-Doc\TOP Academy\Data Science\422\scripts
# D:\G-Doc\TOP Academy\Data Science\422
# D:\G-Doc\TOP Academy\Data Science
# D:\G-Doc\TOP Academy
# D:\G-Doc
# D:\


# >>> for p in path5.iterdir():
# ...     print(p)
# ...
# D:\G-Doc\TOP Academy\Data Science\422\scripts\files\data.txt
# D:\G-Doc\TOP Academy\Data Science\422\scripts\files\log
# D:\G-Doc\TOP Academy\Data Science\422\scripts\files\paths.py

