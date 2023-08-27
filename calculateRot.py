import pandas as pd
from scipy.spatial.transform import Rotation as R
import numpy as np
# Read the CSV file
data_original = pd.read_csv('grab_new.csv')

# This function will compute the rotation angle between two quaternions
def rotation_angle(rotation1, rotation2):
    r1 = R.from_quat(rotation1)
    r2 = R.from_quat(rotation2)
    relative_rotation = r2.inv() * r1
    return relative_rotation.magnitude()

# Create an empty DataFrame to store the computed rotation angles
rotation_angles = pd.DataFrame(columns=['Name', 'Value'])

# Compute the number of groups
num_groups = len(data_original) // 24

# Get the first group of data
first_group = data_original.iloc[0:24, :]

# Compute the rotation angle for each group compared to the first group
for g in range(1, num_groups):
    group = data_original.iloc[g*24:(g+1)*24, :]
    # Reset the index of the group
    group.reset_index(drop=True, inplace=True)
    for i in range(24):
        rotation1 = first_group.iloc[i, 1:5]
        rotation2 = group.iloc[i, 1:5]
        angle = rotation_angle(rotation1, rotation2)
        new_row = pd.DataFrame({'Name': [first_group.iloc[i, 0]], 'Value': [angle]})
        rotation_angles = pd.concat([rotation_angles, new_row], ignore_index=True)

# Save the rotation angles to a new CSV file
rotation_angles.to_csv('grab_new_rot.csv', index=False)
