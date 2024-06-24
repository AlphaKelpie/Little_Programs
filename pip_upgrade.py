"""how to upgrade pakages with pip automatically"""

from subprocess import run, PIPE

#upload list of packages to not upgrade
not_upgrade = []
with open('not_upgrade_pip.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        not_upgrade.append(line.split(' ')[0])

FAT = ['grpcio', 'opencv-python']

#upgrade pip
print("\tI upgrade pip")
run(['pip', 'install', 'pip', '--upgrade'], check=False)

print("\n\n\tI upgrade pip packages\n")
#find list of packages
pakages = run(["pip", "list"], stdout=PIPE,
                         text=True, check=False)
vlist = pakages.stdout

vlist = vlist.split()
del vlist[0:4]

i = 1
while i < len(vlist):
    del vlist[i]
    i += 1

#upgrade packages one by one
for i in vlist:
    print(f"\n\033[1;38;5;208mI'm checking to upgrade {i}\033[0;0m")
    if i in not_upgrade:
        print(f"\033[0;31m{i} will not be upgraded\033[0;0m")
        continue
    command = ["pip", "install", '--upgrade', i]
    if i in FAT:
        upgrade = run(command, text=True, check=False)
    else:
        upgrade = run(command, stdout=PIPE, text=True, check=True)
        out = upgrade.stdout
        outs = out.split('\n')

        del outs[-1]
        already_update = all("Requirement already satisfied:" in s for s in outs)
        if already_update:
            print(f"\033[1;36m{i} is already updated\033[0;0m\n")
        else:
            # print('\n'.join(str(i) for i in outs))
            print(f"\033[1;32m{outs[-1]}\033[0;0m\n")


#clean cache
print("\n\n\tI clean the cache")
run(['pip', 'cache', 'purge'], check=False)
