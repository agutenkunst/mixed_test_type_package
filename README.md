# mixed_test_type_package
This package contains a mixture of pytest and nosetests(unittest) and serves
as a foundation for work on
- https://github.com/mikeferguson/code_coverage
- https://github.com/machinekoder/ros_pytest

## Usage
```
rm -rf build/ devel/
catkin_make -DENABLE_COVERAGE_TESTING=ON
catkin_make -DENABLE_COVERAGE_TESTING=ON mixed_test_type_package_coverage -j1
see ~/.ros/htmlcov/index.html
```

one-liner:

```rm -rf build/ devel/ && catkin_make -DENABLE_COVERAGE_TESTING=ON && catkin_make -DENABLE_COVERAGE_TESTING=ON mixed_test_type_package_coverage -j1 && see ~/.ros/htmlcov/index.html```

## Coverage
The modules are expected to be checked 
| Module  | nosetest coverage | pytest_coverage | Comment                                            |     |
| ------- | ----------------- | --------------- | -------------------------------------------------- | --- |
| moduleA | 100%              |                 |                                                    |     |
| moduleB | 100%              |                 | Make sure results from moduleA are not overwritten |     |
| moduleC |                   | 100%            |                                                    |     |
| moduleD |                   | 100%            | Make sure results from moduleC are not overwritten |     |
| moduleE | 86%               | 86 %            | Combined: 100%                                     |     |