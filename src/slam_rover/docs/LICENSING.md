# Licensing scope

## Scope

The full Apache License, Version 2.0 text is in `../LICENSE`; scope notes are
in `../NOTICE`. Copyright 2026 Krrish Bhansali applies to original contributions
only; it does not claim ownership of inherited material.

Apache-2.0 covers original Slam Rover contributions, including original portions
of the new mapping/navigation launch wrappers and documentation. Modifications
to inherited files do not relicense their inherited portions. Previously licensed
third-party portions retain their upstream terms.

## Upstream robot resources: unresolved

Some robot resources were adapted from an upstream tutorial project. Their
applicable licensing has not been established. This workspace copy has no upstream
Git history establishing file-level provenance. A license attached to a base
template alone does not establish the terms of later robot-specific additions.

The inherited robot descriptions, sensor/plugin definitions, worlds, existing
launch code, and other tutorial-derived portions therefore remain under
`LicenseRef-Upstream-Unspecified` until their licensing is established. This is
a status identifier, not a new license or permission grant.

Before presenting the full package as a licensed open-source release, obtain
applicable upstream terms/permission for those portions or replace them with
original or appropriately licensed equivalents. Adding an Apache LICENSE file does not establish permission for those portions.

## Nav2 resources

`config/nav2_params.yaml` and `config/navigation.rviz` are adapted from the local
ROS 2 Humble Nav2 defaults. Nav2 uses Apache-2.0. Keep upstream notices and credit:
https://github.com/ros-navigation/navigation2

Runtime dependencies such as ROS 2, Gazebo, RViz and SLAM Toolbox retain their own
licenses; installing them does not make them part of this project's license grant.
