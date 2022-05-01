#!/bin/bash

# tests that run under 1 minute
/usr/bin/python3 exact.py < test_cases/all_equal_weights.txt
/usr/bin/python3 exact.py < test_cases/several_equal_weights.txt
/usr/bin/python3 exact.py < test_cases/5nodes.txt
/usr/bin/python3 exact.py < test_cases/6nodes.txt
/usr/bin/python3 exact.py < test_cases/7nodes.txt
/usr/bin/python3 exact.py < test_cases/8nodes.txt
/usr/bin/python3 exact.py < test_cases/9nodes.txt
/usr/bin/python3 exact.py < test_cases/10nodes.txt
/usr/bin/python3 exact.py < test_cases/11nodes.txt