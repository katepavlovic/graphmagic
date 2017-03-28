# Copyright 2017: Kate Pavlovic
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import numpy
import six


class Graph(object):

    def triangle_count(self, arr, density_coef=0.5):
        """Counts triangles in the graph

        If arr is low density matrix the method chooses lightweight algorithm
        density_coef defines the amount of ones in arr matrix to choose
        straightforward or lightweight method

        :param arr: adjacency matrix (n x n), which is symmetrical
        :param density_coef: the coefficient that defines which method is used
                            for counting triangles
        :return: Number of triangles in graph
        """
        n = len(arr)
        # density_parameter = 0.2
        max_density = density_coef * (n**2 - n)/2

        matrix_sum = numpy.sum(arr)/2
        if matrix_sum > max_density:
            # use simple straightforward method
            result = self.simple_count(arr)
        else:
            # use sophisticated method
            result = self.low_density_count(arr)

        return result

    def simple_count(self, arr):
        """Calculates the number of triangles in graph using simple method

        Counts triangles iterating over the matrix

        :param arr: list of lists (n x n)
        :return: Number of triangles in graph
        """
        n = len(arr)
        # result = []
        result = 0

        for i in six.moves.range(n):
            for j in six.moves.range(i+1, n):
                if arr[i][j]:
                    for k in six.moves.range(j+1, n):
                        if arr[i][k] and arr[j][k]:
                            # there exists triangle([i, j, k])
                            result = result + 1
        return result

    def low_density_count(self, arr):
        """Calculates the number of traingailes in graph.

        Uses algorithm based on lists of connections. This method is faster
        than simple_count, but requires more memory, hence it is useful
        for high dimension and low density metrices.

        :param arr: list of lists (n x n)
        :return: Number of triangles in graph.
        """
        n = len(arr)
        # array of arrays that consists of all connections between the points
        connection = {}
        result = 0

        for i in six.moves.range(n):
            temp = []
            for j in six.moves.range(i+1, n):
                if arr[i][j]:
                    temp.append(j)
            if temp:
                connection[i] = temp

        for item in connection.keys():
            # length of connection list
            itemlength = len(connection[item])
            for l in six.moves.range(itemlength):
                j = connection[item][l]
                for m in six.moves.range(l+1, itemlength):
                    k = connection[item][m]

                    if j in connection.keys():
                        if k in connection[j]:
                            # there exists triangle([item, j, k])
                            result = result + 1

        return result
