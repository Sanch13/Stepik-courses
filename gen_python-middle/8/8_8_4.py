"""
Используя генератор множеств, напишите программу, которая выбирает из списка files уникальные имена файлов c
расширением .png, независимо от регистра имен и расширений. Имена файлов выведите вместе с расширением, все на
 одной строке, в нижнем регистре, в алфавитном порядке через пробел.
Примечание. Считайте, что список files уже объявлен в вашей программе, и вы имеете к нему доступ.
"""

import pathlib

files = ['pygen_icon.png', 'Oppenheimer(2024).mkv', 'ideas.TxT', 'codes.txt', 'avatar.PNG']
# avatar.png pygen_icon.png

unique_files = {file.lower() for file in files if pathlib.Path(file.lower()).suffix == ".png"}
print(*sorted(unique_files))


