# SixDegreesOfNS
Source code for https://www.nationstates.net/page=dispatch/id=2639438

# Setup

Install required packages:
`pip install -r requirements.txt`

Download the data dump:
`wget https://www.nationstates.net/pages/regions.xml.gz`

`gzip -d regions.xml.gz`

Create a file named `exclude.txt`. It can be empty, but it needs to exist.
If you want to exclude any region from the network (say, embassy collector), put it there, newline-separated.

# Usage
`python parse-dump.py` to generate a GML file from the data dump.

`python shortest-path.py` to use that to calculate the shortest path between two regions.

`python crunch-paths.py` to find all paths between all regions.

After paths are crunched, use
`sh filter-lengths.sh lengths.txt 3` to find the number of 3-node-long paths, for example
