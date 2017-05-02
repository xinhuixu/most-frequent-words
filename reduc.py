f = open('warandpeace.txt', 'r')
l = f.read()
f.close()


def freq(word, l):
    return len(filter(lambda w: w==word, l.split()))
