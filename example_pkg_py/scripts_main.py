#!/bin/python3
import rclpy
from rclpy.node import Node

from example_pkg_py import a
from example_pkg_py.B import b
from example_pkg_py.C.C_child import c

class example_node(Node):
    def __init__(self) -> None:
        super().__init__("scripts_main")
        self.self_introduction()
        
    def hello(self):
        print("Hello! I'm main")
    
    def self_introduction(self):
        class_a = a.classA()
        class_b = b.classB()
        class_c = c.classC()

        self.hello()
        class_a.hello()
        class_b.hello()
        class_c.hello()

        print("\ntomorrow...")

        self.hello()
        a.classA.hello(self)
        b.classB.hello(self)
        c.classC.hello(self)

def ros_main(args = None):
    rclpy.init(args=args)
    ros_class = example_node()
    
    try:
        rclpy.spin(ros_class)
    except KeyboardInterrupt:
        pass
    finally:
        ros_class.destroy_node()
        rclpy.shutdown()

if __name__=='__main__':
    ros_main()
