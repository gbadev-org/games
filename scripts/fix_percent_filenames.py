"""
Renames files whose filename contains a literal "%" (replacing it with "t"),
and updates the "filename" and "screenshots" references in the corresponding
entry's game.json accordingly.
"""

import json
import os

path = "../entries/"
games_list = os.listdir(path)

renamed_count = 0

for entry_dir in games_list:
    manifest_path = f"{path}{entry_dir}/game.json"
    with open(manifest_path) as f:
        game = json.load(f)

    base_dir = f"{path}{entry_dir}"
    changed = False

    for file in game.get("files", []):
        if "%" in file["filename"]:
            old_filename = file["filename"]
            new_filename = old_filename.replace("%", "t")
            old_path = os.path.join(base_dir, old_filename)
            new_path = os.path.join(base_dir, new_filename)
            print(f"{entry_dir}: {old_filename} -> {new_filename}")
            os.rename(old_path, new_path)
            file["filename"] = new_filename
            changed = True
            renamed_count += 1

    screenshots = game.get("screenshots", [])
    for i, screenshot in enumerate(screenshots):
        if "%" in screenshot:
            old_screenshot = screenshot
            new_screenshot = old_screenshot.replace("%", "t")
            old_path = os.path.join(base_dir, old_screenshot)
            new_path = os.path.join(base_dir, new_screenshot)
            print(f"{entry_dir}: {old_screenshot} -> {new_screenshot}")
            os.rename(old_path, new_path)
            screenshots[i] = new_screenshot
            changed = True
            renamed_count += 1

    if changed:
        with open(manifest_path, "w") as f:
            json.dump(game, f, indent=4)
            f.write("\n")

print(f"Renamed {renamed_count} files.")
