import pandas as pd
import numpy as np

data = pd.read_csv('grab_new_rot.csv')
# Assume df is your DataFrame with columns 'Name' and 'Value'
df = data.copy()

# Create a new column 'Group' to identify each group of 24 rows
df['Group'] = df.index // 24

# Define the mapping and new column names as before
mapping = {
    'Hand_Index1': 'FFJ3',
    'Hand_Index2': 'FFJ2',
    'Hand_Index3': 'FFJ1',
    'Hand_Middle1': 'MFJ3',
    'Hand_Middle2': 'MFJ2',
    'Hand_Middle3': 'MFJ1',
    'Hand_Ring1': 'RFJ3',
    'Hand_Ring2': 'RFJ2',
    'Hand_Ring3': 'RFJ1',
    'Hand_Pinky0': 'LFJ5',
    'Hand_Pinky1': 'LFJ4',
    'Hand_Pinky2': 'LFJ3',
    'Hand_Pinky3': 'LFJ2',
    'Hand_Thumb0': 'THJ5',
    'Hand_Thumb1': 'THJ4',
    'Hand_Thumb2': 'THJ3',
    'Hand_Thumb3': 'THJ2',
}
columns_new = ['WRJ2', 'WRJ1', 'FFJ4', 'FFJ3', 'FFJ2', 'FFJ1', 'FFtip', 'MFJ4', 'MFJ3', 'MFJ2', 'MFJ1', 'MFtip', 'RFJ4', 'RFJ3', 'RFJ2', 'RFJ1',
               'RFtip', 'LFJ5', 'LFJ4', 'LFJ3', 'LFJ2', 'LFJ1', 'LFtip', 'THJ5', 'THJ4', 'THJ3', 'THJ2', 'THJ1', 'thtip']

# Create a new DataFrame to hold the transformed data
df_new = pd.DataFrame(columns=columns_new)

# For each group of 24 rows...
for group, data in df.groupby('Group'):
    # Create a new row in the new DataFrame
    row_new = pd.Series(index=columns_new)
    # Fill the new row using the original data and the mapping
    for col_new in columns_new:
        if col_new in mapping.values():
            col_original = [k for k, v in mapping.items() if v == col_new][0]
            row_new[col_new] = data[data['Name'] == col_original]['Value'].values[0]
        else:
            row_new[col_new] = 0
    # Add the new row to the new DataFrame using pd.concat
    df_new = pd.concat([df_new, pd.DataFrame(row_new).transpose()])
df_new.to_csv('grab_new_rot2.csv', index=False)
print(df_new)
