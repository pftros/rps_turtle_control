cmake_minimum_required(VERSION 3.0.2)
project(rps_turtle_control)

find_package(catkin REQUIRED)

## The catkin_package macro generates cmake config files for your package
catkin_package()

#############
## Install ##
#############

# all install targets should use catkin DESTINATION variables
# See http://ros.org/doc/api/catkin/html/adv_user_guide/variables.html

# Mark executable scripts (Python etc.) for installation
# in contrast to setup.py, you can choose the destination
catkin_install_python(PROGRAMS
  scripts/turtle_control.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

# Mark launch files for installation
install(FILES
  launch/turtlesim_and_turtle_control.launch
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/launch
)
