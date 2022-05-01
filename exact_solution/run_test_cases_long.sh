#!/bin/bash

# tests that run under 1 minute
/usr/bin/python3 exact.py < test_cases/12nodes.txt
/usr/bin/python3 exact.py < test_cases/13nodes.txt