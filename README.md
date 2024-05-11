# Little_Programs

Some programs to remember some tasks.

## Introduction

In this repository I put some program that could be usefull to menage packages, file or other.  
I use them on a MacBookAir 6.2 with macOS Catalina 10.15.7 with a zsh shell. The Python version is Python 3.10.  
In the next sections I will describe each program. The title of the section is the same of the name's file of the code.

## pip_upgrade.py

### Upgrade packages using pip

First of all it looks for pip's packages that shall not be upgraded in ```not_upgrade_pip.txt``` file.
Then it looks for new pip's release.

It stores all the packages installed with pip and check to upgrade each of them that are not in ```not_upgrade_pip.txt```.

It print in orange the package. In red if it will not be upgraded. In cyan if it is already updated. In green if it has been upgraded.

At the end clean the cache and upgrades ```not_upgrade_pip.txt``` file.

## brew_upgrade.py

### Upgrade packages using HomeBrew

First of all it looks for Homebrew's packages that shall not be upgraded in ```not_upgrade.txt``` file.

Then it stores the list of outdated packages.
It prints all the outdated ones and then all the one it will try to upgrade.

At the end it cleans the cache and prints all the packagest that have been outdated yet and upgrades ```not_upgrade.txt``` file.

**Beware**: the upgrade of the still outdated packages could be download anyway. The script is not able to delete them. I suggest to use CCleaner or other programs when the code has finished.

## Ansi_style.py

### Guide of shell's output

This code prints on shell texts with different colors, backgrownd, and style. It uses ANSI escape sequence.

- Changes text color;
- Changes backgrownd color;
- Changes text and backgrownd;
- Changes (text) color 8-bit;
- Changes style.

Some sequences are not supported on Mac Terminal app.

## Multi.py

### Multiprocessing example

That is just an example how to use multiprocessing map.

## Music_tag.py

### Music_tag example

That is just an example how to use music_tag.
