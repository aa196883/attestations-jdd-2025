import os

# Dossiers d'attestations
sections = {
    "attestation_3h": {
        "fr": "Participation le matin (3h)",
        "en": "Morning participation (3h)"
    },
    "attestation_6h": {
        "fr": "Participation matin + après-midi (6h)",
        "en": "Full-day participation (6h)"
    },
    "attestation_presentation": {
        "fr": "Présentations",
        "en": "Presentations"
    }
}

output_file = "index.html"

with open(output_file, "w", encoding="utf-8") as f:
    f.write("""<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8" />
  <title>Attestations – JDD 2025</title>
  <style>
    body { font-family: Arial, sans-serif; max-width: 900px; margin: auto; padding: 2rem; background-color: #f9f9f9; color: #333; }
    h1, h2 { color: #004080; }
    .lang-switch { text-align: right; margin-bottom: 1rem; }
    .lang-switch button { background: none; border: none; font-size: 1rem; cursor: pointer; margin-left: 1rem; color: #004080; }
    ul { list-style: none; padding-left: 0; }
    li { margin: 0.3rem 0; }
    a { text-decoration: none; color: #0066cc; }
    a:hover { text-decoration: underline; }
    .section { margin-bottom: 2rem; }
  </style>
</head>
<body>
  <div class="lang-switch">
    <button onclick="setLang('fr')">🇫🇷 Français</button>
    <button onclick="setLang('en')">🇬🇧 English</button>
  </div>

  <h1 data-fr="Téléchargement des attestations – JDD 2025"
      data-en="Download your certificates – PhD Day 2025">
      Téléchargement des attestations – JDD 2025
  </h1>
""")

    for folder, labels in sections.items():
        f.write(f'''
  <div class="section">
    <h2 data-fr="{labels['fr']}" data-en="{labels['en']}">{labels['fr']}</h2>
    <ul>
''')
        folder_files = sorted([file for file in os.listdir(folder) if file.endswith(".pdf")])
        for pdf in folder_files:
            f.write(f'      <li><a href="{folder}/{pdf}" download>{pdf}</a></li>\n')
        f.write("    </ul>\n  </div>\n")

    # Lang switch script
    f.write("""
  <script>
    function setLang(lang) {
      document.querySelectorAll("[data-fr]").forEach(el => {
        el.textContent = el.getAttribute("data-" + lang);
      });
    }
  </script>
</body>
</html>
""")

print(f"✅ Fichier HTML généré : {output_file}")
