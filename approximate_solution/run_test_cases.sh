#!/bin/bash

echo "Path cost should be cerca: 40"
/usr/bin/python3 approximate.py < test_cases/all_equal_weights.txt

echo
echo "Path cost should be cerca: 23"
/usr/bin/python3 approximate.py < test_cases/several_equal_weights.txt

echo
echo "Path cost should be cerca: 14"
/usr/bin/python3 approximate.py < test_cases/5nodes.txt

echo
echo "Path cost should be cerca: 24"
/usr/bin/python3 approximate.py < test_cases/6nodes.txt

echo
echo "Path cost should be cerca: 25"
/usr/bin/python3 approximate.py < test_cases/7nodes.txt

echo
echo "Path cost should be cerca: 34"
/usr/bin/python3 approximate.py < test_cases/8nodes.txt

echo
echo "Path cost should be cerca: 35"
/usr/bin/python3 approximate.py < test_cases/9nodes.txt

echo
echo "Path cost should be cerca: 18"
/usr/bin/python3 approximate.py < test_cases/10nodes.txt

echo
echo "Path cost should be cerca: 29"
/usr/bin/python3 approximate.py < test_cases/11nodes.txt

echo
echo "Path cost should be cerca: ~35"
/usr/bin/python3 approximate.py < test_cases/12nodes.txt

echo
echo "Path cost should be cerca: ~28"
/usr/bin/python3 approximate.py < test_cases/13nodes.txt
