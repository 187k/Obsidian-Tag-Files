import os

# Папка с вашими заметками Obsidian
vault_path = "H:/Мой диск/obsidian vault/05 - Projects/NYC Gangs/Queens"
tag_to_add = "#nycgang"

for filename in os.listdir(vault_path):
    if filename.endswith(".md"):
        file_path = os.path.join(vault_path, filename)
        with open(file_path, "r+", encoding="utf-8") as file:
            content = file.read()
            if tag_to_add not in content:  # Чтобы не дублировать теги
                file.seek(0, 0)
                file.write(tag_to_add + "\n" + content)