import xmltodict
import Bio.Entrez as ez

ez.email = "christoph-knorr@gmx.de"

# with ez.efetch(db="gene", id="92344", retmode="xml") as handle:
#     record2 = xmltodict.parse(handle)

with ez.efetch(db="protein", id="2187428178", retmode="xml") as handle:
    record2 = xmltodict.parse(handle)

print(record2)
#print(record2.keys())
print(record2["Entrezgene-Set"]["GBSeq"]["GBSeq_definition"])
print(record2["Entrezgene-Set"]["GBSeq"]["GBSeq_source"])
print(record2["Entrezgene-Set"]["GBSeq"]["GBSeq_sequence"])
