#todo: Требуется создать csv-файл «algoritm.csv» со следующими столбцами:
#– id - номер по порядку (от 1 до 10);
#– текст из списка algoritm

algoritm = [ "C4.5" , "k - means" , "Метод опорных векторов" , "Apriori" ,
"EM" , "PageRank" , "AdaBoost", "kNN" , "Наивный байесовский классификатор" , "CART" ]

#Каждое значение из списка должно находится на отдельной строке.

FILE = 'algoritm.csv'

def create_file():
    fd = open(FILE, mode='wt')
    i = 0
    for id in range(1,11):
        i += 1
        fd.write('id_' + str(id) + ' - ' + algoritm[i-1] + '\n')
    fd.close()

create_file()