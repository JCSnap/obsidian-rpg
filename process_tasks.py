import re
import subprocess
import sys

if len(sys.argv) != 2:
    print("Usage: python process_tasks.py <vault_path>")
    sys.exit(1)

vault_path = sys.argv[1]

database_file = vault_path + "/RLRPG/RLRPG Database.md"

with open(database_file, "r") as db:
    config = {line.split("| ")[0]: line.split("| ")[1].strip() for line in db}

main_file = vault_path + "/RLRPG/" + config["main_file_name"]

active_tasks_marker = config["active_tasks_location"]
passive_tasks_marker = config["passive_tasks_location"]
task_pattern = re.compile(r"- \[([ x])\] (.+?)\s+`(-?\d+)`")

def process_tasks():
    """First, update gold for completed tasks. Then, reset tasks in the main file."""
    with open(main_file, "r") as f:
        content = f.readlines()

    updated_content = []
    in_active_section, in_passive_section = False, False
    transactions = []

    for line in content:
        if active_tasks_marker in line:
            in_active_section = True
            in_passive_section = False
            updated_content.append(line)
            continue
        elif passive_tasks_marker in line:
            in_passive_section = True
            in_active_section = False
            updated_content.append(line)
            continue

        match = task_pattern.match(line)
        if match:
            checked, task_name, gold = match.groups()
            gold = int(gold)

            if checked == "x":
                transactions.append((gold, f"Completed: {task_name}"))

                if in_passive_section:
                    updated_content.append(f"- [ ] {task_name} `{gold}`\n")
            else:
                updated_content.append(line)

        else:
            updated_content.append(line)

    for gold, description in transactions:
        cmd = ["python3", vault_path + "/add_gold.py", str(gold), description, vault_path]
        print(f"Executing command: {' '.join(cmd)}")

        result = subprocess.run(cmd, capture_output=True, text=True)

        print("STDOUT:", result.stdout)
        print("STDERR:", result.stderr)

    with open(main_file, "r") as f:
        content = f.readlines()

    final_content = []
    in_active_section, in_passive_section = False, False

    for line in content:
        if active_tasks_marker in line:
            in_active_section = True
            in_passive_section = False
            final_content.append(line)
            continue
        elif passive_tasks_marker in line:
            in_passive_section = True
            in_active_section = False
            final_content.append(line)
            continue

        match = task_pattern.match(line)
        if match:
            checked, task_name, gold = match.groups()

            if checked == "x":
                if in_passive_section:
                    final_content.append(f"- [ ] {task_name} `{gold}`\n")
            else:
                final_content.append(line)

        else:
            final_content.append(line)

    with open(main_file, "w") as f:
        f.writelines(final_content)

    print("Processed tasks successfully!")

process_tasks()

