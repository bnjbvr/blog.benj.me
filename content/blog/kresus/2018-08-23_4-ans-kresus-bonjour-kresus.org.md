Title: Quatre ans de Kresus, bonjour Kresus.org
Date: 2018-08-23 10:00
Author: Benjamin Bouvier
Lang: fr
Tags: kresus
Slug: 4-ans-de-kresus-bonjour-kresus-org

## De la volonté derrière Kresus

Il y a une dizaine d'années, alors fervent utilisateur de HomeBank, je découvre
avec stupéfaction et beaucoup d'intérêt l'application mobile de Linxo.  Ce
service permet de récupérer ses opérations bancaires depuis le site de sa
banque, de manière automatisée, tout en analysant les transactions et en
permettant de les catégoriser, afin de générer des graphes simples et clairs
pour expliquer aux utilisateur.ice.s comment évoluent leurs finances
personnelles : combien a été dépensé ou économisé tel mois ? quelles sont les
trois sources principales de dépenses au cours des six derniers mois ? J'ai
utilisé un peu cette application mobile à l'époque. Elle m'était très utile,
alors jeune étudiant, n'ayant qu'un budget limité et aucune idée de comment le
gérer.

### Si c'est gratuit, c'est quoi le produit ?

Il m'est apparu assez vite que le service étant gratuit, Linxo devait avoir une
autre source de financement que l'unique option premium qu'ils proposaient
alors. En y réfléchissant un peu, on peut trouver plusieurs possibles intérêts
pour eux. Par exemple, ce pourrait être tout simplement de pouvoir récupérer
une grande quantité de données bancaires, utilisable comme source de données
pour un algorithme de catégorisation automatique. Un tel algorithme de
catégorisation pourrait ensuite être revendu à des services tiers. De mémoire,
j'ai aussi vu une autre source de financement basée sur des publicités ciblées.
Dans ce cas, le logiciel propose d'analyser les transactions bancaires pour
permettre d'identifier des coûts récurrents, et ensuite met en avant des offres
de services similaires d'entreprises partenaires ; le revenu est ici une
commission. Par exemple, si vous avez une assurance habitation dont l'échéance
est mensuelle, le système peut le détecter et vous proposer des publicités pour
d'autres assurances habitations moins chères (mais pas forcément équivalentes
!) chez des concurrents. Dans le pire des cas, l'intérêt caché pourrait être de
revendre des informations extraites des transactions bancaires, comme la
récurrence et les noms des enseignes où nous effectuons des paiements. Au
mieux, cela est effectué de manière anonyme et n'a pas une grande incidence
personnelle. Au pire, cela révèle des détails de notre intimité, notamment si
l'information est rattachée à une personne identifée. Ces informations peuvent
être très utiles pour les assurances et les banques pour évaluer divers
risques liés à des emprunts ou des polices d'assurance. Mais des entreprises
plus classiques peuvent également en faire usage, en mettant en place des
publicités ultra-ciblées qui touchent aux aspects émotionnels.

De manière certaine, j'ai été immédiatement gêné par le fait de devoir confier
à une entreprise mes identifiants bancaires, à savoir mon login et mon mot de
passe, le sésame pour accéder au site de ma banque, attribuant parfois des
autorisations plus variées que la simple lecture seule, comme celle d'effectuer
des virements. Après cette réflexion, je me désinscris. Je cherche une
alternative libre aussi complète, car je veux être capable de vérifier dans le
code du logiciel ce qui est fait avec mes identifiants ; un
logiciel libre peut difficilement fomenter des coups fourrés. N'en trouvant
pas, je brandis ma liste de projets à long terme, aussi connue sous le nom de
liste des projets que je ne mettrai probablement jamais en place, ou encore
liste des rêves libristes. J'y ajoute une entrée : créer une alternative libre
et auto-hébergeable qui fasse la même chose que Linxo, sans trop savoir comment
m'y prendre.

## CozyCloud et son gestionnaire de finances personnelles

![Capture de cozypfm]({filename}/images/cozypfm.png)

Un peu plus tard, je découvre CozyCloud, et notamment l'application
[cozy-pfm](https://github.com/seeker89/cozy-pfm), développée par un prestaire.
C'est ce clône libre dont j'ai tant rêvé. La clé qui me manquait, c'était
l'intégration avec l'outil pour récupérer les données bancaires : ce logiciel
s'appuie sur les épaules d'un outil complet de scrapping [1] libre,
[weboob](https://weboob.org). Très vite, l'application montre ses limites : des
doublons apparaissent dans mes opérations bancaires. En effet, l'outil de
scrapping est capable de nous fournir un cliché de nos comptes bancaires à un
instant donné. Un gestionnaire de finances personnelles essaie de mettre en
place une continuité, donc de joindre les instantanés en un film à 24 images
par seconde, qui retracerait l'historique plus complet de nos comptes. Mais
parfois, ce dernier se trompe parce qu'il ne dispose pas d'assez
d'informations, ou parce que les banques changent la manière dont sont
présentées les opérations au cours du temps (et ça arrive beaucoup plus souvent
qu'on ne le croit !). Naîvement, on pourrait penser que si deux transactions
récupérées lors de différentes synchronisations ont la même date, le même
libellé et le même montant, alors ce sont des doublons. Mais les banques se
permettent de modifier au cours du temps l'une ou plusieurs de ces composantes,
rendant la tâche du gestionnaire de finances personnelles bien plus complexe.
C'est ainsi que des doublons apparaissent : ce sont des paires d'opérations qui
ont tout en commun sauf une composante qui a changé entre deux instantanés pris
sur le site de la banque.

L'autre souci de CozyPFM est que l'application a été développée sur commande,
par un prestataire qui a ensuite fini sa mission et *rendu les clés*. Une fois
la mission du consultant accomplie, l'application passe en mode maintenance, ce
qui signifie que seuls les gros bugs sont corrigés et que celle-ci ne connaît
plus de grandes nouveautés. Quand j'essaie de contribuer au code, je me heurte
à une difficulté, celle-ci technique : l'utilisation d'une technologie que je
ne comprends pas, qui m'impose beaucoup de contraintes pour essayer de
simplifier le développement, et que je n'ai pas envie de faire l'effort
d'apprendre. L'intuition a sonné juste, au vu de l'actuelle désuètude de
l'outil : il s'agissait de la bibliothèque de code JavaScript
[backbone](http://backbonejs.org/).

## Kresus, d'hier à aujourd'hui

Je m'en souviens encore précisément, c'était juste hier, le 31 juillet 2014,
que j'écris un [premier
commit](https://github.com/bnjbvr/kresus/commit/f458312356ab61f36a0a3193100f18fa436bc1c2),
parce que je n'arrive pas à démarrer le serveur  de cozy-pfm. Très vite, je
décide que si je veux pouvoir m'approprier le code, il va falloir de plus
grosses modifications structurelles sur le client Web ; ainsi naquit un fork,
sous le nom de Kresus (pour devenir riche comme
[Crésus](https://fr.wikipedia.org/wiki/Cr%C3%A9sus) !). S'ensuivent de nombreux
changements, autant dans les choix techniques (réécriture complète du serveur
de CoffeeScript vers du JavaScript moderne, réécriture du client Web avec
React.js, puis plus tard en ajoutant une couche Redux.js) que dans les
fonctionnalités apportées (écran de déduplication manuelle des transactions
bancaires pour palier au problème initial, ajout de la catégorisation, mise en
place de graphiques). D'autres gens sont intéressés, notamment d'autres
personnes qui contribuent à CozyCloud ; je tire parti de l'expérience de la
contribution chez Mozilla pour tâcher d'être chaleureux, remercier ces
inconnu.e.s qui m'offrent des retours, voire des patches, trop content d'avoir
des utilisateur.ice.s.

![Capture de Kresus en aout 2018]({filename}/images/2018-08-kresus.png)

Aujourd'hui, quatre ans plus tard, il y a suffisamment de contributeur.i.ces
externes pour que mes deux mains ne suffisent plus à les compter. Il y a une
(tentative de) gouvernance commune du projet. Il y a une gestion du produit
avec une vision plus long terme, même si celle-ci n'est pas toujours clairement
définie. Hey, il y a même un [forum](https://community.kresus.org) pour que tout
un chacun puisse s'exprimer, et un [site officiel](https://kresus.org), avec
son propre [blog](https://kresus.org/blog/), que je vous incite à suivre ; mon
blog personnel ne mentionnera Kresus que rarement dorénavant, plutôt sur les
aspects personnels si j'en ressens l'envie. Le travail s'effectue de manière
distribuée, parfois se bloque temporairement, parce que l'on a une vie qui se
déroule en parallèle, et moins de temps libre ; et c'est bien naturel et
entièrement irréprochable !  Les exigences d'un certain niveau de qualité font
que les contributions peuvent mettre du temps à être intégrées. Est-ce que la
conception est cohérente ? Est-ce que les éléments introduits n'interagissent
pas négativement avec d'autres fonctionnalités ? Peut-on généraliser ou
simplifier le besoin ?  Ensuite il faut tester les changements apportés pour
s'assurer que rien d'autre ne casse, vérifier un éventuel impact sur la
réactivité de l'application, jeter un coup d'oeil pour vérifier le rendu et la
réactivité sous mobile. Des corrections peuvent être demandées, pour les plus
prolifiques, démarrant un possible cycle d'aller-retours. Comme le dit la
sagesse populaire : tout seul, on va plus vite ; ensemble, on va plus loin. Il
y a des fonctionnalités dans Kresus auxquelles je n'aurais jamais pensées, il y
a des éléments d'interface bien plus peaufinés que ce que je n'aurais jamais su
faire, il y a des questions de design que je ne me serais jamais posées. Et
c'est tant mieux !

### Merci, toi !

Une petite communauté se créé, autour de personnes qui discutent du projet,
décrivent comment l'installer sur son serveur, résolvent des soucis lors de la
mise en place ou de l'utilisation, partagent leurs trucs et astuces. Que ce
soit en utilisant Kresus, en en parlant à des gens autour d'elles et d'eux, en
nous faisant des retours (quand quelque chose se passe mal ou quand quelque
chose pourrait mieux se passer), en nous posant des questions sur les valeurs
et les principes sous-jacents du projet, ou en contribuant au code ou aux
systèmes pour que d'autres puissent l'installer chez eux : vous contribuez
activement à Kresus, et à ce titre je vous remercie personnellement. Vous
faites vivre ce logiciel, c'est par vous qu'il est libre et vous pouvez être
fières et fiers de vos contributions.

Et si vous avez envie de contribuer également, et que vous avez peur de ne pas
savoir comment faire, détrompez-vous ! Tout le monde a sa pierre à apporter à
un logiciel libre, tout le monde est légitime de poser des questions ou de
présenter ses problématiques ; nous ferons de notre mieux pour les comprendre.
Donc n'hésitez-pas, venez sur le forum, ouvrez un sujet, commentez-en un autre,
essayez Kresus sur le [site de démo](https://demo.kresus.org) ! Et surtout, si
quelque chose ne fonctionne pas pour vous ou ne vous convient pas,
n'hésitez-pas à venir nous le signaler ! On ne peut travailler sur les défauts
que si on les a clairement identifiés. Et à force de scruter de très (trop)
près le logiciel, on perd parfois le recul nécessaire pour identifier de
bénignes bévues. On a commencé à mettre en place des tests d'expérience
utilisateur.ice, et on a encore beaucoup de chemin à faire. Bref, c'est un
petit geste pour vous, mais pour nous, ça peut vouloir dire beaucoup !

En conclusion, joyeux anniversaire Kresus, joyeux 4 ans, essayons ensemble de
te faire grandir encore ! Dans les vastes chantiers futurs, nous aimerions
toujours passer à un système d'auto-catégorisation des transactions bancaires,
avoir un meilleur système de dédoublonnage des transactions, trouver d'autres
informations pertinentes à présenter (identifier les transactions récurrentes
et prévoir les soldes négatifs). Et dans les grands plans futurs, il y a
toujours cette volonté de faire voyager Kresus en dehors de France, et donc de
trouver des systèmes pour se brancher sur les banques étrangères ! La route est
longue, mais la banque est libre...

[1] Le scrapping est une méthode qui permet artificiellement de créer des APIs
pour des sites qui n'en ont pas, en se faisant passer pour un navigateur Web,
en connaissant a priori la structure des pages et en extrayant les données
recherchées. C'est très fragile, mais absolument nécessaire quand il n'y a rien
d'autre (et les banques sont très jalouses de la propriété de leurs données !).
