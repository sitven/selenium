#!/usr/bin/python3
# coding=utf-8
import os
print(os.path.split(os.path.realpath(__file__))[0])
numbers = range(5)
for number in numbers:
    print(number)