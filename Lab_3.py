#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 19:37:46 2019

@author: eduardofernandez
"""

class Node (object):
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

class SortedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        
    def isEmpty(self):
        return self.head == None
    
    def AppendList(self,python_list):
        for d in python_list:
            self.Insert(d)
                
    def GetLength(self):
        t = self.head
        w = 0
        while t is not None:
          w += 1
          t = t.next
        return w
    
    def BubbleSort(self):
        listlen = self.GetLength()
        for i in range (1,listlen):
            t = self.head
            for j in range (listlen - 1):
                if t.data > t.next.data:
                    t.next.data, t.data = t.data, t.next.data
                t = t.next
            
            
    def Print(self):
        t = self.head
        while t is not None:
            print(t.data,end = ' ')
            t = t.next
        print()
        
    def Insert(self,x):
        if self.head is None:
            self.head = Node(x)
            self.tail = self.head
            self.BubbleSort()
        else:
            self.tail.next = Node(x)
            self.tail = self.tail.next
            self.BubbleSort()
            
                
    def Delete (self,i):
        t = self.head
        while t is not None:
            if t.next is None:
                return
            elif i == t.next.data:
                t.next = t.next.next
            t = t.next
               
    
    def Merge(self,M):
        t = M.head
        while t is not None:
            self.Insert(t.data)
            t = t.next
    
    def IndexOf(self,i): 
        t = self.head
        index = 0
        if t is None:
          return 
        while t is not None:
          if t.data == i:
            return index
          t = t.next
          index += 1
                
    def Clear (self):
        self.head = None
        self.tail = None
        
    def Min(self):
        return self.head.data
    
    
    def Max(self):
        return  self.tail.data
    
    
    def HasDuplicates(self):
        if self.head == None:
            return False
        t = self.head
        while t != self.tail:
            if t.data == t.next.data:
                return True
            t = t.next
        return False
         
    
    def Select(self,k):
        t = self.head
        index = 0
        if t is None:
            return 0
        while t is not None:
            if index == k:
                return t.data
            t = t.next
            index += 1
         

    