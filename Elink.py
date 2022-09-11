import Bio.Entrez as ez
import xml.etree.ElementTree as ET

ez.email = "mohammed.albughaili@gmail.com"


# pmid = "19304878"
# record = ez.read(ez.elink(db="pubmed", dbfrom="pubmed", id=pmid))
# print(record)

# gene = "92344"
# record = ez.read(ez.elink(db="pubmed", dbfrom="protein", id=gene))
# print(record)

protein = "27604556"
record = ez.read(ez.elink(db="pubmed", dbfrom="pubmed", id=protein))
print(record)

# nucleotide = "27604556"
# record = ez.read(ez.elink(db="pubmed", dbfrom="pubmed", id=nucleotide))
# print(record)
