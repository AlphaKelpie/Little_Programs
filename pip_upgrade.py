"""how to upgrade pakages with pip automatically"""

import subprocess

"""find list of packages"""
pakages = subprocess.run(["pip", "list"], stdout=subprocess.PIPE,
                         text=True, check=False)
vlist = pakages.stdout

vlist = vlist.split()
del vlist[0:4]

i = 1
while i < len(vlist):
    del vlist[i]
    i += 1

"""upgrade packages all togheder"""
command = ["pip", "install"]
command = command + vlist
command = command + ["-U"]
upgrade = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                         text=True, check=False)
print(upgrade.stdout)

"""manage errors"""
exception = ["\n\n",
            "*********************************\n",
            "\n*********************************",
            "I was not be able to upgrade these packages:\t"]
while upgrade.stderr != '':
    error_str = upgrade.stderr
    error_list = error_str.split()
    error_package = error_list[3]
    error_package = error_package.replace('\'', '')
    error_package = error_package.replace('.', '')
    command.remove(error_package)
    error_package += ", "
    exception = exception + [error_package]
    upgrade = subprocess.run(command, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE, text=True, check=False)

print(upgrade.stdout)

if len(exception) > 4:
    for element in exception:
        print(element)
