import os
hexdata = []
bindata = []
asciidata = []
chardata = []
outfile = 'out.txt'

def writelog(message):
    file = open(outfile, 'a+')
    file.write(message + '\n')
    file.close()

with open('Disc 1 - 2 - Master of Puppets.mp3','rb') as file:
    first_32 = file.read(256)

for i in range(0, len(first_32)):
    hexdata.append(hex(first_32[i]))

for i in range(0, len(first_32)):
    bindata.append(bin(first_32[i]))

for i in range(0, len(first_32)):
    asciidata.append(ascii(first_32[i]))


for i in range(0, len(first_32)):
    chardata.append(chr(first_32[i]))

# for i in range(0, len(first_32)):
#     writelog(str(hex(first_32[i])) + '  ' + str(bin(first_32[i])) + '  ' + str(ascii(first_32[i])) + '  ' + str(chr(first_32[i])))

for i in range(0, len(first_32)):
    writelog('{:<6}{:<10} {:<6}{:<2}'.format(str(hex(first_32[i])), str(bin(first_32[i])), str(ascii(first_32[i])), str(chr(first_32[i]))))

# print(*chardata)
# print('\n\r')
# print(*hexdata)
# print('\n\r')
# print (*bindata)
# print('\n\r')
# print(*asciidata)    