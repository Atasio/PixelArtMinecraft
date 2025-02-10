#!/bin/env python3

# Code partielement généré avec Chatgpt4-o mini
# Prompt : 
#   Agis en temps que developpeur UI et occupe toi uniquement de l'interface, pas d'algorithmique.
#   Utilise tkinter pour faire une interface graphique, voici le cahier des charges, un bouton pour imorter une image et un autre pour lancer l'algorithme (qui la modifiera en blocks minecraft) 
# la possibilité de rentrer des paramètre pour choisisr la resolution finale, le tout de façon pratique et moderne

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from image_generator import image_generator
from image import Image

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("PixelArtMinecraft")
        self.geometry("600x350")
        self.resizable(False, False)
        self.image_path = None  # Chemin de l'image importée
        self.image : Image = None
        self.minecraftPixelArt : Image = None

        self.create_widgets()

    def create_widgets(self):
        # Création d'un frame principal avec padding
        main_frame = ttk.Frame(self, padding="20")
        main_frame.pack(expand=True, fill="both")

        # Label pour afficher le nom de l'image importée
        self.image_label = ttk.Label(main_frame, text="Aucune image importée", wraplength=400)
        self.image_label.grid(row=0, column=0, columnspan=3, pady=(0, 15))

        # Bouton pour importer une image
        import_button = ttk.Button(main_frame, text="Importer une image", command=self.import_image)
        import_button.grid(row=1, column=0, columnspan=3, sticky="ew", pady=(0, 15))

        # Labels et champs pour saisir la résolution finale (X et Y)
        resolution_x_label = ttk.Label(main_frame, text="Résolution X (block 16px) :")
        resolution_x_label.grid(row=2, column=0, sticky="w")
        self.resolution_x_entry = ttk.Entry(main_frame)
        self.resolution_x_entry.grid(row=2, column=1, sticky="ew", padx=5)

        resolution_y_label = ttk.Label(main_frame, text="Résolution Y (block 16 px) :")
        resolution_y_label.grid(row=3, column=0, sticky="w", pady=(5, 0))
        self.resolution_y_entry = ttk.Entry(main_frame)
        self.resolution_y_entry.grid(row=3, column=1, sticky="ew", padx=5, pady=(5, 0))

        # Bouton pour lancer l'algorithme
        algo_button = ttk.Button(main_frame, text="Lancer l'algorithme", command=self.launch_algorithm)
        algo_button.grid(row=4, column=0, columnspan=3, sticky="ew", pady=(20, 0))

        # Text chargement
        self.text_chargement = ttk.Label(main_frame, text="", wraplength=400)
        self.text_chargement.grid(row=5, column=0, columnspan=3, sticky="ew", pady=(20, 0))

        # Configuration de la répartition des colonnes
        main_frame.columnconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=2)

    def import_image(self):
        # Boîte de dialogue pour sélectionner un fichier image
        filetypes = [
            ("Fichiers image", "*.png *.jpg *.jpeg *.bmp *.gif"),
            ("Tous les fichiers", "*.*")
        ]
        path = filedialog.askopenfilename(title="Sélectionner une image", filetypes=filetypes)
        if path:
            self.image_path = path
            self.image = Image.lecture(path)
            # Affichage du nom de l'image dans le label (on affiche uniquement le nom de fichier)
            self.image_label.config(text=f"Image importée : {path.split('/')[-1]}")
            self.resolution_x_entry.delete(0, tk.END)
            self.resolution_y_entry.delete(0, tk.END)
            self.resolution_x_entry.insert(0, self.image.pixels.shape[0])
            self.resolution_y_entry.insert(0, self.image.pixels.shape[1])
        else:
            messagebox.showwarning("Avertissement", "Aucune image sélectionnée.")

    def launch_algorithm(self):
        self.text_chargement.config(text=f"Traitement de l'image '{self.image_path.split('/')[-1]}' avec une résolution de {self.resolution_x_entry.get()}x{self.resolution_y_entry.get()}px en cours...")

        # Vérifie si une image a bien été importée
        if not self.image_path:
            messagebox.showerror("Erreur", "Veuillez d'abord importer une image.")
            return

        # Vérifie que les résolutions X et Y sont des nombres entiers valides
        res_x = self.resolution_x_entry.get()
        res_y = self.resolution_y_entry.get()
        try:
            resolution_x = int(res_x)
            resolution_y = int(res_y)
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer des valeurs numériques valides pour la résolution.")
            return

        self.image.changeResolution(resolution_x, resolution_y)
        self.minecraftPixelArt = image_generator.createPixelArtMinecraft(self.image)
        self.minecraftPixelArt.show()
        
        # Effacer le message après le chargement
        self.text_chargement.config(text="")

if __name__ == "__main__":
    app = App()
    app.mainloop()
