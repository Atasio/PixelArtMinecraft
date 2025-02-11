# PixelArtMinecraft

**PixelArtMinecrat** est un outil permettant de réaliser un *PixelArt* d'une image avec des textures de blocs du jeu vidéo *Minecraft*.

Cet outil devra donc, en fonction de la résolution choisie (1 ou plusieurs pixels par blocs), transformer le ou les pixels avec la texture du bloc qui se rapproche le plus de ce(s) dernier(s).

Pour cela, nous récupérons les textures des blocs minecraft, et uniquement les blocs pleins.

Nous créons ensuite un jeu de données avec la moyenne des niveaux de couleur de chaque blocs.

Ensuite, pour ce qui est de la partie "génération de l'image":
- Pour chaque pixel ou groupe de pixels de l'image d'entrée, nous récupérons la moyenne des niveau de couleur.
- On créé l'image de sortie en tranformant chaque pixels avec la texture qui possède les niveaux de couleurs les plus proches.

## Usage
1. Créez un environnement python : `python -m venv .venv`
2. Activez l'environnement : `source .venv/bin/activate` (bash) ou `.\.venv\Scripts\activate` (pwsh)
3. Importez les dépendances : `pip install -r ./requirements.txt`
4. Lancez `python main.py` pour l'application en ligne de commande et `python app.py` pour l'application avec interface graphique.


## Auteurs
- Loris O.
- Alexandre A.
