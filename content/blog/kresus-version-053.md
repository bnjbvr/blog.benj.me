Title: Kresus : version 0.5.3
Date: 2015-09-01 12:16
Author: Benjamin Bouvier
Lang: fr
Tags: kresus, cozycloud
Slug: kresus-version-0-5-3

Je viens de publier une nouvelle version de
[Kresus](https://github.com/bnjbvr/kresus/), le gestionnaire de finances
personnelles open-source sur lequel je travaille. Pour rappel, cette
application est disponible dans [CozyCloud](https://cozy.io/en/) et vous
permet de vous connecter à votre compte bancaire, récupérer vos
opérations et les classifier pour savoir où votre argent passe.

#### Action requise {#actionrequise}

Une action est requise de votre part, suite à cette mise à jour, **si la
synchronisation ne marche plus**, ou si votre balance ne correspond pas
à celle indiquée par votre site de banque :

-   Aller dans Préférences.
-   Aller dans l'onglet Gestion de Weboob.
-   Cliquer sur le bouton pour mettre à jour Weboob.
-   Aller dans l'onglet Comptes bancaires.
-   Cliquer sur le bouton de synchronisation des comptes (flèches
    imbriquées).
-   Vérifier et traiter les doublons, dans l'onglet correspondant.

#### Nouveautés {#nouveauts}

-   Merci [@ZeHiro](https://github.com/ZeHiro/): Import des types
    d'opérations bancaires en base (est-ce que l'opération est une carte
    bleue, un chèque, un virement, etc.). Pas encore d'affichage, mais
    c'est [pour bientôt](https://github.com/bnjbvr/kresus/pull/175).
-   Merci @ZeHiro: quand une opération est associée à un fichier, le nom
    et le type du fichier joint sont correctement associés.
-   Merci @ZeHiro: la balance de chaque compte est maintenant affichée
    dans le menu de sélection des comptes.
-   Merci [@cylwin](https://github.com/cylwin/): l'IBAN est maintenant
    importé avec chaque compte. Cela n'est pas encore visible dans
    l'interface, mais j'ai quelques idées pour rendre cette information
    utile.
-   Merci [@nicofrand](https://github.com/nicofrand/) pour quelques
    accents manquants dans la traduction française.
-   Ajout d'un bouton pour mettre à jour Weboob, sans avoir à le
    réinstaller entièrement, ce qui permet des mises à jour plus
    rapides.
-   Ajout de fonctionnalités d'import / export d'une instance Kresus
    (c'est-à-dire toutes les banques, tous les comptes, toutes les
    opérations, toutes les catégories, etc.). Notez que le mot de passe
    n'est pas inclus dans l'export, pour des raisons évidentes de
    sécurité, et qu'il sera donc nécessaire de le remettre à la main
    dans l'onglet préférences après un import.
-   Affichage d'un message d'erreur explicite si le mot de passe est
    incorrect, lors d'une synchronisation manuelle.
-   Kresus peut maintenant [s'installer et être lancé en dehors de
    CozyCloud](https://github.com/bnjbvr/kresus/#on-debian), sans aucune
    dépendence à Cozy. Pour le moment, c'est très instable et pas
    recommandé : il n'y a aucune protection par mot de passe, beaucoup
    de risques de sécurité, des fonctionnalités sont manquantes (pas de
    notifications, pas d'emails d'alertes, etc.). Je reviendrai plus en
    détail dessus quand la version standalone sera prête.
-   Fusion des comptes similaires : lorsque une banque change son site,
    il se peut que les comptes ne soient plus identifiés de la même
    manière ; Kresus est maintenant capable de s'en rendre compte et
    d'effectuer la maintenance nécessaire.
-   Le fichier
    [README](https://github.com/bnjbvr/kresus/blob/master/README.md) a
    été grandement amélioré et un code de conduite générique a été
    ajouté au projet.
-   Beaucoup d'améliorations de code interne (refactoring), patches pour
    des petits bugs (notamment le tri hasardeux des opérations devrait
    être réglé), le processus de développement a été grandement
    simplifié également.

#### Le mot de la fin {#lemotdelafin}

Comme d'habitude, si vous avez des remarques ou suggestions,
n'hésitez-pas à me le faire savoir, par
[twitter](https://twitter.com/bnjbvr/) ou sur le
[forum](https://forum.cozy.io/t/app-kresus/224) de cozy !

