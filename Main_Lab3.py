#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 14:00:10 2019

@author: eduardofernandez
"""

from Lab_3 import SortedList

from timeit import default_timer as timer

if __name__ == "__main__": 
    
    
    L1 = SortedList()
    L1.AppendList([7,5,3,1])
    print ("Printing list ")
    start = timer()
    L1.Print()
    end = timer()
    print('Runtime:',str(end-start))
    
    print ("Inserting 8 into list ")
    start = timer()
    L1.Insert(8)
    end = timer()
    print('Runtime:',str(end-start))
    L1.Print()
    
    print ("Deleting 3 from list ")
    start = timer()
    L1.Delete(3)
    end = timer()
    print('Runtime:',str(end-start))
    L1.Print()
    
    print ("Merging M to List" )
    M = SortedList()
    M.AppendList([6,4,2])
    M.Print()
    start = timer()
    L1.Merge(M)
    end = timer()
    print('Runtime:',str(end-start))
    L1.Print()
    
    print ("Returning index of 1 ")
    start = timer()
    print (L1.IndexOf(1))
    end = timer()
    print('Runtime:',str(end-start))
    
    print ("Returning Min Value ")
    start = timer()
    print (L1.Min())
    end = timer()
    print('Runtime:',str(end-start))
    print ("Returining Max Value" )
    start = timer()
    print (L1.Max())
    end = timer()
    print('Runtime:',str(end-start))
    
    print ("Checking if there are duplicates ")
    start = timer()
    print (L1.HasDuplicates())
    end = timer()
    print('Runtime:',str(end-start))
    
    print ("Returing k-th smallest element ")
    start = timer()
    print (L1.Select(0))
    end = timer()
    print('Runtime:',str(end-start))
    
    print ("Clearing List: ")
    start = timer()
    L1.Clear()
    end = timer()
    print('Runtime:',str(end-start))
    L1.Print()