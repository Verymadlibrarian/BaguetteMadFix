filename = "Steins;Gate - 01 - Copy.ass"

with open(filename, "r", encoding="utf-8") as f:
    lines = f.readlines()

new_lines = [line for line in lines if "Default,," not in line]

with open(filename, "w", encoding="utf-8") as f:
    f.writelines(new_lines)

print("Lignes 'Default,,' supprimées avec succès.")