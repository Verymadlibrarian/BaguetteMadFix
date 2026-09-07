filename = "Steins;Gate - 01 - Copy.ass"

with open(filename, "r", encoding="utf-8") as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    if line.startswith("Dialogue: 0,") and "Default,," in line:
        line = line.replace("Dialogue: 0,", "Dialogue: 1,", 1)
    new_lines.append(line)

with open(filename, "w", encoding="utf-8") as f:
    f.writelines(new_lines)

print("Layer modifié de 0 à 1 pour les lignes 'Default,,'")