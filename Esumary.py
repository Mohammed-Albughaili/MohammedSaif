import Bio.Entrez as ez


ez.email = "Mohammed Albughaili@gmaili.com"

id_list = ["27604556", "19304878", "18606172", "16403221", "16377612", "14871861", "14630660"]

for ids in id_list:
    with ez.esummary(db="pubmed", id=ids) as handle:
        record = ez.read(handle)

    print("Journal info\nid:",record[0]["Id"],"\nTitle: ",record[0]["Title"])


with ez.esearch(db="Gene", term="ALDH18A1", id=ids) as query:
        record_gene = ez.read(query)

for ids in record_gene["IdList"]:
    with ez.esummary(db="gene", id=ids) as handle:
        record = ez.read(handle)
    print(record)

with ez.esearch(db="Protein", term="PYCR1", id=ids) as query:
    record_Protein = ez.read(query)

for ids in record_Protein["IdList"]:
        with ez.esummary(db="Protein", id=ids) as handle:
            record = ez.read(handle)
        print(record)
