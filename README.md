# graphmagic

Tool for counting triangles in graphs

## Install

Clone Git repo

    git clone https://github.com/katepavlovic/graphmagic
    cd graphmagic

Install and activate virtualenv (optional)

    virtualenv venv
    . venv/bin/activate

Install requirements and graphmagic

    pip install -r requirements.txt
    python setup.py install


## Usage

Use graphmagic command with csv matrix:

    graphmagic examples/Adjacency_Matrix1.csv

It is going to output number of triangles in graph
