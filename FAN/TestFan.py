# import fan class
from fan_class import Fan

def test_fan(): # create function

    # create objects
    fan_1 = Fan()
    fan_2 = Fan()

    # set objects's properties
    fan_1.set_speed(Fan.fast_speed)
    fan_1.set_radius(10)
    fan_1.set_color('Yellow')
    fan_1.set_status(1)

    fan_2.set_speed(Fan.medium_speed)
    fan_2.set_radius(5)
    fan_2.set_color('Blue')
    fan_2.set_status(0)

    # display object's properties
    print("Properties of FAN 1")
    fan_1.fan_properties()

    print("\nProperties of FAN 2")
    fan_2.fan_properties()

test_fan()