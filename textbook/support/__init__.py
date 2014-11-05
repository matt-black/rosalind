"""
Support library for Python
"""
import abc

class RosalindProblem(abc.ABCMeta):
    """
    Represents a problem on Rosalind
    """

    def __init__(self, number, args=None):
        self.number = number
        self.args = args

    @abstractmethod
    def args_from_file(self, arg_file='./data/{0}/rosalind_{0}.txt'.format(self.number)):
        pass
