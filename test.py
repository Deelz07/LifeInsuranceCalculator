import unittest
# import lifei
import lifeinsurancetable as LI 
# from LifeInsuranceCalculator.txt_to_list import convert_to_table


class testLifetable(unittest.TestCase):
    table = LI.convert_to_table('lifetable.txt')
    
    lifetable = LI.Lifetable(table,17)
    def test_survival(self):

        res1 = testLifetable.lifetable.survive(17,1)
        self.assertEqual(res1,0.9994)

        res2 = testLifetable.lifetable.survive(72,18)
        self.assertAlmostEqual(res2,0.21715591064)
    
    def test_deferred_death(self):
        res1 = testLifetable.lifetable.deferred_death(17,0,1)
        self.assertAlmostEqual(res1,0.0006)

        res2 = testLifetable.lifetable.deferred_death(23,7,2)
        self.assertAlmostEqual(res2,0.0011868923)
    
    def test_assurance_EV(self):

        #Testing whole life assurance
        res1 = testLifetable.lifetable.assurance_EV(0.04,50)
        self.assertAlmostEqual(res1/10,0.32907/10)

        res2 = testLifetable.lifetable.assurance_EV(0.06,73)
        self.assertAlmostEqual(res2/100,0.53236/100)

        res3 = testLifetable.lifetable.assurance_EV(0.04,60)
        self.assertAlmostEqual(res3/10,0.45640/10)
        #Test for the case where it is alsm

        #Testing partial assurance
        res4 = testLifetable.lifetable.assurance_EV(0.04,50,60)
        test_4 = res1 - ((1.04)**(-10))*testLifetable.lifetable.survive(50,10)*res3
        self.assertAlmostEqual(res4/100,test_4/100)












if __name__ == "__main__":
    unittest.main()