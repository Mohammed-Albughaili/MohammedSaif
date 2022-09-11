import Bio.Entrez as ez
import xml.etree.ElementTree as ET
from Bio import SeqIO

ez.email = "mohammed.albughaili@gmail.com"

handle = ez.egquery(term="GORAB")
record = ez.read(handle)
# for row in record["eGQueryResult"]:
#     print(row["DbName"], row["Count"])

with ez.esearch(db="pubmed", term="GORAB[title]", retmax="100" ) as query:
    record_pub = ez.read(query)

pub_id = record_pub["IdList"]
#print(pub_id)
for i in pub_id:
    with ez.efetch(db="protein", id= i, rettype="fasta", retmode="text") as handle:
        record = SeqIO.read(handle, "fasta")
        print(record)
