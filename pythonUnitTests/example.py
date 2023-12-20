import unittest

def sum(a,b):
    return  a+b
class LearnTest(unittest.TestCase):

    def test_func1(self):
        pass
    def test_func2(self):
        pass
    def test_func3(self):
        pass

def sum(a,b):
    return  a+b
class AnotherTest(unittest.TestCase):

    def setUp(self):
        self.a = 10
        self.b = 4
        print("test started")
    def tearDown(self):
        print("test completed")
    def test_sumFunc1(self):
        #arrange
        # a = 10
        # b = 4

        #act
        result =sum(self.a, self.b)

        #assert
        self.assertEqual(result,self.a + self.b)

    def test_sumFunc2(self):
        #arrange
        # a = 10
        # b = 4

        result = sum(self.a, self.b)

        # assert
        self.assertEqual(result, self.a + self.b)

if __name__ == "__main__":
    unittest.main()
