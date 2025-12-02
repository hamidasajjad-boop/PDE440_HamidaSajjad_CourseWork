cmake_minimum_required(VERSION 3.8)
project(ball_bot_pde4430)

find_package(ament_cmake REQUIRED)
find_package(xacro REQUIRED)

# No xacro build step needed — xacro is processed at runtime in launch file

ament_package()
