#!/usr/bin/env python 

'''
Follower node which listens to published tf messages,calculates relative transformation between polaris and turtlebot and make turtlebot orientates continuously in z axis(yaw) towards polaris.

'''

import roslib
roslib.load_manifest('assignment')
import rospy
import math
import tf
import geometry_msgs.msg
import turtlesim.srv

if __name__ == '__main__':
    #create node listener
    rospy.init_node('tf_listener')

    listener = tf.TransformListener()
    
    #service call for turtlebot to appear
    rospy.wait_for_service('spawn')
    spawner = rospy.ServiceProxy('spawn', turtlesim.srv.Spawn)
    spawner(6, 3, 0, 'turtlebot')

    #publish in velocity topic geometry messages
    robot_vel = rospy.Publisher('turtlebot/cmd_vel', geometry_msgs.msg.Twist,queue_size=1)

    rate = rospy.Rate(10.0)

    #we want to calcutate tranformation between polaris and turtlebot
    while not rospy.is_shutdown():
        try:
            (trans,rot) = listener.lookupTransform('/turtlebot', '/polaris', rospy.Time(0))
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            continue
        
        #calcutate angle difference between turtlebot and polaris
        angular = 4 * math.atan2(trans[1], trans[0])
        linear = 0.5 * math.sqrt(trans[0] ** 2 + trans[1] ** 2)

        #move turtlebot
        msg = geometry_msgs.msg.Twist() 
        #we publish angular vel only, since the robot only orientates in z axis
        msg.angular.z = angular
        robot_vel.publish(msg)

        rate.sleep()
