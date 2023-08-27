import os
import pybullet as p
import pybullet_data as pd
import numpy as np
import pandas as pds

p.connect(p.GUI)
p.setGravity(0,0,0)

p.setAdditionalSearchPath(pd.getDataPath())
p.resetDebugVisualizerCamera(cameraDistance=0.5,cameraYaw=30,
                             cameraPitch=-30,cameraTargetPosition=[0.5,-0.9,0.75])

handuid=p.loadURDF(os.path.join(pd.getDataPath(),r"C:\Users\Aliewanre\PycharmProjects\pythonProject3\simox_ros-master\simox_ros-master\sr_grasp_description\urdf\shadowhand.urdf"),useFixedBase=True)
joints = [p.getJointInfo(handuid, i) for i in range(p.getNumJoints(handuid))]
print(joints)

data = pds.read_csv('bettery x-y_rotated.csv')
dataset = data.values.tolist()

num_joints = p.getNumJoints(handuid)
# 遍历每个关节，打印关节的名称
#for i in range(num_joints):
    #joint_info = p.getJointInfo(handuid, i)
    #joint_name = joint_info[1]
    #print(f"Joint {i} name: {joint_name.decode('utf-8')}")

# Print the initial angle of each joint
#for i in range(num_joints):
    #joint_info = p.getJointState(handuid, i)
    #print(f"Joint {i} angle: {joint_info[0]}")


for data in dataset:
    # 在每个仿真步骤中，设置每个关节的目标位置
    for i, target_position in enumerate(data):
        p.setJointMotorControl2(handuid, i, p.POSITION_CONTROL, targetPosition=target_position)

    # 让仿真向前运行一步
    p.stepSimulation()

    for i in range(num_joints):
        #print(f"Joint {i} state: {p.getJointState(handuid, i)}")
        print(f"Link {i} state: {p.getLinkState(handuid, i)}")
    #while 1:
        #p.stepSimulation()
