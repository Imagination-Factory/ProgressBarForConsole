#!/usr/bin/env python
# coding: utf-8


# Print iterations progress
def printProgressBar(iteration, total, prefix = '', suffix = '', decimals = 1, width = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  :  Int : current iteration
        total       - Required  :  Int : total iterations
        prefix      - Optional  :  Str : prefix string
        suffix      - Optional  :  Str : suffix string
        decimals    - Optional  :  Int : positive number of decimals in percent complete
        width       - Optional  :  Int : character length of bar
        fill        - Optional  :  Str : bar fill character
        printEnd    - Optional  :  Str : end character (e.g. "\r", "\r\n")
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(width * iteration // total)
    bar = fill * filledLength + '-' * (width - filledLength)
    
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    
    # After completion we print a new line
    if (iteration == total): 
        print()



import time

# Any list of items to iterate over
items = list(range(0, 82))
l = len(items)

# Initial call to print 0% progress
printProgressBar(0, l, prefix = 'Progress:', suffix = 'Complete', width = 50)
for i, item in enumerate(items):
    # Here we can do our computation...
    time.sleep(0.1)
    # Update Progress Bar
    printProgressBar(i + 1, l, prefix = 'Progress:', suffix = 'Complete', width = 50)

