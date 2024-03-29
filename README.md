# RPM Diffusion Policy

[[Project page]](https://milesprieb.github.io/umn_rpm_softbubble/)

## 🛠️ Installation

We recommend [Mambaforge](https://github.com/conda-forge/miniforge#mambaforge) instead of the standard anaconda distribution for faster installation: 
```console
$ mamba env create -f conda_environment.yaml
```
### 🦾 Real Robot
Hardware (for Rotate Bottle):
* 1x [UR5-CB3](https://www.universal-robots.com/cb3) or [UR5e](https://www.universal-robots.com/products/ur5-robot/) ([RTDE Interface](https://www.universal-robots.com/articles/ur/interface-communication/real-time-data-exchange-rtde-guide/) is required)
* 3x [RealSense D415](https://www.intelrealsense.com/depth-camera-d415/)
* 1x [Spark Teleoperation Arm](https://github.com/RPM-lab-UMN/Spark)(for teleop in 6D)
* 1x [Logitech G Extreme 3D Pro USB Joystick](https://www.amazon.com/Logitech-Joystick-Programmable-Weighted-Rapid-fire/dp/B00009OY9U/ref=asc_df_B00009OY9U/?tag=hyprod-20&linkCode=df0&hvadid=242012519199&hvpos=&hvnetw=g&hvrand=13455296410321615427&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9019667&hvtargid=pla-365326647739&psc=1&gclid=CjwKCAiAqNSsBhAvEiwAn_tmxWpI0FA5F8BWtP9rXqOIj4wvWpt-_XWver9XrMex7w2nhUEnpV4mpRoC0qQQAvD_BwE) (for teleop in 2D)
* 2x Soft Bubble Grippers
* USB-C cables and screws for RealSense

Software:
* Ubuntu 20.04.3 (tested)
* [RealSense SDK](https://github.com/IntelRealSense/librealsense/blob/master/doc/distribution_linux.md)
* Conda environment `mamba env create -f conda_environment_real.yaml`

## 🦾 Demo, Training and Eval on a Real Robot
Make sure your UR5 robot is running and accepting command from its network interface (emergency stop button within reach at all time), your RealSense cameras plugged in to your workstation (tested with `realsense-viewer`).

Start the demonstration collection script. Press "C" to start recording. Use Spark/Joystick to move the robot. The current codebase is setup to be compatible with the joystick and the axis of movement can be modified wihtin the demo script [here](https://github.com/RPM-lab-UMN/rpm_diffusion_policy/blob/1fc17214a7b2d3d4d646cb388aa9e044740e05b9/demo_real_robot.py#L143C103-L143C103). Press "S" to stop recording. 
```console
(robodiff)[diffusion_policy]$ python demo_real_robot.py -o data/demo_rotate_bottle --robot_ip 192.168.0.102
```

This should result in a demonstration dataset in `data/demo_rotate_bottle` with in the same structure as our example [Rotate Bottle training dataset](https://drive.google.com/drive/folders/16crkVl_co_ZVIiBG2vHfvlFCGSCfubKa?usp=sharing).

To train a Diffusion Policy, launch training with config:
```console
(robodiff)[diffusion_policy]$ python train.py --config-name=train_diffusion_unet_real_image_workspace task.dataset_path=data/demo_rotate_bottle
```
Edit [`diffusion_policy/config/task/real_pusht_image.yaml`](./diffusion_policy/config/task/rotate_bottle.yaml) if your camera setup is different.

Assuming the training has finished and you have a checkpoint at `data/outputs/blah/checkpoints/latest.ckpt`, launch the evaluation script with:
```console
python eval_real_robot.py -i data/outputs/blah/checkpoints/latest.ckpt -o data/eval_rotate_bottle --robot_ip 192.168.0.102
```
Press "C" to start evaluation (handing control over to the policy). Press "S" to stop the current episode.

## 🩹 Adding a Task
Read and imitate:
* `diffusion_policy/dataset/real_pusht_image_dataset.py`
* `diffusion_policy/env_runner/real_pusht_image_runner.py`
* `diffusion_policy/config/task/real_pusht_image.yaml`

Edit 'task' under 'defaults' in:
* `diffusion_policy/config/train_diffusion_unet_real_image_workspace.yaml`

Make sure that `shape_meta` correspond to input and output shapes for your task. Make sure `env_runner._target_` and `dataset._target_` point to the new classes you have added. When training, add `task=<your_task_name>` to `train.py`'s arguments.

