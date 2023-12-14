import zarr
import matplotlib.pyplot as plt
import numpy as np

## 10 ##
# (A) 90: 4, 5, 46 -> 
# (B) 45: 3, 2, 27, 43
# (C) 180: 30, 31, 32

# Specify the path to the .zarr directory
zarr_path = 'data/demo_handover'

# Open the .zarr directory
store = zarr.DirectoryStore(zarr_path)
root = zarr.group(store)

plt.plot(root['replay_buffer.zarr/data/action'])
plt.show()

# episode_idxs_10 = [2, 3, 4, 5, 27, 30, 31, 32, 43, 46]
# episode_idxs_30 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
#                    11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
#                    21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

# action = []
# robot_eef_pose = []
# robot_eef_pose_vel = []
# robot_gripper_state = []
# robot_joint = []
# robot_joint_vel = []
# stage = []
# timestamp = []
# episode_ends = []

# # create dict with the arrays above
# data_dict = {
#     'action': action,
#     'robot_eef_pose': robot_eef_pose,
#     'robot_eef_pose_vel': robot_eef_pose_vel,
#     'robot_gripper_state': robot_gripper_state,
#     'robot_joint': robot_joint,
#     'robot_joint_vel': robot_joint_vel,
#     'stage': stage,
#     'timestamp': timestamp,
#     'episode_ends': episode_ends
# }
# episode_end = 0

# for ep_idx in episode_idxs_30:
#     ep_start_stamp = root['replay_buffer.zarr/meta/episode_ends'][ep_idx-1]
#     ep_end_stamp = root['replay_buffer.zarr/meta/episode_ends'][ep_idx]
#     ep_diff = ep_end_stamp - ep_start_stamp
#     episode_end += ep_diff
#     data_dict['episode_ends'].append(episode_end)
#     for key in root['replay_buffer.zarr/data']:
#         for i in range(ep_start_stamp, ep_end_stamp):
#             data_dict[key].append(root['replay_buffer.zarr/data/'+key][i])

# # create a new zarr file
# zarr_path_new = 'data/demo_rotate_bottle_30'
# store_new = zarr.DirectoryStore(zarr_path_new)
# root_new = zarr.group(store_new)

# replay_buffer = root_new.create_group('replay_buffer.zarr')
# data = replay_buffer.create_group('data')
# meta = replay_buffer.create_group('meta')

# # create the arrays in the new zarr file
# for key in data_dict.keys():
#     if key != 'episode_ends':
#         if key == 'action':
#             data.create_dataset(key, data=data_dict[key], chunks=(100,))
#         else:
#             data.create_dataset(key, data=data_dict[key], chunks=(100,))
#     else:
#         meta.create_dataset(key, data=data_dict[key], chunks=(1,))

