import Bio.Entrez as ez
import xml.etree.ElementTree as ET

ez.email = "mohammed.albughaili@gmail.com"

# handle = ez.egquery(term="GORAB")
# record = ez.read(handle)
# for row in record["eGQueryResult"]:
#     print(row["DbName"], row["Count"])

# handle = ez.egquery(term="malaria")
# record = ez.read(handle)
# for row in record["eGQueryResult"]:
#     print(row["DbName"], row["Count"])


# handle = ez.egquery(term="ALDH18A1")
# record = ez.read(handle)
# for row in record["eGQueryResult"]:
#     print(row["DbName"], row["Count"])

# handle = ez.egquery(term="cancer")
# record = ez.read(handle)
# for row in record["eGQueryResult"]:
#     print(row["DbName"], row["Count"])

handle = ez.egquery(term="mls")
record = ez.read(handle)
for row in record["eGQueryResult"]:
    print(row["DbName"], row["Count"])
