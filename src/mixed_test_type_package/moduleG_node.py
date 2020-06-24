#!/usr/bin/env python

import rospy

class ModuleG:
    def __init__(self):
        pass

    @staticmethod
    def return_true():
        return True

rospy.init_node('moduleG_node')
g = ModuleG()
g.return_true()
rospy.spin()

