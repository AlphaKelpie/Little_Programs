"""
The code that would fit at $PLACEHOLDER$ is used to print colored text in the
terminal using ANSI escape sequences. Each line of code sets the color of the
text and then prints the color code itself.
"""
print("Cambia colore al testo:")
print(f"\033[0;30m1;30m\033[0;0m nero")
print(f"\033[0;90m0;90m\033[0;0m grigio")
print(f"\033[0;31m0;31m\033[0;0m rosso")
print(f"\033[0;91m0;91m\033[0;0m chiaro")
print(f"\033[0;32m1;32m\033[0;0m verde")
print(f"\033[0;92m0;92m\033[0;0m chiaro")
print(f"\033[0;33m0;33m\033[0;0m giallo")
print(f"\033[0;93m0;93m\033[0;0m chiaro")
print(f"\033[0;34m0;34m\033[0;0m blu")
print(f"\033[0;94m0;94m\033[0;0m chiaro")
print(f"\033[0;35m0;35m\033[0;0m magenta")
print(f"\033[0;95m0;95m\033[0;0m chiaro")
print(f"\033[0;36m0;36m\033[0;0m ciano")
print(f"\033[0;96m0;96m\033[0;0m chiaro")
print(f"\033[0;37m0;37m\033[0;0m bianco")
print(f"\033[0;97m0;97m\033[0;0m chiaro")

print("\nCambia colore allo sfondo:")
print(f"\033[0;40m0;40m\033[0;0m nero")
print(f"\033[0;100m0;100m\033[0;0m chiaro")
print(f"\033[0;41m0;41m\033[0;0m rosso")
print(f"\033[0;101m0;101m\033[0;0m chiaro")
print(f"\033[0;42m0;42m\033[0;0m verde")
print(f"\033[0;102m0;102m\033[0;0m chiaro")
print(f"\033[0;43m0;43m\033[0;0m giallo")
print(f"\033[0;103m0;103m\033[0;0m chiaro")
print(f"\033[0;44m0;44m\033[0;0m blu")
print(f"\033[0;104m0;104m\033[0;0m chiaro")
print(f"\033[0;45m0;45m\033[0;0m magenta")
print(f"\033[0;105m0;105m\033[0;0m chiaro")
print(f"\033[0;46m0;46m\033[0;0m ciano")
print(f"\033[0;106m0;106m\033[0;0m chiaro")
print(f"\033[0;47m0;47m\033[0;0m bianco")
print(f"\033[0;107m0;107m\033[0;0m chiaro")

print("\nCambia colore al testo e allo sfondo:")
for i in range(8):
    for j in range(8):
        print(f"\033[0;{30 + i};{40 + j}m0;{30 + i};{40 + j}m\033[0;0m")

print("\nColore sfumature (testo):")
for i in range(16, 256):
    print(f"\033[1;38;5;{i}m1;38;5;{i}m\033[0;0m")
print("\nSelezionando 0;48;5;<n>m si cambia il colore dello sfondo.")

print("\nCambia stile del testo:")
print(f"\033[0;30m0;30m\033[0;0m normale")
print(f"\033[1;30m1;30m\033[0;0m grassetto")
print(f"\033[2;30m2;30m\033[0;0m debole")
print(f"\033[3;30m3;30m\033[0;0m corsivo")
print(f"\033[4;30m4;30m\033[0;0m sottolineato")
print(f"\033[7;30m7;30m\033[0;0m invertito")
print(f"\033[8;30m8;30m\033[0;0m occulta")
print(f"\033[9;30m9;30m\033[0;0m barrato")
print(f"\033[20;30m20;30m\033[0;0m gotico")
print(f"\033[21;30m21;30m\033[0;0m doppio sottolineato")

print(f"\033[51;30m51;30m\033[0;0m incorniciato")
print(f"\033[52;30m52;30m\033[0;0m circondato")
print(f"\033[53;30m53;30m\033[0;0m sovrallineato")
