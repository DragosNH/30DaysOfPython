# --- Day 25: 30 Days of python programming ---
import pandas as pd
import numpy as np


data = {
    'Name': ['John', 'Bob', 'George', 'Janne', 'Milly', 'Rebecca'],
    'Country': list(['Romania', 'France', 'Marroco', 'Vietnam', 'Egypt', 'US']),
    'City': list(['Ploiesti', 'Mulhouse', 'Casablanca', 'Hanoi', 'Cairo', 'Denver'])
}

df = pd.DataFrame(data, columns=['Name','Country','City'])
print(df[:5])