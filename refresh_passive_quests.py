import sys
import subprocess
import os
import re
from dataclasses import dataclass
from typing import List

if len(sys.argv) != 2:
    print("Usage: refresh_passive_quests.py <vault_path>")
    sys.exit(1)

vault_path = sys.argv[1]

@dataclass
class CheckedPassiveQuest:
    name: str
    gold: str
    source: str

database_file = os.path.join(vault_path, "RLRPG/RLRPG Database.md")
with open(database_file, "r") as db:
    config = {line.split("| ")[0]: line.split("| ")[1].strip() for line in db}

character_full_folder = os.path.join(config.get("folder"), config.get("character_folder"))

if character_full_folder is None:
    print("Could not find character folder")
    sys.exit(1)

main_file_path = os.path.join(vault_path, config.get("folder"), config.get("main_file_name"))
character_folder_path = os.path.join(vault_path, character_full_folder)
task_pattern = re.compile(r"- \[([ x])\] (.+?)\s+`(-?\d+)`")

def add_checked_passive_task(file_path, file_title, tasks: List[CheckedPassiveQuest]):
    with open(file_path, "r") as f:
        content = f.readlines()

    for line in content:
        match = task_pattern.match(line)
        if not match:
            continue
        checked, task_name, gold = match.groups()
        if not checked.strip():
            continue
        tasks.append(CheckedPassiveQuest(name=task_name, gold=gold, source=file_title))

def overwrite_passive_tasks_in_main_with(tasks: List[CheckedPassiveQuest]):
    passive_task_header = config.get("passive_tasks_location")
    if not passive_task_header:
        print("Passive task location not found.")
        sys.exit(1)
    with open(main_file_path, "r") as f:
        content = f.readlines()
    new_task_lines = [f"- [ ] {task.name} `{task.gold}` #{task.source.lower().replace(' ','-')}\n" for task in tasks]

    header_index = None
    for i, line in enumerate(content):
        if line.strip() == passive_task_header:
            header_index = i
            break

    if header_index is None:
        content.append(f"\n{passive_task_header}\n")
        content.extend(new_task_lines)
    else:
        next_section_index = None
        for i in range(header_index + 1, len(content)):
            if content[i].startswith("## "):
                next_section_index = i
                break

        if next_section_index is None:
            content = content[:header_index + 1] + new_task_lines
        else:
            content = content[:header_index + 1] + new_task_lines + ["\n"] + content[next_section_index:]

    with open(main_file_path, "w") as f:
        f.writelines(content)

tasks: List[CheckedPassiveQuest] = []
for character_file in os.listdir(character_folder_path):
    file_path = os.path.join(character_folder_path, character_file)
    file_title = character_file.split(".md")[0]                                          
    add_checked_passive_task(file_path, file_title, tasks)
    overwrite_passive_tasks_in_main_with(tasks)
print("Updated passive quests!")
