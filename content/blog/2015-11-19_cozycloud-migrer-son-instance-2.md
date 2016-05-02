Title: CozyCloud : migrer son instance 2, le retour
Date: 2015-11-19 14:00
Author: Benjamin Bouvier
Lang: fr
Tags: cozycloud
Slug: cozycloud-migrer-son-instance-2-le-retour

Si vous vous rappelez bien, j'ai [déjà écrit un
article]({filename}./2015-04-21_cozycloud-migrer-son-instance.md)
pour expliquer comment migrer son instance [https://cozy.io](CozyCloud) d'un
endroit vers un autre. Ces derniers jours, je me suis rendu compte que mon
serveur personnel était sous-utilisé et qu'il me serait possible d'en prendre
un plus léger et moins cher, d'où la nécessité d'une nouvelle migration d'un
serveur à un autre.

Edit (10 février 2016) : j'ai ajouté la copie des répertoires permanents à
cette procédure, sans avoir pu tester. Vos retours sur cette partie sont les
bienvenus !

Les étapes sont les suivantes :

- Récupérer la base de l'ancien Cozy.
- Recopier le répertoire de données permanentes des apps.
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

D'abord, réduire la taille de la base de données, c'est-à-dire effectuer un
compactage de la base de données. C'est parti, depuis l'ancien serveur :

        # On éteint Cozy pour éviter l'apparition de nouvelles données
        sudo service supervisor stop
        # On fait une sauvegarde de la base, en cas de pépin
        cd /var/lib/couchdb/
        sudo cp cozy.couch cozy.couch.backup
        # On compacte la base
        sudo cozy-monitor compact

Ensuite, récupérer la base elle-même. Celle-ci est contenue dans le répertoire
`/var/lib/couchdb/` et porte le nom de `cozy.couch`, sauf si vous l'avez
modifié vous-même.

#### L'ancien Cozy était installé par le package Debian

Si vous avez installé votre serveur avec le package Debian ou Ubuntu, il est
possible d'utiliser l'outil `scp` pour effectuer cette tâche, en vous
connectant depuis le nouveau serveur vers l'ancien. Si vous utilisez cette
méthode, prenez soin de nommer la version sur le nouveau serveur
`cozy.couch.new`, c'est important pour la suite.

#### L'ancien Cozy était installé avec Docker
Si comme moi vous avez préféré jouer avec le feu et utiliser Docker pour
installer votre cozy, il va falloir ruser un peu. Personnellement, j'ai choisi
la méthode *malpropre*, à savoir exposer la base de données sur le serveur web
pendant un court instant et utiliser `wget` sur le nouveau cozy. Il est
sûrement possible d'extraire le fichier depuis le Docker vers l'hôte, mais
j'avoue ne pas avoir cherché ; si quelqu'un connaît une méthode, je suis
preneur ! Pour ma méthode « malpropre », il faut modifier le fichier de
configuration de nginx pour donner accès au fichier :

        # Copier la base vers /var/www
        sudo cp /var/lib/couchdb/cozy.couch /var/www/cozy.couch.new
        # Donner les droits en lecture à nginx
        sudo chown www-data:www-data -R /var/www
        # Editer le fichier de config de nginx avec le meilleur éditeur du monde
        sudo vim /etc/nginx/sites-available/cozy.conf

J'ai remplacé le bloc `location/ { proxy_set_header ...` par le suivant :

        location / {
            root /var/www;
            try_files $uri $uri/ /index.html;
        }

Toujours depuis l'ancien serveur, bien penser à relancer nginx :

        sudo service nginx restart

Ensuite, depuis le nouveau serveur, sur lequel je suppose que vous avez
déjà installé le paquet `cozy` et qu'il tourne correctement :

        cd /var/lib/couchdb
        # Stopper supervisor va arrêter tout cozy
        sudo service supervisor stop
        sudo service couchdb stop
        sudo wget https://monanciencozy.tld/cozy.couch.new

Recopier les données permanentes des applications
===

Cela a été rajouté depuis l'écriture initiale de ce blog post, il est donc
probable que cela ne fonctionne pas, dans quel cas contactez-moi svp !

Depuis des versions récentes de la plateforme, Cozy autorise les applications à
avoir un répertoire de données permanentes, qui sont conservées même si
l'application a été désinstallée. C'est très pratique pour porter facilement
des applications qui utilisent des fichiers comme mémoire vers Cozy !

Pour porter ce répertoire, voici la procédure à effectuer :

- copier le répertoire sur la machine précédente et le mettre dans un zip, par
  exemple:

        # depuis la machine qui héberge l'ancien cozy
        cd /usr/local/var/cozy
        zip /tmp/usr-local-var-cozy.zip -r ./*

- transférer le zip vers le nouveau serveur (avec votre méthode préférée : FTP,
  Web, scp, etc.). Par exemple, avec `scp`:

        # depuis la nouvelle machine
        scp user@ancienne-machine:/tmp/usr-local-var-cozy.zip /tmp

- remplacer le répertoire sur la nouvelle machine:

        # depuis la nouvelle machine
        mkdir -p /usr/local/var/cozy
        cd /usr/local/var/cozy && zip backup.zip -r ./*
        unzip /tmp/usr-local-var-cozy.zip


Mettre en place la base dans le nouveau cozy {#mettre-en-place-base-nouveau-cozy}
====

Je suppose que vous avez déjà récupéré la base d'une manière ou d'une autre, et
que celle-ci est déjà présente dans `/var/lib/couchdb`, sous le nom
`cozy.couch.new`. Depuis le nouveau serveur, effectuez les commandes suivantes :

            cd /var/lib/couchdb
            # On arrête Cozy (via supervisor) et couchdb
            sudo service supervisor stop
            sudo service couchdb stop
            # Backup de l'ancienne base
            sudo mv cozy.couch cozy.couch.old
            sudo mv cozy.couch.new cozy.couch
            sudo chown -R couchdb:couchdb ./cozy.couch
            # On relance le tout
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
Heureusement, l'équipe a pensé à ça et nous a fourni une commande qui permet de
réinstaller les applications utilisateurs. C'est parti, depuis le nouveau
serveur :

        # Mettre à jour cozy-monitor (utile pour les installation à partir 
        # d'une image préinstallée comme pour le RPI2
        sudo npm install -g cozy-monitor
        # Mettre à jour l'ensemble de la pile Cozy pour commencer
        sudo cozy-monitor update-all-cozy-stack
        # Réinstaller les applications manquantes
        sudo cozy-monitor reinstall-missing-app

J'ai eu plusieurs erreurs à ce moment-là, souvent liées à des applications qui
n'étaient plus trouvées sur github, ou des erreurs réseaux. En général,
relancer la commande fonctionne, sinon j'ai purement et simplement désinstallé
l'application en question. Par exemple, si l'application plantée était
[Kresus]({filename}./2015-11-16_kresus-version-060.md), j'ai simplement effectué

        sudo cozy-monitor uninstall kresus

Ce n'est pas un problème, car la désinstallation d'une application n'implique
pas la désinstallation des données. Ensuite, il est possible de réinstaller les
applications depuis l'interface du site web.

Pour terminer, il faut mettre à jour les permissions des dossiers contenant les données 
persistantes : 

       # On va dans le dossier 
       cd /usr/local/var/cozy
       # On change les permieesions pour chaque dossier. Note, penser à changer le nom de 
       # l'application à chaque fois
       sudo chown -R cozy-nomApp nomApp
       


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
également. ;-)
