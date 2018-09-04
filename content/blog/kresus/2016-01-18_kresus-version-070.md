Title: Kresus: version 0.7.0
Date: 2016-01-18 23:59
Author: Benjamin Bouvier
Lang: fr
Tags: kresus
Slug: kresus-version-0-7-0

Je viens de publier une nouvelle version de
[Kresus](https://github.com/bnjbvr/kresus/), le gestionnaire de finances
personnelles open-source sur lequel je travaille. Pour rappel, cette
application, basée sur [Weboob](http://weboob.org/), est disponible dans
[CozyCloud](https://cozy.io/en/) et vous permet de vous connecter à votre
compte bancaire, récupérer vos opérations et les classifier pour savoir où
votre argent passe.

### La version courte

- Coup de pinceau magistral sur l'interface, merci @AwYiss !
- Support de nouvelles banques, merci @ZeHiro !
- Possibilité de sélectionner un compte par défaut, merci @nicofrand !
- Réparation du lien entre factures et opérations bancaires, merci @ZeHiro !
- Couleurs associées aux catégories, merci @nicofrand !
- Réparation du module HelloBank.
- Mise à jour automatique quotidienne de Weboob.
- L'installation sera désormais plus rapide (l'application est précompilée par
  les développeurs, et non plus compilée au moment de l'installation).

### Les contributions en détail

Un grand merci à tous les contributeurs qui ont été hyperactifs ce mois-ci !

- [@AwYiss](https://github.com/AwYiss) a personnalisé et donné un coup de jeune
  à toute l'interface ! Notamment, l'interface est maintenant utilisable sur
  mobile. Merci @AwYiss!
- [@nicofrand](https://github.com/nicofrand) a été prolifique :
    - Il y a désormais un bouton "fermer" et un bouton "vider et fermer" dans
      la fenêtre de recherche des opérations, qui explicitent mieux les
      intentions.
    - Il est maintenant possible d'éditer les champs personnalisés de connexion
      aux banques (par ex. la phrase secrète de connexion, etc.).
    - Un compte peut désormais être sélectionné comme compte par défaut, dans
      les préférences (étoile à côté des comptes). C'est ce compte-là qui
      s'affichera en premier quand vous vous connecterez à Kresus.
    - Kresus a une belle favicon, pour les versions mobiles !
    - Weboob peut être mis à jour sans qu'aucun compte ne soit présent, grâce à
      l'onglet "avancé" affiché lors de l'installation.
    - Il est désormais possible d'assigner une couleur à une catégorie. Cette
      couleur sera utilisée dans les graphiques en barre et en camembert pour
      représenter ladite catégorie.
- [@ZeHiro](https://github.com/ZeHiro) a également été très efficace :
    - Il est désormais possible de retirer un libellé personalisé d'une
      opération.
    - Il est possible de quitter le champ de libellé personalisé en pressant
      Echap.
    - Les factures liées par Konnector n'étaient pas récupérées correctement,
      c'est maintenant réparé !
    - Support de quelques nouvelles banques et intégration de toutes les
      variantes des banques, avec les icônes associées !
    - Des opérations peuvent être rajoutées à la main dans un compte. Bien que
      cela soit très utile, c'est pour le moment mal géré par la reconnaissance
      automatique des opérations, et donc à n'utiliser que si vous savez
      vraiment bien ce que vous faites.
    - Qualité du code : début de lint côté client.
- [votre serviteur](https://github.com/bnjbvr) :
    - mise à jour du module bancaire HelloBank
    - fusion automatique des comptes doublons très probables
    - mise à jour automatique des modules weboob, une fois par jour
    - possibilité de changer le login d'accès à une banque
    - amélioration de la qualité du code avec un lint côté serveur
    - meilleur affichage des erreurs côté client
    - mise à jour du système de build, des fichiers lisez-moi, etc.
    - simplification des traductions et ajout d'un script pour vérifier la
      cohérence entre les traductions.

Si vous voulez voir encore plus de détails, les commits sont présentés [par
là](https://github.com/bnjbvr/kresus/compare/2c502f6c32fc6c51b60eae17fd53453343c8e305...f42832a23826ad3f003e84840ae5af59885304a9).

### Le mot de la fin

Comme d'habitude, si vous avez des remarques ou suggestions,
n'hésitez-pas à me le faire savoir, par
[twitter](https://twitter.com/bnjbvr/) ou sur le
[forum](https://forum.cozy.io/t/app-kresus/224) de cozy !

