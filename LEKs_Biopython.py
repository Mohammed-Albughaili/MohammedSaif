import Bio.Entrez as ez
from Bio import SeqIO
import xml.etree.ElementTree as ET



ez.email = "mohammed.albughaili@gmail.com"

with ez.einfo() as query:
    xml_string = query.read()
with ez.einfo() as query:
    parse_dict = ez.read(query)

print(xml_string)
print(parse_dict["DbList"])

with ez.einfo(db="Genome") as query:
        GenomeDict = ez.read(query)

print(GenomeDict["DbInfo"].keys())
for field in GenomeDict["DbInfo"]["FieldList"]:
    print("%(Name)s, %(FullName)s, %(Description)s" % field)



with ez.esearch(db="pubmed", term="GORAB[title]", retmax="20" ) as query:
    record_pub = ez.read(query)

if "27604556" in record_pub["IdList"]:
    print("Your article was found")


with ez.esearch(db="Protein", term="PYCR1", id=ids) as query:
    record_Protein = ez.read(query)

for ids in record_Protein["IdList"]:
        with ez.esummary(db="Protein", id=ids) as handle:
            record = ez.read(handle)
        print(record



with ez.efetch(db="protein", id="2187428178", rettype="fasta", retmode="text") as handle:
    record1 = SeqIO.read(handle, "fasta")
print(record1.id)

with ez.efetch(db="protein", id="2187428178", retmode="xml") as handle:
    record2 = ez.read(handle)

print(record2[0]["GBSeq_definition"])
print(record2[0]["GBSeq_source"])


protein = "27604556"
record = ez.read(ez.elink(db="pubmed", dbfrom="pubmed", id=protein))
print(record)
