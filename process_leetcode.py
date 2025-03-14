import sys
import re
import subprocess

if len(sys.argv) != 3:
    print("Usage: process_leetcode.py <leetcode_file_path> <vault_path>")
    sys.exit(1)

leetcode_file_path = sys.argv[1]
vault_path = sys.argv[2]
leetcode_title = leetcode_file_path.split("/")[-1].replace(".md", "")

database_file = vault_path + "/RLRPG/RLRPG Database.md"
with open(database_file, "r") as db:
    config = {line.split("| ")[0]: line.split("| ")[1].strip() for line in db}

def get_difficulty(leetcode_file_path) -> str:
    with open(leetcode_file_path, "r", encoding="utf-8") as f:
        for line in f:
            if match := re.match(r"difficulty:\s*(easy|medium|hard)", line, re.IGNORECASE):
                difficulty = match.group(1).lower()
                return difficulty
    return None

def add_gold_and_transaction(vault_path, leetcode_title, difficulty):
    difficulty_variable = "leetcode_" + difficulty + "_gold"
    gold_to_add = config.get(difficulty_variable)
    if not gold_to_add:
        raise Exception("could not find difficulty level in DB")
    print(difficulty_variable)
    description = f"completed {difficulty} leetcode {leetcode_title}"
    cmd = ["python3", vault_path + "/add_gold.py", str(gold_to_add), description, vault_path]
    result = subprocess.run(cmd, capture_output=True, text=True)
    print(result.stdout)


difficulty = get_difficulty(leetcode_file_path)

add_gold_and_transaction(vault_path, leetcode_title, difficulty)

