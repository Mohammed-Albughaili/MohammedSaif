import Bio.Entrez as ez



with ez.esearch(db="pubmed", term="GORAB[title]", retmax="20" ) as query:
    record_pub = ez.read(query)

if "27604556" in record_pub["IdList"]:
    print("Your article was found")

with ez.esearch(db="Gene", term="ALDH18A1", idtype="acc") as query:
    record_gene = ez.read(query)


print(record_gene["Count"])
print(record_gene["IdList"])

with ez.esearch(db="Protein", term="PYCR1", idtype="acc") as query:
    record_Protein = ez.read(query)


print(record_Protein["Count"])
print(record_Protein["IdList"])

with ez.esearch(db="nlmcatalog", term="genetics[Journal]", retmax="20") as handle:
    record_jou = ez.read(handle)

print(record_jou["Count"],"genetics journals found")
print("The first 20 are\n",record_jou["IdList"])
