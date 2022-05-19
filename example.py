f = open('/Users/Tdols12/Desktop/CS classes and info/python/camelot.txt', 'w')
f.write("We're the knights of the round table \n We dance whenever we're able")
f.close()

with open("/Users/Tdols12/Desktop/CS classes and info/python/camelot.txt") as song:
    print(song.read(2))
    print(song.read(8))
    print(song.read())
