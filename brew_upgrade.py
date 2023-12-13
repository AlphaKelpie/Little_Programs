"""how to upgrade all packages by homebrew"""

from subprocess import run, PIPE


#create some string
ast_start = '\n\n' + '*'*30 + '\n' + '*'*30 + '\n'
ast_end = '\n' + '*'*30 + '\n' + '*'*30 + '\n\n'


#upload list of packages to not upgrade
not_update = []
with open("not_upgrade.txt","r") as input_file:
    lines = input_file.readlines()
for line in lines:
    line = line.replace('\n','')
    not_update.append(line)


#find outdated packages
packages = run(["brew", "outdated"], stdout=PIPE,
                          text=True, check=True)
outdated = stdout.split()
print(ast_start, 'Packages that are outdated:\n', '\n'.join(str(i) for i in outdated), ast_end)
print(ast_start, 'Packages that will not be upgraded:\n',
      '\n'.join(str(i) for i in not_update), ast_end)


#upgrade packages one by one & manage un-upgradable packages
command = ["brew", "upgrade", ""]
for i in outdated:
    if i in not_update:
        continue
    else:
        command[2] = i
        upgrade = run(command, stderr=PIPE,
                                 text=True, check=False)
        if upgrade.stderr != '':#remove this and create a control between list (if doesn't work)
            error_str = upgrade.stderr
            print(error_str)
            not_update.append(i)


#clean
print(ast_start, 'Clean cache and outdated downloads')
clean = subprocess.run(["brew", "cleanup", "--prune=all"], check=False)
print(ast_end)


#return packages still outdated
packages = subprocess.run(["brew", "outdated"], stdout=subprocess.PIPE,
                          text=True, check=False)
outdated = packages.stdout.split()
if outdated != []:
    outdated.sort()
    print(ast_start, 'I was not able to upgrade these packages:\n',
          '\n'.join(str(i) for i in outdated), ast_end)


#download packages not upgraded in txt
not_update.sort()
with open('not_upgrade.txt', 'w') as outfile:
    outfile.write('\n'.join(str(i) for i in not_update))
