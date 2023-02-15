from functions import print_colorvars
from os.path import exists

testNames = [
    'test_M05D02O2',
    'test_M05D02O4',
    'test_M05D02O5',
    'test_M05D02O6',
    'test_M05D02O7',
    'test_M05D02O8',
    'test_M05D02O9',
    'test_M05D02O10',
    'test_M05D02O12',
    'test_M05D02O13',
]

for testName in testNames:
    print('')
    print_colorvars(vars=[testName])
    if exists(testName + '.py'):
        __import__(testName)
    else:
        print_colorvars(vars=['TESTFILE NOT FOUND!'], color='red')
