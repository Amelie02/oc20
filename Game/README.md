# Casse-briques

## But du jeu
Nous allons reprendre le jeu classique appelé le "**casse-brique**" qui consiste à faire rebondir une petite balle sur un plateau afin qu'elle atteigne des briques pour les casser.

## Comment jouer ?
Il suffit de déplacer le plateau de droite à gauche pour ne pas faire tomber la petite balle. Le plateau pourra se déplacer grâce au mouvement de la souris. La petite balle, elle, se déplacera de haut en bas et dès qu'elle touchera le plateau elle rebondira vers le murs de brique qui se situe sur le haut du jeu. Les briques se brisent dès que la petite balle les touche et disparaissent si elles sont déjà brisées et qu'elles sont à nouveau touchées par la petite balle. 

![Capture d’écran 2021-04-22 à 14 09 30](https://user-images.githubusercontent.com/77777393/115711932-74709080-a374-11eb-909d-a354875b959d.png)


## Les classes et méthodes
Nous avons imaginé faire une classe *briques* et une sous-classe *briques cassées*, une classe *plateau*, et une classe *balle*. Pour la classe *briques* nous allons utiliser la méthode *break itself*, ensuite nous utiliserons la méthode *bounce* et *move* (right/left) pour le *plateau*, la *balle* aura les même méthodes que le *plateau* mais se déplacera de haut en bas, *move(up/down)* et en plus elle aura la méthode *pop* comme celle de la *brique-cassée*.

- **break**: sert à briser la brique
- **bounce**: sert à faire rebondir la balle
- **move**: sert à déplacer un objet, ici le plateau et la balle, de haut en bas ou de gauche à droite. 
- **pop**: sert à faire disparâitre les brique déjà brisées.

![Capture d’écran 2021-04-22 à 14 19 18](https://user-images.githubusercontent.com/77777393/115713002-cb2a9a00-a375-11eb-820f-8f43bbf92bef.png)


#### Notre diagramme de classes
https://app.diagrams.net/#HAmelie02%2Foc20%2Fmain%2FGame%2Fcasse-briques.xml
