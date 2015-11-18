Title: Kresus: version 0.6.0
Date: 2015-11-16 10:07
Author: Benjamin Bouvier
Lang: fr
Tags: kresus, cozycloud
Slug: kresus-version-0-6-0

Je viens de publier une nouvelle version de
[Kresus](https://github.com/bnjbvr/kresus/), le gestionnaire de finances
personnelles open-source sur lequel je travaille. Pour rappel, cette
application est disponible dans [CozyCloud](https://cozy.io/en/) et vous
permet de vous connecter à votre compte bancaire, récupérer vos
opérations et les classifier pour savoir où votre argent passe.

#### Les gros changements de cette version {#lesgroschangementsdecetteversion}

-   Support des banques ING et HSBC (merci **nicofrand** !).
-   Libellés personnalisés : dans la liste des opérations, il est
    possible de renommer une opération en cliquant sur son libellé, en
    ajoutant des informations personnalisées dessus. Ce libellé
    personnalisé est également pris en compte dans la recherche par
    mots-clés (merci **ZeHiro** !).
-   Notifications par email : Il est maintenant possible d'envoyer des
    notifications si le solde d'un compte dépasse ou est en dessous d'un
    seuil donné; ou si une nouvelle opération dépasse un certain seuil.
    Il est également possible d'envoyer des rapports quotidiens,
    hebdomadaires ou mensuels, qui contiennent les nouvelles opérations
    importées durant la période. Plus à venir dans les prochaines
    versions.

![]({filename}/images/kresus-060.png)

#### Tous les changements de cette version {#tousleschangementsdecetteversion}

Merci à tous les contributeurs de cette version, que ce soit en patches
ou en rapports d'erreurs !

-   **ZeHiro**:
    -   Meilleure détection des doublons (moins de faux positifs).
    -   Le tri des opérations / catégories etc. est maintenant conscient
        de la *locale* utilisée (les accents sont pris en compte, etc.).
    -   Support des libellés personnalisés (voir ci-dessus).
-   **nicofrand**:
    -   Support des champs personnalisés pour l'identification sur
        certaines banques en ligne. Certaines banques demandent la
        réponse à une question personnalisée ou la date de naissance,
        pour pouvoir s'identifier, en plus du login et du mot de passe.
        Cette contribution apporte les bases nécessaires pour supporter
        ces champs supplémentaires. En pratique, cela veut dire qu'ING
        et HSBC sont maintenant supportés par Kresus !
    -   Le bouton "vider" dans la fenêtre de recherche est maintenant en
        orange, pour alerter l'utilisateur.
    -   Ajout d'un bouton "vider et fermer" dans cette même fenêtre,
        afin de bien distinguer les deux actions : "vider" efface les
        champs du formulaire, "vider et fermer" ferme le formulaire de
        recherche.
-   **babolivier**:
    -   Vérification de la présence de `virtualenv` lors de
        l'installation de Weboob, avec fallback sur `virtualenv2` s'il
        est présent.
-   **dattaz**:
    -   Ajout de `npm` comme dépendance à l'installation Debian
        standalone
-   **padenot**:
    -   Amélioration d'une traduction de chaîne en anglais
-   **rlustin**:
    -   Suppression des espaces en fin de ligne

Et les autres ajouts et modifications dans Kresus :

-   Implémentation des rapports par emails et des alertes par email
    (voir ci-dessus).
-   Possibilité de rechercher les libellés personnalisés, lors d'une
    recherche par mots-clés.
-   Les imports d'instance évitent maintenant de réimporter les données
    internes à Kresus et les catégories si elles sont déjà présentes, ce
    qui évite des bugs par la suite.
-   Kresus est capable de détecter si Weboob est installé de manière
    globale et l'utiliser de préférence, plutôt que télécharger et
    l'installer localement, si c'est possible.
-   Le démarrage de l'application est plus séquentiel, ce qui évite des
    ralentissements au lancement (notamment pour la version standalone)
    et implique une meilleure cohérence des données.
-   Réécriture complète du serveur, pour passer de CoffeeScript à
    ECMAScript 6. Le code est maintenant moderne, propre, plus facile à
    comprendre et n'utilise plus que JavaScript, de partout ! Cela va
    grandement faciliter les mises à jour du serveur.
-   Comme d'habitude, beaucoup de bugs mineurs ont été écrasés et de
    plus petits nettoyages dans le code ont eu lieu.

#### Les prochains chantiers {#lesprochainschantiers}

Les prochains chantiers sont les choses sur lesquelles j'aimerais me
pencher pour la (les ?) prochaines versions. Bien sûr, toute
contribution sur ces sujets est plus qu'encouragée et ce sera avec
plaisir que je vous aiderai à parcourir et comprendre le code. Cela
inclut, mais ne se limite pas à :

-   Une réécriture partielle du code client, pour qu'il soit moins dense
    (certains fichiers font plus de 1,000 lignes !) et plus
    compartementalisé.
-   Une meilleure gestion des erreurs affichées à l'utilisateur, pour
    qu'elles soient plus faciles à comprendre et à gérer, donc plus
    utiles.
-   Une manière de marquer des paires d'opérations comme n'étant PAS des
    doublons, de dé-fusionner des doublons, ainsi qu'une détection
    automatique intelligente de la plupart des doublons.
-   Une catégorisation automatique des opérations (enfin !).

#### Le mot de la fin {#lemotdelafin}

Comme d'habitude, si vous avez des remarques ou suggestions, n'hésitez
pas à me le faire savoir, par [twitter](https://twitter.com/bnjbvr/) ou
sur le [forum](https://forum.cozy.io/t/app-kresus/224) de cozy !
