from ast import Delete
from logging import root
from tkinter import *
from tkinter import ttk
import random
import tkinter.messagebox
import time
import threading
import multiprocessing

class Sorting:

    def __init__(self,num_elem = -1,min_num = -1,max_num = -1):
        self.num_elem = num_elem
        self.min_num = min_num
        self.max_num = max_num
        self.arr = []
    
        for x in range(self.num_elem):
            self.arr.append(random.randint(self.min_num,self.max_num))

    def selection_sort(self,mode,guiObj,speed):
        if mode == True:
            for i in range (self.num_elem):
                smallest = i
                #guiObj.draw_data(['green' if x == i else 'red' for x in range(len(self.arr))])
                guiObj.arrFrame.append((self.arr.copy(),['green' if x == i else 'red' for x in range(len(self.arr))]))
                #time.sleep(speed)
                for j in range (i+1, self.num_elem):
                    #guiObj.draw_data(['green' if x == i or x == j else 'blue' if x == smallest and x != i else 'red' for x in range(len(self.arr))])
                    guiObj.arrFrame.append((self.arr.copy(),['green' if x == i or x == j else 'blue' if x == smallest and x != i else 'red' for x in range(len(self.arr))]))
                    #time.sleep(speed)
                    if self.arr[smallest] > self.arr[j]:
                        smallest = j
                if i != smallest:
                    temp = self.arr[smallest]
                    self.arr[smallest] = self.arr[i]
                    self.arr[i] = temp
                    #guiObj.draw_data(['green' if x == i else 'red' for x in range(len(self.arr))])
                    guiObj.arrFrame.append((self.arr.copy(),['green' if x == i else 'red' for x in range(len(self.arr))]))
                    #time.sleep(speed)
        else:
            for i in range (self.num_elem):
                largest = i
                #guiObj.draw_data(['green' if x == i else 'red' for x in range(len(self.arr))])
                guiObj.arrFrame.append((self.arr.copy(),['green' if x == i else 'red' for x in range(len(self.arr))]))
                #time.sleep(speed)
                for j in range (i+1, self.num_elem):
                    #guiObj.draw_data(['green' if x == i or x == j else 'blue' if x == largest and x != i else 'red' for x in range(len(self.arr))])
                    guiObj.arrFrame.append((self.arr.copy(),['green' if x == i or x == j else 'blue' if x == largest and x != i else 'red' for x in range(len(self.arr))]))
                    #time.sleep(speed)
                    if self.arr[largest] < self.arr[j]:
                        largest = j
                if i != largest:
                    temp = self.arr[largest]
                    self.arr[largest] = self.arr[i]
                    self.arr[i] = temp
                    #guiObj.draw_data(['green' if x == i else 'red' for x in range(len(self.arr))])
                    guiObj.arrFrame.append((self.arr.copy(),['green' if x == i else 'red' for x in range(len(self.arr))]))
                    #time.sleep(speed)
        #guiObj.draw_data(['green' for x in range(len(self.arr))])
        guiObj.arrFrame.append((self.arr.copy(),['green' for x in range(len(self.arr))]))

    def bubble_sort(self,mode,guiObj,speed):
        if mode == True:
            for i in range (self.num_elem):
                for j in range(self.num_elem-(i+1)):
                    if self.arr[j] > self.arr[j+1]:
                        temp = self.arr[j]
                        self.arr[j] = self.arr[j+1]
                        self.arr[j+1] = temp
                        #guiObj.draw_data(['green' if x == j or x == j+1 else 'red' for x in range(len(self.arr))])
                        guiObj.arrFrame.append((self.arr.copy(),['green' if x == j or x == j+1 else 'red' for x in range(len(self.arr))]))
                        #time.sleep(speed)
        else:
            for i in range (self.num_elem):
                for j in range(self.num_elem-(i+1)):
                    if self.arr[j] < self.arr[j+1]:
                        temp = self.arr[j]
                        self.arr[j] = self.arr[j+1]
                        self.arr[j+1] = temp
                        #guiObj.draw_data(['green' if x == j or x == j+1 else 'red' for x in range(len(self.arr))])
                        guiObj.arrFrame.append((self.arr.copy(),['green' if x == j or x == j+1 else 'red' for x in range(len(self.arr))]))
                        #time.sleep(speed)
        #guiObj.draw_data(['green' for x in range(len(self.arr))])
        guiObj.arrFrame.append((self.arr.copy(),['green' for x in range(len(self.arr))]))


    def insertion_sort(self,mode,guiObj,speed):
        if mode == True:
            for i in range (1,self.num_elem):
                #guiObj.draw_data(['green' if x == i or x == i-1 else 'red' for x in range(len(self.arr))])
                guiObj.arrFrame.append((self.arr.copy(),['green' if x == i or x == i-1 else 'red' for x in range(len(self.arr))]))
                #time.sleep(speed)
                if self.arr[i] < self.arr[i-1]:
                    replace = i
                    for j in range(i,0,-1):
                        #guiObj.draw_data(['green' if x == i or x == j else 'red' for x in range(len(self.arr))])
                        guiObj.arrFrame.append((self.arr.copy(),['green' if x == i or x == j else 'red' for x in range(len(self.arr))]))
                        #time.sleep(speed)
                        if(self.arr[i] > self.arr[j-1]):
                            replace = j
                            break
                    if replace == i: replace = 0
                    temp = self.arr[i]
                    for j in range (i, replace, -1):
                        self.arr[j] = self.arr[j-1]
                        #guiObj.draw_data(['green' if x == i or x == replace else 'blue' if x == j or x == j-1 else 'red' for x in range(len(self.arr))])
                        guiObj.arrFrame.append((self.arr.copy(),['green' if x == i or x == replace else 'blue' if x == j or x == j-1 else 'red' for x in range(len(self.arr))]))
                        #time.sleep(speed)
                    self.arr[replace] = temp
        else:
            for i in range (1,self.num_elem):
                #guiObj.draw_data(['green' if x == i or x == i-1 else 'red' for x in range(len(self.arr))])
                guiObj.arrFrame.append((self.arr.copy(),['green' if x == i or x == i-1 else 'red' for x in range(len(self.arr))]))
                #time.sleep(speed)
                if self.arr[i] > self.arr[i-1]:
                    replace = i
                    for j in range(i,0,-1):
                        #guiObj.draw_data(['green' if x == i or x == j else 'red' for x in range(len(self.arr))])
                        guiObj.arrFrame.append((self.arr.copy(),['green' if x == i or x == j else 'red' for x in range(len(self.arr))]))
                        #time.sleep(speed)
                        if(self.arr[i] < self.arr[j-1]):
                            replace = j
                            break
                    if replace == i: replace = 0
                    temp = self.arr[i]
                    for j in range (i, replace, -1):
                        self.arr[j] = self.arr[j-1]
                        #guiObj.draw_data(['green' if x == i or x == replace else 'blue' if x == j or x == j-1 else 'red' for x in range(len(self.arr))])
                        guiObj.arrFrame.append((self.arr.copy(),['green' if x == i or x == replace else 'blue' if x == j or x == j-1 else 'red' for x in range(len(self.arr))]))
                        #time.sleep(speed)
                    self.arr[replace] = temp
        #guiObj.draw_data(['green' for x in range(len(self.arr))])
        guiObj.arrFrame.append((self.arr.copy(),['green' for x in range(len(self.arr))]))
          
    def merge_sort(self,mode,guiObj,arr,drawArr,speed,left = 0,right = 0):
        if len(arr) == 0: arr = self.arr.copy()
        #last = False
        # check if number of elements in arr is greater than 1
        if len(arr) > 1:
            # dividing array into sub arrays'
            left_arr = arr[:len(arr)//2]
            right_arr = arr[len(arr)//2:]
            middle = (left + right)//2  # middle var for self.arr the arr that we are displaying on screen
            # recursion
            self.merge_sort(mode,guiObj,left_arr,drawArr,speed,left,middle)
            self.merge_sort(mode,guiObj,right_arr,drawArr,speed,middle,right)

            i = 0 # left
            j = 0 # right
            k = 0 # new
            # acsending order
            if mode == True:
                drawArr = ['#f1b6fa' if left <= x < middle else '#7dfdff' if middle <= x < right else 'red' for x in range(len(self.arr))]
                #guiObj.draw_data(drawArr)
                guiObj.arrFrame.append((self.arr.copy(),drawArr.copy()))
                while i < len(left_arr) and j < len(right_arr):
                    if left_arr[i] < right_arr[j]:
                        self.arr[left] = left_arr[i] 
                        arr[k] = left_arr[i]
                        drawArr[left] = 'green'
                        guiObj.arrFrame.append((self.arr.copy(),drawArr.copy()))
                        #guiObj.draw_data(drawArr)
                        #time.sleep(speed)
                        i += 1
                        left += 1
                    else:
                        self.arr[left] = right_arr[j] 
                        arr[k] = right_arr[j]
                        drawArr[left] = 'green'
                        guiObj.arrFrame.append((self.arr.copy(),drawArr.copy())) 
                        #guiObj.draw_data(drawArr)
                        #time.sleep(speed)
                        j += 1
                        left += 1 
                    k += 1

                while i < len(left_arr):
                    self.arr[left] = left_arr[i] 
                    arr[k] = left_arr[i]
                    drawArr[left] ='green'
                    guiObj.arrFrame.append((self.arr.copy(),drawArr.copy()))
                    #guiObj.draw_data(drawArr)
                    #time.sleep(speed)
                    i += 1
                    k += 1
                    left+=1

                while j < len(right_arr):
                    self.arr[left] = right_arr[j] 
                    arr[k] = right_arr[j]
                    drawArr[left] = 'green'
                    guiObj.arrFrame.append((self.arr.copy(),drawArr.copy()))   
                    #guiObj.draw_data(drawArr)
                    #time.sleep(speed)
                    j += 1
                    k += 1
                    left+=1   
            # decsending order
            else:
                drawArr = ['#f1b6fa' if left <= x < middle else '#7dfdff' if middle <= x < right else 'red' for x in range(len(self.arr))]
                #guiObj.draw_data(drawArr)
                guiObj.arrFrame.append((self.arr.copy(),drawArr.copy()))
                while i < len(left_arr) and j < len(right_arr):
                    if left_arr[i] > right_arr[j]:
                        self.arr[left] = left_arr[i] 
                        arr[k] = left_arr[i]
                        drawArr[left] = 'green'
                        guiObj.arrFrame.append((self.arr.copy(),drawArr.copy()))
                        #guiObj.draw_data(drawArr)
                        #time.sleep(speed)
                        i += 1
                        left += 1
                    else:
                        self.arr[left] = right_arr[j] 
                        arr[k] = right_arr[j]
                        drawArr[left] = 'green'
                        guiObj.arrFrame.append((self.arr.copy(),drawArr.copy()))
                        #guiObj.draw_data(drawArr)
                        #time.sleep(speed)
                        j += 1
                        left += 1
                    k += 1

                while i < len(left_arr):
                    self.arr[left] = left_arr[i] 
                    arr[k] = left_arr[i]
                    drawArr[left] ='green'
                    guiObj.arrFrame.append((self.arr.copy(),drawArr.copy()))
                    #guiObj.draw_data(drawArr)
                    #time.sleep(speed)
                    i += 1
                    k += 1
                    left+=1

                while j < len(right_arr):
                    self.arr[left] = right_arr[j] 
                    arr[k] = right_arr[j]
                    drawArr[left] = 'green'
                    guiObj.arrFrame.append((self.arr.copy(),drawArr.copy()))
                    #guiObj.draw_data(drawArr)
                    #time.sleep(speed)
                    j += 1
                    k += 1
                    left+=1
                
    def quick_sort(self,guiObj,mode,left,right):
        if left < right:
            # recursion
            partition_pos = self.partition(guiObj,mode,left,right)
            self.quick_sort(guiObj, mode, left, partition_pos-1)
            self.quick_sort(guiObj, mode, partition_pos+1,right)
        #guiObj.draw_data(['green' for x in range(len(self.arr))])
        guiObj.arrFrame.append((self.arr.copy(),['green' for x in range(len(self.arr))]))
        #return arr
    # helper function to quick sort
    def partition(self,guiObj,mode,left,right):
        i = left           # left incrementer
        j = right-1        # right incrementer
        pivot = self.arr[right] # piviot will always be the right most element

        #guiObj.draw_data(['pink' if left <= x <= right else'red' for x in range(len(self.arr))])
        guiObj.arrFrame.append((self.arr.copy(),['pink' if left <= x <= right else'red' for x in range(len(self.arr))]))
        # acsending order
        if mode == True:
            while i < j:
                while i < right and self.arr[i] < pivot: # increment i until we find an element that is bigger than pivot
                    i += 1
                    #guiObj.draw_data(['blue' if x == i else 'purple' if x == j else 'pink' if left <= x <= right else 'red' for x in range(len(self.arr))])
                    guiObj.arrFrame.append((self.arr.copy(),['blue' if x == i else 'purple' if x == j else 'pink' if left <= x <= right else 'red' for x in range(len(self.arr))]))
                while j > left and self.arr[j] >= pivot:  # increment j until we find a element less than less than pivot
                    #guiObj.draw_data(['blue' if x == i else 'purple' if x == j else 'pink' if left <= x <= right else 'red' for x in range(len(self.arr))])
                    guiObj.arrFrame.append((self.arr.copy(),['blue' if x == i else 'purple' if x == j else 'pink' if left <= x <= right else 'red' for x in range(len(self.arr))]))
                    j -= 1
                if i < j:   # swap these elements if i and j did not cross yet
                    self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
                    #guiObj.draw_data(['blue' if x == i else 'purple' if x == j else 'pink' if left <= x <= right else 'red' for x in range(len(self.arr))])
                    guiObj.arrFrame.append((self.arr.copy(),['blue' if x == i else 'purple' if x == j else 'pink' if left <= x <= right else 'red' for x in range(len(self.arr))]))
            if self.arr[i] > pivot:  # if our ending position of i is greater than pivot, swap these values
                self.arr[i], self.arr[right] = self.arr[right], self.arr[i]
                #guiObj.draw_data(['blue' if x == i else 'purple' if x == j else 'pink' if left <= x <= right else 'red' for x in range(len(self.arr))])
                guiObj.arrFrame.append((self.arr.copy(),['blue' if x == i else 'purple' if x == j else 'pink' if left <= x <= right else 'red' for x in range(len(self.arr))]))
        # decsending order
        '''
        else:
            while i < j:
                while i < right and arr[i] > pivot:
                    i += 1
                while j > left and arr[j] < pivot:
                    j -= 1
                if i < j:
                    arr[i], arr[j] = arr[j], arr[i]
            if arr[i] < pivot:
                arr[i], arr[right] = arr[right], arr[i]
        '''
        return i

    def heap_sort(self,mode,guiObj):
        #arr = self.arr.copy()
        # first loop iteration will bring largest element to root, heapify
        for i in range((len(self.arr)-2)//2,-1,-1): # range is the last parent
            self.sift_down(mode,guiObj,i,len(self.arr))
        # second loop iteration actually sorts the list
        for j in range(len(self.arr)-1,0,-1):
            self.arr[0], self.arr[j] = self.arr[j], self.arr[0]
            self.sift_down(mode,guiObj,0,j)
        #guiObj.draw_data(['green' for x in range(len(self.arr))])
        guiObj.arrFrame.append((self.arr.copy(),['green' for x in range(len(self.arr))]))
    #i is the parent index and upper is the bounds of the array that we are to stay within
    def sift_down(self,mode,guiObj,i,upper):
        #guiObj.draw_data(['red' for x in range(len(self.arr))])
        guiObj.arrFrame.append((self.arr.copy(),['red' for x in range(len(self.arr))]))
        while(True):
            left_child = i*2+1
            right_child = i*2+2
            #guiObj.draw_data(['purple' if x == left_child and left_child < upper else 'blue' if x == right_child and right_child < upper else 'orange' if x == i else 'red' for x in range(len(self.arr))])
            guiObj.arrFrame.append((self.arr.copy(),['purple' if x == left_child and left_child < upper else 'blue' if x == right_child and right_child < upper else 'orange' if x == i else 'red' for x in range(len(self.arr))]))
            # checking if left and right child are valid index's note: upper can be anything 1-len(arr)
            if max(left_child,right_child) < upper:
                # checking if parent is of a higher value than its children, if so then break
                if self.arr[i] >= max(self.arr[left_child],self.arr[right_child]): break
                # if left child is greater than parent, then swap
                elif self.arr[left_child] > self.arr[right_child]:
                    self.arr[left_child], self.arr[i] = self.arr[i], self.arr[left_child]
                    i = left_child  # must update parent
                # if right child is greater than parent, then swap
                else:
                    self.arr[right_child], self.arr[i] = self.arr[i], self.arr[right_child]
                    i = right_child # must update parent
                #guiObj.draw_data(['purple' if x == left_child and left_child < upper else 'blue' if x == right_child and right_child < upper else 'orange' if x == i else 'red' for x in range(len(self.arr))])
                guiObj.arrFrame.append((self.arr.copy(),['purple' if x == left_child and left_child < upper else 'blue' if x == right_child and right_child < upper else 'orange' if x == i else 'red' for x in range(len(self.arr))]))
            # check left child
            elif left_child < upper:
                # if left child is greater than parent, then swap
                if self.arr[left_child] > self.arr[i]:
                    self.arr[left_child], self.arr[i] = self.arr[i], self.arr[left_child]
                    i = left_child  # must update parent
                    #guiObj.draw_data(['purple' if x == left_child and left_child < upper else 'blue' if x == right_child and right_child < upper else 'orange' if x == i else 'red' for x in range(len(self.arr))])
                    guiObj.arrFrame.append((self.arr.copy(),['purple' if x == left_child and left_child < upper else 'blue' if x == right_child and right_child < upper else 'orange' if x == i else 'red' for x in range(len(self.arr))]))
                # if this statement hits, it means that there is no need to continue
                else: break
            elif right_child < upper:
                # if right child is greater than parent, then swap
                if self.arr[right_child] > self.arr[i]:
                    self.arr[right_child], self.arr[i] = self.arr[i], self.arr[right_child]
                    i = right_child  # must update parent
                    #guiObj.draw_data(['purple' if x == left_child and left_child < upper else 'blue' if x == right_child and right_child < upper else 'orange' if x == i else 'red' for x in range(len(self.arr))])
                    guiObj.arrFrame.append((self.arr.copy(),['purple' if x == left_child and left_child < upper else 'blue' if x == right_child and right_child < upper else 'orange' if x == i else 'red' for x in range(len(self.arr))]))
                # if this statement hits, it means that there is no need to continue
                else: break
            # conditional for no children
            else: break

class GUI:

    def __init__(self, root):
        # variables & functions
        self.algChoice = StringVar()
        self.arrObj = Sorting()
        self.mode = StringVar()
        # base window attributes
        self.master = root
        self.master.title("Sorting Algorithm Visuals")
        self.master.geometry("1100x600")
        self.master.maxsize(1100,600)
        self.master.config(bg="black")
        # array for frames
        self.arrFrame = []
        

        #frame / base layout
        self.canvas = Canvas(self.master,width=875,height=400,bg='white')
        self.canvas.grid(row=0,column=0,padx=10,pady=5)

        self.UI_frame = Frame(self.master,width=875,height=170,bg="#4f4f4f") #grey
        self.UI_frame.grid(row=1,column=0,padx=10,pady=5)

        self.stat_frame = Frame(self.master,width=190,height=400,bg="#8ec284") #green
        self.stat_frame.grid(row=0,column=1,pady=5)

        self.box_frame = Frame(self.master,width=190,height=170,bg="#ad90d1")    #purple
        self.box_frame.grid(row=1,column=1,pady=5)

        #UI Area ROW 0
        Label(self.UI_frame,text="Algorithm",bg='grey').grid(row=0,column=0,padx=5,pady=5,sticky=W)
        self.algMenu = ttk.Combobox(self.UI_frame,textvariable=self.algChoice,values=['Insertion Sort','Bubble Sort','Selection Sort','Merge Sort','Quick Sort','Heap Sort'])
        self.algMenu.grid(row=0,column=1,padx=5,pady=5)
        self.algMenu.current(0)
        Button(self.UI_frame,text="Generate",command=self.generate,bg='blue').grid(row=0,column=2,padx=5,pady=5)
        Button(self.UI_frame,text="Execute",command=threading.Thread(target=self.execute).start,bg='red').grid(row=0,column=3,padx=5,pady=5)
        #Button(self.UI_frame,text="Execute",command=multiprocessing.Process(target=self.execute).start,bg='red').grid(row=0,column=3,padx=5,pady=5)
        #Button(self.UI_frame,text="Execute",command=self.execute,bg='red').grid(row=0,column=3,padx=5,pady=5)
        Button(self.UI_frame,text="Reset",command=self.reset,bg='green').grid(row=0,column=4,padx=5,pady=5)
        self.modeMenu = ttk.Combobox(self.UI_frame,textvariable=self.mode,values=['Ascending','Decsending'])
        self.modeMenu.grid(row=0,column=5,padx=5,pady=5)
        self.modeMenu.current(0)


        #UI Area ROW 1
        Label(self.UI_frame,text="Array Size",bg='grey').grid(row=1,column=0,padx=5,pady=5,sticky=W)
        self.sizeEntry = Entry(self.UI_frame)
        self.sizeEntry.grid(row=1,column=1,padx=5,pady=5,sticky=W)

        Label(self.UI_frame,text="Lower Bound",bg='grey').grid(row=1,column=2,padx=5,pady=5,sticky=W)
        self.lowerBound = Entry(self.UI_frame)
        self.lowerBound.grid(row=1,column=3,padx=5,pady=5,sticky=W)

        Label(self.UI_frame,text="Upper Bound",bg='grey').grid(row=1,column=4,padx=5,pady=5,sticky=W)
        self.upperBound = Entry(self.UI_frame)
        self.upperBound.grid(row=1,column=5,padx=5,pady=5,sticky=W)

        #UI Area ROW 2
        self.execSpeed = Scale(self.UI_frame,from_=0.0,to=2.0,length=150,digits=2,resolution=0.2,orient=HORIZONTAL,label="Execution Speed",bg="grey")
        self.execSpeed.grid(row=2,column=0,padx=5,pady=5,sticky=W)
        
        #Bottom right UI ROW 0
        self.ppButton = Button(self.box_frame,text="PAUSE",bg='grey')
        self.ppButton.grid(row=0,column=1,padx=5,pady=5)

        Button(self.box_frame,text="<",bg='grey').grid(row=0,column=0,padx=5,pady=5)
        Button(self.box_frame,text=">",bg='grey').grid(row=0,column=2,padx=5,pady=5)
    
    def refresh(self):
        self.master.update()
        self.master.after(1000,self.refresh)
        self.arrFrame.clear()

    def generate(self):
        # checks if parameters taken from GUI are valid
        try:
            self.arrObj = Sorting(int(self.sizeEntry.get()),int(self.lowerBound.get()),int(self.upperBound.get()))
        except:
            self.input_error()
            return
        self.draw_data(['red' for x in range(len(self.arrObj.arr))])

    def reset(self):
        self.canvas.delete("all")
        self.sizeEntry.delete(0,'end')
        self.lowerBound.delete(0,'end')
        self.upperBound.delete(0,'end')

    def frame_play(self):
        for x in self.arrFrame:
            self.draw_data_tup(x)
            self.master.update()
            #time.sleep(1)
        

    def draw_data_tup(self,frame):
        #self.canvas.delete("all")
        c_height = 400
        c_width = 875
        x_width = c_width / (len(self.arrObj.arr)+1)
        offset = 0 #30
        spacing = 0 #10
        max_elem = max(frame[0])
        normalized_data = [i / max_elem for i in frame[0]]
        self.canvas.delete("all")
        for i,x in enumerate(normalized_data):
            #top left
            x0 = i * x_width + offset + spacing
            y0 = c_height - x * 380            
            #bottom right
            x1 = (i+1) * x_width + offset
            y1 = c_height
            self.canvas.create_rectangle(x0,y0,x1,y1,fill=frame[1][i])
            self.canvas.create_text(x0+2,y0,anchor=SW,text=str(frame[0][i]))
            self.master.update()
        #self.master.update_idletasks()
        self.master.update()

    def draw_data(self,colorArr):
        self.canvas.delete("all")
        c_height = 400
        c_width = 875
        x_width = c_width / (len(self.arrObj.arr)+1)
        offset = 0 #30
        spacing = 0 #10
        max_elem = max(self.arrObj.arr)
        normalized_data = [i / max_elem for i in self.arrObj.arr]
        # i = index x = elem
        for i,x in enumerate(normalized_data):
            #top left
            x0 = i * x_width + offset + spacing
            y0 = c_height - x * 380            
            #bottom right
            x1 = (i+1) * x_width + offset
            y1 = c_height
            self.canvas.create_rectangle(x0,y0,x1,y1,fill=colorArr[i])
            self.canvas.create_text(x0+2,y0,anchor=SW,text=str(self.arrObj.arr[i]))
        self.master.update_idletasks()

    def execute(self):
        self.arrFrame.clear()
        if self.algChoice.get() == 'Bubble Sort':
            if self.mode.get() == 'Ascending':
                #self.refresh()
                #threading.Thread(target = self.arrObj.bubble_sort(True,self,self.execSpeed.get())).start()
                self.arrObj.bubble_sort(True,self,self.execSpeed.get())
                #threading.Thread(target = self.frame_play()).start()
                self.frame_play()
            else:
                self.refresh()
                threading.Thread(target = self.arrObj.bubble_sort(False,self,self.execSpeed.get())).start()
                self.frame_play()
        elif self.algChoice.get() == 'Selection Sort':
            if self.mode.get() == 'Ascending':
                self.refresh()
                threading.Thread(target = self.arrObj.selection_sort(True,self,self.execSpeed.get())).start()
                self.frame_play()
            else:
                self.refresh()
                threading.Thread(target = self.arrObj.selection_sort(False,self,self.execSpeed.get())).start()
                self.frame_play()
        elif self.algChoice.get() == 'Insertion Sort':
            if self.mode.get() == 'Ascending':
                self.refresh()
                threading.Thread(target = self.arrObj.insertion_sort(True,self,self.execSpeed.get())).start()
                self.frame_play()
            else:
                self.refresh()
                threading.Thread(target = self.arrObj.insertion_sort(False,self,self.execSpeed.get())).start()
                self.frame_play()
        elif self.algChoice.get() == 'Merge Sort':
            if self.mode.get() == 'Ascending':
                self.refresh()
                threading.Thread(target = self.arrObj.merge_sort(True,self,[],['red' for x in range(len(self.arrObj.arr))],self.execSpeed.get(),0,len(self.arrObj.arr))).start()
                self.frame_play()
            else:
                self.refresh()
                threading.Thread(target = self.arrObj.merge_sort(False,self,[],['red' for x in range(len(self.arrObj.arr))],self.execSpeed.get(),0,len(self.arrObj.arr))).start()
                self.frame_play()
        elif self.algChoice.get() == 'Quick Sort':
            self.refresh()
            threading.Thread(target = self.arrObj.quick_sort(self,True,0,len(self.arrObj.arr)-1)).start()
            self.frame_play()
        elif self.algChoice.get() == 'Heap Sort':
            self.refresh()
            threading.Thread(target = self.arrObj.heap_sort(True,self))
            self.frame_play()

    def input_error(self):
        tkinter.messagebox.showinfo("ERROR","Invalid parameters")


if __name__ == '__main__':
    # True = ascending order
    # False = decending order
    myTkRoot = Tk()
    my_gui = GUI(myTkRoot)
    myTkRoot.mainloop()