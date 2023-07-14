import unittest
import physics
import numpy as np

class TestPhysics(unittest.TestCase):
    def test_calculate_buoyancy(self):
        self.assertEqual(physics.calculate_buoyancy(10,1000), 98100.0)
        self.assertNotEqual(physics.calculate_buoyancy(40,1000),1.0)
        self.assertRaises(ValueError,physics.calculate_buoyancy,-10,1000)
        self.assertRaises(ValueError,physics.calculate_buoyancy,10,-1000)

    def test_will_it_float(self):
        self.assertEqual(physics.will_it_float(100,2),True)
        self.assertEqual(physics.will_it_float(1,30000),False)
        self.assertRaises(ValueError,physics.will_it_float,-5,5)
        self.assertRaises(ValueError,physics.will_it_float,5,-5)
        self.assertEqual(physics.will_it_float(5,5000),None)

    def test_calculate_pressure(self):
        self.assertEqual(physics.calculate_pressure(10),98100.0+101325.0)
        self.assertNotEqual(physics.calculate_pressure(40),1.0)

    def test_calculate_acceleration(self):
        self.assertEqual(physics.calculate_acceleration(10,5),2.0)
        self.assertNotEqual(physics.calculate_acceleration(40,5),1.0)
        self.assertRaises(ValueError,physics.calculate_acceleration,10,0)

    def test_calculate_angular_acceleration(self):
        self.assertEqual(physics.calculate_angular_acceleration(10,5),2.0)
        self.assertNotEqual(physics.calculate_angular_acceleration(40,5),1.0)
        self.assertRaises(ValueError,physics.calculate_angular_acceleration,10,0)

    def test_calculate_torque(self):
        self.assertAlmostEquals(physics.calculate_torque(10,30,5),25.0)
        self.assertNotEqual(physics.calculate_torque(10,40,5),1.0)
        self.assertRaises(ValueError,physics.calculate_torque,0,30,5)
        self.assertRaises(ValueError,physics.calculate_torque,10,30,0)
    
    def test_calculate_moment_of_inertia(self):
        self.assertEqual(physics.calculate_moment_of_inertia(5,3),45.0)
        self.assertNotEqual(physics.calculate_moment_of_inertia(4,3),1.0)
        self.assertRaises(ValueError,physics.calculate_moment_of_inertia,0,5)
        self.assertRaises(ValueError,physics.calculate_moment_of_inertia,5,0)

    def test_calculate_auv_acceleration(self):
        self.assertEqual(np.allclose(physics.calculate_auv_acceleration(50,np.pi/2,25),np.array([2*np.cos(np.pi/2),2*np.sin(np.pi/2)])),True)
        self.assertNotEqual(np.allclose(physics.calculate_auv_acceleration(30,np.pi,1),np.array([1.0,2.0])),True)
        self.assertRaises(ValueError,physics.calculate_auv_acceleration,-10,1,2,3,4)
        self.assertRaises(ValueError,physics.calculate_auv_acceleration,10,1,-2,3,4)
        self.assertRaises(ValueError,physics.calculate_auv_acceleration,10,1,2,-3,4)
        self.assertRaises(ValueError,physics.calculate_auv_acceleration,10,1,2,3,-4)

    def test_calculate_auv_angular_acceleration(self):
        self.assertAlmostEqual(physics.calculate_auv_angular_acceleration(10,np.pi/6,6,3),2.5)
        self.assertNotEqual(physics.calculate_auv_angular_acceleration(100,np.pi,3,2),1.0)
        self.assertRaises(ValueError,physics.calculate_auv_angular_acceleration,-5,np.pi,3,2)
        self.assertRaises(ValueError,physics.calculate_auv_angular_acceleration,10,np.pi,-3,2)
        self.assertRaises(ValueError,physics.calculate_auv_angular_acceleration,10,np.pi,3,-2)




if __name__ == "__main__":
    unittest.main()