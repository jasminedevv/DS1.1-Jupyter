import pandas as pd
import sqlite3
import requests

connection = sqlite3.connect("../datasets/data.db")
spammers = pd.read_sql_query("SELECT id FROM users WHERE spamprob <= 0.01", connection)

spammers.to_csv("../csv/spammers.csv", sep=',',index=False)