import random
#random nucleotide and proteine generator

def split(word):
    return [char for char in word]

bases=[]
qlength = 222

nucs = ['A', 'C', 'G', 'T']
for nuc in nucs:
 for i in range(qlength):
  bases.append(nuc)

random.shuffle(bases)
outstr=''
for base in bases:
    outstr+=base
f = open('/home/helge/py/strpy/data/randnucleot2.txt', 'w')
f.write(">5_sequence\n")
f.write(str(outstr))
f.close()


sequ = list(set(split('MDQSNRYADLTLSEEKLIADGNHLLVAYRLKPAAGYGFLEVAAHVAAESSTGTNVEVSTTDDFTRGVDALVYEIDEAAFGDKGGLMKIAYPVDLFDPNLIDGHYNVSHMWSLILGNNQGMGDHEGLRMLDFMVPEQMVKKFDGPATDISDLWKVLGRPEVDGGYIAGTIIKPKLGLRPEPFAKACYDFWLGGDFIKNDEPQANQPFCPMETVIPMVAETMDRAQQETGEAKLFSANVTADFHEEMIKRGEYILGEFAKYGNEKHVAFLVDGFVTGPAGVTTARRNFPDTYLHFHRAGHGALTSYKSPMGMDPLCYMKLARLMGASGIHTGTMGYGKMEGHGDERVLAYMLERDECQGHYFNQKWYGMKPTTPIISGGMNALRLPGFFENLGHGNVINTCGGGSFGHIDSPAAGGTSLGQAYECWKTGADPIEYAKEHPEFARAFESFPSDADKIFPGWREKLGVHK')))
#to prevent the user from manually typing a d protein names
#print(sequ)

aacds = []
qlength = 111
for s in sequ:
  for i in range(qlength):
    aacds.append(s)
random.shuffle(aacds)
outstr=''
for aacd in aacds:
    outstr+=aacd

f = open('/home/helge/py/strpy/data/randprot2.txt', 'w')
f.write(">5_sequence\n")
f.write(str(outstr))
f.close()
