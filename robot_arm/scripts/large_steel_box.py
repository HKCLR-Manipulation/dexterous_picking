from subprocess import TimeoutExpired
from urx import Robot
import time

import math
from math import pi, sin, cos, atan2
from math import sqrt, pi, acos, sin, cos
import math3d as m3d
import numpy as np


def set_home_configuration(robot):

    robot.set_tcp((0, 0, 0, 0, 0, 0))
    time.sleep(1)

    pose = m3d.Transform()
    pose.pos = m3d.Vector([0.39, 0.05, 0.21])
    pose.orient.rotate_x(pi)
    pose.orient.rotate_y(-10*pi/180)
    pose.orient.rotate_z(-pi/4)

    robot.set_pose(pose, acc=0.01, vel=0.01, wait=True)
    time.sleep(1)


def approach_object(robot):
    """
    gently press the object against the wall-like support
    """

    while True:
        print(robot.get_tcp_force()[0])
        if robot.get_tcp_force()[0]>-40:
            robot.speedl((0.004, 0, 0, 0, 0, 0), 0.01, min_time=10)
        else:
            robot.stopl(0.5)
            break
    


def tilt_force_motion(robot, z_des, theta_des):
    """
    tilt up the object while pressing it, and at the same time, reorient the end-effector
    """

    err_z = robot.getl()[2]-z_des
    err_theta = abs(robot.getl()[4])-theta_des

    
    while np.linalg.norm([err_z,err_theta])>0.05:

        x=robot.get_orientation().inverse*m3d.Vector([0, 0, -0.15*err_z])
        y_pos=robot.get_orientation().inverse*m3d.Vector([0.02, 0, 0])
        y_neg=robot.get_orientation().inverse*m3d.Vector([-0.02, 0, 0])


        if robot.get_tcp_force()[0]>-5:
            robot.speedl_tool((x[0]+y_pos[0], 0, x[2]+y_pos[2], 0, 0.1*err_theta, 0), 0.01, min_time=1)

        else:
            robot.speedl_tool((x[0]+y_neg[0], 0, x[2]+y_neg[2], 0, 0.1*err_theta, 0), 0.01, min_time=1)

        err_z = robot.getl()[2]-z_des
        err_theta = abs(robot.getl()[4])-theta_des

    robot.stopl(0.5)


def regrasp(robot, angle):
    """
    rotate end-effector about contact point to tuck it underneath the object
    """

    pose = m3d.Transform()
    pose.orient.rotate_y((-angle)*pi/180)

    robot.add_pose_tool(pose, acc=0.01, vel=0.01, wait=True)  
    time.sleep(1)


def rotate_tip(robot, angle):
    """
    rotate end-effector about its distal tip to bring the object into a shallower angle
    """

    time.sleep(1)

    pose = m3d.Transform()
    pose.orient.rotate_y((-angle)*pi/180)

    robot.add_pose_tool(pose, acc=0.01, vel=0.01, wait=True)  
    time.sleep(1)



def lift_up(robot):
    """
    lift and retract the end-effector to detach the object from the supporting surfaces
    """

    pose = m3d.Transform()
    pose.pos.x = -0.01

    robot.add_pose_base(pose, acc=0.01, vel=0.01, wait=True)  
    time.sleep(1)

    pose = m3d.Transform()
    # pose.pos.x = -0.03
    pose.pos.z = 0.10
    pose.orient.rotate_y((-5)*pi/180)

    robot.add_pose_base(pose, acc=0.01, vel=0.01, wait=True) 
    time.sleep(1)



def main():

    robot = Robot("192.168.0.15", use_rt=True)

    robot.set_tcp((0, 0, 0, 0, 0, 0))
    time.sleep(1)


    set_home_configuration(robot)
    time.sleep(2)
    
    frame0 = m3d.Transform(robot.get_orientation().inverse, m3d.Vector(0,0,0))
    frame1 = m3d.Transform(robot.get_orientation().inverse, m3d.Vector(0.09/sqrt(2), 0.09/sqrt(2), 0.14))
    frame2 = m3d.Transform(robot.get_orientation().inverse, m3d.Vector(-0.07/sqrt(2), -0.07/sqrt(2), 0.28))

    robot.set_tcp(frame0)
    time.sleep(1)


    approach_object(robot)

    tilt_force_motion(robot, z_des=0.35, theta_des=np.radians(42))


    robot.set_tcp(frame1)
    time.sleep(1)


    regrasp(robot, angle=55)


    robot.set_tcp(frame2)
    time.sleep(1)


    rotate_tip(robot, angle=36.)
    
    
    lift_up(robot)



if __name__ == "__main__":
    main()
