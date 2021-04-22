# Casse-briques

## But du jeu
Nous allons reprendre le jeu classique appelé le "casse-brique" qui consiste à faire rebondir une petite balle sur un plateau afin qu'elle atteigne des briques pour les casser.

## Comment jouer ?
Il suffit de déplacer le plateau de droite à gauche pour ne pas faire tomber la petite balle. Le plateau pourra se déplacer grâce au mouvement de la souris. La petite balle, elle, se déplacera de haut en bas et dès qu'elle touchera le plateau elle rebondira vers le murs de brique qui se situe sur le haut du jeu. Les briques 🧱 se brisent dès que la petite balle les touche et disparaissent si elles sont déjà brisées et qu'elles sont à nouveau touchées par la petite balle. 

## Les classes et méthodes
Nous avons imaginé faire une classe *briques* et une sous-classe *briques cassées*, une classe *plateau*, et une classe *balle*. Pour la classe *briques* nous allons utiliser la méthode ###### break itself #####, ensuite nous utiliserons la méthode *bounce* et *move* (right/left) pour le *plateau*, la balle aura les même méthodes que le plateau mais se déplacera de haut en bas, *move(up/down)* et en plus elle aura la méthode *pop* comme celle de la *brique-cassée*.


#### Notre diagramme de classes
https://app.diagrams.net/#HAmelie02%2Foc20%2Fmain%2Fprojet%20jeu%2Fcasse-briques
