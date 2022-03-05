'''
TestClass2のコメントはどうなる？
'''
class TestClass2:
    """Summary line.
    - あ
    - い
    う
    
    え
    お
    """

    def testfunc(self, x, y):
        """sum

        Args:
            x (int): 1st argument
            y (int): 2nd argument

        Returns:
            int: sum result

        Examples:
            >>> print(testfunc(2,5))
            7
        """
        return x + y