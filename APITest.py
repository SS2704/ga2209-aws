import numpy as np
import flask
from flask import Flask, request
import json

app = Flask(__name__)


@app.route('/test', methods=['GET'])
def test_api():
    return "API is working"


def calculate_mean(num_array):
    """
    This function will calculate the mean of array components
    :return: mean of all the numbers in an array
    :parameter: array of numbers [0 ,1, 2, 3, 4]
    example:
        (0+1+2+3+4)/5
    """
    mean = 0
    for elem in num_array:
        mean += elem

    return mean / len(num_array)


@app.route('/std', methods=['POST'])
def calculate_std():
    """
    This function calculates the standard deviation of an array
    :return:
    """
    arr = json.loads(request.data.decode())['arr']
    print("The input is: {}".format(arr))
    std = 0
    mean = calculate_mean(arr)
    for elem in arr:
        std = (elem - mean) ** 2

    return str(np.sqrt(std / len(arr)))


def calculate_num_count():
    """
     This function returns the count of array elements
     :return: count(array_elements)
     """


# std_dev = calculate_std([3, 4, 5, 6, 7])
# print(std_dev)
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
