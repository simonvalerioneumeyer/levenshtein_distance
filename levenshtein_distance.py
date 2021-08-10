import pandas as pd
import numpy as np


class Levenshtein:
    def __init__(self):
        """
        The init function here is solely used to read and store the names of the input file
        """
        self.namelist = pd.read_csv("20210103_hundenamen.csv")["HUNDENAME"].values

    def edit_distance(self, str_1, str_2):
        """
        This module takes as inputs two strings and returns as output the minimum edit (Levenshtein's) distance
        between these two strings. The algorithm is a classic dynamic programming algorithm.
        """
        # Initializing a distance matrix with zeros
        m = len(str_1)
        n = len(str_2)
        D = np.zeros([m + 1, n + 1])

        # Setting O-th row
        for j in range(n + 1):
            D[0, j] = j
        for i in range(m + 1):
            D[i, 0] = i

        # Recursion
        for j in range(1, n + 1):
            for i in range(1, m + 1):
                if str_1[i - 1] == str_2[j - 1]:
                    D[i, j] = D[i - 1, j - 1]
                else:
                    D[i, j] = min(D[i, j - 1], D[i - 1, j], D[i - 1, j - 1]) + 1

        return D[m, n]

    def test_levenshtein(self):
        """
        This module tests the above coded edit_distance function for correctness.
        """
        # example from youtube video: https://www.youtube.com/watch?v=We3YDTzNXEk&ab_channel=TusharRoy-CodingMadeSimple
        assert self.edit_distance("azced", "abcdef") == 3

        # example from wikipedia: https://en.wikipedia.org/wiki/Levenshtein_distance#Example
        assert self.edit_distance("kitten", "sitting") == 3

        # example from https://www.geeksforgeeks.org/edit-distance-dp-5/
        assert self.edit_distance("dumbledore", "voldemort") == 7

        print("All tests passed \n")

    def is_dist_1(self, str_1):
        """
        This module takes a string, computes its edit distance to 'Luca'
        and returns it only if that distance is equal to 1.
        """
        if self.edit_distance("Luca", str_1) == 1:
            return str_1

    def main(self):

        # test the dynamic programming algorithm:
        self.test_levenshtein()

        # get the names with distance = 1:
        names = list(
            set([x for x in map(self.is_dist_1, self.namelist) if x is not None])
        )
        print(f"Names with Levenshtein's distance of 1: \n{names}")
