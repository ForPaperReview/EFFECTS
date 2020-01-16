import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv

data = {
    '1': [2,3,3,2,3,2,3,2,3,3,3,2,2,2,3,2,2,2,3,3,2,2,2,2,2,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3,2,3,2,2,3,2,2,2,3,2,2,2,3,2,2,2,2,2,2,2,2,3,2,2,2,3,3,2,3,2,2,2,3,2,2,2,2,2,2,2,2,3,2,2,2,3,3,3,2,2,2,3,3,2,3,2,3,3,2,2,2,2,2,2,2,3,2,2,3,3,3,2,3,2,2,2,2,2,2,2,3,2,2,2,3,2,2,3,2,2,2,3,2,3,2,3,2,3,3,3,3,3,2,2,2,2,3,3,2,3,3,3,2,2,3,2,2,3,2,2,3,2,2,3,2,2,2,3,2,3,2,3,2,3,2,2,3,2,2,3,3,2,2,3,2,3,2,2,2,2,3,2,2,2,3,2,2,3,2,2,3,2,2,2,2,3,3,2,2,2,2,3,3,3,2,2,2,3,2,2,2,2,2,2,2,2,3,2,3,2,2,3,3,3,2,2,3,2,2,2,2,2,2,2,2,2,2,2,2,3,3,2,3,3,2,2,3,2,3,2,2,2,2,2,3,3,2,2,3,3,2,3,2,2,2,2,2,2,3,2,2,2,2,2,2,2,2,2,2,2,3,2,2,2,2,2,3,2,3,3,3,2,2,2,2,2,2,2,2,2,2,2,2,3,3,2,3,3,2,2,2,2,3,3,3,2,2,2,2,2,3,3,2,2,3,3,2,2,2,3,3,3,2,2,2,3,3,3,2,3,2,2,2,3,2,3,3,3,2,2,2,3,3,3,2,2,2,3,3,2,2,3,2,2,2,3,2,2,2,2,2,2,2,3,3,2,3,2,2,2,2,2,2,2,2,2,2,3,2,3,3,2,3,2,2,2,2,2,3,2,3,2,2,2,2,2,3,2,2,3,3,2,2,3,2,2,3,3,2,2,2,2,2,2,3,2,3,2,2,2,2,3,2,3,2,2,2,3,2,2,2,2,3,2,2,3,3,3,3,2,2,2,2,3,2,2,3,2,3,2,2,3,2,3,2,3,2,2,2,3,2,3,3,2,2,2,2,2,2,2,3,3,2,2,2,2,2,2,3,2,2,3,3,2,3,3,2,2,2,2,3,3,2,3,2,3,2,2,2,2,2,2,3,2,2,2,3,3,2,2,2,3,2,2,3,2,2,3,2,2,2,2,3,3,2,2,3,2,2,2,2,2,2,3,3,2,2,3,3,2,3,2,3,3,2,2,3,2,3,3,3,2,2,2,2,2,3,2,2,2,2,3,2,2,2,3,2,2,3,2,2,3,3,3,2,2,3,3,3,2,3,2,2,2,3,2,3,2,2,3,2,2,3,2,2,3,2,3,3,3,2,2,2,2,3,2,3,3,2,3,3,2,2,2,2,2,2,2,2,2,2,2,3,2,2,3,3,2,3,2,2,3,2,2,2,2,2,3,3,2,2,2,2,2,3,2,2,2,2,2,2,3,2,2,3,2,2,2,2,2,2,3,2,2,2,3,2,2,3,2,2,2,2,3,2,2,2,2,3,2,2,2,2,3,2,2,2,3,3,2,3,3,3,3,2,2,2,2,3,3,2,2,2,2,2,2,2,3,3,2,2,3,2,3,2,3,2,2,2,2,2,2,3,2,3,2,2,3,2,2,3,3,2,3,2,3,2,2,2,2,3,2,3,2,3,2,2,2,2,2,2,2,3,3,2,2,2,3,2,2,3,2,2,2,3,2,2,3,2,2,3,2,2,2,2,2,2,3,2,2,2,2,2,2,2,2,2,2,2,2,2,3,2,3,2,2,2,3,3,3,2,3,3,2,2,2,2,2,3,2,2,2,2,3,2,2,2,2,3,2,2,2,2,2,2,2,2,3,2,2,2,2,2,3,3,2,3,3,3,3,2,2,3,3,2,3,3,2,3,2,2,3,2,3,2,3,2,2,3,2,2,3,2,2,2,2,2,2,2,2,2,3,2,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3,2,3,2,3,2,2,2,3,2,3,2,2,2,2,3,3,2,2,3,3,2,3,3,3,2,2,2,2,3,3,2,3,2,2,3,2,2,2,2,2,3,3,2,3,2,3,2,3,3,2,2,2,3,2,2,2,2,2,2,3,2,3,2,2,2,2,3,2,3,2,2,3,3,2,3,2,2,3,2,2,3,3,2,3,3,3,2,2],
    '2': [2,3,2,3,4,4,4,4,4,2,3,2,3,3,3,5,2,3,3,4,2,4,3,2,2,4,4,3,2,2,3,3,3,3,3,3,3,2,4,3,4,2,3,3,3,5,2,4,4,2,3,3,2,5,5,3,3,3,2,4,2,4,4,2,2,2,4,2,3,3,4,2,3,4,3,2,4,3,3,3,4,3,4,3,4,3,5,2,4,2,2,2,3,3,2,2,4,3,3,3,4,4,3,2,2,2,4,4,3,2,2,3,3,4,4,2,3,2,3,2,4,4,3,4,3,2,2,4,3,3,4,5,3,4,2,2,3,3,3,3,4,3,3,2,3,2,3,4,4,4,2,2,4,3,3,3,3,5,3,3,4,4,2,3,4,3,4,2,2,2,4,4,4,4,5,3,3,3,4,2,3,2,3,2,3,2,2,3,4,3,3,3,4,4,3,4,2,3,4,2,3,2,4,3,2,3,3,2,3,3,5,4,4,4,4,4,3,3,2,3,3,2,3,2,2,3,5,3,5,4,4,2,4,2,3,4,5,2,2,4,4,4,2,4,4,3,3,5,4,4,4,2,3,2,2,3,2,3,2,4,3,5,5,2,3,4,3,4,3,2,4,2,3,2,4,2,2,4,2,3,2,4,2,3,4,2,3,4,4,5,3,4,4,2,3,2,2,3,2,5,2,2,4,3,3,4,4,3,2,2,2,3,2,2,4,2,2,4,3,4,4,2,4,4,3,3,3,3,3,5,4,2,3,2,3,3,4,2,2,2,2,4,3,3,3,4,2,3,3,2,5,4,5,3,4,2,2,4,4,4,5,3,4,3,4,3,3,4,4,4,4,3,4,2,2,2,4,3,2,2,3,4,4,3,2,2,4,3,3,3,2,3,5,2,4,4,3,2,4,4,3,3,4,3,2,3,4,3,3,4,3,3,3,3,2,3,5,3,4,2,3,5,4,4,4,2,4,2,3,4,2,2,4,2,3,3,3,4,5,3,4,4,2,3,3,4,2,5,4,3,4,4,2,4,3,3,3,4,4,4,3,2,2,4,2,4,5,2,2,3,3,4,4,2,3,2,2,3,4,4,4,2,5,2,4,2,3,2,4,4,4,2,2,2,2,5,2,2,2,3,4,3,2,5,5,2,4,5,3,3,2,2,4,3,4,4,3,3,3,2,2,2,3,4,2,2,2,4,3,3,4,4,2,3,3,2,4,5,3,3,2,3,2,2,3,4,3,2,3,2,3,5,2,3,4,4,4,4,3,3,4,3,3,4,4,2,3,4,2,3,3,4,3,2,4,2,4,2,5,4,5,4,3,5,3,2,5,5,3,3,3,5,5,5,2,3,2,3,4,4,5,4,3,2,5,2,4,3,4,4,3,4,3,2,2,4,3,3,3,4,3,3,3,3,3,4,3,2,4,2,3,4,4,5,3,4,2,2,3,4,4,3,3,2,5,3,3,3,3,3,4,2,2,4,3,4,3,2,4,2,2,3,2,3,2,3,4,4,4,4,2,2,3,4,2,2,3,4,4,2,4,2,3,4,4,3,2,3,4,2,3,2,3,2,2,4,2,3,4,2,5,4,4,4,5,4,2,3,4,2,2,5,4,4,3,3,3,4,3,3,4,2,5,3,3,3,3,3,4,2,3,4,3,3,3,2,3,4,2,4,3,2,2,3,5,4,2,2,3,3,3,4,4,3,2,2,3,4,2,4,3,3,2,4,3,3,2,3,2,2,2,3,3,3,4,4,4,2,4,3,2,2,4,5,2,4,2,3,5,3,3,2,2,4,4,3,2,3,3,4,2,2,4,3,3,2,3,4,3,5,3,3,2,4,2,4,4,3,4,4,3,3,3,4,4,5,2,2,4,3,3,3,3,4,4,2,3,3,3,4,4,2,2,2,2,2,3,3,3,3,4,4,3,3,4,2,2,2,3,3,3,2,3,2,3,2,4,4,3,4,3,3,2,2,2,2,4,4,2,4,3,4,3,2,3,4,2,5,2,4,4,2,4,3,3,3,3,4,2,3,4,3,4,4,2,4,4,4,3,2,2,2,2,2,2,3,4,2,2,2,4,3,2,3,2,2,2,3,5,5,3,3,4,4,3,2,4,3,4,3,3,4,4,5,3,4,2,3,3,3,4,2,2,4,4,3,5,2,3,2,2,4,3,4,3,4,2,2,3,3,3,5,4,2,3,5,2,2,2,4,2,5,4,2,3,4,3,3,3,2,3,3,3,3,4,4,4,3,4,3],
    '3': [5,6,7,4,4,6,5,7,6,3,4,2,7,4,6,4,3,7,4,3,8,5,6,2,3,6,3,3,8,5,2,2,5,4,6,4,4,6,4,3,3,5,7,3,6,3,2,4,6,8,4,5,8,5,4,6,5,6,6,7,3,6,3,6,9,7,8,4,3,8,3,3,3,7,3,2,3,6,5,4,3,3,3,7,6,4,5,7,4,8,7,3,4,6,3,7,4,5,3,6,8,2,4,5,6,7,3,3,3,4,6,3,4,4,4,5,6,4,6,4,6,7,6,3,2,7,6,5,4,7,7,6,6,5,4,5,2,3,4,3,4,2,2,6,6,4,4,7,5,7,4,3,5,6,4,5,5,2,5,6,3,3,5,4,4,6,5,5,8,7,3,6,2,5,4,4,7,3,2,8,2,2,2,4,5,4,5,4,4,3,5,6,4,3,4,6,4,5,3,5,8,4,2,7,4,9,4,8,4,4,4,6,4,3,6,5,4,4,4,6,3,4,2,6,5,2,8,3,5,2,4,2,3,5,2,7,5,4,5,3,7,4,5,4,6,4,5,7,5,7,5,3,5,3,4,6,5,5,3,4,5,6,5,4,5,4,5,4,2,7,3,2,4,5,2,4,8,7,2,6,3,4,4,3,4,3,4,2,3,3,4,6,3,4,6,4,2,5,4,4,4,4,7,5,8,6,3,8,6,6,2,5,3,4,3,3,6,4,4,6,5,6,8,2,5,5,4,4,6,7,4,4,4,7,5,8,8,7,5,5,5,4,5,7,3,5,6,4,5,5,6,5,4,5,5,3,7,4,3,3,4,4,3,7,3,6,5,7,6,6,6,7,7,4,2,4,5,3,3,6,6,6,4,4,5,5,5,6,6,7,2,8,8,5,4,3,3,6,6,7,7,4,5,6,3,4,6,6,3,7,4,2,3,3,3,3,7,6,4,5,3,4,4,3,7,3,7,4,4,4,5,5,5,3,3,6,8,3,3,7,6,5,4,8,6,3,6,6,6,2,5,3,2,2,5,7,3,5,5,5,5,5,5,4,4,6,7,4,5,5,5,5,4,8,5,6,2,5,5,4,6,6,4,6,6,3,7,6,3,7,4,7,2,4,5,3,4,2,5,5,3,4,2,6,3,6,2,3,3,2,5,4,4,6,5,4,4,4,6,4,5,2,5,4,3,4,5,5,7,6,7,5,4,5,5,6,6,6,6,6,3,8,3,7,2,6,3,5,6,6,5,5,3,4,7,4,6,4,8,6,6,4,4,4,6,6,5,3,5,3,5,5,2,7,3,2,6,3,6,4,2,6,2,6,4,4,3,6,4,6,6,4,8,7,5,4,6,5,5,7,3,4,6,3,3,3,4,4,5,4,7,3,3,4,2,2,3,6,7,6,2,3,5,3,6,8,4,4,3,6,6,5,3,2,6,7,5,3,2,3,7,2,4,5,3,3,4,7,3,4,3,3,4,3,5,5,5,5,4,3,2,5,3,5,3,3,2,6,7,5,6,3,3,6,7,4,8,6,6,5,5,5,6,5,2,2,6,4,5,6,4,5,3,3,3,5,5,6,3,5,7,2,5,2,4,4,5,6,3,5,4,2,2,6,5,5,6,5,4,3,6,2,6,5,5,4,7,2,7,5,5,3,7,6,4,2,8,5,4,5,2,6,3,3,6,5,4,3,7,5,3,2,5,7,4,2,6,5,4,6,7,5,5,7,5,6,4,7,6,2,6,6,5,4,5,6,5,5,6,6,4,3,5,4,3,5,4,6,4,4,2,6,5,8,3,2,3,5,3,6,2,6,5,4,5,2,3,4,5,4,5,6,4,4,6,4,4,3,4,4,7,6,2,4,5,3,2,7,3,3,4,6,6,6,4,6,7,7,4,7,4,5,5,2,7,6,6,7,4,7,5,6,5,6,4,7,5,3,3,3,2,7,6,2,3,2,7,6,4,7,3,3,5,3,2,6,3,6,4,9,7,3,5,4,5,6,3,6,8,7,2,6,3,6,4,4,5,6,6,4,4,5,7,4,7,8,5,5,2,7,6,5,5,6,5,4,3,4,2,2,3,5,6,6,6,7,5,5,7,3,2,4,5,5,4,4,6,5,5,5,5,5,6,5,4,4,3,3,5,6,3,6,4,4,8,4,5,8,5,5,4,6,5,4,7,6,3,3,2,5,3,6,4,5,5,3,4,5,6,3,7,6,5,4,7,4,7,3,4,5,8,3,6,4,4,6,4,5,6,5],
    "4": [4,7,4,3,6,8,7,11,8,8,10,11,9,13,5,9,3,12,8,10,8,2,3,5,7,9,7,12,6,3,2,5,9,4,11,9,7,6,5,8,8,2,4,13,7,4,4,9,6,7,9,6,12,8,11,6,6,4,6,2,7,7,10,3,3,4,7,7,7,7,3,4,5,8,9,5,4,8,5,12,4,7,10,5,8,9,5,8,7,6,6,6,4,4,7,7,9,4,6,11,9,12,10,11,5,8,8,9,4,6,6,5,5,5,8,7,4,8,6,12,6,6,10,5,8,7,5,12,12,9,5,7,8,4,11,8,3,7,9,7,5,7,7,5,6,8,7,3,6,4,6,9,5,7,4,10,3,3,6,2,8,8,11,4,9,5,10,5,8,12,6,8,3,6,7,4,9,3,4,9,10,8,7,4,10,6,6,5,11,8,5,11,8,11,11,10,3,9,7,5,11,6,6,7,8,12,10,6,6,8,8,11,6,4,9,7,9,4,5,8,5,10,7,7,6,10,10,7,10,11,5,5,13,5,5,7,9,7,4,6,4,5,8,6,8,4,6,11,2,9,11,13,8,14,13,8,9,11,6,11,8,6,7,6,5,4,5,7,9,6,11,10,6,5,10,6,6,6,9,7,9,12,6,7,8,8,4,8,8,4,12,9,7,5,4,8,6,6,8,5,3,10,6,7,5,8,11,6,5,11,8,2,12,8,6,5,11,2,10,11,12,9,11,10,6,7,7,7,10,3,4,11,2,7,11,11,10,6,9,9,8,5,10,10,10,9,10,6,12,7,8,6,7,9,8,6,8,7,10,4,6,9,2,10,5,4,10,5,9,10,6,6,9,8,9,7,9,11,8,7,7,11,8,8,11,8,8,5,12,4,3,4,9,3,7,4,4,9,5,11,11,12,8,6,12,5,9,9,8,5,3,8,7,6,6,3,5,5,7,5,10,3,7,8,4,8,9,8,6,5,10,8,9,11,5,4,9,3,8,11,7,9,7,9,10,8,9,5,7,10,5,4,5,12,7,9,6,5,11,7,11,5,8,12,6,7,8,6,3,5,4,6,9,9,7,5,4,3,7,10,4,4,7,5,7,6,10,7,6,10,3,3,8,7,5,6,4,9,8,8,7,7,8,7,9,6,5,6,8,13,4,6,9,9,10,2,9,8,6,8,8,7,9,7,12,10,9,6,10,7,6,14,7,6,9,10,5,6,4,8,6,5,8,7,8,4,10,8,6,10,6,9,12,6,10,4,11,11,10,8,6,3,8,9,5,5,5,9,11,11,10,13,5,4,5,7,5,5,6,11,6,6,6,8,7,12,8,6,12,3,7,8,2,3,7,6,9,6,13,4,9,10,11,5,9,5,3,10,8,9,10,7,6,3,7,4,7,5,8,9,7,7,7,6,2,10,8,3,4,11,5,9,14,8,4,8,2,8,8,7,6,2,5,7,7,6,7,7,8,4,10,5,11,3,12,4,5,9,7,6,9,8,10,11,6,11,9,6,11,10,6,9,8,10,10,7,6,7,6,7,9,9,8,6,14,7,7,7,4,8,5,3,4,8,8,5,3,4,6,10,7,7,5,10,10,5,8,5,5,7,6,12,2,7,8,3,8,4,10,11,9,4,8,10,8,11,8,7,4,6,6,11,9,9,5,11,6,4,9,9,8,8,8,6,9,10,9,6,4,12,12,7,9,6,5,11,4,10,8,7,7,9,8,3,3,4,3,6,8,7,4,10,10,9,8,9,13,11,9,9,2,4,5,2,4,8,11,6,3,13,8,9,9,4,12,4,4,9,4,10,12,6,11,10,9,7,7,11,9,9,2,6,4,3,4,10,8,6,8,9,8,6,6,6,4,12,12,7,7,7,11,7,4,10,8,6,11,6,10,5,11,9,9,6,8,2,8,7,4,9,6,8,5,8,8,7,2,7,4,10,8,8,2,7,6,8,12,11,9,7,6,14,10,9,8,9,5,5,6,3,8,9,5,9,12,6,11,8,9,10,8,6,10,11,6,8,4,7,6,4,9,9,13,10,11,6,3,3,10,9,4,10,12,6,5,6,5,9,7,11,11,4,7,6,6,7,9,5,4,6,4,3,6,10,10,12,7,8,7,9,8,4,7,8,4,9,11,2,12,10,7,10,8,4,6,6,8,8,13,8,4,7,5,10,5,8,2,7,5,8,10,3,4,7,10,10,6,11,9,12,9,3,5,7,4,2,6,8,13,5,8,9,6,9,7,8,10,10,7,7],
    "5": [9,13,9,4,13,18,13,8,15,18,9,17,12,18,6,9,16,6,8,12,6,12,13,5,17,9,3,12,3,18,16,12,15,6,3,13,17,12,10,11,7,13,18,10,9,9,8,18,11,12,15,7,3,14,6,13,10,21,5,7,13,5,16,15,13,13,8,7,17,19,11,20,10,9,17,15,6,9,2,11,12,16,20,14,3,6,15,20,11,10,20,16,17,15,9,16,12,15,7,7,3,17,16,19,10,11,10,10,11,9,9,16,5,11,8,8,15,15,15,17,10,12,5,8,14,11,4,17,7,6,12,11,11,16,13,7,5,15,10,17,5,18,11,10,19,15,15,15,13,5,8,9,3,4,10,5,14,11,16,9,13,6,5,7,10,16,4,3,13,6,18,13,5,14,14,14,14,11,9,9,7,22,19,15,9,6,12,8,15,8,13,14,18,8,14,4,16,11,16,10,10,13,11,13,19,8,18,11,9,11,12,13,13,17,16,9,8,11,10,16,12,11,7,8,11,12,10,21,11,13,19,10,15,15,20,11,9,7,18,7,2,15,19,6,13,3,9,15,8,14,8,18,8,6,15,14,9,9,3,14,18,4,8,8,17,13,7,10,8,8,18,14,5,11,13,11,8,10,10,13,20,7,18,17,15,11,7,3,14,17,10,13,12,16,12,9,5,6,21,5,8,5,7,13,9,19,12,17,13,7,12,7,17,7,15,7,7,16,12,15,3,3,11,13,14,13,14,18,8,15,13,14,9,4,14,9,10,4,16,4,13,17,12,8,12,8,17,17,6,9,9,16,5,8,12,14,6,18,17,19,19,10,16,3,11,17,10,13,14,14,16,8,16,13,4,12,10,11,13,11,3,12,18,7,12,14,16,6,8,13,18,9,5,18,10,11,13,12,14,12,8,9,8,15,10,14,8,9,7,11,15,16,6,10,20,13,12,13,14,11,9,18,5,9,4,5,15,6,11,11,10,11,11,14,4,6,16,5,9,19,6,9,10,16,3,10,15,4,21,6,13,7,15,18,8,6,11,5,5,7,5,6,10,11,15,10,17,2,15,10,8,3,20,17,16,11,11,17,17,3,17,10,3,5,11,8,13,5,16,8,10,14,8,18,11,5,16,6,11,8,19,8,20,7,15,11,8,5,10,11,10,15,10,12,10,10,6,22,15,5,13,17,15,7,11,7,14,11,20,17,12,11,17,12,13,21,7,19,12,14,17,21,3,16,14,15,3,13,14,8,13,13,7,14,6,2,10,13,9,8,5,12,7,16,5,4,6,11,9,4,16,16,14,5,19,8,6,9,9,19,8,12,16,2,12,13,15,9,19,5,10,14,8,13,9,14,12,16,6,12,12,14,15,12,19,10,13,10,12,14,18,8,14,5,21,15,18,14,16,10,14,6,5,14,3,2,8,5,10,10,12,19,11,9,7,12,7,6,5,16,12,18,15,13,14,7,18,9,10,8,9,19,14,8,18,14,7,7,16,12,7,5,10,4,14,18,4,8,16,11,7,9,4,11,5,17,5,10,10,9,11,10,19,16,14,11,7,8,12,8,18,10,3,10,11,9,13,6,11,20,10,7,13,6,13,7,12,12,2,8,13,10,4,20,13,18,14,5,17,9,8,9,20,11,7,4,5,9,12,10,10,16,13,11,18,7,7,12,18,18,10,5,18,6,20,7,14,4,7,11,8,6,17,12,14,4,16,14,10,17,8,16,6,16,9,2,13,13,4,10,10,15,11,15,17,6,4,15,13,12,10,16,11,16,6,13,19,12,17,13,7,5,6,9,7,8,9,12,6,10,16,13,16,18,6,7,12,15,10,14,18,5,18,8,11,13,16,6,14,15,13,13,14,6,16,14,9,10,9,8,9,16,6,9,8,9,13,13,11,12,16,11,8,10,5,7,18,4,14,13,10,10,15,21,10,8,6,12,6,14,14,14,12,4,9,15,11,20,15,8,16,18,9,4,5,7,7,6,12,8,11,17,17,7,16,20,17,12,6,15,16,13,6,5,8,10,6,10,16,4,8,11,18,16,9,9,10,13,12,23,7,4,9,9,9,12,9,6,3,20,16,20,5,9,13,10,13,4,8,7,16,15,20,15,11,8,12,8,18,13,3,17,15,12,5,7,15,19,11,9,20,21,11,11,8,5,9,13,7,16,9,5,11,9,3,16,11,9,16,16,7,9,18,16,11,11,9,5,15,11,15,10,17,2,14,8,11,7,11,11,21,6,18,14,18,20,8,21,20,11],
    "6": [22,11,15,19,30,25,16,28,13,21,30,8,19,14,13,31,14,27,12,20,18,29,13,9,6,12,18,8,14,20,16,20,22,14,18,14,14,16,25,19,26,28,13,13,16,24,5,11,12,7,14,20,27,11,15,16,25,18,18,22,30,26,12,11,16,33,13,8,27,15,18,22,6,24,20,22,15,23,12,30,11,5,16,14,17,30,19,10,11,21,13,18,30,12,19,23,19,27,19,27,20,23,13,19,21,12,27,23,31,21,19,10,18,28,5,12,12,32,18,30,21,20,17,20,22,13,13,12,30,16,20,18,38,10,3,26,7,15,21,13,16,7,31,3,30,26,20,24,19,12,20,12,9,22,8,17,24,26,14,14,26,5,13,26,21,15,25,12,32,31,29,17,7,4,13,5,11,22,33,12,17,31,25,24,21,22,15,11,7,14,18,14,16,15,17,11,19,29,14,21,16,14,14,21,15,27,27,10,3,6,26,15,36,18,23,23,13,17,15,19,14,20,30,13,23,14,11,18,15,15,11,23,22,23,9,3,9,16,19,30,4,18,7,6,12,10,12,17,15,17,27,11,11,7,8,13,19,15,17,19,14,9,18,22,5,5,20,8,17,10,19,24,20,16,9,21,38,17,12,25,19,35,5,15,17,18,21,17,27,17,12,12,24,2,16,12,23,13,26,22,11,17,10,18,19,6,15,9,13,10,21,15,20,13,5,14,16,22,12,12,4,33,13,27,21,17,14,16,31,9,11,15,21,9,9,13,8,33,14,14,32,5,20,28,21,23,14,7,21,24,14,18,27,16,15,15,33,30,9,25,19,15,16,4,21,14,13,8,29,22,30,17,17,10,17,12,27,24,12,12,13,22,15,22,17,19,9,16,12,24,27,10,27,23,11,12,16,11,5,4,16,11,5,22,11,15,14,18,16,11,19,16,11,26,22,14,16,16,17,7,16,30,4,27,32,31,25,10,25,20,26,27,6,11,10,18,14,22,10,13,5,21,18,6,15,17,21,26,23,13,5,9,8,21,33,5,28,16,17,24,12,23,13,9,24,20,14,20,20,16,3,6,20,18,30,14,17,19,14,14,24,2,18,13,15,18,14,14,27,21,26,21,25,26,18,21,12,20,21,15,22,17,15,23,24,19,10,15,18,9,12,31,34,6,24,15,7,21,14,19,8,17,20,15,7,23,9,16,21,12,29,27,11,4,11,11,20,8,27,12,18,11,12,15,20,5,8,14,10,10,19,13,12,21,17,29,14,27,29,6,16,18,17,27,10,10,10,22,7,25,5,20,13,21,13,17,28,28,35,6,12,10,18,8,15,16,7,19,14,35,13,13,22,8,26,31,30,38,30,18,33,10,13,9,11,17,11,16,32,10,10,18,16,20,17,19,18,17,28,13,26,23,12,18,29,15,25,14,15,30,12,5,20,5,20,10,17,5,12,12,22,26,21,15,9,21,28,31,19,16,27,8,15,11,16,13,14,7,21,16,24,20,18,22,7,4,21,19,20,5,14,16,11,34,7,28,18,22,19,28,20,9,17,17,25,7,11,9,9,15,23,24,15,32,11,13,29,21,25,14,12,31,8,17,23,15,14,10,16,17,17,25,28,25,24,21,28,15,25,22,6,5,31,5,5,17,26,16,27,16,18,25,13,7,20,17,14,9,8,7,19,19,13,16,42,11,8,12,10,16,21,21,8,16,17,16,30,24,21,20,8,14,17,21,24,15,12,21,18,5,29,21,27,20,25,16,23,24,22,17,25,19,29,25,17,5,10,8,21,19,20,13,7,15,23,26,18,32,15,12,14,13,27,3,19,26,20,16,24,18,22,25,25,14,18,19,26,6,14,11,31,9,4,20,26,19,17,17,21,5,16,10,23,10,16,18,22,6,13,15,12,14,18,27,19,18,22,26,30,8,4,15,17,12,25,10,5,16,22,16,11,17,9,14,26,18,20,13,29,23,16,7,17,7,2,26,6,25,15,25,8,19,7,16,7,11,18,16,13,2,15,20,6,20,18,16,15,14,3,15,19,16,11,9,28,16,7,27,18,16,10,15,10,12,16,13,7,20,18,28,16,24,10,6,7,17,36,24,14,20,18,19,13,16,20,23,19,16,29,7,17,13,11,24,34,25,17,36,16,20,16,18,18,19,15,30,16,22,3,20,14,20,15,6,16,16,24,27,18,18,15,22,16,10,14,12,27,15,27,18,19,26,25,10,21,22,16,20,30,34,7,31,8,14,7,6,17,16,13,19],
    "7": [36,29,30,34,16,13,33,22,44,9,33,10,28,30,17,42,23,24,47,24,15,40,22,34,28,43,26,46,45,5,43,21,26,33,27,52,18,47,38,44,38,49,31,41,29,51,23,38,31,43,33,46,26,32,33,44,16,19,30,24,45,42,39,30,18,19,30,8,39,21,33,29,27,35,39,31,24,22,30,46,47,35,20,45,15,28,46,17,19,44,26,21,14,13,48,26,35,37,41,24,30,22,37,36,32,35,28,24,15,31,39,36,4,13,30,7,9,19,9,36,44,25,47,51,50,45,28,12,38,37,44,34,37,38,21,50,24,46,21,28,16,37,41,25,25,44,50,37,46,35,36,15,14,42,30,43,17,37,17,18,47,19,38,28,17,27,50,15,23,36,12,40,13,13,31,34,7,44,45,33,34,38,42,11,47,23,13,10,39,48,37,40,44,21,37,11,23,26,18,31,25,20,11,52,30,36,23,35,38,48,10,28,20,33,60,20,56,14,12,28,61,43,25,12,29,24,3,6,19,16,24,41,14,42,45,65,34,32,31,35,4,43,37,39,40,20,14,40,19,33,31,39,53,23,20,49,23,14,39,17,21,16,12,23,20,48,28,29,36,43,23,18,42,15,42,16,22,29,19,21,54,24,47,38,26,18,33,22,13,24,22,6,34,24,56,24,23,38,32,24,46,31,22,34,6,36,26,34,44,15,29,19,20,18,24,48,29,29,28,20,26,41,2,16,8,36,55,53,43,8,34,35,41,11,22,12,48,22,21,40,40,15,39,28,35,30,18,57,29,29,59,10,34,25,18,38,52,47,42,30,16,14,45,19,41,37,34,11,34,36,56,30,17,39,23,18,19,36,25,47,58,21,15,32,20,40,6,25,15,34,39,50,17,35,19,13,12,45,33,14,58,25,36,23,52,50,23,12,13,33,12,26,25,10,30,40,41,6,49,38,26,28,26,16,38,13,23,39,38,59,10,48,28,28,21,27,22,39,24,20,18,29,39,21,29,17,31,26,34,26,27,16,3,22,22,3,33,41,10,40,20,41,20,32,18,12,22,21,11,29,42,42,34,42,21,41,41,36,4,33,40,42,17,24,23,16,20,38,39,32,25,30,33,63,36,28,41,24,27,14,21,31,9,24,12,21,16,14,43,16,13,40,39,38,9,33,35,20,11,17,39,39,22,27,21,38,7,20,27,48,40,44,22,42,19,10,31,54,31,29,26,39,26,18,38,45,5,59,19,19,11,14,29,32,23,7,24,12,11,49,14,40,41,29,2,37,44,30,57,32,53,38,58,36,26,22,18,22,32,27,28,27,23,29,23,24,43,39,53,33,56,34,30,4,29,33,21,37,26,23,14,18,40,17,27,20,25,19,23,33,21,40,30,47,17,39,15,40,22,23,14,54,26,23,31,24,35,32,39,3,25,39,32,48,43,44,35,25,13,14,20,40,16,25,24,16,32,40,34,41,30,6,39,27,33,25,15,49,20,22,41,47,54,5,31,18,26,51,59,27,34,29,32,13,27,13,14,40,32,50,47,27,42,14,24,6,27,20,13,16,24,27,49,46,22,44,27,29,23,38,24,26,21,40,46,39,22,9,48,21,16,8,9,45,18,23,24,29,46,35,38,15,28,24,27,40,25,43,7,39,11,48,33,17,43,33,26,33,25,36,26,31,24,21,44,10,5,26,43,41,36,39,48,49,21,16,29,18,56,27,29,35,41,15,23,48,27,34,19,20,41,31,62,28,27,41,14,32,45,29,51,23,45,20,9,28,34,20,40,5,36,32,28,33,18,5,32,17,41,21,14,25,24,38,25,41,19,44,24,14,37,34,22,27,37,15,30,17,27,52,30,44,39,20,25,18,18,19,26,17,54,15,56,48,17,25,40,30,12,14,27,31,24,25,35,27,18,34,18,30,42,20,31,41,37,43,29,34,21,8,44,43,21,8,24,46,11,11,30,22,35,39,33,20,30,20,52,23,13,16,28,35,39,9,41,13,42,49,40,36,41,28,10,24,30,8,11,24,36,21,20,32,23,28,33,23,19,26,45,12,49,21,37,22,44,47,43,19,17,46,28,27,22,28,36,53,21,13,22,45,16,25,17,19,25,13,11,23,23,36,19,25,22,34,22,33,40,53,13,36,30,27,33,31,44,49,40,39,53,27,26,21,22,18,43,29,43,20,31,22,39,16,31,27,20,33,5,13,31,60,28,32,17,30,20,29,20,27,29,21,34,29,38,19,54,3,40,24,22,45],
    "8": [54,42,60,56,46,24,33,33,69,37,37,34,70,39,103,7,76,56,48,37,28,9,45,73,40,9,19,34,18,18,56,82,70,29,53,58,29,24,43,57,55,40,63,42,17,39,38,31,66,53,40,34,83,65,70,60,45,28,48,44,56,48,59,50,25,49,27,69,39,11,46,50,32,44,65,30,85,71,84,28,9,51,14,86,58,45,50,57,16,93,63,38,20,46,64,16,67,28,49,60,39,53,40,37,56,51,61,51,52,66,4,33,70,28,19,67,32,44,35,61,36,82,73,30,44,75,47,44,63,14,51,21,21,61,81,68,32,29,35,34,67,31,78,12,40,64,38,43,37,57,92,59,47,45,58,42,16,15,58,7,21,47,46,34,35,57,55,59,36,41,43,44,56,50,6,39,61,35,44,47,31,27,47,23,58,39,39,37,77,10,54,55,42,35,27,91,48,15,71,46,48,47,53,38,48,46,61,36,10,56,24,21,29,35,27,45,64,56,70,63,56,61,50,71,81,81,78,27,52,56,43,46,45,48,13,47,53,46,20,14,47,36,36,53,81,25,23,49,54,16,97,56,78,58,67,83,50,18,11,21,25,39,49,47,96,62,47,70,33,39,29,61,37,21,44,46,55,20,38,78,48,20,39,68,46,62,56,52,37,56,33,59,37,43,51,95,91,25,13,71,53,42,45,40,12,63,50,57,67,29,76,93,65,73,49,59,30,30,68,25,70,34,36,36,54,83,29,51,79,37,72,62,77,51,39,37,19,25,69,74,41,41,78,65,79,75,39,65,70,48,41,33,79,50,33,52,23,52,52,25,65,21,75,27,35,58,64,14,46,32,63,35,80,50,53,87,60,22,47,44,40,32,36,39,42,61,62,31,38,79,73,32,37,82,44,60,42,46,68,35,22,38,47,54,74,76,120,29,78,46,50,69,76,63,63,51,54,41,58,46,63,75,40,57,37,50,29,59,83,33,85,18,25,109,82,87,85,19,67,49,30,72,44,58,60,60,46,25,15,50,83,65,82,74,92,36,47,11,38,60,49,52,85,35,71,26,67,19,41,57,55,61,35,70,63,39,34,34,61,68,64,79,36,34,63,51,9,52,33,68,74,45,47,11,36,26,89,39,76,81,49,34,96,27,81,81,37,23,75,53,64,39,13,52,20,28,51,43,17,46,65,66,31,18,65,36,70,55,55,102,34,80,9,56,52,75,75,29,49,13,46,42,42,41,34,52,43,22,49,18,74,35,51,22,80,72,49,6,27,95,68,53,28,46,50,20,67,40,40,18,42,50,61,40,52,52,39,67,65,25,27,43,36,66,82,56,89,23,52,77,64,69,38,59,51,64,57,57,45,16,35,68,22,71,25,54,9,16,85,51,78,40,36,53,47,42,21,25,25,55,60,90,25,23,36,74,60,36,49,51,43,52,67,50,19,25,30,63,31,43,14,29,37,49,34,38,61,36,72,29,37,33,34,39,37,44,46,68,83,57,78,44,16,72,74,31,48,73,37,22,16,30,28,28,36,49,73,25,75,37,32,55,45,57,40,44,33,27,21,47,28,43,66,44,44,68,15,23,91,47,27,74,24,34,48,20,72,10,35,73,58,70,46,64,81,22,85,27,58,71,70,53,74,55,25,45,24,94,66,48,82,63,57,112,15,62,35,48,35,53,41,47,76,27,59,58,73,33,13,54,40,44,30,77,18,86,54,19,75,13,70,47,42,38,16,18,68,56,56,46,36,75,70,93,67,36,12,51,23,69,47,16,49,71,59,19,19,81,9,57,78,60,62,53,19,31,84,19,34,39,75,93,28,36,57,47,59,34,27,33,31,37,95,49,43,54,63,62,40,10,25,60,27,34,43,54,55,12,90,90,51,25,15,36,43,44,63,50,62,35,38,78,29,52,47,73,57,27,44,63,20,77,44,61,86,66,53,42,43,53,23,67,54,57,40,50,49,61,42,44,24,5,29,73,61,31,58,88,6,63,74,5,47,38,44,44,63,45,54,22,42,52,47,60,51,86,25,12,52,44,38,39,34,39,40,31,45,28,53,55,33,53,63,63,74,29,57,46,52,47,55,51,44,8,55,64,59,48,41,51,40,45,70,58,42,29,9,26,35,49,65,73,45,20,17,62,51,53,70,27,34,21,73,71,33,30,73,36,54,21,52,33,43,15,64,12,37,83,28,10,38,61,54,107,56,25,58,53,17,9,32,10,60,8,71,86,25,37,32,85,52,43,55,24,70,65,50,44,51,76],
    "9": [6,48,96,118,67,51,80,60,62,105,106,88,19,111,75,110,109,88,117,131,59,78,35,50,59,53,65,93,44,80,70,92,94,63,56,133,79,77,46,36,65,119,23,131,60,91,85,73,68,155,53,66,135,116,60,59,69,77,49,87,28,151,75,58,107,69,15,113,155,53,70,80,120,56,95,87,62,32,73,90,48,98,105,71,63,82,101,98,79,146,132,117,36,113,70,90,98,53,69,101,77,148,89,107,122,99,51,95,91,31,89,96,82,83,156,23,59,57,43,22,39,95,128,127,121,96,99,123,103,111,74,90,76,75,102,15,48,33,30,72,77,41,80,20,49,98,84,9,55,42,60,106,48,46,24,148,83,86,54,107,96,81,55,86,41,26,29,63,17,126,55,64,121,154,13,118,54,100,42,74,69,104,96,23,118,70,43,149,78,93,101,71,39,123,103,63,49,54,56,116,60,99,35,44,127,120,47,88,80,139,61,125,27,106,53,130,84,64,62,113,111,118,50,75,23,161,82,78,25,74,43,101,23,72,41,76,26,74,68,54,109,70,117,78,28,62,87,83,73,109,74,124,89,115,105,140,51,189,69,73,67,148,34,54,149,59,55,92,53,178,53,47,52,102,75,152,111,63,101,65,42,67,126,98,159,88,142,22,68,76,67,45,40,51,88,72,41,40,39,53,38,100,38,72,111,49,52,15,91,133,137,147,35,57,61,123,20,101,141,59,139,11,48,52,56,50,52,88,32,94,108,44,92,73,67,115,52,79,112,36,110,49,125,74,32,86,134,119,22,12,89,41,30,77,51,69,117,39,38,125,28,70,119,74,130,99,45,63,141,43,135,144,55,54,104,131,95,150,84,62,52,36,49,82,51,60,17,49,78,127,152,121,62,41,107,71,138,128,38,53,46,66,89,62,84,83,73,32,51,60,60,48,54,99,65,62,97,88,121,49,79,63,59,81,75,34,75,81,14,44,39,140,107,122,80,99,93,125,110,104,76,31,93,78,109,55,58,85,116,85,95,108,94,72,31,98,100,69,35,92,82,69,89,82,101,94,104,67,56,20,41,82,48,73,123,62,58,82,25,22,19,108,63,70,73,104,114,54,99,86,18,140,41,112,91,94,52,100,75,59,41,37,101,73,89,120,91,115,53,52,107,90,134,85,154,114,43,77,29,50,29,80,35,61,43,40,12,104,33,144,73,56,80,68,128,118,28,103,65,116,55,60,64,110,122,101,48,65,27,117,67,77,110,54,82,89,134,64,85,26,47,57,62,95,82,73,84,50,98,98,66,114,23,97,134,78,65,32,16,41,100,114,109,164,170,113,50,119,65,77,45,71,125,65,124,76,119,65,55,28,65,139,115,35,144,99,39,50,124,138,113,84,37,152,89,139,66,41,75,120,97,86,129,68,57,99,24,58,15,86,80,97,82,65,81,92,79,106,33,39,131,109,104,15,29,80,39,113,83,122,20,46,61,27,104,99,144,59,43,88,76,121,80,135,31,78,92,11,148,52,91,63,99,66,124,131,83,61,32,49,108,101,70,125,114,72,52,91,102,86,46,126,65,102,108,63,36,140,53,127,79,40,105,124,136,114,80,102,61,96,35,88,69,65,165,122,129,30,53,119,117,50,40,48,74,113,34,120,40,48,91,60,124,13,106,144,82,108,22,60,99,41,106,51,33,95,39,67,72,79,77,79,56,46,129,114,61,72,62,68,108,153,52,82,30,14,117,66,89,69,128,56,142,96,65,58,130,29,103,97,78,18,143,99,80,53,30,80,67,73,152,118,134,74,36,58,126,76,48,106,32,82,64,71,92,137,158,89,58,105,91,82,50,45,83,67,13,41,46,71,47,42,77,24,61,13,61,112,114,122,58,38,89,132,70,89,49,103,64,53,105,97,41,36,110,78,82,148,35,160,41,46,106,87,93,26,13,111,107,72,79,95,73,129,20,62,42,146,54,163,71,37,65,25,89,47,54,45,59,71,144,53,28,69,121,30,42,90,37,67,37,109,109,135,90,164,102,69,22,133,38,69,38,68,51,53,27,75,25,76,73,133,106,46,121,84,125,93,96,126,62,75,39,66,139,54,79,102,58,130,116,79,64,69,34,39,96,86,150,20,48,86,59,39,90,154,130,56,44,83,106,111,112,130,69,123,102,38,45,120,90,46,57,49,68,112,41,86,95,70,68,96,138,95,92,113,72,76,68,52,49,62,36,43,87,78,128,56,49,26,101,116,69,99,92,81,63,81,106,124],
 #  "10": [86,128,118,132,115,182,91,132,79,243,196,138,85,106,152,33,211,66,91,37,234,68,142,215,136,70,56,193,209,223,125,148,123,177,80,168,148,174,142,135,50,204,132,185,180,92,88,111,30,60,59,54,157,144,184,158,162,148,120,63,140,114,179,94,130,126,186,28,98,64,216,128,197,74,27,67,52,203,240,174,62,201,89,77,87,156,121,63,68,73,138,144,110,111,135,79,114,178,109,75,130,210,104,207,55,194,118,77,241,137,57,96,138,88,233,130,57,214,24,150,136,61,206,98,110,97,145,89,34,231,163,137,141,135,195,122,136,226,113,185,43,168,105,35,169,157,130,164,42,172,129,125,152,79,254,227,133,129,100,96,150,63,30,111,109,58,173,120,160,100,129,94,19,129,225,81,118,140,60,69,213,132,140,123,118,68,250,206,101,109,128,142,209,197,203,200,129,130,248,66,178,70,183,143,69,199,103,106,238,170,125,98,134,75,24,76,182,71,177,129,72,151,44,205,192,103,101,159,155,29,196,122,120,155,99,139,107,151,151,201,52,201,69,274,63,280,83,98,222,40,280,43,40,178,79,90,148,70,21,133,228,97,60,273,90,154,130,207,67,105,155,247,138,169,32,92,73,78,87,97,75,260,169,194,163,146,254,47,93,292,156,147,133,169,209,120,225,127,191,144,25,121,132,158,98,160,70,83,137,121,114,52,175,28,135,96,50,18,127,97,30,135,157,238,150,107,112,63,58,152,84,158,217,108,163,23,130,65,16,133,98,71,163,99,196,98,197,25,129,128,61,134,73,173,86,111,242,84,77,41,97,236,56,60,135,49,111,127,186,187,165,69,106,120,172,87,104,88,37,128,154,147,66,179,37,127,68,145,143,105,124,133,184,37,244,95,205,131,74,96,79,191,133,316,85,168,169,190,218,219,32,255,28,98,120,139,53,148,129,153,91,28,61,188,117,133,268,224,149,42,97,173,35,59,44,104,35,83,173,62,50,176,150,183,192,214,113,82,178,108,145,131,152,113,128,31,170,114,91,131,152,21,188,103,264,162,257,157,55,141,83,189,201,221,77,225,153,67,44,189,237,209,221,49,124,171,160,150,186,126,103,97,141,112,171,127,90,77,52,114,65,204,232,200,28,275,184,212,225,88,183,225,138,123,136,140,122,38,125,202,226,123,182,215,70,177,145,182,49,112,46,14,136,140,124,47,68,106,185,166,96,229,93,90,209,157,68,197,182,141,115,188,128,126,130,121,126,178,170,144,87,59,101,246,42,127,54,68,71,182,55,111,76,187,74,111,196,190,159,70,75,111,146,134,41,186,227,47,179,203,166,131,146,54,55,130,135,142,23,220,207,131,220,111,134,217,197,160,124,185,67,140,146,134,191,170,223,143,216,27,114,180,121,78,230,123,12,136,81,155,70,218,68,95,55,85,179,159,215,183,256,165,100,38,160,55,138,187,200,139,224,61,207,69,174,128,197,134,159,181,149,76,96,71,55,145,109,145,109,144,148,62,10,132,28,78,273,169,162,97,140,71,81,86,160,192,69,184,85,192,125,134,26,192,111,43,158,135,59,246,64,73,202,114,150,198,83,81,38,71,144,144,69,176,223,53,143,109,84,215,108,194,165,33,69,194,144,146,143,83,122,147,228,139,252,171,173,98,84,97,206,71,160,160,44,109,271,42,50,125,236,160,56,152,128,165,77,93,145,114,75,167,101,85,181,212,76,229,41,249,147,115,244,68,111,176,132,187,80,103,256,222,142,163,162,63,99,79,176,220,108,172,48,94,121,40,123,104,123,156,119,188,50,89,81,149,49,115,144,122,139,159,159,166,172,109,74,177,194,131,68,175,65,16,244,49,138,144,184,137,104,117,160,63,164,144,326,290,62,165,141,26,64,77,118,33,90,77,56,129,89,68,83,254,100,113,146,159,278,167,29,195,145,111,70,200,52,228,92,134,34,91,40,157,243,152,108,187,70,125,96,136,277,165,100,260,284,220,199,168,121,210,198,151,146,67,47,236,169,135,246,50,153,170,14,99,211,118,19,41,56,101,112,97,76,255,143,176,193,198,69,132,129,88,109,183,47,184,137,173,98,175,74,200,191,122,71,131,281,142,142,173,221,144,141,67,201,173,9,166,140,185,285,114,197,119,100,145,120,162,150,204,136,112,120,197,22,93,97,288,70,151,145,177,23,134,118,83,187,154,141,83,146,81,243,141,171,139,81,107,119,104,84,50,59,81,172,214,109,53]
}
df = pd.DataFrame(data)

# df.plot.box(title="Consumer spending in each country", vert=False)
df.plot.box(title="")
plt.xlabel(u"Height of the regular expression.")
plt.ylabel(u"State number of the NFA.")
plt.grid(linestyle="-", alpha=0.1)
plt.savefig('/Users/mac/Desktop/hg/CAV2020/plots/Height_State.png')
#plt.show()

colnames = ["Entil", "S1", "S2", "ReC", "StateC", "TimeC", "ReM", "StateM", "TimeM"]
df = pd.read_csv(r'/Users/mac/Desktop/hg/EFFECTS/DataAnylase/data/result_height_5.csv', names=colnames, header=None)
print("TIMEC", df['TimeC'].mean())
print("TimeM", df['TimeM'].mean())
print("S1", df['S1'].mean(), "|- S2", df['S2'].mean())
print("StateC", df['StateC'].mean())
print("StateM", df['StateM'].mean())
print("completeness",  (df['ReM']- df['ReC']).sum() )
temp = df['TimeC']- df['TimeM']

print (temp)
#predicate: a bool value function
#ue simple math to descrbe algorithmn
#patial correctness
#inductive invanriants

#still need to translate to low level?

#x= [0,1,2,3,4,5,6]
#antichain=[2,2.1988,2.8636 , 5.1608, 9.3329, 60.1115, 1289.0355]
#antimirov=[2,2.0442,2.2843 , 3.365,5.4141, 19.1076, 896.2009]


#plt.figure()
#plt.plot(x,antichain,antimirov)
#plt.xlabel("time(s)")
#plt.ylabel("value(m)")
#plt.title("A simple plot")
#plt.show()

