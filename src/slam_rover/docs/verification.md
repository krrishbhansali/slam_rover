# Local verification — 29 October 2026

Verified in `/home/krrish/github_ws` using ROS 2 Humble and Gazebo Classic:

- `colcon build --symlink-install --packages-select slam_rover` passed.
- All six launch files passed `ament_flake8` and launch-argument inspection.
- Xacro expansion and `check_urdf` passed; the robot name is `slam_rover`.
- Headless simulation spawned the `slam_rover` entity.
- Received `/scan` in `laser_frame`, `/odom`, `/tf`, `/camera/image_raw` in
  `camera_link_optical`, and `/map` in `map` while SLAM Toolbox was running.
- `nav2_map_server map_saver_cli` saved a 155 x 120 occupancy grid at 0.05 m/cell.
- With that map, simulation, and an explicit initial pose, all nine checked Nav2
  lifecycle nodes reached `active`: map_server, amcl, controller_server,
  planner_server, smoother_server, behavior_server, bt_navigator,
  waypoint_follower and velocity_smoother.
- The original package in the separate `amr_ws` workspace remained byte-for-byte
  unchanged across 22 files. Only the copy in this workspace was renamed.

These were headless data-flow and bringup checks. A completed navigation goal,
full-room exploration, GUI layout, and physical camera/lidar drivers were not
verified. Nav2 waits for AMCL's initial pose before global-costmap activation;
use RViz's 2D Pose Estimate during normal operation.

The old generated `build/`, `install/`, and `log/` directories were backed up
outside this workspace before rebuilding, avoiding stale package names and caches.
