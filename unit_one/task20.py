#todo: Выведите все строки данного файла в обратном порядке.
# Для этого считайте список всех строк при помощи метода readlines().

#Содержимое файла import_this.txt

fd = open('import_this.txt', 'r', encoding='utf-8')
lines = fd.readlines()

for line in reversed(lines):
    print(line.strip())

fd.close()