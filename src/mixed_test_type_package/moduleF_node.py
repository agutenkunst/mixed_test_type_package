#!/usr/bin/env python

import rospy

class ModuleF:
    def __init__(self):
        pass

    @staticmethod
    def return_true():
        return True

rospy.init_node('moduleF_node')
f = ModuleF()
f.return_true()
rospy.spin()

