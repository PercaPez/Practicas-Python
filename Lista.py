# list= []
# amigos = ["Billy", "Bonnie", "Lucky"]
# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(type(list))
# list.append("pedro")
# list.append ("25")
# list.insert(0 , "pepito")
# list.reverse()
# # print(list[-2])
# print(list)
# list2 = [4, 8, 12, 21, 5, 6, 10, 9, 11]
# list3 = list1 + list2
# print(list3)
# list3.remove(21)
# print(list3)
# amigos.append("Lucy")
# amigos.append("Autoinvitada")
# print(amigos)
# amigos.insert(2 , "Mechas")
# print(amigos)
# amigos.pop(3) #El Pop recibe el indice del objeto que se desee quitar
# print(amigos)
# amigos.reverse()
# copia = amigos.copy()
# print(amigos)
# amigos.remove("Autoinvitada")
# print(copia)

#------ Sacar tajadas de las listas -------
lista = [1, 2.5, 'DevCode', [5, 6], 4]
print("Hicimos este cambio -->", lista[1 : 4])
print(lista[1 : 6 : 3])
print(lista[1 : 6 : 2])
print(lista[1 : 5])
lista.append("coquitos")
print(lista)
