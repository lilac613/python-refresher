import unittest
import physics


class TestPhysics(unittest.TestCase):
    def test_calculate_buoyancy(self):
        self.assertEqual(physics.calculate_buoyancy(10,1000), 98100.0)
        self.assertNotEqual(physics.calculate_buoyancy(10,1000),1.0)
        self.assertRaises(ValueError,physics.calculate_buoyancy,-10,1000)
        self.assertRaises(ValueError,physics.calculate_buoyancy,10,-1000)

    def test_will_it_float(self):
        self.assertEqual(physics.will_it_float(100,2),True)
        self.assertEqual(physics.will_it_float(1,30000),False)
        self.assertRaises(ValueError,physics.will_it_float,-5,5)
        self.assertRaises(ValueError,physics.will_it_float,5,-5)
        self.assertEqual(physics.will_it_float(5,5000),None)

    def test_calculate_pressure(self):
        self.assertEqual(physics.calculate_pressure(10),98100.0+101325)
        self.assertNotEqual(physics.calculate_pressure(10),1.0)




if __name__ == "__main__":
    unittest.main()