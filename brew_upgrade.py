"""how to upgrade all packages by homebrew"""
#use an if over stderr of packages: if false stop program
import subprocess

"""find outdated packages"""
packages = subprocess.run(["brew", "outdated"], stdout=subprocess.PIPE,
                          text=True, check=False)
outdated_str = packages.stdout
print(outdated_str)

outdated_list = outdated_str.split()

"""upgrade packages one by one & manage un-upgradable packages"""
exception = """*********************************||\n||
            \n*********************************||\n
            I was not be able to upgrade these packages:"""
command = ["brew", "upgrade", ""]
for i in outdated_list:
    command[2] = i
    upgrade = subprocess.run(command, stderr=subprocess.PIPE,
                             text=True, check=False)
    if upgrade.stderr != '':#remove this and create a control between list (if doesn't work)
        error_str = upgrade.stderr
        print(error_str)
        exception = exception + '\t' + i

clean = subprocess.run(["brew", "cleanup"], check=False)

if exception.find('\t'):
    print(exception)
