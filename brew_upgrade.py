"""how to upgrade all packages by homebrew"""

import subprocess

"""find outdated packages"""
packages = subprocess.run(["brew", "outdated"], stdout=subprocess.PIPE,
                          text=True, check=False)
outdated_str = packages.stdout
print(outdated_str)

outdated_list = outdated_str.split()

"""upgrade packages one by one & manage un-upgradable packages"""
exception = ["\n\n",
            "*********************************\n",
            "\n*********************************",
            "I was not be able to upgrade these packages:\t"]
command = ["brew", "upgrade"]
for i in outdated_list:
    command = command + [i]
    upgrade = subprocess.run(command, stderr=subprocess.PIPE,
                             text=True, check=False)

    if upgrade.stderr != '':
        error_str = upgrade.stderr
        print(error_str)
        
    del command[-1]

clean = subprocess.run(["brew", "cleanup"], check=False)
