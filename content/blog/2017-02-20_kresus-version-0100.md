Title: Kresus: version 0.10.0
Date: 2017-02-20 11:00
Author: Benjamin Bouvier
Lang: fr
Tags: kresus, cozycloud
Slug: kresus-version-0-10-0

L'équipe de Kresus vient de publier une nouvelle version de
[Kresus](https://framagit.org/bnjbvr/kresus/), un gestionnaire libre de
finances personnelles sur lequel je travaille. Pour rappel, cette application
web, basée sur [Weboob](http://weboob.org/) et disponible [de manière
autonome](https://www.karolak.fr/blog/2016/03/18/kresus-un-gestionnaire-web-de-finances-personnelles-libre)
ou dans [CozyCloud](https://cozy.io/), vous permet de vous connecter à votre
compte bancaire, de récupérer vos opérations et de les classifier pour savoir
comment vous dépensez votre argent afin de mieux maîtriser vos finances.

## En résumé

Cette nouvelle version apporte de nombreuses améliorations de l'interface
utilisateur et met à niveau la version autonome (en dehors de Cozy) en termes
de fonctionnalités. Merci aux 3 contributeurs de cette nouvelle version, et
aux [80
commits](https://framagit.org/bnjbvr/kresus/compare/bf048fca9687f139d1a1d670bec0b5ac138448ce...906ffac4d341b4e08bfda9bebe68cf86d1cd29c6)
effectués, pour un total de 151 fichiers modifiés, avec 2080 ajouts et 1406
suppressions de lignes de code !

### Nouvelles banques

Kresus s'appuie sur les épaules du logiciel libre [Weboob](http://weboob.org/)
pour récupérer les données bancaires. Nous avons donc ajouté le support pour
les nouvelles entités que Weboob supporte désormais : la banque *Nuger* (groupe
*Crédit du Nord*) et l'assurance vie *Spirica* (groupe *Crédit Agricole*).

### Version autonome

Suite aux [récentes
décisions](https://blog.cozycloud.cc/post/2016/11/21/En-route-vers-Cozy-version-3?lang=fr)
de l'équipe CozyCloud, et aux changements techniques qui en résultent, cette
version de Kresus pourrait être la dernière à fonctionner avec Cozy. Cependant,
rien de grave ! D'une part, Kresus continuera de fonctionner tant que la mise à
jour vers la version 3 de Cozy n'aura pas eu lieu. D'autre part, nous mettons
tout en œuvre pour que la version autonome de Kresus, c'est-à-dire celle qui
peut se lancer sans Cozy, soit la plus simple à installer et la plus
fonctionnelle possible, afin que la transition soit très simple.  Par ailleurs,
nous cherchons de l'aide pour [empaqueter
Kresus](https://framagit.org/bnjbvr/kresus/issues/515) dans YunoHost, à bon
entendeur :-)

Pour cela, voici quelques améliorations apportées dans cette version :

* Il est désormais possible de changer la langue d'utilisation de Kresus dans
  la version autonome, au grand bonheur des francophones, puisque la langue par
  défaut était celle de Shakespeare.
* Il est désormais possible de configurer un relais SMTP, afin que Kresus
  puisse envoyer des emails. Les utilisateurs de la version autonome pourront
  désormais profiter des alertes et des rapports emails ! Pour cela, allez dans
  la section des Préférences, puis Alertes, et dépliez le petit panneau de
  "Configuration" pour régler les paramètres du relais SMTP.
* Le fichier README (Lisez-moi, pour les puristes) a été partiellement revu et
  mis à jour, pour correspondre plus précisément au processus d'installation.
  Installer Kresus en mode autonome est aussi simple qu'installer Weboob et
  exécuter `npm install -g kresus` en ligne de commande !

### Amélioration de l'interface utilisateur et de l'expérience utilisateur

* Désormais, tous les comptes sont affichés depuis le menu, ainsi que le solde
  total des comptes associés à la banque en question, le tout dans une
  interface plus légère et plus simple.
* Les graphiques ont également subi un coup de peinture,  notamment les
  graphiques qui représentent des données sur de longues périodes, pour
  lesquels les labels ne se chevaucheront désormais plus. La sélection des
  types d'entrées (crédits, débits, ou les deux) pour le graphique par
  catégorie a également été simplifiée. Vous pouvez désormais sélectionner le
  graphique à afficher par défaut, en utilisant le menu de préférences intégré.
* La section des paramètres a été simplifiée, et les paramètres par défaut sont
  désormais accessibles depuis les sections qui les concernent. Toujours dans
  les paramètres, les IBANs sont désormais affichés plus proprement.
* La saisie des montants, lors de recherches, dans les budgets ou lors d'un
  ajout manuel d'opérations, a également été revue, puisqu'une icône de signe
  accompagne désormais les montants entrés par l'utilisateur.
* C'est bientôt le printemps, et la liste des opérations commence déjà à
  rayonner de couleurs ! En effet, chaque opération assignée à une catégorie
  revêtira la couleur associée à cette catégorie.
* Dans la section *Doublons*, vous pouvez désormais vérifier le libellé
  personnalisé d'une opération, en plus de son libellé bancaire, en survolant
  l'icône *?* afin de vous ôter tout doute.
* Dans la section *Budget*, les seuils négatifs sont désormais possibles et
  deux nouvelles possibilités d'affichage font leur apparition : la vue en
  pourcentages et le fait de pouvoir cacher les catégories sans seuils.
* La synchronisation des comptes d'une banque envoie beaucoup moins de données
  sur le réseau et est plus fluide à l'affichage.

### Mobile

Plusieurs améliorations ont été apportées pour rendre l'application plus accessible sur mobile :

* Le défilement vertical est désormais utilisable dans le menu.
* Les marges et espaces vides entre les différents blocs ont été réduits et
  optimisés.
* L'affichage du solde, des dépenses, revenus et balance est réorganisé sous
  forme de damier au lieu de quatre lignes.
* Des menus déroulants sont utilisés pour les sous-menus des sections
  paramètres et graphiques au lieu des menus hamburgers.
* Les champs du formulaire de recherche ont été réagencés pour être plus
  lisibles.

### Nouvelles fonctionnalités

* Pour les utilisateurs de Cozy, une notification est émise par compte
  bancaire, et non plus par accès à une banque. Lorsqu'une seule opération a
  été importée, son montant est directement affiché dans la notification.
* Il arrive que les informations liées aux comptes bancaires changent au cours
  du temps (par exemple, le libellé d'un compte peut changer), impliquant des
  problèmes de doublons au sein de Kresus. Désormais, un algorithme efficace de
  détection de comptes en double a été implémenté, et les comptes ne devraient
  plus être mélangés. Le prochain chantier sur le sujet concerne une meilleure
  détection automatique des opérations en double.
* La gestion de Weboob a été améliorée : les erreurs sont désormais mieux
  indiquées, mieux gérées et plus explicites. Les mises à jours des modules
  sont également plus robustes.

### Le mot de la fin

Merci à tous les contributeurs, et en particulier aux hyperactifs
[nicofrand](https://nicofrand.eu) et [ZeHiro](https://github.com/ZeHiro) pour
avoir participé à l'écriture de ce billet et pour leurs très nombreuses
contributions !

Comme d'habitude, si vous avez des remarques ou suggestions, n'hésitez-pas à
nous le faire savoir, par [twitter](https://twitter.com/kresusapp), le [canal
IRC](https://kiwiirc.com/client/chat.freenode.net/kresus), la [liste de
diffusion](https://framalistes.org/sympa/info/kresus), ou encore
[diaspora](https://framasphere.org/people/315a5640ead10132c4cc2a0000053625)  !
