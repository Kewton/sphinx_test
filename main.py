'''
ファイルヘッダー
'''
class TestClass:
    """
    クラスヘッダー
    """
    def testfunc(self, x, y):
        """
        ファンクションヘッダー

        Args:
            x (int): 1st argument
            y (int): 2nd argument

        Returns:
            int: sum result

        Examples:
            >>> print(testfunc(2,5))
            7
        
        Note:
            注意事項などを記載
        """
        return x + y