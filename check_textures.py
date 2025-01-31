import os
from plainBlocs import getBlocs

def delete_unusable_png(directory, allowed_names):
    """
    Parcourt un dossier et supprime les fichiers PNG qui ne sont pas dans la liste des noms.
    
    :param directory: Chemin du dossier à analyser
    :param allowed_names: Liste des noms de fichiers autorisés (sans extension)
    """
    for filename in os.listdir(directory):
        if filename.lower().endswith(".png"):
            name_without_ext = os.path.splitext(filename)[0]
            if name_without_ext not in allowed_names and not any(name_without_ext.startswith(name) and name_without_ext[len(name):] in ["_side", "_top", "_bottom"] for name in allowed_names):
                file_path = os.path.join(directory, filename)
                os.remove(file_path)
                print(f"Supprimé : {file_path}")
                
                
def check_missing_textures(directory, allowed_names):
    """
    Retourne la liste des textures PNG manquantes (noms autorisés non trouvés dans le dossier).
    
    :param directory: Chemin du dossier à analyser
    :param allowed_names: Liste des noms de fichiers autorisés (sans extension)
    :return: Liste des noms de fichiers manquants
    """
    existing_names = {os.path.splitext(filename)[0] for filename in os.listdir(directory) if filename.lower().endswith(".png")}
    missing_textures = []
    
    for name in allowed_names:
        if name not in existing_names:
            alternative_textures = [f"{name}_side", f"{name}_top", f"{name}_bottom"]
            if any(alt in existing_names for alt in alternative_textures):
                print(f"Texture principale manquante, mais alternative trouvée : {name}")
            else:
                missing_textures.append(name)
    return missing_textures

def blocs_with_textures_only(blocs_names, directory, defaultPosition="side"):
    """
    Retourne uniquement les blocs ayant une texture. Si la texture principale est absente,
    retourne la texture à la position spécifiée.
    
    :param blocs_names: Liste des noms de blocs
    :param directory: Chemin du dossier contenant les textures
    :param defaultPosition: Position par défaut à vérifier si la texture principale est absente
    :return: Dictionnaire {bloc: texture_trouvée}
    """
    existing_names = {os.path.splitext(filename)[0] for filename in os.listdir(directory) if filename.lower().endswith(".png")}
    valid_blocs = {}
    
    for bloc in blocs_names:
        if bloc in existing_names:
            valid_blocs[bloc] = bloc
        else:
            alternative_texture = f"{bloc}_{defaultPosition}"
            if alternative_texture in existing_names:
                valid_blocs[bloc] = alternative_texture
    
    return valid_blocs

    
directory_path = "resource/blocks_textures/"
blocs_names = getBlocs()

print(blocs_with_textures_only(blocs_names, directory_path))