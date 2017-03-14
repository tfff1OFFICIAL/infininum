"""
Main file for infininum project
"""
from infininum import util

"""
TODO: implement multithreading in calculations?
"""


class InfiniNum:
    def __init__(self, number="0", enable_logging=False):
        self.num = []
        self.enable_logging = enable_logging
        for char in str(number)[::-1]: # reversed so that looping from 0: will read in correct order
            self.num.append(char)

    def _log(self, text):
        """
        Logs things
        :param text: string, to print
        :return: void
        """
        if self.enable_logging:
            print(text)

    def __iadd__(self, right_num):
        """
        += support
        :param right_num: Inifininum object
        """
        self._log("Starting:\n for n in range(0, {})".format(len(right_num.num)))
        for n in range(0, len(right_num.num)):
            self._log("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            # loop through the right Number
            try:
                num = self.num[n]
                # number does exist in num:
                calc = int(num) + int(right_num[n])
                self._log("Calculated {} + {} to be: {}".format(num, right_num[n], calc))

                if calc > 9:
                    self._log("{} is > 9".format(calc))

                    self.num[n] = str(calc)[-1]

                    self._log("Set self.num[{}] to {}".format(n, str(calc)[-1]))

                    new_calc = int("{}{}".format(str(calc)[0], "0"))

                    self._log("Infininum({}{})".format(new_calc, "0"*(n-1)))
                    # It's > 1 digit. RIP, call self again...
                    self.plus(InfiniNum("{}{}".format(new_calc, "0"*(n-1))))
                else:
                    # It's 1 digit, we can handle that...
                    self.num[n] = str(calc)
            except:
                # location doesn't exist in number
                self.num.append(right_num[n])
        self._log("Finished")

        return self

    def round_whole_num(self, digits):
        """
        Rounds the self.num part
        :param digits: Inifininum,
        :return:
        """

    # Python built in things:
    def __getitem__(self, item):
        """
        for eg Infininum[1]
        :param item: int, location in Inifininum.num
        :return: char, the character in that location
        """
        return self.num[item]

    def __str__(self):
        """
        Print itself
        :return: string, itself
        """
        to_out = ""
        for i in self.num[::-1]:
            to_out += i

        return to_out

    def __bool__(self):
        """
        :return: bool
        """

        if len(self.num) == 1 and self.num[0] == "0":
            return False
        else:
            return True