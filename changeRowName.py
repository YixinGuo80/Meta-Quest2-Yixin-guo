import pandas as pd

# Read the CSV file
data = pd.read_csv('grab cup h 10 G.csv')

# Define the old and new names
old_names = data['Joint'].unique().tolist()
new_names = ['Hand_WristRoot', 'Hand_ForearmStub',
             'Hand_Thumb0', 'Hand_Thumb1', 'Hand_Thumb2', 'Hand_Thumb3',
             'Hand_Index1', 'Hand_Index2', 'Hand_Index3',
             'Hand_Middle1', 'Hand_Middle2', 'Hand_Middle3',
             'Hand_Ring1', 'Hand_Ring2', 'Hand_Ring3',
             'Hand_Pinky0', 'Hand_Pinky1', 'Hand_Pinky2', 'Hand_Pinky3',
             'Hand_ThumbTip', 'Hand_IndexTip', 'Hand_MiddleTip', 'Hand_RingTip','Hand_PinkyTip']

# Create a dictionary mapping old names to new names
name_dict = dict(zip(old_names, new_names))

# Replace the old names with the new names
data['Joint'] = data['Joint'].replace(name_dict)

# Select the columns to keep
data = data[['Joint', 'RotationX', 'RotationY', 'RotationZ', 'RotationW']]

# Save the modified DataFrame to a new CSV file
data.to_csv('grab_new.csv', index=False)
