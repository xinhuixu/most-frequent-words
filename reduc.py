f = open('warandpeace.txt', 'r')
l = f.read().split()
f.close()

#filter creates list of ele for which a func returns TRUE.

def freq(word, l):
    return len(filter(lambda w: w==word, l))

def g_freq(words, l):
    return len(filter(lambda w: w in words, l))

print "freq('Andrew', l):", freq('Andrew', l)
print "freq('war', l):", freq('war', l)

group = ['war','and','peace']
print "g_freq(['war','and','peace'], l):", g_freq(group, l)

