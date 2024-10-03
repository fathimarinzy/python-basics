# import unittest
# def add(a,b):
#     return a+b

# class unittesting(unittest.TestCase):
#     def test1(self):
#         self.assertEqual(add(2,3),5)
#     def test2(self):
#         self.assertTrue("ABC".isupper())
#     def test3(self):
#         self.assertFalse("ABC".isupper())

# if __name__ =="__main__":
#     unittest.main()


import unittest
def add(a,b):
    return a+b

# class unittesting(unittest.TestCase):
#     # def test_six(self):
#     #     result=10
#     #     self.assertGreater(result,5)

# if __name__ =="__main__":
#     unittest.main()


# class unittesting(unittest.TestCase):
#     def test_seven(self):
#         result=10
#         self.assertGreater(5,result)

# if __name__ =="__main__":
#     unittest.main()


# class unittesting(unittest.TestCase):
#     def test_six1(self):
#         result=5
#         self.assertGreaterEqual(result,5)

# if __name__ =="__main__":
#     unittest.main()

# class unittesting(unittest.TestCase):
#     def test_six2(self):
#         result=3
#         self.assertLess(result,5)

# if __name__ =="__main__":
#     unittest.main()

# class unittesting(unittest.TestCase):
#     def test_six3(self):
#         result=5
#         self.assertLessEqual(result,5)

# if __name__ =="__main__":
#     unittest.main()


# class unittesting(unittest.TestCase):
#     def test_eight(self):
#         result=[1,2,3,4,5]
#         self.assertIn(5,result)

# if __name__ =="__main__":
#     unittest.main()

# class unittesting(unittest.TestCase):


#     # def test_eights(self):
#     #     result=[1,2,3,4,5] 
#     #     self.assertNotIn(51,result)   


# if __name__ =="__main__":
#     unittest.main()


# class unittesting(unittest.TestCase):
#     def test_ones(self):
       
#         self.assertNotEqual(add(1,2),4)

# if __name__ =="__main__":
#     unittest.main()

class unittesting(unittest.TestCase):
    def test_fives(self):
       
        self.assertFalse("HAI".isupper())

if __name__ =="__main__":
    unittest.main()


# class unittesting(unittest.TestCase):

#     def test_count(self):
     
#         self.assertCountEqual([1,2,3],[1,2,3])   

# if __name__ =="__main__":
#     unittest.main()


# class unittesting(unittest.TestCase):

#     def test_counts(self):
     
#         self.assertCountEqual([1,2,3],[2,3,1])   

# if __name__ =="__main__":
#     unittest.main()

# class unittesting(unittest.TestCase):

#     def test_count1(self):
     
#         self.assertCountEqual([1,2,3],[4,5,6])   

# if __name__ =="__main__":
#     unittest.main()


# class unittesting(unittest.TestCase):

#     def test_regex(self):
     
#         self.assertRegex("hello","^h.*$")   

# if __name__ =="__main__":
#     unittest.main()



# class unittesting(unittest.TestCase):

#     def test_regex1(self):
     
#         self.assertNotRegex("hello","^x.*$")   

# if __name__ =="__main__":
#     unittest.main()

# class unittesting(unittest.TestCase):

#     def test_list(self):
#         l1=[1,2,3]
#         l2=[1,2,3]
#         self.assertListEqual(l1,l2)   

# if __name__ =="__main__":
#     unittest.main()


# class unittesting(unittest.TestCase):

#     def test_tuple(self):
#         l1=(1,2,3)
#         l2=(1,2,3)
#         self.assertTupleEqual(l1,l2)   

# if __name__ =="__main__":
#     unittest.main()

    # class unittesting(unittest.TestCase):

    #     def test_dict(self):
    #         d1={"a":1,"b":2,"c":3}
    #         d2={"a":1,"b":2,"c":3}
    #         self.assertDictEqual(d1,d2)   

    # if __name__ =="__main__":
    #     unittest.main()