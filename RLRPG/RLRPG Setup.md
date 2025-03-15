Note: Since this is a "proof of concept", there are many parts that are "hardcoded". I am actively trying to make this as easily implementable as possible so do not hesitate to create issues to provide feedback!

## Plugins
### Required
#####  [Execute Code](https://github.com/twibiral/obsidian-execute-code): This is needed for us to run the code blocks
- Go to the settings of the plugin under `Language Specific Settings`, select `Python`
- Insert your Python path  (eg. `/usr/local/bin/python3`)
- If you are unsure, you can open up your terminal and enter the command `which python`
- Note: I am "hardcoding" python3 in my inbuilt scripts so that might cause some issues if you are using python, open an [issue](https://github.com/JCSnap/obsidian-rpg/issues) if you are facing a problem
##### [Templater](https://github.com/SilentVoid13/Templater): This is needed if you are using the Leetcode template (or any future templates)
### Optional
##### [Homepage](https://github.com/mirnovov/obsidian-homepage): This is so that the `RLRPG Main` is opened by default if no other pages are opened
##### [VS Code](https://github.com/sunxvming/obsidian-vscode-editor): This is so that none `.md` files like the python scripts I created are visible and viewable

## Applying the template
- Copy the folder `RLRPG` into your vault, and the files at the root of this directory (except `README.md`) into the root of your directory. This should be sufficient for the RPG todo-list
- If you want the leetcode template, copy the `templates` folder as well. If you already have a folder for your templates, you can copy the content of my `templates` folder into yours

## Optional setup
- If you want to "reduce" the size of the code block, this template includes a `css` snippet that prevents long line of code from wrapping around. Go to `Settings` -> `Appearance` -> `CSS Snippets` and toggle on `no-wrap`