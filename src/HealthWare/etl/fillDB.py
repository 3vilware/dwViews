from .models import *
import pandas as pd

path = 'C:/Users/ricar/Documents/Universidad/7to/mineria/datawarehouse/db/couchBase/Establecimientos.csv'
pathEspera = 'C:/Users/ricar/Documents/Universidad/7to/mineria/datawarehouse/db/mongo/enEsperaOrg.csv'
pathTransplantes = 'C:/Users/ricar/Documents/Universidad/7to/mineria/datawarehouse/db/mysql/Trasplantes.csv'
pathDonantes = 'C:/Users/ricar/Documents/Universidad/7to/mineria/datawarehouse/db/postgres/donantes.csv'

doc = pd.read_csv(pathDonantes, encoding='latin-1')

headers = doc.head(2)

for col in headers:
    print("<th>", "FIELD", "</th>")

print("Table Data\n")
for col in headers:
    print("<td>", col, "</td>")
