Title: Une image Docker pour Kresus / Weboob
Date: 2016-08-29 11:30
Author: Benjamin Bouvier
Lang: fr
Tags: kresus
Slug: kresus-weboob-docker

Si vous suivez ce blog, vous avez dû entendre parler de
[Kresus](https://framagit.org/bnjbvr/kresus/), le gestionnaire de finances
personnelles open-source sur lequel je travaille. Pour rappel, cette
application, basée sur [Weboob](http://weboob.org/), est disponible dans
[CozyCloud](https://cozy.io/en/) et vous permet de vous connecter à votre
compte bancaire, récupérer vos opérations et les classifier pour savoir où
votre argent passe.

## Kresus sans Cozy

Depuis quelques versions, vous pouvez également lancer Kresus sans avoir à
installer une instance complète de CozyCloud. Toutes les fonctionnalités ne
sont pas présentes, car soit elles ne sont pas implémentées pour le moment (par
exemple, l'envoi d'alertes par emails), soit elles n'ont pas d'équivalents (par
exemple, les notifications dans le dashboard cozy). Mais tout le reste est là,
et c'est une manière simple et rapide d'utiliser Kresus. Un contributeur,
[Nicolas](https://twitter.com/_nikaro), a même écrit un [excellent
tutoriel](https://www.karolak.fr/blog/2016/03/18/kresus-un-gestionnaire-web-de-finances-personnelles/)
pour ce mode d'installation ! Merci à lui.

## Des précautions

A savoir : dans la version autonome (ou *standalone*) de Kresus, il n'y a
aucune couche d'authentification incluse par défaut, vous devez donc l'ajouter
vous-même pour protéger votre accès à Kresus (sinon tous les gens qui
connaissent l'URL de votre Kresus pourront lire vos comptes !). Aussi, aucune
donnée n'est chiffrée dans la version autonome (pas même le mot de passe), donc
isolez et protégez correctement votre instance.

## Nouveau : une image Docker pour Kresus et Weboob

J'ai rajouté récemment, et notablement mis à jour hier soir une [image
Docker](https://framagit.org/bnjbvr/kresus/blob/master/Dockerfile) qui contient
une version récente de Weboob et lance un Kresus autonome, exposant vers
l'extérieur son port d'écoute (9876 par défaut) et un volume de données. Ce qui
veut dire que vous pouvez maintenant lancer kresus ou weboob en quelques
commandes :

- D'abord, récupérer le dépôt :

    `git clone https://framagit.org/bnjbvr/kresus && cd kresus`

- Une première fois, créer l'image :

    `docker build -t kresus .`

- Puis ensuite, autant de fois que vous le voulez, vous pouvez instancier
  l'image créée :

    `docker run -p 9876:9876 -v /home/moi/kresus-data:/usr/data -ti -d kresus --name kresus`

- Si vous désirez exposer Kresus sur le web, pensez bien à suivre le tutoriel
  de Nicolas pour rajouter une couche d'authentification et un serveur web
  proxy.

Suite à ça, vous pouvez ouvrir un navigateur sur `http://localhost:9876` et
jouer avec Kresus. Par ailleurs, le répertoire `/home/moi/kresus-data`
contiendra les données, dans cet exemple (et vous pouvez donc supprimer
l'image Docker sans perdre vos données). C'est aussi simple que ça !

Si vous voulez jouer avec les applications de Weboob, il suffit d'ouvrir un
terminal dans le docker qui fait tourner Kresus :

- `docker exec -ti kresus /bin/bash`
- Puis dans le bash ouvert : `boobank --help`

## Des idées de modifications pour la suite

Si vous êtes intéressés pour contribuer à Kresus et notamment à cette nouvelle
image Docker, voici quelques idées :

- rajouter un `cron` qui mette à jour Weboob régulièrement.
- mettre en place les *bonnes pratiques* Docker dans ce Dockerfile.
- mettre en place un serveur frontal `nginx` (ou un lien possible) avec un mot
  de passe défini par une variable d'environnement défini au moment de `docker
  run` (ou quelque autre solution qui permettrait de rajouter une
  authentification facilement).

## Le mot de la fin !

Comme d'habitude, si vous avez des remarques ou suggestions,
n'hésitez-pas à me le faire savoir, sur [irc](https://kiwiirc.com/client/chat.freenode.net/kresus), par
[twitter](https://twitter.com/bnjbvr/), sur [diaspora](https://framasphere.org/people/315a5640ead10132c4cc2a0000053625) ou sur le
[forum](https://forum.cozy.io/t/app-kresus/224) de cozy !
