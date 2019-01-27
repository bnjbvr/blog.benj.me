Title: Kresus : version 0.5.1
Date: 2015-05-09 17:38
Author: Benjamin Bouvier
Lang: fr
Tags: kresus
Slug: kresus-version-0-5-1

Je viens de publier une nouvelle version de
[Kresus](https://github.com/bnjbvr/kresus), le gestionnaire de finances
personnelles open-source sur lequel je travaille. Pour rappel, cette
application est disponible uniquement dans [CozyCloud](https://cozy.io)
(pour l'instant) et vous permet de vous connecter à votre compte
bancaire, récupérer vos opérations et les classifier pour savoir où
votre argent passe.

![Graphiques]({static}/images/kresus-051.png)

Parmi les nouveautés :

-   Meilleurs graphiques : il est possible d'afficher des graphiques des
    opérations par catégories par mois, sur des périodes données (tout
    le temps, mois courant, mois précédent, 3 derniers mois, 6 derniers
    mois), pour des types d'opérations données (toutes, dépenses ou
    revenus uniquement). De plus, des graphiques en "camembert" sont
    maintenant générés si l'on regarde les dépenses ou les revenus.
-   Il est également possible de choisir quelle période et quel type
    d'opérations s'affichent par défaut (depuis les Préférences
    avancées).
-   La gestion des opérations en doublons a été améliorée : maintenant,
    c'est l'application qui choisit lequel des deux doublons il est
    nécessaire de supprimer. Ainsi, on ne parle plus de suppression de
    doublons mais de
    [FUSION](https://www.youtube.com/watch?v=JatzJYDqfAE).
-   Utilisation de Dygraph et c3 pour la partie graphiques, ce qui fait
    que Kresus ne dépend plus de Highcharts, dont la license pouvait
    poser problème au sein de CozyCloud.

Comme d'habitude, si vous avez des remarques ou suggestions,
n'hésitez-pas à me le faire savoir, par twitter ou sur le [forum de
cozy](https://forum.cozy.io/t/app-kresus/224) !
