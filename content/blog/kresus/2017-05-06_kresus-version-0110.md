Title: Kresus: version 0.11.0
Date: 2017-05-06 20:30
Author: Benjamin Bouvier
Lang: fr
Tags: kresus, cozycloud
Slug: kresus-version-0-11-0

L'équipe vient de publier une nouvelle version de [Kresus](https://kresus.org),
un gestionnaire libre de finances personnelles sur lequel je travaille. Pour
rappel, cette application web, basée sur [Weboob](http://weboob.org/) et
disponible [de manière
autonome](https://www.karolak.fr/blog/2016/03/18/kresus-un-gestionnaire-web-de-finances-personnelles/)
ou dans [CozyCloud](https://cozy.io/), vous permet de vous connecter à votre
compte bancaire, de récupérer vos opérations et de les classifier pour savoir
comment vous dépensez votre argent afin de mieux maîtriser vos finances.

## En résumé

De nouvelles banques, une expérience utilisateur encore améliorée, un
chargement initial un peu plus rapide, plus de stabilité pour la récupération
des données bancaires, et des simplifications pour l'auto-hébergement au
sommaire de cette version mineure !

### Nouvelles banques et support de Weboob

Kresus s'appuie sur les épaules du logiciel libre [Weboob](http://weboob.org)
pour récupérer les données bancaires.

La version minimale de weboob pour utiliser Kresus est maintenant la **version
1.2**. Cependant, comme nous avons observé que de plus en plus de modules
bancaires ne fonctionnent plus en version 1.2, nous recommandons d’installer la
version de développement pour profiter des mises à jour continues.

Nous avons ajouté le support pour les nouvelles entités bancaires que Weboob
supporte désormais :

* Laydernier et Société Marseillais de Crédit (groupe Crédit du Nord)
* Les comptes professionnels du Crédit Mutuel de Bretagne
* Le Crédit Mutuel du Massif Central
* BTP Banque

Le support des épargnes salariales a été largement augmenté également :

* Prado Epargne
* Crédit Mutuel Epargne Salariale
* CIC Epargne Salariale
* BNP Epargne Salariale
* Axa Epargne Salariale
* Société Générale Epargne Salariale
* HSBC Epargne Salariale

Par ailleurs, le module S2E (qui gère les plans épargne entreprises de
plusieurs banques) a été supprimé ; les accès actuellement configurés seront
migrés automatiquement vers les modules bancaires appropriés.

### Amélioration de l'interface utilisateur et de l'expérience utilisateur

Notre travail sur l'interface et l'expérience utilisateur continue :

* Il est maintenant possible de cacher le menu, indépendemment de la taille de
  l'écran (ce n’était possible que sur mobile jusqu’à présent).
* Les dates sont enfin affichées de manière homogène entre les navigateurs, en
  fonction de la langue choisie par l’utilisateur.
* Les sélecteurs ont été stylisés pour s’afficher de manière uniforme dans tous
  les navigateurs.
* Les graphiques utilisent maintenant les mêmes couleurs que la page de
  rapport.
* Les sélecteurs de type et catégories dans la vue des opérations s'ouvrent dès
  le premier clic.
* Beaucoup de corrections de vocabulaire, d'erreurs de typographie et
  d’affichage.

Kresus se chargera également plus rapidement, dorénavant ! Le client a été
allégé en supprimant plusieurs dépendances peu usitées et en minifiant les
fichiers de code, diminuant la taille totale des fichiers que le navigateur
doit charger, ce qui implique un chargement plus rapide. Ce nettoyage des
dépendances s'accompagne d'un travail d'intégration de toutes ces dernières
sous forme de paquets npm. Ceci permettra un suivi plus fin de la mise à jour
de ces dépendances.

### Stabilité

Côté serveur, l’import des opérations a été amélioré de manière à s’assurer du
bon séquencement de toutes les opérations asynchrones (import de comptes puis
d’opérations). Ceci devrait régler plusieurs problèmes observés d'imports
multiples, d'opérations allouées aux mauvais comptes etc.

### Auto-hébergement

Il est maintenant possible d’héberger Kresus autrement qu’à la racine d’un
domaine (par exemple `https://mondomaine.fr/kresus`). Pour cela, il faut passer
la variable d'environnement `KRESUS_URL_PREFIX` à l'application. Cette variable
désigne le chemin d'accès depuis la racine (`/kresus` dans l'exemple).

Le Dockerfile a été amélioré pour couvrir de plus nombreuses dépendances des
modules bancaires par défaut.

### Le mot de la fin

Merci à tous les contributeurs, et en particulier aux hyperactifs
[nicofrand](https://nicofrand.eu) et [ZeHiro](https://github.com/ZeHiro) pour
avoir écrit ce billet et pour leurs très nombreuses contributions !

Comme d'habitude, si vous avez des remarques ou suggestions, n'hésitez-pas à
nous le faire savoir, sur [mastodon](https://tutut.delire.party/@kresus),
[twitter](https://twitter.com/kresusapp), le [canal
IRC](https://kiwiirc.com/client/chat.freenode.net/kresus), la [liste de
diffusion](https://framalistes.org/sympa/info/kresus), ou encore
[diaspora](https://framasphere.org/people/315a5640ead10132c4cc2a0000053625)  !
