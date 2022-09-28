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

#### Hardware and Software
* Each of the two joints connected to the ground is actuated by a HT8108-J6 DC motor (rated torque: 6.9 Nm at 24 volts, according to the manufacturer1) through a built-in planetary gear train. (http://www.haitaijd.cn/)
* The axes of the motors are horizontally offset to realize the desired manipulation behavior of the palm. The palm is 3D printed and covered with a high-friction rubber material. Its proximal end features a curved, ellipsical surface to facilitate tilting by rolling.

#### Implementation
To execute the picking operation:
```
cd dexterous_picking/robot_arm/scripts/5 bar mechanism

python Control by keys.py
```
To get plots of the result data:
```
cd dexterous_picking/robot_arm/scripts/5 bar mechanism

python Plot by Python.py
```

## 3. Impelmentation with a Conventional Manipulator

#### Hardware and Software
* [**UR3 robot arm**](https://www.universal-robots.com/products/ur3-robot/)
* [**curved end-effector**](https://github.com/HKCLR-Manipulation/dexterous_picking/blob/main/stl/curved_effector.stl)
* [**python-urx**](https://github.com/jkur/python-urx)

#### Implementation
To execute the picking operation on a [large steel box](https://www.ikea.com.hk/en/products/storing-and-washing/food-containers/hasthage-art-30524361?gclid=Cj0KCQjw7KqZBhCBARIsAI-fTKIbWbrx3Ruw259k6Z14LGE6XrLX204dTrdWhTHrctDt_6FZkfHPCtoaAqFcEALw_wcB&gclsrc=aw.ds)
```
cd dexterous_picking/robot_arm/scripts

python large_steel_box.py
```


