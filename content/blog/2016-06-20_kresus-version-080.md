Title: Kresus: version 0.8.0
Date: 2016-06-21 11:00
Author: Benjamin Bouvier
Lang: fr
Tags: kresus, cozycloud
Slug: kresus-version-0-8-0

Je viens de publier une nouvelle version de
[Kresus](https://github.com/bnjbvr/kresus/), le gestionnaire de finances
personnelles open-source sur lequel je travaille. Pour rappel, cette
application, basée sur [Weboob](http://weboob.org/), est disponible dans
[CozyCloud](https://cozy.io/en/) et vous permet de vous connecter à votre
compte bancaire, récupérer vos opérations et les classifier pour savoir où
votre argent passe.

### Action requise pour les auto-hébergés : installation de Weboob

Avant de passer à la liste détaillée des changements, il y a une procédure de
migration qui nécessitera une action de votre part, si vous êtes auto-hébergés
(c'est-à-dire si vous n'utilisez **pas** d'instance bêta sur l'infrastructure
de CozyCloud). Si vous êtes utilisateur de l'infrastructure de CozyCloud, le
changement devrait avoir été effectué par l'équipe des administrateurs systèmes
de Cozy, et vous pouvez passer à la partie suivante.

Si vous êtes auto-hébergés, il vous faudra [installer
Weboob](http://weboob.org/install) par vos propres moyens et vous assurer que
l'utilisateur qui lance le processus de Kresus ait accès à Weboob. J'ai
personnellement effectué une installation globale. Je **recommande d'installer
la version 1.1 ou supérieure** de Weboob, pour être certain que les modules des
sites ne soient pas dépassés.

Auparavant, Weboob, le système qui se connecte à votre banque pour récupérer la
liste des comptes et opérations, était installé par Kresus et cela nécessitait
des dépendences externes. Il a été décidé que Weboob devait désormais être
installé au préalable par l'administrateur système : Kresus n'essaiera plus de
l'installer. Cela simplifie beaucoup de choses, notamment en facilitant
l'installation.

### La version courte

Pour cette version, beaucoup de changements peu visibles pour l'utilisateur :
c'est beaucoup de nettoyage et de changements structurels dans le code
(séparation du code client en composants logiques et lint complet), qui
devraient faciliter la maintenance et l'amélioration du code par le futur.
Aussi, beaucoup de problèmes relatifs à la détection des doublons et à la
synchronisation automatique des comptes ont été réglés.

Un changement visible et notable : la liste des opérations est désormais
[beaucoup plus fluide](https://twitter.com/bnjbvr/status/730309653943492612)
lors du scroll, même si vous avez des tonnes d'opérations.

### En cas de problèmes de montants

Si vous rencontrez des problèmes de synchronisation entre Kresus et votre
banque, par exemple si Kresus affiche des soldes de comptes qui ne
correspondent pas aux montants indiqués sur le site de votre banque, il est
conseillé de vérifier les doublons dans la section correspondante et d'essayer
de les fusionner à la main.

Si malgré la détection de doublons, vous avez encore des problèmes de montant,
laissez un message sur le [fil associé](https://forum.cozy.io/t/app-kresus/224)
sur le forum de Cozy ! J'aimerais expérimenter des méthodes plus agressives de
détection automatique de doublons, et cela nécessite de savoir quelles sont les
situations qui posent fréquemment problème.

### Les contributions en détail

Un grand merci aux 7 contributeurs de cette nouvelle version, pour un total de
96 commits !

- [@AwYiss](https://github.com/AwYiss), qui avait déjà grandement amélioré
  l'interface utilisateur, a frappé de nouveau, en intégrant les préférences au
  niveau design, rendant cette partie plus consistente avec le reste de
  l'application et très élégante.
- [@nicofrand](https://github.com/nicofrand) a corrigé des soucis de style
  (CSS) lors de l'ajout manuel d'opération.
- [Bezleputh](https://www.openhub.net/accounts/Bezleputh) (de la communauté
  Weboob) a corrigé un bogue qui empêchait l'import d'opérations, si celles-ci
  présentaient des informations manquantes.
- [@brouberol](https://github.com/brouberol) a ajouté un Dockerfile (ou
  [RecetteÀMarcel](https://github.com/brouberol/marcel) pour les puristes de l'OS
  souverain) afin de pouvoir tester Kresus rapidement en production. J'espère
  pouvoir écrire un peu plus sur le sujet bientôt.
- [@PandiPanda69](https://github.com/PandiPanda69) a effectué une revue du code
  avec la sécurité à l'esprit :
    - Correction de bogue : lors de l'import d'une instance, si le fichier JSON
      contient des erreurs de syntaxe, ne pas essayer de l'importer.
    - Ajout de la possibilité de chiffrer l'export de son instance Kresus et
      d'importer une instance chiffrée de Kresus. Avec cette nouvelle méthode
      d'import, le mot de passe peut être inclus dans le fichier exporté, en
      toute sécurité ! (cette fonctionnalité n'est pas encore activée car elle
      nécessite une réflexion et des tests approfondis ainsi qu'une
      implémentation côté interface)
- [@ZeHiro](https://github.com/ZeHiro):
    - Amélioration sensible des traductions : les notifications et textes des
      emails sont désormais traduits en français ou en anglais, selon la langue
      choisie dans votre Cozy !
    - Utilisation de la vraie monnaie du compte, avec le symbole monétaire
      associé, dans toute l'interface utilisateur.
    - Amélioration de la détection manuelle des doublons (deux opérations sont
      considérées comme des doublons seulement si leurs types sont identiques).
    - Suppression de faux positifs dans la détection automatique des doublons
      (deux opérations avec la même date, le même montant et le même libellé).
    - Si votre mot de passe expire, Kresus vous enverra désormais un mail une
      et une seule fois pour vous le signaler, et n'importera plus d'opérations
      automatiquement jusqu'à la mise à jour du mot de passe (le même comportement
      est prévu si le mot de passe devient erroné, s'il n'est pas mis à jour dans
      Kresus)
- De manière notable, ZeHiro et moi-même avons contribué ensemble à des
  fonctionnalités majeures :
    - Grâce à une implémentation de *l'infinite scrolling* dans la
      liste des opérations, celle-ci est bien plus fluide à s'afficher, même si
      vous avez beaucoup d'opérations !
    - Découpage du code en modules logiques et refactoring pour que le code
      client passe le lint (validation statique du style du code). Ce n'est pas
      visible pour l'utilisateur, mais ça aide grandement les développeurs en
      leur évitant de se poser plein de questions futiles sur le style du code.
- [votre serviteur](https://github.com/bnjbvr):
    - utilisation de Weboob au niveau global (voir paragraphe sur la procédure
      de migration).
    - meilleure représentation des erreurs. Normalement, les erreurs devraient
      être plus claires à comprendre, côté client comme ou dans les logs côté
      serveur, grâce à une meilleure cohérence et à des logs plus détaillés et
      facultatifs. Un mode de debugging pour Weboob a été également rajouté, ce
      qui est très utile en cas de problèmes de synchronisation avec votre
      banque, pour remonter des logs aux développeurs de Weboob !
    - la récupération automatique des opérations ne s'arrête plus en cas
      d'échec. Si les opérations n'étaient plus récupérées automatiquement
      toutes les nuits chez vous, c'était peut-être à cause de ce bug.
    - les graphiques des opérations en valeurs négatives pointent désormais
      vers le haut et non plus vers le bas.

Si vous voulez voir encore plus de détails, les 96 (!) commits sont présentés [par
là](https://github.com/bnjbvr/kresus/compare/19312b5c081404eda3d1d23bea410cfb04b103da...6fb93ab3a45ccbb3afcd8ccc62b737fe63c4d395).

### Le mot de la fin

Comme d'habitude, si vous avez des remarques ou suggestions,
n'hésitez-pas à me le faire savoir, par
[twitter](https://twitter.com/bnjbvr/) ou sur le
[forum](https://forum.cozy.io/t/app-kresus/224) de cozy !

