import Bio.Entrez as ezez.
email = "adegbesan4olabisi@gmail.com"
#term_name = input("what is your search term?: ")

handle = ez.egquery(term="Helicobacter Pylori")
record = ez.read(handle)
for row in record["eGQueryResult"]:
    print(row["DbName"], row["Count"])

def search():
    with ez.esearch(db="sequences", term="Helicobacter Pylori[title]", retmax=100, retmode="xml") as query:
        record_seq =ez.read(query)
    print(row["DbName"], row["Count"])
 return record_seq["IdList"]

for ids in record_seq["IdList"]:
    with ez.esummary(db="sequences", id=ids) as handle:
        record = ez.read(handle)
    print(record)
