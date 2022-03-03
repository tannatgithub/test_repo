import os

import numpy as np

env_var = os.environ

def test1():
    a = 10
    b = 20 
    print(a+b)

def main():
    test1()
    print('Now run through test1')
if __name__=="__main__":
    main()