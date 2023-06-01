from regular_expressions import RegEx
import unittest


class TestRegEx(unittest.TestCase):
    def test_dots(self):
        self.assertEqual(RegEx().compare_expressions('apple|apple'), True)
        self.assertEqual(RegEx().compare_expressions('ap|apple'), True)
        self.assertEqual(RegEx().compare_expressions('le|apple'), True)
        self.assertEqual(RegEx().compare_expressions('a|apple'), True)
        self.assertEqual(RegEx().compare_expressions('.|apple'), True)
        self.assertEqual(RegEx().compare_expressions('apwle|apple'), False)
        self.assertEqual(RegEx().compare_expressions('peach|apple'), False)

    def test_circumflexus(self):
        self.assertEqual(RegEx().compare_expressions('^app|apple'), True)
        self.assertEqual(RegEx().compare_expressions('^a|apple'), True)
        self.assertEqual(RegEx().compare_expressions('^apple|apple pie'), True)
        self.assertEqual(RegEx().compare_expressions('^le|apple'), False)

    def test_dollar(self):
        self.assertEqual(RegEx().compare_expressions('le$|apple'), True)
        self.assertEqual(RegEx().compare_expressions('.$|apple'), True)
        self.assertEqual(RegEx().compare_expressions('apple$|tasty apple'), True)
        self.assertEqual(RegEx().compare_expressions('app$|apple'), False)

    def test_circumflexus_and_dollar(self):
        self.assertEqual(RegEx().compare_expressions('^apple$|apple'), True)
        self.assertEqual(RegEx().compare_expressions('^apple$|tasty apple'), False)
        self.assertEqual(RegEx().compare_expressions('^apple$|apple pie'), False)

    def test_question(self):
        self.assertEqual(RegEx().compare_expressions('colou?r|color'), True)
        self.assertEqual(RegEx().compare_expressions('colou?r|colour'), True)
        self.assertEqual(RegEx().compare_expressions('colou?r|colouur'), True)

    def test_asterisk(self):
        self.assertEqual(RegEx().compare_expressions('colou*r|color'), True)
        self.assertEqual(RegEx().compare_expressions('colou*r|colour'), True)
        self.assertEqual(RegEx().compare_expressions('colou*r|colouur'), True)

    def test_plus(self):
        self.assertEqual(RegEx().compare_expressions('colou+r|color'), False)
        self.assertEqual(RegEx().compare_expressions('colou+r|colouuuuur'), True)
        self.assertEqual(RegEx().compare_expressions('colou+r|colouur'), True)



if __name__ == "__main__":
    TestRegEx.main()


#
        #
        #
        # # print("Find dollar function for circ" + self.find_dollar())
        #
        # if self.regular_expression.__contains__('+'):
        #     print('+')
        #     return self.find_plus()
        #
        # if self.regular_expression.__contains__('*'):
        #     print('*')
        #     return self.find_asterisk()
        #
        # if self.regular_expression.__contains__('?'):
        #     print('?')
        #     return self.find_question()
        #
        # if self.regular_expression.__contains__('^'):
        #     print("^")
        #     tmp_bool = self.find_circumflexus()
        #     if self.regular_expression.__contains__('$') and tmp_bool == True:
        #         print("$")
        #         return self.find_dollar()
        #     return tmp_bool
        #
        # if self.regular_expression.__contains__('$'):
        #     print("$")
        #     tmp_bool = self.find_dollar()
        #     if self.regular_expression.__contains__('^') and tmp_bool == True:
        #         print("^")
        #         return self.find_circumflexus()
        #     return tmp_bool
        #
        # if self.comparison_expression.__contains__(self.regular_expression) or self.find_dots():
        #     print("True")
        #     return self.comparison_expression.__contains__(self.regular_expression) or self.find_dots()
        #
        # for i, symbol in enumerate(self.regular_expression):
        #     # print(symbol)
        #     if symbol != '.' and symbol != self.comparison_expression[i]:
        #         print("False")
        #         return False
        # print("True")
        # return True

