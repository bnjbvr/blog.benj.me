Title: Kresus: version 0.9.0
Date: 2016-10-31 18:30
Author: Benjamin Bouvier
Lang: fr
Tags: kresus
Slug: kresus-version-0-9-0

L'équipe de Kresus vient de publier une nouvelle version de
[Kresus](https://framagit.org/bnjbvr/kresus/), un gestionnaire de finances
personnelles open-source sur lequel je travaille. Pour rappel, cette
application, basée sur [Weboob](http://weboob.org/), est disponible dans
[CozyCloud](https://cozy.io/en/) ou
[en dehors](https://www.karolak.fr/blog/2016/03/18/kresus-un-gestionnaire-web-de-finances-personnelles/)
et vous permet de vous connecter à votre compte bancaire, récupérer vos
opérations et les classifier pour savoir où votre argent passe.

### Kresus Utilise Des Nouveaux Moyens De Communication, Son Facteur Le Déteste, Découvrez Son Secret

Kresus prend son envol et a désormais un
[site web officiel](https://kresus.org) avec une section Foire Aux Questions en
construction ! Des nouveaux moyens de communication ont également été mis en
place : en plus du classique [canal
IRC](https://kiwiirc.com/client/chat.freenode.net/kresus) déjà existant, une
[liste de diffusion](https://framalistes.org/sympa/info/kresus) a été ouverte
pour les annonces de mises à jour, mais aussi pour faciliter le support à
toutes les étapes, lors de l'installation ou de l'utilisation quotidienne de
Kresus. N'hésitez-pas à vous
[inscrire](https://framalistes.org/sympa/subscribe/kresus) ! Pour des
interactions plus courtes et pour rester au courant des nouveautés, un
[compte twitter](https://twitter.com/kresusapp) a également été ouvert,
n'hésitez-pas à nous envoyer des remarques courtes ou vos messages d'amour, ça
fait toujours plaisir ;-)

### Les nouveautés de cette version

Un grand merci aux 4 contributeurs de cette nouvelle version, pour un total de 62 commits !

#### Nouvelles banques

De nombreux nouveaux modules bancaires ont été intégrés dans Kresus :

* Amundi
* AFER
* Banque de Savoie
* Crédit agricole Épargne Longue des Salariés
* Crédit du nord Plan Épargne Entreprise
* Number26
* Yomoni

#### Budget

Vous pouvez désormais évaluer vos dépenses pour un compte donné, catégorie par
catégorie, et savoir si vous avez dépassé le budget alloué à une catégorie pour
le mois ou combien il vous reste à dépenser.  Il suffit pour ça d'affecter dans
la nouvelle section "Budget" un budget à chaque catégorie et le calcul se fera
automatiquement. Pour vérifier vos transactions des mois précédents, modifiez
la période souhaitée.  Pour accéder rapidement aux transactions affectées à une
catégorie pour la période sélectionnée, cliquez sur l'icône "Recherche".

#### Interface et expérience utilisateur
* La section "Catégories" a été revue pour une utilisation plus simple et
  rapide : vous pouvez désormais directement modifier le titre d'une catégorie
  sans cliquer sur le bouton "Éditer".
* La section "À propos" située jusqu'ici dans la section "Préférences" a été
  déplacée dans le menu, tout en bas. Par défaut repliée, cliquez sur la ligne
  tout en bas du menu pour ouvrir cette section et accéder aux raccourcis vers
  le site web de Kresus, la license, le code source ou encore le blog.
* Lorsque vous ajoutez Kresus à l'écran d'accueil de votre smartphone, celui-ci
  est détecté comme une application web et la barre de navigation du navigateur
  est automatiquement cachée afin de gagner de l'espace (si votre navigateur le
  supporte).
* L'affichage des détails d'une opération se fait dans une modale sur un
  navigateur de bureau.
* Les types d'opérations sont désormais triés dans l'ordre alphabétique.
* Lorsque vous demandez à effectuer une opération qui prend du temps (comme
  importer un nouveau compte), des écrans d'attente vous sont désormais
  affichés, vous prévenant qu'il est normal que l'opération prenne un peu de
  temps. Un des plus gros problèmes d'expérience utilisateur (et un des plus
  vieux trolls du canal IRC de CozyCloud) est ainsi réglé !
* Il est désormais possible de naviguer au clavier dans la liste des opérations
  afin de modifier le type, l'intitulé ou la catégorie. Pour déplier le menu
  déroulant, il suffit d'appuyer sur la touche espace de votre clavier et de
  sélectionner le bon type/catégorie avec les flèches et valider par la touche
  entrée.
* Dans la section "Doublons", il est désormais possible de trouver facilement
  plus de doublons en cliquant sur les boutons "En trouver plus/moins".

#### Accès multiples à une même banque
Kresus ne savait auparavant pas gérer le fait d'avoir plusieurs comptes avec
plusieurs logins / mots de passe dans une même banque (par exemple si vous et
votre compagnon.ne êtes tous les deux dans la même banque). C'est désormais un
problème du passé et réglé dans cette version !

#### Forcer la resynchronisation du solde
Si vous observez un écart entre le solde sur le site de votre banque et dans
Kresus, et que vous avez essayé toutes les solutions suivantes pour que le
montant affiché dans Kresus corresponde au montant affiché par la banque :
    - Détecter les doublons et les fusionner.
    - Supprimer une opération qui serait dans Kresus mais pas sur le site de
      votre banque.
    - Ajouter manuellement une opération présente sur le site de votre banque
      mais pas dans Kresus.

Il existe une nouvelle solution (de dernier recours) qui consiste à
resynchroniser purement et simplement le montant donné par Kresus avec celui
indiqué par votre banque.  Dans les paramètres > Comptes bancaires, sur la
ligne du compte à synchroniser, une nouvelle icône (roue crantée) a fait son
apparition ; en cliquant dessus, vous pourrez automatiquement resynchroniser le
solde de votre compte.

#### Le point sysadmin / devops
* Si vous avez installé Kresus depuis la version précédente, vous avez
  probablement dû installer Weboob de manière globale sur votre machine. Comme
  c'était une pratique controversée d'un point de vue administration de
  système, il est maintenant possible d'installer Weboob de manière locale (par
  exemple dans un `virtualenv`), tout en indiquant à Kresus où se trouve cette
  installation locale, à l'aide de la variable d'environnement
  `KRESUS_WEBOOB_DIR` à définir au moment du lancement du serveur :

    ```
        $ KRESUS_WEBOOB_DIR=/code/weboob ./bin/kresus
    ```

    Merci [@nledez](https://github.com/nledez) pour cette contribution !

* Pour éviter des erreurs lorsque la récupération de vos opérations est trop
  longue (notamment en cas de nombreuses transactions à récupérer), le temps
  d'attente du retour (et traitement) des modules Weboob a été augmenté à 5
  secondes. Pour les utilisateurs de cozy, il vous faudra cependant également
  augmenter le timeout de `cozy-proxy`.

#### Maintenance

* Presque chaque version de Kresus arrive avec sa réécriture ; cette fois-ci,
  c'est presque tout le client qui a été réarrangé à l'aide du framework Redux,
  afin d'éviter la duplication d'état et les inconsistances graphiques dans
  l'interface.
* Diverses améliorations ont été apportées afin de faciliter le développement :
  des [tests unitaires](http://gph.is/2eH1UlU), des vérifications de cohérence
  au moment de la construction binaire, etc.

### Le mot de la fin

Merci à tous les contributeurs, et en particulier aux hyperactifs
[nicofrand](https://nicofrand.eu) et [ZeHiro](https://github.com/ZeHiro) pour
avoir participé à l'écriture de ce billet et pour leurs très nombreuses
contributions !

Comme d'habitude, si vous avez des remarques ou suggestions,
n'hésitez-pas à nous le faire savoir, par
[twitter](https://twitter.com/kresusapp), le
[canal IRC](https://kiwiirc.com/client/chat.freenode.net/kresus),
la [liste de diffusion](https://framalistes.org/sympa/info/kresus),
[diaspora](https://framasphere.org/people/315a5640ead10132c4cc2a0000053625) ou
encore sur le [forum](https://forum.cozy.io/t/app-kresus/224) de cozy !
