"""
Main file for infininum project
"""
from infininum import util

"""
TODO: implement multithreading in calculations?
"""


class InfiniNum:
    def __init__(self, number="0"):
        self.num = []
        for char in str(number)[::-1]: # reversed so that looping from 0: will read in correct order
            self.num.append(char)

    def plus(self, right_num):
        print("Starting:\n for n in range(0, {})".format(len(right_num.num)))
        for n in range(0, len(right_num.num)):
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            # loop through the right Number
            try:
                num = self.num[n]
                # number does exist in num:
                calc = int(num) + int(right_num[n])
                print("Calculated {} + {} to be: {}".format(num, right_num[n], calc))
                if calc > 9:
                    print("is > 9:\nInfininum({}{})".format(calc, "0"*(n-1)))
                    # It's 2 digit. RIP, call self again...
                    self.plus(InfiniNum("{}{}".format(calc, "0"*(n-1))))
                else:
                    # It's 1 digit, we can handle that...
                    self.num[n] = str(calc)
            except:
                # location doesn't exist in number
                self.num.append(right_num[n])
        print("Finished")

    # Python built in things:
    def __getitem__(self, item):
        """
        for eg Infininum[1]
        :param item: int, location in Inifininum.num
        :return: char, the character in that location
        """
        return self.num[item]
