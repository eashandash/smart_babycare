# -*- coding: utf-8 -*-

__all__ = [
    'MajorityVoter'
]


class MajorityVoter:
    """
    Class to make a majority vote over multiple (5 or more? odd number anyway) classifications
    """

    def __init__(self, prediction_list):
        self.predictions = prediction_list
        print ("INIT MV")


    def vote(self):
        """

        :return:
        """
        print ("voting func - > :", self.predictions)

        if sum(self.predictions) > len(self.predictions)/5.0:
            return 1
        else:
            return 0


