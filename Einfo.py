import Bio.Entrez as ez


ez.email = "mohammed.albughaili@gmail.com"

with ez.einfo() as query:
    xml_string = query.read()
with ez.einfo() as query:
    parse_dict = ez.read(query)

# print(xml_string)
# print(parse_dict["DbList"])

with ez.einfo(db="pubmed") as query:
    PubMedDict = ez.read(query)

with ez.einfo(db="ClinVar") as query:
        ClinVarDict = ez.read(query)

with ez.einfo(db="Gene") as query:
        GeneDict = ez.read(query)

with ez.einfo(db="Genome") as query:
        GenomeDict = ez.read(query)

with ez.einfo(db="SNP") as query:
        SNPDict = ez.read(query)

print(ClinVarDict["DbInfo"].keys())
for field in ClinVarDict["DbInfo"]["FieldList"]:
    print("%(Name)s, %(FullName)s, %(Description)s" % field)

print(GenomeDict["DbInfo"].keys())
for field in GenomeDict["DbInfo"]["FieldList"]:
    print("%(Name)s, %(FullName)s, %(Description)s" % field)

print(ClinVarDict["DbInfo"].keys())
for field in ClinVarDict["DbInfo"]["FieldList"]:
    print("%(Name)s, %(FullName)s, %(Description)s" % field)

print(SNPDict["DbInfo"].keys())
for field in SNPDict["DbInfo"]["FieldList"]:
    print("%(Name)s, %(FullName)s, %(Description)s" % field)

print(PubMedDict["DbInfo"].keys())
for field in PubMedDict["DbInfo"]["FieldList"]:
    print("%(Name)s, %(FullName)s, %(Description)s" % field)
