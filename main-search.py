from itertools import count
from docsx import *
import math


class VecComp:
    def magnitude(self, concordance):
        if type(concordance) != dict:
            raise ValueError("Supplied argument is not a dictionary")
        total = 0
        for w, c in concordance.items():
            total += c ** 2
        return math.sqrt(total)

    def relation(self, con1, con2):
        if type(con1) != dict:
            raise ValueError("Supplied argument is not a dictionary")
        if type(con2) != dict:
            raise ValueError("Supplied argument is not a dictionary")
        relevance = 0
        topval = 0
        for w, c in con1.items():
            if w in con2:
                topval += c * con2[w]
            if (self.magnitude(con1) * self.magnitude(con2)) != 0:
                return topval/self.magnitude(con1) * self.magnitude(con2)
            else:
                return 0

    def concordance(self, doc):
        if type(doc) != str:
            raise ValueError("Supplied argument is not a string")
        con = {}
        for w in doc.split(' '):
            if w in con:
                con[w] = con[w]+1
            else:
                con[w] = 1
        return con


v = VecComp()

index = {
    0: v.concordance(documents[0].lower()),
    1: v.concordance(documents[1].lower()),
    2: v.concordance(documents[2].lower()),
    3: v.concordance(documents[3].lower()),
    4: v.concordance(documents[4].lower()),
    5: v.concordance(documents[5].lower()),
    6: v.concordance(documents[6].lower()),
}

searchterm = input('Enter Search Term: ')

matches = []

for i in range(len(index)):
    relation = v.relation(v.concordance(searchterm.lower()), index[i])
    if relation != 0:
        matches.append((relation, documents[i][:100]))

matches.sort(reverse=True)

for i in matches:
    print(i[0], i[1])
