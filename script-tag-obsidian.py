import os

vault_path = "path to folder"
tag_to_add = "tag" # example: #itnewtag

for filename in os.listdir(vault_path):
    if filename.endswith(".md"):
        file_path = os.path.join(vault_path, filename)
        with open(file_path, "r+", encoding="utf-8") as file:
            content = file.read()
            if tag_to_add not in content: 
                file.seek(0, 0)
                file.write(tag_to_add + "\n" + content)
