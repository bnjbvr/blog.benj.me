Title: CozyCloud : migrer son instance d'un serveur vers un autre
Date: 2015-04-21 21:12
Author: Benjamin Bouvier
Lang: fr
Tags: cozycloud, kresus
Slug: cozycloud-migrer-son-instance-dun-serveur-vers-un-autre

Il arrive de temps en temps de devoir changer de serveur, et puisque le
credo de [CozyCloud](http://cozy.io/) est de pouvoir partir à n'importe
quel moment, encore faut-il pouvoir le faire facilement et savoir
comment le faire ! En attendant que l'équipe mette en place un moyen
officiel d'effectuer cette tâche, voici une méthode que j'ai utilisée
pour migrer mon instance cozy d'un serveur vers un cozy situé sur un
autre serveur distant. C'est dangereux, vous allez mettre les mains dans
le cambouis et vous salir, mais au final vous ne perdrez aucune donnée
après la migration !

Post scriptum {#postscriptum}
-------------

[Nicolas](https://twitter.com/nledez), de l'équipe Cozy, m'a dit qu'il
est plus rapide et plus efficace de faire une simple copie du fichier de
la base de données cozy `cozy.couch` depuis la machine source et de le
remplacer dans la machine distante. Dans ce cas, pas besoin de vous
embêter avec toutes les péripéties de ce tutoriel ! Des gens en parlent
[ici](https://forum.cozy.io/t/comment-faire-un-backup-de-la-base-de-donnees-couchdb/531).
Si quelqu'un a plus de détails sur la méthode et confirme que celle-ci
fonctionne, je serai ravi de mettre à jour cet article, n'hésitez-pas à
me contacter ! (cf fin du message)

La méthode {#lamthode}
----------

Dans ce tutoriel, j'utiliserai le vocabulaire suivant :

-   la machine **source** sera la machine depuis laquelle on fait la
    copie du cozy. C'est elle qui contient toutes les données et que
    l'on cherche à répliquer.
-   la machine **cible** sera la machine vers laquelle on migre son
    cozy. Je recommande que cette instance dispose d'un cozy pré
    installé, **à jour** (la plateforme devrait être à jour), mais sans
    aucune donnée à l'intérieur (c'est-à-dire un cozy tel qu'il serait
    juste après l'installation par les scripts). Idéalement, il faudrait
    que le nom d'utilisateur (email) de ce cozy cible soit quelque chose
    de facilement reconnaissable, vu que l'on devra identifier cet
    utilisateur plus tard... Par exemple, utiliser `demo@domain.tld`
    comme email de login.

Cible : Désactiver la sécurité des appareils authentifiés {#cibledsactiverlascuritdesappareilsauthentifis}
---------------------------------------------------------

Pour cette procédure, nous allons en fait nous faire passer pour
n'importe quel appareil qui voudrait se synchroniser avec le cozy,
c'est-à-dire que l'on va se faire passer pour l'application mobile
`cozy-mobile` ou pour l'application bureau `cozy-desktop`. Cependant, la
synchronisation avec ces appareils marche (grossièrement) de la manière
suivante :

-   l'appareil qui veut se synchroniser avec le cozy s'authentifie la
    première fois, avec le mot de passe du cozy.
-   l'appareil est inscrit dans la liste des appareils autorisés.
-   lors des synchronisations, le serveur cozy vérifie que l'appareil
    est autorisé avant de transmettre la requête de réplication à
    couchdb, qui lui gérera l'authentification.

Seulement dans notre cas, on n'a pas la possibilité de s'inscrire en
tant qu'appareil autorisé, on va donc devoir contourner le code qui fait
cette vérification ! Bien sûr, ce ne sera que temporaire et on remettra
le code tel qu'il était à l'origine, dans la dernière étape...

On se place dans le bon répertoire, tout d'abord :

    cd /usr/local/cozy/apps/proxy/build/server/controller/

Il faut ensuite ouvrir le fichier `devices.js` avec les droits de
modification (je suis passé par `sudo vim devices.js` pour le faire,
mais vous avez le droit à d'autres éditeurs de texte, inférieurs
soient-ils :D).

On identifie la fonction `replication`, et plus particulièrement la
partie qui vérifie l'authentification :

    return deviceManager.isAuthenticated(username, password, function(auth) {
        var error;
        if (auth) {
            if (process.env.NODE_ENV === "production") {
                req.headers['authorization'] = getCredentialsHeader();
            } else {
                req.headers['authorization'] = null;
            }
            return getProxy().web(req, res, {
                target: "http://" + couchdbHost + ":" + couchdbPort
            });
        } else {
            error = new Error("Request unauthorized");
            error.status = 401;
            return next(error);
        }
    });

On va juste remplacer `auth` par `true` dans la première condition, pour
faire croire au proxy que l'appareil est toujours authentifié :

    return deviceManager.isAuthenticated(username, password, function(auth) {
        var error;
        if (true) {   // <============= ICI, j'ai remplacé auth par true
            if (process.env.NODE_ENV === "production") {
                req.headers['authorization'] = getCredentialsHeader();
            } else {
                req.headers['authorization'] = null;
            }
            return getProxy().web(req, res, {
                target: "http://" + couchdbHost + ":" + couchdbPort
            });
        } else {
            error = new Error("Request unauthorized");
            error.status = 401;
            return next(error);
        }
    });

On sauvegarde et on quitte, puis on relance le proxy pour être sûr que
les modifications sont prises en compte :

    cozy-monitor restart proxy

Cible : Récupérer le mot de passe de couchdb {#ciblercuprerlemotdepassedecouchdb}
--------------------------------------------

On a maintenant besoin de l'identifiant et du mot de passe pour accéder
à la base de données couchdb de la machine cible. Pour cela, il suffit
de regarder dans `/etc/cozy/couchdb.login`:

    cat /etc/cozy/couchdb.login

Chez moi, ça affiche :

    bonjour
    motdepasse

La première ligne correspond au login, la seconde au mot de passe. On
note ça quelque part, et c'est parti pour lancer la copie.

Source : lancer la copie {#sourcelancerlacopie}
------------------------

Depuis la machine source maintenant, on va lancer la copie. Imaginons
que ma machine cible soit située sur le nom de domaine
`cozy.example.tld`, alors la commande à lancer est la suivante :

    cozy-monitor backup https://bonjour:motdepasse@cozy.example.tld/cozy

où `bonjour` et `motdepasse` sont respectivement le nom d'utilisateur et
le mot de passe couchdb de la machine cible.

La manipulation va prendre un peu de temps, et il arrive qu'elle échoue
même si vous avez beaucoup de données. Personnellement, il m'a fallu la
relancer plusieurs fois avant que ça finisse sans encombre, mais au bout
d'un moment, ça s'est arrêté de planter et ça a finalement marché.

Cible : Remettre l'authentification des appareils dans son état initial {#cibleremettrelauthentificationdesappareilsdanssontatinitial}
-----------------------------------------------------------------------

La sécurité étant cruciale pour éviter que n'importe qui ne puisse
récupérer vos données personnelles, pensez bien à remettre le fichier de
code modifié `devices.js` dans son état initial (c'est-à-dire changer la
condition de `if (true)` à `if (auth)`), et à redémarrer le proxy sur la
machine cible :

    cozy-monitor restart proxy

Cible : Rafistoler les données {#ciblerafistolerlesdonnes}
------------------------------

Maintenant, on va se connecter via l'interface web à la machine cible,
comme on se connecterait à n'importe quel moment pour aller voir son
cozy. A ce point-là, je me suis connecté avec mon login et mot de passe
utilisés lors de la création du cozy cible, mais il se pourrait bien que
ça marche avec le login et mot de passe de la machine source également
(à confirmer).

Le cozy cible est dans un état inconsistent. Pourquoi ?

-   Il y a plusieurs données qui sont censées être présentes de manière
    unique (informations sur l'instance, l'utilisateur, etc.), et qui
    sont présentes en doublons. En effet, ces données sont créées une
    fois lors de la création du cozy, et on les a en double à cause de
    la copie du cozy source. Il va falloir nettoyer ces données.
-   Les mots de passe stockés dans la base sont chiffrés avec des clés
    qui dépendent du mot de passe de l'utilisateur et d'un sel
    cryptographique, uniques par utilisateur. Du coup, comme il y a
    plusieurs utilisateurs (rappelez-vous, les données sont en double),
    le mot de passe pourrait ne pas être déchiffré correctement, ce qui
    fait que les applications de récupération de données (comme
    [kresus](https://github.com/bnjbvr/kresus) ou
    [konnectors](https://github.com/frankrousseau/konnectors)) ne vont
    plus marcher correctement.

La bonne nouvelle, c'est que ces deux problèmes se résolvent tous les
deux en supprimant les données présentes en doublons. Pour faire cela,
voici la liste des étapes :

-   depuis l'interface web du cozy cible, on désinstalle l'appli
    `data browser` (toutes mes données) si elle était présente, puis on
    la réinstalle. Cela est nécessaire parce que le cozy pourrait croire
    que l'application est installée en double (le cozy a des
    enregistrements en base de données sur les applications actuellement
    installées).
-   on lance l'application `data-browser`
-   dans la table `CozyInstance`, on supprime l'instance qui ne
    correspond pas à celle du cozy cible (a priori, c'est celle qui n'a
    pas de nom de domaine, sauf si vous en aviez défini un sur le cozy
    cible).
-   dans la table `StackApplication`, on supprime toutes les lignes en
    double. Comme il s'agit des applications de la plateforme, si le
    cozy cible était bien mis à jour avant de faire ces opérations, il
    suffit de supprimer les lignes avec les numéros de version
    inférieurs ou égaux.
-   dans la table `Applications`, on supprime toutes les lignes (en
    cliquant sur l'icône de corbeille), **sauf data-browser** qu'on a
    remis dans un état consistent à la main.
-   dans la table `User`, on supprime la ligne qui correspond à
    l'utilisateur du cozy cible (si vous avez suivi mon exemple, c'est
    le `demo@domain.tld` dont je parlais au tout début).
-   on se déconnecte et on se reconnecte sur le cozy.
-   laisser reposer, mettre au four thermostat 6 pendant 1 minute.
-   c'est prêt, vous pouvez déguster !

Conclusion
----------

J'espère que cette procédure aura marché pour vous, je n'ai pas pu la
réessayer, du coup cette procédure est extraite de mes notes
personnelles et il se pourrait que j'ai oublié quelques détails. Si
c'est le cas, n'hésitez pas à me contacter sur
[twitter](https://twitter.com/bnjbvr) ou sur irc (mon nick est
`bnjbvr`). Si ça a marché et que vous avez apprécié, n'hésitez pas à me
le dire également ;-)

