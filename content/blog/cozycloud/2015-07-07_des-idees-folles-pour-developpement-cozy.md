Title: Des idées folles pour faciliter le développement sous Cozy
Date: 2015-07-07 18:37
Author: Benjamin Bouvier
Lang: fr
Tags: cozycloud
Slug: des-idees-folles-pour-faciliter-le-developpement-sous-cozy

Récemment, sur le forum de CozyCloud,
[Clochix](https://blog.benj.me/2015/07/07/des-idees-folles-pour-faciliter-le-developpement-sous-cozy/twitter.com/Clochix)
(employé de l'entreprise CC), demandait comment l'on pourrait faciliter
le développement d'applications pour Cozy. Bonne initiative ! J'ai
essayé de structurer un peu mes idées dans le forum d'abord, mais comme
ça devenait beaucoup trop long, j'ai préféré écrire ce post, vu que j'ai
beaucoup de commentaires :)

Parmi ces commentaires, il y a beaucoup d'idées saugrenues, sûrement
difficiles à implémenter, mais je fais le pari que si je les écris ici,
elles pourront inspirer les lecteurs, qui crééeront leurs propres idées
à partir de celles-ci, ou en les fusionnant, etc. Les idées
appartiennent à tout le monde !

### Du statique {#dustatique}

Tout d'abord, il me semble primordial de permettre de développeur sur
son cozy depuis son cozy. Pour commencer, on pourrait partir avec **un
site statique et un éditeur de texte**. Imaginons un instant un
répertoire spécial `www` par exemple, accessible depuis Files. Une
nouvelle application ferait office de serveur statique, et pourrait
servir tous les fichiers présents dans ce répertoire `www` sur une
adresse publique. Ensuite, une autre application saurait ouvrir tous les
fichiers textes importés dans Files et les éditer directement. Avec ces
deux choses, on a la possibilité de **créer son site statique et le
modifier directement depuis son cozy**. Cela me paraît une bonne
première étape !

L'intégration d'outils comme [WebMaker](https://webmaker.org) pourrait
même permettre de créer des sites facilement pour les débutants, et de
propager l'apprentissage des technologies web auprès du grand public.

### Des outils de développement {#desoutilsdedveloppement}

Ensuite, [comme le dit
@Clochix](https://forum.cozy.io/t/comment-pouvons-nous-vous-aider-a-bidouiller-cozy/880/2?u=ben),
**réduire le nombre d'outils à utiliser pour le développement**. A
l'heure actuelle, quand je veux modifier
[Kresus](https://github.com/bnjbvr/kresus) (mon application de finances
personnelles hébergée sur cozy) depuis ma machine de tous les jours, je
dois :

1.  lancer la VM de développement dans le bon répertoire, ce qui prend
    facilement 2 minutes (vérification de l'image, timeouts
    malheureusement réguliers sur le SSH, etc.)
2.  aller dans le répertoire de Kresus depuis la machine hôte
3.  lancer `cozy-dev deploy 9876` (parce que le cozy de dev ne se
    souvient pas que j'ai pu faire un deploy auparavant... peut-être que
    ça vaut un bug ?). C'est instantané, mais c'est redondant de le
    faire à chaque fois !
4.  lancer kresus

Si jamais je veux modifier kresus depuis une nouvelle machine, je dois
en plus de ça télécharger et installer la VM (ce qui peut facilement
prendre 10 minutes, en fonction du débit et de la puissance de la
machine).

Dans un monde idéal de développement d'applications pour Cozy,
j'aimerais avoir à faire simplement :

1.  lancer kresus

C'est-à-dire qu'il y ait une machine toute prête pour le développement.
Peu m'importe l'implémentation :

-   que ce soit via le serveur de production, qui utiliserait une
    deuxième base couchdb (si cette notion a du sens ?) pour ne pas
    écraser les données de l'instance de production;
-   que ce soit via [cloud9](https://c9.io/) ou tout autre système de
    dév avec VM intégrée en ligne;
-   que ce soit via une app de VM sur le cozy (qemu.js, quelqu'un ?);
-   [insérez d'autres idées folles ici];

Allons plus loin : si j'ai la possibilité d'avoir un éditeur de code
directement dans cozy (coucou
[vim.js](https://github.com/coolwanglu/vim.js)), pourquoi ne pas
modifier à la volée mes apps, côté client comme côté serveur, et
recharger directement depuis le cozy ? Cela permettrait d'avoir des
retours encore plus rapides sur le processus de développement (et de
trouver plein de bugs de cozy-controller, si jamais il en y avait
certain de bien planqués !).

### Du portage {#duportage}

Je désigne par portage le fait de prendre du code d'une app déjà
existante et d'essayer de le porter sous Cozy.

Pour moi, le plus gros problème du portage est sûrement le fait qu'il
faille **réécrire toutes les URLs**, côté client. De nos jours, assez
souvent, les applications web supposent qu'elles ont accès à un domaine
ou un sous-domaine entier, et pas qu'elles vont vivre dans un
sous-répertoire particulier (sauf en PHP, sigh). Par exemple, le système
de blog Ghost suppose qu'il vit dans `http://ghost.example.com`, pas
dans `http://example.com/ghost`, sauf contre-indication. Du coup, la
plupart des URLs doivent être réécrites, et c'est souvent assez
difficile ou obscur de trouver où sont ces dernières.

Bien sûr, il y a des solutions :

-   un sous-domaine par app, mais ça pose des problèmes pour les
    certificats SSL vu qu'il faut des certificats avec *wildcard* sur
    les sous-domaines, mais heureusement [LetsEncrypt devrait sortir en
    septembre](https://letsencrypt.org/2015/06/16/lets-encrypt-launch-schedule.html);
-   utilisation de [service
    workers](https://developer.mozilla.org/en-US/docs/Web/API/ServiceWorker)
    pour réécrire toutes les URLs commandées par le client, côté client
    : beurk, mais efficace;

L'autre problème du portage est **l'intégration des données** : même
s'il est *faisable* d'intégrer les données d'apps existantes pour
qu'elles vivent dans le couchdb du cozy (voir dernière partie), cela
n'assure pas de créer facilement des interactions entre les données des
apps existantes et des apps portées. Quand bien même l'on voudrait
rajouter ces interactions, il faut modifier l'interface utilisateur de
l'app portée (difficile), ou bien le faire depuis une autre app (étrange
en termes d'interaction utilisateur). Le portage n'est pas un problème
simple (et ce n'est vraiment pas la faute de Cozy, c'est inhérent à tous
les clouds personnels, à mon avis).

### Des choix technologiques {#deschoixtechnologiques}

[Le blog de
N\`](http://blog.menfin.info/posts/2015-07-01-sur-un-petit-nuage-cozy/)
lit : "[...] je regrette certains choix techniques et les conséquences
associées. CouchDB n’est plus très populaire ces derniers temps.". A
vrai dire, quelle que fût la technologie utilisée comme backend, on
aurait pu trouver ces remarques, avec "postgre", ou "mongo", ou
n'importe quel autre produit à la place de "couchdb". Et ce n'est pas
que la dite technologie est mauvaise, loin de là ; c'est simplement que
les différents auteurs d'app voudront utiliser des technologies
différentes.

Personnellement, l'utilisation de CouchDB m'a demandé un effort initial
(à cause du système de vues) que ne m'aurait pas demandé une bête base
de données SQL. Ce n'est pas pour autant quelque chose de difficile,
mais c'est quelque chose de nouveau, et l'amas de nouveaux concepts liés
au développement dans Cozy peut être un frein.

Et qu'il s'agisse de la base de données ou du langage, le problème dans
les deux cas est la dispersion : plus d'outils, ça signifie plus de
maintenance nécessaire, plus de vecteurs d'attaques, etc. Pourtant,
combien de personnes adoreraient développer une app pour Cozy, mais ne
le font pas parce qu'il n'est pas possible d'écrire sa web app en
Python, Erlang, Haxe, allez soyons fous, PHP ? Combien de projets ne
sont pas portés, pour les mêmes raisons ? Avec la mode de la
containerisation, sandboxer un interpréteur ou une VM est quasiment
gratuit et pourrait permettre cette utilisation d'autres langages dans
Cozy.

Pour le problème de la base de données, il y a plusieurs approches :

-   juste installer plusieurs systèmes de gestion de base de données
    dans la plateforme (mongo, cassandra, whatever), mais ce n'est
    vraiment pas idéal, pour les raisons exposées ci-dessus;
-   utiliser un protocole de stockage de données indépendant du langage,
    l'implémenter dans cozy puis écrire quelques bibliothèques de code
    réutilisables pour pouvoir utiliser ce protocole. C'est l'approche
    prise par ces bons gars de Mozilla avec
    [Kinto](http://kinto.readthedocs.org/), comme expliqué
    [ici](http://www.servicedenuages.fr/stockage-generique-ecosysteme).
    En y réfléchissant bien, c'est *presque* l'approche prise par le
    système de données dans Cozy, vu qu'il utilise des appels à un point
    d'accès HTTP : la seule différence réside dans le fait que ces
    appels sentent et rappellent trop Couch;
-   écrire un meta-adaptateur : une application qui comprenne les
    protocoles de plusieurs bases de données (de manière à ce que
    l'utilisateur puisse avoir l'impression de communiquer avec par
    exemple mongo, ou mariadb, indifféremment), et qui retranscrive cela
    en structures de données et requêtes couchdb. Je pense que c'est
    illusoire : vu que les différents systèmes de stockage peuvent
    assurer différentes parties du théorème CAP, beaucoup de
    fonctionnalités pourraient ne pas être équivalentes (ou ne pas être
    imitées de manière efficace).

### De ce qui marche {#decequimarche}

Les mêmes problèmes se posent pour d'autres plateformes de cloud
personnel comme [OwnCloud](http://owncloud.com/) et ne vont pas se
résoudre du jour au lendemain. Chacune de ces idées demande un temps
d'implémentation considérable (sauf peut-être le serveur statique et
l'éditeur de texte -- à croire que c'en est une bonne idée !), du temps
pour tester de la part des utilisateurs et beaucoup de retours entre
développeurs et utilisateurs. Pourtant, certains ont déjà été confrontés
à ces problématiques et les ont résolues avec panache.

Un modèle en la matière est [App.net](http://app.net/) (ADN pour les
intimes), un réseau social *centralisé* mais qui assure de ne pas
espionner les données des utilisateurs, en contrepartie d'un abonnement
de quelques dollars par mois. Des apps pour ADN peuvent être créées par
les utilisateurs très facilement, et il en existe de très bonnes.
Qu'est-ce qui a attiré les développeurs pour créer des apps pour ADN ?

-   une [documentation exemplaire](https://developers.app.net/docs/),
    avec de nombreux tutoriels, des présentations de l'API, plein de
    liens vers différents canaux de communications réservés aux
    développeurs, des articles de blog juste pour présenter des
    nouvelles APIs aux développeurs, des podcasts, etc. La documentation
    est open-source et peut être modifiée par n'importe qui, comme pour
    Cozy.
-   une [diversité au niveau des
    technologies](http://blog.app.net/2013/11/18/adnpy-a-new-python-library-from-app-net/)
    utilisées pour écrire des apps clientes pour ADN : python, objective
    c, android, etc.;
-   l'[organisation de
    hackathons](http://blog.app.net/2014/01/27/app-net-hackathon-recap-3/)
    pour lancer des projets en commun, faire se rencontrer des
    développeurs et provoquer le démarrage de nouvelles apps;
-   des articles de blog [présentant des nouvelles apps pour
    ADN](http://blog.app.net/2014/01/17/sunlit/) (n.b.: kresus n'a pas
    encore atteint ce niveau de maturité à mon avis);
-   encore plus fou, [un programme d'incentives pour le développement
    d'app](http://blog.app.net/2013/03/01/updates-to-the-app-net-developer-incentive-program/).
    En gros, si votre application a été sélectionnée comme étant une des
    plus utiles à la communauté, vous recevez une part d'un budget
    alloué à la promotion du développement des nouvelles apps. C'est un
    argument pécunier, mais c'est sûrement ce qui a fait la différence
    entre ADN et [tent](https://tent.io), par exemple (tent est mort,
    vite tent).

A mon avis, les trois premiers points demandent un investissement
relativement mineur et permettraient de donner un coup de pied au
développement d'apps sous Cozy. Par ailleurs,
[Kresus](https://github.com/bnjbvr/kresus) cherche toujours de nouveaux
contributeurs, si vous êtes intéressés, n'hésitez-pas à me contacter !

Si vous avez des remarques par rapport à cet article, je vous invite à
m'en faire part sur [twitter](https://twitter.com/bnjbvr) pour les
remarques courtes ou sur [le
forum](https://forum.cozy.io/t/comment-pouvons-nous-vous-aider-a-bidouiller-cozy/)
pour les remarques plus longues. Cheers !
