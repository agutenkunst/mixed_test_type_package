cmake_minimum_required(VERSION 3.0.2)
project(mixed_test_type_package)

find_package(catkin REQUIRED COMPONENTS)

if(CATKIN_ENABLE_TESTING AND ENABLE_COVERAGE_TESTING)
  find_package(code_coverage REQUIRED)
  APPEND_COVERAGE_COMPILER_FLAGS()
endif()

catkin_python_setup()
catkin_package()

#############
## Testing ##
#############

if(CATKIN_ENABLE_TESTING)

  find_package(ros_pytest REQUIRED)

  if(ENABLE_COVERAGE_TESTING)
    include(CodeCoverage)
    append_coverage_compiler_flags()
  endif()

  catkin_add_nosetests(test/moduleA_unittest.py)
  catkin_add_nosetests(test/moduleB_unittest.py)
  add_pytests(test/moduleC_pytest.py)
  add_pytests(test/moduleD_pytest.py)

  # Both pytest and nosetest need to be combined for moduleE to have 100% coverage
  catkin_add_nosetests(test/moduleE_unittest.py)
  add_pytests(test/moduleE_pytest.py)


  # Fasest way to generate coverage - Make sure to run the test in sequence:
  # catkin_make -DCMAKE_BUILD_TYPE=Debug -DENABLE_COVERAGE_TESTING=ON tests
  # catkin_make -DCMAKE_BUILD_TYPE=Debug -DENABLE_COVERAGE_TESTING=ON pilz_minimal_python_pytest_coverage -j1
  # or
  # catkin config --cmake-args -DENABLE_COVERAGE_TESTING=ON -DCMAKE_BUILD_TYPE=Debug
  # catkin build pilz_minimal_python_pytest -v --no-deps --catkin-make-args tests
  # catkin build pilz_minimal_python_pytest -j 1 -v --no-deps --catkin-make-args pilz_minimal_python_pytest_coverage

  if(ENABLE_COVERAGE_TESTING)
    set(COVERAGE_EXCLUDES "*/${PROJECT_NAME}/test/*"
	    )

    add_code_coverage(
      NAME ${PROJECT_NAME}_coverage
      DEPENDS tests
    )
  endif()
endif()