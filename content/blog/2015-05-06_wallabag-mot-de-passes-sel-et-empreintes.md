Title: Wallabag, mot de passes, sel et empreintes
Date: 2015-05-06 19:53
Author: Benjamin Bouvier
Tags: opensource
Lang: fr
Slug: wallabag-changer-mot-de-passe-perdu

Changer son mot de passe Wallabag, TL:DR; {#changersonmotdepassewallabagtldr}
=========================================

    $ cd /var/www/wallabag
    $ printf "motdepasseLogin"`cat inc/poche/config.inc.php | grep "SALT" | cut -d \' -f 4` | openssl sha1
    > c87c3d3f823c166602a0ddfc2d96c82aa7b27d9e
    $ sqlite3 db/poche.sqlite
    sqlite> update users set password="c87c3d3f823c166602a0ddfc2d96c82aa7b27d9e" where id=1;
    sqlite> ^D

Comment changer son mot de passe Wallabag, à la dure {#commentchangersonmotdepassewallabagladure}
====================================================

##### aka, comment perdre son mot de passe Wallabag en premier lieu {#akacommentperdresonmotdepassewallabagenpremierlieu}

![Wallabag, mot de passes, sel et
empreintes]({filename}/images/kangourou.jpeg)

J'utilise [Wallabag](http://wallabag.org/), un service de liste de
lecture libre et décentralisé, donc un concurrent de
[Pocket](https://getpocket.com/) et [autres
alternatives](http://alternativeto.net/software/read-it-later/), que je
recommande particulièrement pour son efficacité et sa simplicité. En
particulier, j'utilise une [image
Docker](https://registry.hub.docker.com/u/bobmaerten/docker-wallabag/)
prête à l'usage, pour éviter d'avoir à installer `php` directement sur
mon serveur. Tout allait bien, jusqu'à que je redémarre le container :
il m'était alors impossible de me reconnecter. En fouillant un peu, je
me rends compte qu'il y a un sel utilisé pour le hash des mots de passe,
et qu'il est possible que ce sel ait changé suite au redémarrage du
docker (si vous avez cliqué sur le lien du docker registry ci-dessus,
vous verrez qu'il est recommandé de définir ce sel comme une variable
d'environnement, ce que j'avais bien sûr omis). Dans ce cas-là, je me
suis trouvé bloqué hors de mon Wallabag, avec aucune possibilité de
changer le mot de passe (ou de m'envoyer un email de récupération de
compte), ce qui revient à perdre ses données.

Du sel pour le hash ? Mais bien sûr ! {#duselpourlehashmaisbiensr}
-------------------------------------

Petite explication technique pour ceux qui veulent savoir de quoi on
parle ici. Si sel, hash et SHA1 n'ont pas de secrets pour vous, vous
pouvez passer à la suite.

Il est dangereux de sauvegarder des mots de passe utilisateur en base de
données, en clair : sinon, cela signifie que les administrateurs du site
ou d'éventuels pirates peuvent s'authentifier sur le compte de
l'utilisateur et accéder à toutes ses données. De telles fuites de mots
de passe ont lieu assez couramment. Pour éviter cela, plutôt que stocker
le mot de passe en clair dans une base de données, on utilise une
fonction mathématique à sens unique qui transforme le mot de passe à
l'aide d'une formule mathématique compliquée en une "empreinte"
numérique. Cela signifie qu'il est facile de calculer l'empreinte à
partir du mot de passe, mais qu'il est (théoriquement) compliqué de
retrouver le mot de passe à partir de l'empreinte.

Du coup, plutôt que stocker le mot de passe en clair dans la base de
données, on stocke l'empreinte générée dans la base. Ainsi, pour
vérifier si un mot de passe entré par l'utilisateur sur le site est le
bon, il suffit de générer l'empreinte du mot de passe entré sur le site,
et de comparer avec l'empreinte en base de données. Jusque là, tout va
bien.

Tout va bien, sauf si la fonction mathématiquement théoriquement
compliquée ne l'est pas tant que ça. Pour Wallabag, il s'agit de SHA1,
qui a été prouvée comme étant facilement cassable il y a quelques années
de ça déjà. Il y a une très bonne
[explication](http://stackoverflow.com/questions/2772014/is-sha-1-secure-for-password-storage)
ici de la méthode utilisée pour retrouver le mot de passe à partir de
l'empreinte. L'idée est de prendre beaucoup de temps à générer des
tables avec toutes les entrées possibles, de manière à avoir une table
de correspondances entrées / empreintes, et ensuite quand on a une
empreinte donnée, de comparer à celles qui étaient présentes dans la
table avec toutes les correspondances.

Pour contrer cette attaque, il suffit de rajouter un "sel" après le mot
de passe, c'est-à-dire une chaîne de caractères compliquée, connue
uniquement par l'application elle-même. Ainsi, les attaques par table de
correspondance sont (encore une fois, théoriquement) impossibles, car
l'attaquant ne connaît pas le "sel" rajouté.

Et le lien avec le Schmilblick ? {#etlelienavecleschmilblick}
--------------------------------

Dans mon instance de Wallabag, le sel rajouté au mot de passe a été
modifié en redémarrant le container docker, ce qui fait que l'empreinte
que je générais en essayant de me connecter ne correspondait plus à
celle en base de données. Du coup, la solution pour s'en sortir est de
regénérer cette empreinte et la réécrire directement dans la base de
données. Comment faire ?

Heureusement, le code de Wallabag étant open-source, j'ai pu le
consulter sur [github](https://github.com/wallabag/wallabag). En
particulier, en faisant une [recherche sur
SALT](https://github.com/wallabag/wallabag/search?utf8=%E2%9C%93&q=SALT),
j'ai trouvé [cette
ligne](https://github.com/wallabag/wallabag/blob/master/inc/poche/config.inc.default.php#L11)
qui définit le sel rajouté pour calculer l'empreinte :

    @define ('SALT', ''); # put a strong string here

Il suffit donc de regarder la valeur écrite en dur dans ce fichier.
Valeur qui est par ailleurs
[utilisée](https://github.com/wallabag/wallabag/blob/4b1fa4c2febc7abbc6da3d65e4e760949a55843c/install/index.php#L66)
au moment de l'installation pour générer l'empreinte du mot de passe en
base de données :

    $salted_password = sha1($password . $username . $salt);

Donc l'empreinte est générée à partir de la chaîne de caractères
suivante : mot de passe, nom d'utilisateur, sel trouvé dans le fichier
`inc/poche/config.inc.default.php`, le tout sans espaces. Il suffit donc
maintenant de retrouver le sel, regénérer l'empreinte et mettre à jour
la base de données, ce qui se fait en 5 lignes, comme le montre la
section TL:DR ci-dessus.

Conclusion : go meta {#conclusiongometa}
--------------------

Cette méthode de génération d'empreintes pour stocker des mots de passe
en base de données est assez récurrente, du coup il est possible de
l'adapter à d'autres algorithmes (SHA256) et d'autres constructions de
chaînes.

Bien sûr, pour ce qui est du Docker Wallabag, il est plus simple de
définir le sel comme une variable d'environnement, comme indiqué dans la
documentation du container.

Par ailleurs, s'il existe une autre méthode pour récupérer son mot de
passe sous Wallabag, je serai ravi de la connaître ! N'hésitez pas à me
faire part de vos remarques via [twitter](https://twitter.com/bnjbvr).
