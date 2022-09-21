# Dexterous Picking

## 1. Overview

This package is an implementation of robotic in-hand manipulation technique that can be applied to pick an object too large to grasp in a prehensile manner, by taking advantage of its contact interactions with a curved, passive end-effector, and two flat support surfaces. First, the object is tilted up while being held between the end-effector and the supports. Then, the end-effector is tucked into the gap underneath the object, which is formed by tilting, in order to obtain a grasp against gravity. We demonstrate successful picking of objects of various size and geometry using our technique through a set of experiments performed with a custom-made robotic device and a conventional robot arm. Our experiment results show that object picking can be performed reliably with our method using simple hardware and control, and when possible, with appropriate fixture design.


<p align="center">
  <img height="225" src="https://github.com/HKCLR-Manipulation/dexterous_picking/blob/main/media/our_robotic_palm.gif">
  <img height="225" src="https://github.com/HKCLR-Manipulation/dexterous_picking/blob/main/media/robot_arm.gif">
</p>


**Related Paper**

Y. Song, A. Nazir, D. Lau, and Y. Liu, "**Picking by Tilting: In-Hand Manipulation for Object Picking using Effector with Curved Form**," submitted to 2023 International Conference on Robotics and Automation (ICRA).
* [Video attachment](https://drive.google.com/file/d/1GR5UTZ1pRyEswY5hhTyq1UvXdeuAgBqq/view?usp=sharing)


## 2. Impelmentation with Our Robotic Palm


## 3. Impelmentation with a Conventional Manipulator

#### Hardware and Software
* [**UR3 robot arm**](https://www.universal-robots.com/products/ur3-robot/)
* [**curved end-effector**](https://github.com/HKCLR-Manipulation/dexterous_picking/blob/main/stl/curved_effector.stl)
* [**python-urx**](https://github.com/jkur/python-urx)
