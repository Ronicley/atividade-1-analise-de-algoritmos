import time
tempo_i = time.time()
arquivo = open('dataset-1-c.csv','r')
read = arquivo.read()
def acha(n, lista):
    i = 0
    for l in lista[2:10]:
        if (n == l):
            return "True\n" + str(i)
        i = i + 1
    return "False\n" +  str(-1)
lista = read.split("\n")
lista.remove('')
resp = acha(lista[0], lista)
tempo_f = time.time()
s = tempo_f - tempo_i
arq = open('resposta-dataset-1-c.txt','w')
arq.write(str(resp))
arq.write("\n"+str(s))

arq.close()
arquivo.close()


