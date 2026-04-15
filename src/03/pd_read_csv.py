from tempfile import NamedTemporaryFile

import pandas as pd

# create a file that is deleted as soon as the program ends
with NamedTemporaryFile(mode='w', delete=False, suffix='.csv') as temp_file:

    temp_file.write(
"""
int_column,float_column,date_column
1,3.14,2023-08-17 10:30:00
2,2.71,2023-08-17 12:45:00
3,1.618,2023-08-17 15:00:00
"""
    )

# Define data types for columns
data_types = {
    'int_column': int,
    'float_column': float,
}

# Read the CSV file with specified data types
df = pd.read_csv(temp_file.name, dtype=data_types, parse_dates=["date_column"])

print(df)