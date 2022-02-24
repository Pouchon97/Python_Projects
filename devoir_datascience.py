from math import sqrt


data = [2,4,6,8,10,12,14]

def variance(data):
   moy = sum(data) /len(data)
   variance = 0
   for y in data:
      variance = variance + (y - moy)**2
      variance_result =(variance/len(data))
   return variance_result

def ecartype(data):
   resultat_ecart = sqrt(variance(data))
   return resultat_ecart

def some(data):
   somme = 0
   for x in data: 
      somme = (somme+x)
   return somme

def moyenne(data):
    resultat_moyenne = some(data) / len(data)
    return resultat_moyenne
 
 # Lresultat de la some est
print("La somme est : ", some(data))
 
 #La moyenne est 
print("La Moyenne est : ", moyenne(data))

#La variance est 
print("La variance est : ", variance(data))

#L'ecartype est 
print("L'ecaert est : ",ecartype(data))
 