from Bio import SeqIO
import Bio.Entrez as ez


ez.email = "mohammed.albughaili@gmail.com"

handle = ez.efetch(db="gene", id="92344", rettype="null", retmode="text")
print(handle.read())

handle = ez.efetch(db="protein", id="2187428178", rettype="fasta", retmode="text")
print(handle.read())

with ez.efetch(db="protein", id="2187428178", rettype="fasta", retmode="text") as handle:
    record1 = SeqIO.read(handle, "fasta")
print(record1.id)

with ez.efetch(db="protein", id="2187428178", retmode="xml") as handle:
    record2 = ez.read(handle)

print(record2[0]["GBSeq_definition"])
print(record2[0]["GBSeq_source"])
