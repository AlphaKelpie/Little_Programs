"""how to upgrade pakages with pip automatically"""

import subprocess

subprocess.run(['pip', 'install', 'pip', '--upgrade'], check=False)
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

"""upgrade packages one by one"""
for i in vlist:
    print(f"\n\n\tI'm checking to upgrade {i}")
    command = ["pip", "install", '--upgrade', i]
    upgrade = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                         text=True, check=False)
    print(upgrade.stdout)

# """manage errors"""
# exception = ["\n\n",
#             "*********************************\n",
#             "\n*********************************",
#             "I was not be able to upgrade these packages:\t"]
# while upgrade.stderr != '':
#     error_str = upgrade.stderr
#     error_list = error_str.split()
#     error_package = error_list[3]
#     error_package = error_package.replace('\'', '')
#     error_package = error_package.replace('.', '')
#     command.remove(error_package)
#     error_package += ", "
#     exception = exception + [error_package]
#     upgrade = subprocess.run(command, stdout=subprocess.PIPE,
#                              stderr=subprocess.PIPE, text=True, check=False)

# print(upgrade.stdout)

# if len(exception) > 4:
#     for element in exception:
#         print(element)
