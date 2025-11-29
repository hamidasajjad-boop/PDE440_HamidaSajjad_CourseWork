cmake_minimum_required(VERSION 3.8)
project(ball_bot_pde4430)

find_package(ament_cmake REQUIRED)
find_package(xacro REQUIRED)

# Generate URDF from XACRO
xacro_add_files(
  urdf/ball_bot.xacro
  INSTALL DESTINATION share/${PROJECT_NAME}/urdf
)

install(
  DIRECTORY launch urdf worlds
  DESTINATION share/${PROJECT_NAME}
)

ament_package()
