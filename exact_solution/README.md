# Running exact solution code:

# Running individual tests:
python exact.py < test_cases/test_name.txt

OR

python exact.py
Enter input on each line as follows:
number of nodes
start node
number of edges in u v w format.
    denoting an edge from vertex u to vertex v with weight w.
    (all weights should be positive integers)
    (number of edges should be num_nodes * (num_nodes - 1)) / 2)

# Running multiple tests:
Run ./run_test_cases_short.sh to run all tests which take 1 minute or less

Run ./run_test_cases_long.sh to run tests which take over 1 minute.
(Takes ~ 1.7 hrs)

Run ./run_test_cases.sh to run all tests, which range from 4 to 13 nodes
(Takes ~ 1.7 hrs)