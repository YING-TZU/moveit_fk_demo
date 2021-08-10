#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2019 Wuhan PS-Micro Technology Co., Itd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import rospy, sys
import moveit_commander

class MoveItFkDemo:
    def __init__(self):
        # 初始化move_group的API
        moveit_commander.roscpp_initialize(sys.argv)

        # 初始化ROS节点
        rospy.init_node('moveit_fk_demo', anonymous=True)
 
        # 初始化需要使用move group控制的机械臂中的arm group
        arm = moveit_commander.MoveGroupCommander('arm')
        
        # 设置机械臂运动的允许误差值
        arm.set_goal_joint_tolerance(0.001)

        # 设置允许的最大速度和加速度
        arm.set_max_acceleration_scaling_factor(0.5)
        arm.set_max_velocity_scaling_factor(0.5)
        
        # 控制机械臂先回到初始化位置
        arm.set_named_target('home')
        arm.go()
        rospy.sleep(1)

         
#1        # 设置机械臂的目标位置，使用六轴的位置数据进行描述（单位：弧度）
        joint_positions = [0.085870199198, -0.53791047546, 0.14049900479, 1.5592771537, -1.4681709668, 0.54332099615]
        arm.set_joint_value_target(joint_positions)
        arm.go()
        rospy.sleep(1)
#2
        joint_positions2 = [0.10018189906, -0.64786621834, 0.033510321638, 1.9893262814, -1.752310569, 0.95801122642]
        arm.set_joint_value_target(joint_positions2)
        # 控制机械臂完成运动
        arm.go()
        rospy.sleep(1)
#3
        joint_positions3 = [0.14189526819, -0.73914693822, 0.046600291028, 2.1230185021, -1.9214329735, 0.95801122642]
        arm.set_joint_value_target(joint_positions3)
        # 控制机械臂完成运动
        arm.go()
        rospy.sleep(1)
#4
        joint_positions4 = [0.15934856071, -0.73286375291, 0.047472955654, 2.1614157457, -1.9118336626, 1.3681636006]
        arm.set_joint_value_target(joint_positions4)
        # 控制机械臂完成运动
        arm.go()
        rospy.sleep(1)
#5
        joint_positions5 = [0.097214839336, -0.59899699928, 0.10088003077, 1.7585937543, -1.5406021307, 1.1786208439]
        arm.set_joint_value_target(joint_positions5)
        # 控制机械臂完成运动
        arm.go()
        rospy.sleep(1)
#6
        joint_positions6 = [0.10960667703, -0.54401912785, 0.19076448724, 1.4666001705, -1.4014993894, 0.78435096585]
        arm.set_joint_value_target(joint_positions6)
        # 控制机械臂完成运动
        arm.go()
        rospy.sleep(1)
#7
        joint_positions7 = [0.12479104152, -0.54908058268, 0.1745329252, 1.5112805993, -1.3842206298, 0.83688537633]
        arm.set_joint_value_target(joint_positions7)
        # 控制机械臂完成运动
        arm.go()
        rospy.sleep(1)
#8
        joint_positions8 = [0.11938052084, -0.59341194568, 0.077841684639, 1.8243926671, -1.5294320235, 1.1262609663]
        arm.set_joint_value_target(joint_positions8)
        # 控制机械臂完成运动
        arm.go()
        rospy.sleep(1)
#9
        joint_positions9 = [0.17051866792, -0.70685834706, 0.03054326191, 2.207317905, -1.8661060362, 1.5364133405]
        arm.set_joint_value_target(joint_positions9)
        # 控制机械臂完成运动
        arm.go()
        rospy.sleep(1)


        # 控制机械臂先回到初始化位置
        arm.set_named_target('home')
        arm.go()
        rospy.sleep(1)
        
        # 关闭并退出moveit
        moveit_commander.roscpp_shutdown()
        moveit_commander.os._exit(0)

if __name__ == "__main__":
    try:
        MoveItFkDemo()
    except rospy.ROSInterruptException:
        pass
