import sys
import re
from datetime import datetime

if len(sys.argv) != 4:
    print("Usage: add_coins.py <gold_count> <description> <vault_path>")
    sys.exit(1)

gold_count = int(sys.argv[1])
description = sys.argv[2]
vault_path = sys.argv[3]

database_file = vault_path + "/RLRPG/RLRPG Database.md"
with open(database_file, "r") as db:
    config = {line.split("| ")[0]: line.split("| ")[1].strip() for line in db}

main_file = vault_path + "/RLRPG/" + config["main_file_name"]
transaction_file = vault_path + "/RLRPG/" + config["transaction_file_name"]
gold_prefix = config["gold_prefix"]

def get_gold():
    """Extracts the current gold count from the main file."""
    with open(main_file, "r") as f:
        content = f.read()
    print("prefix", gold_prefix)
    match = re.search(rf"{re.escape(gold_prefix)}\s*`(-?\d+)`", content)
    if match:
        print(f"Gold Found: {match.group(1)}")
    return int(match.group(1)) if match else 0

def update_gold():
    """Updates the gold count in the main file and logs the transaction."""
    current_gold = get_gold()
    new_gold = current_gold + gold_count

    with open(main_file, "r") as f:
        content = f.read()

    updated_content = re.sub(
        rf"({re.escape(gold_prefix)}\s*)`-?\d+`", 
        rf"\1`{new_gold}`", 
        content
    )

    with open(main_file, "w") as f:
        f.write(updated_content)

    date_today = datetime.today().strftime('%Y-%m-%d')
    transaction_entry = f"{date_today}: {'+' if gold_count > 0 else ''}{gold_count} ({description})\n"
    with open(transaction_file, "a") as f:
        f.write(transaction_entry)

    print(f"Updated gold: {current_gold} → {new_gold}")

update_gold()

