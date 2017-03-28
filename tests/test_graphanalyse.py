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

import mock
import testtools

from graphmagic import graphanalyse


class GraphTestCase(testtools.TestCase):
    def setUp(self):
        super(GraphTestCase, self).setUp()
        A = [
            [0, 1, 1, 1],
            [1, 0, 1, 0],
            [1, 1, 0, 1],
            [1, 0, 1, 0]
        ]
        B = [
            [0, 1, 0, 1, 0],
            [1, 0, 0, 1, 1],
            [0, 0, 0, 1, 1],
            [1, 1, 1, 0, 1],
            [0, 1, 1, 1, 0]
        ]
        self.cases = [[[1], 0], [A, 2], [B, 3]]

    @mock.patch('graphmagic.graphanalyse.Graph.low_density_count')
    def test_triangle_count_low(self, mock_low_density_count):
        mock_low_density_count.return_value = 10
        self.assertEqual(
            graphanalyse.Graph().triangle_count(self.cases[2][0], 0.9), 10)

    @mock.patch('graphmagic.graphanalyse.Graph.simple_count')
    def test_triangle_count_simple(self, mock_simple_count):
        mock_simple_count.return_value = 10
        self.assertEqual(
            graphanalyse.Graph().triangle_count(self.cases[2][0], 0.1), 10)

    def test_simple_count(self):
        for item in self.cases:
            self.assertEqual(
                graphanalyse.Graph().simple_count(item[0]), item[1])

    def test_low_density_count(self):
        for item in self.cases:
            self.assertEqual(
                graphanalyse.Graph().low_density_count(item[0]), item[1])
