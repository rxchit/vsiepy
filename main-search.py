from docsx import *
import math


class VecComp:
    def magnitude(self, concordance):
        if type(concordance) != dict:
            raise ValueError('Supplied Argument should be of type dict')
        total = 0
        for word, count in concordance.items():
            total += count ** 2
        return math.sqrt(total)

    def relation(self, concordance1, concordance2):
        if type(concordance1) != dict:
            raise ValueError('Supplied Argument 1 should be of type dict')
        if type(concordance2) != dict:
            raise ValueError('Supplied Argument 2 should be of type dict')
        # relevance = 0
        topvalue = 0
        for word, count in concordance1.items():
            if word in concordance2.keys():
                topvalue += count * concordance2[word]
        if (self.magnitude(concordance1) * self.magnitude(concordance2)) != 0:
            return topvalue / (self.magnitude(concordance1) * self.magnitude(concordance2))
        else:
            return 0

    def concordance(self, document):
        if type(document) != str:
            raise ValueError('Supplied Argument should be of type string')
        con = {}
        for word in document.split(' '):
            if word in con.keys():
                con[word] = con[word] + 1
            else:
                con[word] = 1
        return con


v = VecComp()

index = {
    0: v.concordance(docx[0].lower()),
    1: v.concordance(docx[1].lower()),
    2: v.concordance(docx[2].lower()),
    3: v.concordance(docx[3].lower()),
    4: v.concordance(docx[4].lower()),
    5: v.concordance(docx[5].lower()),
    6: v.concordance(docx[6].lower()),
}

searchterm = input('Enter Search Term: ')

matches = []

for i in range(len(index)):
    relation = v.relation(v.concordance(searchterm.lower()), index[i])
    if relation != 0:
        matches.append((relation, docx[i][:100]))

matches.sort(reverse=True)

for i in matches:
    print(i[0], i[1])
