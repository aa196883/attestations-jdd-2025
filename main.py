import os
import subprocess

# ----------- CONFIGURATION -----------
TEMPLATE_PATH = "attestation_presentation"
OUTPUT_DIR = TEMPLATE_PATH
NOM_PLACEHOLDER = "{{NOM}}"

matin = ['Alexandre RICO', 'BUI Quang Tu', 'Gaillard Georges', 'Joseph Romain', 'Lénaïg GUEHO', 'Muller Thomas', 'Nour Chiboub', 'Joseph Zanduta', 'Viviana Volonnino']
matin_aprem = ['Adam Lakhdari', 'Ajdor Nouhaila', 'ALY Adel', 'ANDERSOHN Marco', 'Boulahmel Amine', 'BOURGEOIS Gabriel', 'Driessens Léa', 'Guillemé Wilfread', 'Hichem Ammar Khodja', 'Kouddane Nada', 'Lemesle Quentin', 'Lounes Gaëtan', 'Moussa Taha', 'Pauline Mas', 'Philippe Martin', 'Rohmer Constant', 'Sassi Dorra']
presentation = ['Adam Lakhdari', 'Alexandre RICO', 'ANDERSOHN Marco', 'Boulahmel Amine', 'Gaillard Georges', 'Hichem Ammar Khodja', 'Joseph Romain', 'Pauline Mas']
organisation = ['ALY Adel', 'BOURGEOIS Gabriel', 'Lamotte Quentin', 'Pauline Mas', 'Philippe Martin']
NOMS = presentation

# --------------------------------------

os.makedirs(OUTPUT_DIR, exist_ok=True)

# Lire le modèle LaTeX
with open(TEMPLATE_PATH+".tex", 'r', encoding='utf-8') as f:
    template = f.read()

# Générer un fichier par nom
for nom in NOMS:
    nom_safe = nom.replace(" ", "_").lower()
    tex_filename = f"{TEMPLATE_PATH}_{nom_safe}.tex"
    tex_path = os.path.join(OUTPUT_DIR, tex_filename)

    # Remplacer le placeholder
    contenu = template.replace(NOM_PLACEHOLDER, nom)

    # Écrire le fichier LaTeX personnalisé
    with open(tex_path, 'w', encoding='utf-8') as f:
        f.write(contenu)

    # Compiler avec pdflatex
    print(f"📄 Compilation de {tex_filename}...")
    subprocess.run([
        "pdflatex",
        "-interaction=nonstopmode",
        "-output-directory", OUTPUT_DIR,
        tex_path
    ], check=True)

    # Nettoyer les fichiers auxiliaires
    for ext in ["aux", "log", "out", "tex"]:
        aux_path = os.path.join(OUTPUT_DIR, f"{TEMPLATE_PATH}_{nom_safe}.{ext}")
        if os.path.exists(aux_path):
            os.remove(aux_path)

print("✅ Terminé. Les attestations PDF sont dans:", OUTPUT_DIR)
