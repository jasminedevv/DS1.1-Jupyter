import pandas as pd
import sqlite3
import requests

connection = sqlite3.connect("datasets/data.db")
xx_ids = pd.read_sql_query("SELECT id FROM users WHERE ychrom = 0", connection)
xy_ids = pd.read_sql_query("SELECT id FROM users WHERE ychrom = 1", connection)

# ids = list(ids['id'])

xx_ids.to_csv("../csv/xx_chrom_users.csv", sep=',',index=False)
xy_ids.to_csv("../csv/xy_chrom_users.csv", sep=',',index=False)