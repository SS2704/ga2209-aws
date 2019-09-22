class ArithmeticOperations:
    """

    """

    def __init__(self, num1, num2):
        """

        :param num1:
        :param num2:
        """
        self.num1 = num1
        self.num2 = num2

    def get_division_result(self):
        """
        This returns the result of division of two numerical numbers

        :param num1: numerical number with any format : flot or integer
        :param num2: numerical number with any format : flot or integer
        :return: result if division of num1 divided by num2
        """
        return self.num1 / self.num2

    def get_input_for_division(self):
        """
        This method takes the input
        :return:
        """
        self.num1 = input("enter number 1: ")
        self.num2 = input("enter number 2: ")

    def start_arithmetic_operations(self):
        """

        :return:
        """
        #self.get_input_for_division()
        self.check_type()

    def check_type(self):
        if type(self.num1) is not float:
            print("Supply a number of type float or integer")
        elif type(self.num1) is not int:
            print("Supply a number of type float or integer")
        elif self.num1 == 0 or self.num2 ==0:
            print("Supply number greater than zero")