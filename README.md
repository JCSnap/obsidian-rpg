# RPG in Obsidian
Your notes are not just static text files.

This is an example template to make your Obsidian workflow more dynamic. To demonstrate this, we will be "gamifying" our todo-list into an RPG.

The premise is simple - complete tasks to earn coins! Learn how to setup [here](https://github.com/JCSnap/obsidian-rpg/blob/main/RLRPG/RLRPG%20Setup.md)

# Main features
## Todo-list
In Your `RLRPG Main`, there are 3 main sections:
1. Your gold count
2. Your active tasks
3. Your passive tasks

Active tasks are one-time off tasks meant to be completed. Passive tasks are recurring tasks that once completed, will be reset the next day. You can add your own tasks and the gold count associated with each task in an inline code block `like this`. You can also link to your other [[notes]] using Obsidian syntax

At the end of the day, run the code at the end of the `RLRPG Main` file. It will go through all your tasks.
1. Add gold for completed tasks, log the transactions in `RLRPG Transactions`. Your link to other [[notes]] will be preserved
2. Delete completed active tasks, reset completed passive tasks

![RLRPG tasks demo](https://github.com/JCSnap/obsidian-rpg/blob/main/assets/RLRPG-tasks.gif)

## Rotate passive tasks
You can set relevant tasks within the character pages. Eg. health related passive tasks can be set in `RLRPG Health`. You can go into these pages and toggle the ones that you want to focus on. Then run the code below in `RLRPG Main` to refresh the passive task.

Your new toggled tasks will be reflected, along with their reward amount and their sources.

![RLRPG passive tasks demo](https://github.com/JCSnap/obsidian-rpg/blob/main/assets/RLRPG-passive.gif)

## Leetcode
This gamification is very extensible. Other than your normal tasks, you can incorporate it into your templates. For instance, I have included a `Leetcode Template`, which you can use to track your Leetcode progress. Every time you are done with a Leetcode problem, run the code block at the bottom and your account will be updated with gold!

![RLRPG leetcode demo](https://github.com/JCSnap/obsidian-rpg/blob/main/assets/RLRPG-leetcode.gif)

## Generate analytics
After completing tasks for a while, your `RLRPG Transactions` file should be populated with many entries.

Under `RLRPG Analytics`, you can run a script to view analytics on your coins in ASCII charts!

![RLRPG analytics demo](https://github.com/JCSnap/obsidian-rpg/blob/main/assets/RLRPG-analytics.gif)

Current supported analytics:
- Cumulative gold over time

# Additional Info
## How does this work?
1. File created in Obsidian are stored locally as `.md` files
2. There is an Obsidian [plugin](https://github.com/twibiral/obsidian-execute-code) that can allow you to execute code blocks written in Obsidian (basically turning your `.md` files into jupyter notebooks)
3. I have pre-built some python scripts which will be run under the hood to update your files

For instance, here is a pseudo-code of what one of the function does:
```
// open up `Main.md`
// check if tasks are completed
// if completed, add coins and reset tasks
```

Except you do not have to manually create the scripts since it will be provided by this template

## Main File structure
- `RLRPG Main`: The "home screen" for your game. For QOL improvement, you can download the [homepage plugin](https://github.com/mirnovov/obsidian-homepage) and set your home page to this file
- `RLRPG Transactions` This will serve as a book-keeping for all your coins inflow and outflow (think a Bitcoin ledger)
- `RLRPG Database`: The source of truth for all variables (actually more like pointers to source of truth)?
- `RLRPG Analytics`: See analytics about your account (your gold count over time etc.)
- `RLRPG Skill Tree`: Contain links to resources for the important skills you want to develop. Contain quests for you to earn gold
- The character files like `RLRPG Academics` and `RLRPG Health` etc. will contain important links, information and quests related to that aspect
- `RLRPG Scripts`: Contains API documentation for some of the functions behind the hood. You only need to care about this if you are intending to extend this template and implement your own automation

## Skill Tree
You can create your own skill tree and define tasks which when completed, will add gold and experience points to your skill (enough experience points will cause your level for the skill to increase)