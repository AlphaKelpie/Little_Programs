# Little_Programs
Some programs to menage

## Introduction

In this repository I put some program that could be usefull to menage packages, file or other.  
I use them on a MacBookAir 6.2 with macOS Catalina 10.15.7 with a zsh shell. The Python version is Python 3.10.  
In the next sections I will describe each program. The title of the section is the same of the name of the code.


## pip_upgrade.py

### Upgrade packages using pip

## brew_upgrade.py

### Upgrade packages using HomeBrew
The program use the library subprocess that could be installed by the shell with the command:  
pip install subprocess.run  
This library works on Python3 or latest version, so the code doesn't work on Python2.  

To execute the code by shell the command is:  
python3 brew_ugrade.py  
On the the shell you will see the list of packages that are outdated and that will be upgraded by the program.
The program try to upgrade packages one by one, executing the HomeBrew command:  
brew upgrade <*name of the package*>  
so before check dependencies, download files of the dependencies and of the package, try to install the dependencies and then the package.
If it was not able to upgrade some packages or dependencies, it print the error that HomeBrew returns.
When it has tried to upgrade all the packages in the list, it's call the cleanup function althought it is usually called after any upgrade automatically:  
brew cleanup  
At the end of the program, it prints the list of packages that was not able to upgrade.
A common error is that the version of your computer is not supported becouse too old.
In that case the only solution is to upgrade the operating system (or be better than me in these stuff, that is not so difficult).