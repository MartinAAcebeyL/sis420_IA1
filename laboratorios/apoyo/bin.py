
esdato =[0,0,0,0]
number = 12
def invento(estado, number):
    dic={1:0, 2:1, 4:2, 8:3}
    dic1 = {}
    for key in dic.keys():
        a = number - key
        dic1[a]=key
    minimo = min(dic1.keys())
    valor = dic1[minimo]
    indice =dic[valor] 
    print("{} {}".format(indice,valor))
    return indice,valor

indice,valor=invento(esdato, number)
esdato[indice]=1
print(esdato)




        

    