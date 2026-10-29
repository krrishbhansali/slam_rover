# Slam Rover

ROS 2 Humble differential-drive rover with a simulated RGB camera and 2D lidar,
Gazebo Classic worlds, SLAM Toolbox mapping, and Nav2 saved-map navigation.

The camera is an RGB camera; mapping uses the lidar and odometry, not camera images.
The drive uses Gazebo's differential-drive plugin rather than ros2_control.

## Build

From the workspace root (the directory containing `src/`):

```bash
source /opt/ros/humble/setup.bash
# Optional physical drivers, only when using the hardware launch files:
# sudo apt install ros-humble-v4l2-camera ros-humble-rplidar-ros
rosdep install --from-paths src --ignore-src -r -y --rosdistro humble
colcon build --symlink-install
source install/setup.bash
```

`package.xml` also declares the optional physical camera and lidar drivers.
Initialize rosdep if it has not already been configured on your machine.
In every new terminal, source `/opt/ros/humble/setup.bash` and your workspace's
`install/setup.bash` before running the commands below.

## Simulation

```bash
ros2 launch slam_rover launch_sim.launch.py
```

This starts robot_state_publisher, Gazebo, the rover, and simulated sensor plugins.
The default is the included `obstacles.world`. Use `gui:=false` for headless Gazebo,
or `world:=/absolute/path/to/file.world` to select a different world.
Do not start `rsp.launch.py`, `camera.launch.py`, or `rplidar.launch.py` alongside
this simulation: the required description and simulated sensors are already running.

To drive, run in a separate terminal:

```bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```

Install `ros-humble-teleop-twist-keyboard` if needed. Follow its on-screen key bindings.
Stop keyboard control before allowing Nav2 to control the rover.

## Mapping

Leave the simulation running and open another terminal:

```bash
ros2 launch slam_rover slam.launch.py
```

This starts SLAM Toolbox with `config/slam.yaml` and RViz. It does not start a second
simulation. Drive around the environment to build the map. Use `rviz:=false` to
skip RViz. For a physical robot with working odometry/TF and sensors, use
`use_sim_time:=false`.

Save the map from a sourced terminal at the workspace root:

```bash
mkdir -p maps
ros2 run nav2_map_server map_saver_cli -f "$PWD/maps/room" \
  --ros-args -p use_sim_time:=true
```

This saves an occupancy image and YAML file for Nav2; it does not save the full
SLAM Toolbox pose graph for continued mapping.

## Saved-map navigation

Keep the simulation running. Stop the SLAM launch and keyboard teleoperation, then:

```bash
ros2 launch slam_rover navigation.launch.py map:=/absolute/path/to/maps/room.yaml
```

This starts AMCL, map server, Nav2, and RViz with `config/nav2_params.yaml`.
Set the initial pose in RViz with **2D Pose Estimate**, then choose a goal with
**Nav2 Goal**. Use `rviz:=false` to skip RViz. Nav2 tuning is a starting point;
validate goal execution and collision clearance for your intended environment.
Do not run AMCL and SLAM Toolbox together: both would publish `map -> odom`.

## Launch files

| File | Purpose |
| --- | --- |
| `launch_sim.launch.py` | Complete Gazebo simulation; includes `rsp.launch.py` |
| `rsp.launch.py` | Robot description and robot_state_publisher only |
| `slam.launch.py` | SLAM Toolbox and optional RViz; requires a running rover |
| `navigation.launch.py` | Saved-map localization/navigation and optional RViz; requires a running rover |
| `camera.launch.py` | Optional physical V4L2 camera (`video_device:=/dev/video0`) |
| `rplidar.launch.py` | Optional physical RPLidar (`serial_port:=/dev/ttyUSB0`) |

Physical driver launches are helpers, not a complete hardware bringup: motor control,
odometry, correct TF, device permissions and model-specific driver settings remain
necessary. `rsp.launch.py` alone does not publish changing wheel joint positions.

## Important topics and frames

- `/cmd_vel`: velocity commands (`geometry_msgs/msg/Twist`).
- `/odom`: simulated wheel odometry.
- `/scan`: lidar (`laser_frame`).
- `/camera/image_raw` and `/camera/camera_info`: simulated camera (`camera_link_optical`).
- `/map`: occupancy grid from SLAM or the navigation map server.
- TF: `map -> odom -> base_link`, then the body and sensor frames.

## Verification

On the local ROS 2 Humble installation, the renamed package built, the Xacro/URDF
parsed, and launch arguments resolved. A headless Gazebo check received camera,
lidar, odometry, TF and SLAM map messages and saved a map. See `docs/verification.md`
for the navigation bringup result and limits of these checks.

## Licensing

Maintainer: **Krrish Bhansali** (`krrishbhansali2005@gmail.com`).

Original contributions use **Apache-2.0**; see [LICENSE](LICENSE). Licensing for
some inherited robot resources remains unresolved. The complete repository is
not declared Apache-2.0. See [NOTICE](NOTICE) and
[licensing scope](docs/LICENSING.md) for details.
