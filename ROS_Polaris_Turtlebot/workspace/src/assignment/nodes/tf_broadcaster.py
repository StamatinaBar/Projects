#!/usr/bin/env python

'''
Broadcaster node which broadcasts coordinates frames of polaris and turtlebot to tf and their transformation as they move related to frame earth. 

'''


import rospy
import tf
import turtlesim.msg
import geometry_msgs.msg

#get messages of robot's position and name
#implement transformations from parent frame "earth" to children (polaris,turtlebot)
#position msg.z=0 because we have a 2D simulation
def handle_robot_pose(msg, name):
    br = tf.TransformBroadcaster()
    br.sendTransform((msg.x, msg.y, 0),
                     tf.transformations.quaternion_from_euler(0, 0, msg.theta),
                     rospy.Time.now(),
                     name,
                     "earth")

    #publish in velocity topic to make polaris moving in a circle
    robot_vel=rospy.Publisher("polaris/cmd_vel",geometry_msgs.msg.Twist,queue_size=1)
    move=geometry_msgs.msg.Twist()

    move.linear.x=1.0
    move.linear.y=2.0
    move.angular.z=-0.4

    robot_vel.publish(move)

def tf_publisher():
    #create node broadcaster
    rospy.init_node('tf_broadcaster')
    #get turtle names from parameter server
    name = rospy.get_param('~turtle')
    #subscribe to /pose topic to get turtle position and call callback function handle_robot_pose
    rospy.Subscriber('/%s/pose' % name,
                     turtlesim.msg.Pose,
                     handle_robot_pose,
                     name)

    rospy.loginfo("Publishing TF data...")

    rospy.spin()

if __name__ == '__main__':
    tf_publisher()
   
