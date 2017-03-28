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

import csv
import sys

from graphmagic import graphanalyse


def main():
    """Takes csv file path as a parameter in command line call."""

    # take path from sysarg
    if len(sys.argv) < 2:
        print("Please enter csv file source")
        return
    path = sys.argv[1]

    with open(path, 'rb') as csvfile:
        matrix = [[int(r) for r in rec]
                  for rec in csv.reader(csvfile, delimiter=',')]

    print("The number of triangles in the graph is: %s"
          % graphanalyse.Graph().triangle_count(matrix))


if __name__ == '__main__':
    main()
