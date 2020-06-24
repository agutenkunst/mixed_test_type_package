#!/usr/bin/env python

import unittest
import time
import rospy

class TestModuleF(unittest.TestCase):
    # Nothing is done here with ModuleF since it is a node loaded separately
    # Usually here you would trigger the ROS Api (topics, services) of the node. Feel free to add.
    def test(self):
        self.assertTrue(True)

if __name__ == '__main__':
    import rostest
    rospy.init_node('moduleF_rostest_unittest')
    rostest.rosrun('mixed_test_type_package', 'moduleF_rostest_unittest', TestModuleF)
