from tkinter import *
import random

class Sorting:

    def __init__(self,num_elem,min_num,max_num):
        self.num_elem = num_elem
        self.min_num = min_num
        self.max_num = max_num
        self.arr = []

        for x in range(self.num_elem):
            self.arr.append(random.randint(self.min_num,self.max_num))


    def selection_sort(self,mode):
        arr = self.arr.copy()
        if mode == True:
            for i in range (self.num_elem):
                smallest = i
                for j in range (i+1, self.num_elem):
                    if arr[smallest] > arr[j]:
                        smallest = j
                if i != smallest:
                    temp = arr[smallest]
                    arr[smallest] = arr[i]
                    arr[i] = temp
        else:
            for i in range (self.num_elem):
                largest = i
                for j in range (i+1, self.num_elem):
                    if arr[largest] < arr[j]:
                        largest = j
                if i != largest:
                    temp = arr[largest]
                    arr[largest] = arr[i]
                    arr[i] = temp
        return arr

    def bubble_sort(self,mode):
        arr = self.arr.copy()
        if mode == True:
            for i in range (self.num_elem):
                for j in range(self.num_elem-(i+1)):
                    if arr[j] > arr[j+1]:
                        temp = arr[j]
                        arr[j] = arr[j+1]
                        arr[j+1] = temp
        else:
            for i in range (self.num_elem):
                for j in range(self.num_elem-(i+1)):
                    if arr[j] < arr[j+1]:
                        temp = arr[j]
                        arr[j] = arr[j+1]
                        arr[j+1] = temp
        return arr

    def insertion_sort(self,mode):
        arr = self.arr.copy()
        if mode == True:
            for i in range (1,self.num_elem):
                if arr[i] < arr[i-1]:
                    replace = i
                    for j in range(i,0,-1):
                        if(arr[i] > arr[j-1]):
                            replace = j
                            break
                    if replace == i: replace = 0
                    temp = arr[i]
                    for j in range (i, replace, -1):
                        arr[j] = arr[j-1]
                    arr[replace] = temp
        else:
            for i in range (1,self.num_elem):
                if arr[i] > arr[i-1]:
                    replace = i
                    for j in range(i,0,-1):
                        if(arr[i] < arr[j-1]):
                            replace = j
                            break
                    if replace == i: replace = 0
                    temp = arr[i]
                    for j in range (i, replace, -1):
                        arr[j] = arr[j-1]
                    arr[replace] = temp
        return arr
                    
    def merge_sort(self,mode,arr = []):
        if len(arr) == 0: arr = self.arr.copy()
        if len(arr) > 1:
            left_arr = arr[:len(arr)//2]
            right_arr = arr[len(arr)//2:]

            self.merge_sort(mode,left_arr)
            self.merge_sort(mode,right_arr)

            i = 0 # left
            j = 0 # right
            k = 0 # new
            if mode == True:
                while i < len(left_arr) and j < len(right_arr):
                    if left_arr[i] < right_arr[j]:
                        arr[k] = left_arr[i]
                        i += 1
                    else:
                        arr[k] = right_arr[j]
                        j += 1
                    k += 1

                while i < len(left_arr):
                    arr[k] = left_arr[i]
                    i += 1
                    k += 1

                while j < len(right_arr):
                    arr[k] = right_arr[j]
                    j += 1
                    k += 1
            else:
                while i < len(left_arr) and j < len(right_arr):
                    if left_arr[i] > right_arr[j]:
                        arr[k] = left_arr[i]
                        i += 1
                    else:
                        arr[k] = right_arr[j]
                        j += 1
                    k += 1

                while i < len(left_arr):
                    arr[k] = left_arr[i]
                    i += 1
                    k += 1

                while j < len(right_arr):
                    arr[k] = right_arr[j]
                    j += 1
                    k += 1
            return arr


    def quick_sort(self,mode):
        arr = self.arr.copy()

    def heap_sort(self,mode):
        arr = self.arr.copy()

    def radix_sort(self,mode):
        arr = self.arr.copy()


if __name__ == '__main__':
    # True = ascending order
    # False = decending order
    
    L = Sorting(10,0,100)
    print(L.arr)
    print(L.merge_sort(False))