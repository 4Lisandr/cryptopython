import pandas as pd
import requests

EM = "https://ethermine.org/miners/0x562d1588bA0A59f8A54CbD69728e7593333aC875/dashboard"


def get_content(start):
    return requests.get(start)


def get_list(req, write_csv=False):
    table = pd.read_html(req.text)[0]
    print(table)
    if write_csv:
        name = "Table.csv"
        table.to_csv(name, index=False)


# get_list(get_content(EM))
panda = requests.get(EM).text
print(panda)
