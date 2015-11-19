Title: CozyCloud : migrer son instance 2, le retour
Date: 2015-04-21 21:12
Author: Benjamin Bouvier
Lang: fr
Tags: cozycloud, kresus
Slug: cozycloud-migrer-son-instance-2-le-retour

Si vous vous rappelez bien, j'ai [déjà écrit un
article]({filename}./cozycloud-migrer-son-instance-dun-serveur-vers-un-autre.md)
pour expliquer comment migrer son instance [https://cozy.io](CozyCloud) d'un
endroit vers un autre. Ces derniers jours, je me suis rendu compte que mon
serveur personnel était sous-utilisé et qu'il me serait possible d'en prendre
un plus léger et moins cher, d'où la nécessité d'une nouvelle migration d'un
serveur à un autre.

Les étapes sont les suivantes :

- Récupérer la base de l'ancien Cozy.
- La mettre en place dans le nouveau Cozy.
- Réinstaller les applications.

Récupérer la base de l'ancien Cozy  {#recuperer-base-ancien-cozy}
===

Il s'agit d'un fichier qui contient toutes les données relatives à votre Cozy,
que ce soit des données internes (par exemple, quelles applications
installées) ou propres aux applications (par exemple, vos comptes en banques).

Si votre Cozy est hébergé par CozyCloud (sur
[cozycloud.cc](https://cozycloud.cc) donc), il est possible de demander
l'export de la base de données CouchDB à l'équipe Cozy. Problème réglé.

Si vous êtes auto-hébergé, il va falloir mettre les mains dans le cambouis :
- d'abord, réduire la taille de la base de données, c'est-à-dire effectuer un
  compactage de la base de données. Depuis votre serveur, effectuez les
  commandes suivantes :

        cozy-monitor compact
        cozy-monitor compact-all-views

- ensuite, récupérer la base elle-même. Celle-ci est contenue dans le
  répertoire `/var/lib/couchdb/` et porte le nom de `cozy.couch`, sauf si vous
  l'avez modifié vous-même.
    - Si vous avez installé votre serveur avec le package Debian ou Ubuntu, il
      est possible d'utiliser l'outil `scp` pour effectuer cette tâche, en vous
      connectant depuis le nouveau serveur vers l'ancien.
    - Si comme moi vous avez préféré jouer avec le feu et utiliser Docker pour
      installer votre cozy, il va falloir ruser un peu. Personnellement, j'ai
      choisi la méthode *malpropre*, à savoir exposer la base de données sur le
      serveur web pendant un court instant et utiliser `wget` sur le nouveau
      cozy. Il est sûrement possible d'extraire le fichier depuis le Docker
      vers l'hôte, mais j'avoue ne pas avoir cherché ; si quelqu'un connaît une
      méthode, je suis preneur ! Pour ma méthode "malpropre", il faut modifier
      le fichier de configuration de nginx pour donner accès au fichier :

            # Copier la base vers /var/www
            sudo cp /var/lib/couchdb/cozy.couch /var/www
            # Donner les droits en lecture à nginx
            sudo chown www-data:www-data -R /var/www
            # Editer le fichier de config avec le meilleur éditeur du monde
            sudo vim /etc/nginx/sites-available/cozy.conf

      J'ai remplacé le bloc `location/ { proxy_set_header ...` par le suivant :

            location / {
                root /var/www;
                try_files $uri $uri/ /index.html;
            }

      Ensuite, depuis le nouveau serveur, sur lequel je suppose que vous avez
      déjà installé le paquet `cozy` et qu'il tourne correctement :

            cd /var/lib/couchdb
            sudo service supervisor stop
            sudo service couchdb stop
            sudo rm -f cozy.couch
            sudo wget https://monanciencozy.tld/cozy.couch

Mettre en place la base dans le nouveau cozy {#mettre-en-place-base-nouveau-cozy}
====

Je suppose que vous avez déjà récupéré la base d'une manière ou d'une autre, et
que celle-ci est déjà présente dans `/var/lib/couchdb`

            cd /var/lib/couchdb
            sudo chown -R couchdb:couchdb ./cozy.couch
            sudo service couchdb start
            sudo service supervisor start

Et voilà ! Après cela, il va falloir attendre quelques minutes que le
contrôleur Cozy relance les applications.

Réinstaller les applications manquantes {#recuperer-applications-manquantes}
===

L'import de la base comprend les données internes à Cozy, notamment les
informations sur les applications installées. Comme on vient d'importer une
base qui vient d'un autre cozy où des applications sont installées, le nouveau
cozy va penser que certaines applications sont présentes sur le disque, alors
qu'elles ne le sont pas. Il est nécessaire d'effectuer une petite réparation
ici, au niveau de la pile logicielle cozy et des applications installées.
Heureusement, l'équipe a pensé à ça et nous a founri une commande qui permet de
réinstaller les applications utilisateurs. C'est parti, depuis le nouveau
serveur :

        # Mettre à jour l'ensemble de la stack Cozy pour commencer
        sudo cozy-monitor update-all-cozy-stack
        # Réinstaller les applications manquantes
        sudo cozy-monitor reinstall-missing-app

J'ai eu plusieurs erreurs à ce moment-là, souvent liées à des applications qui
n'étaient plus trouvées sur github, ou des erreurs réseaux. En général,
relancer la commande fonctionne, sinon j'ai purement et simplement désinstallé
l'application en question. Par exemple, si l'application plantée était
[Kresus]({filename}./kresus-version-060.md), j'ai simplement effectué

        sudo cozy-monitor uninstall kresus

Ce n'est pas un problème, car la désinstallation d'une application n'implique
pas la désinstallation des données. Ensuite, il est possible de réinstaller les
applications depuis l'interface du site web.

Conclusion
===

Notons que la migration d'un serveur à l'autre est désormais beaucoup plus
facile qu'auparavant ! Pas besoin de rafistoler les données directement dans la
base, et il existe une commande pour réinstaller les applications
automatiquement. Bien joué, l'équipe Cozy !

J'espère que cette procédure aura marché pour vous, j'ai écrit ces notes
rapidement et de mémoire. Si j'ai oublié quoi que ce soit, n'hésitez pas à me
contacter sur [twitter](https://twitter.com/bnjbvr),
[diaspora](https://framasphere.org/u/bnjbvr) ou sur irc (mon nick est
`bnjbvr`). Si ça a marché et que vous avez apprécié, n'hésitez pas à me le dire
également ;-)

