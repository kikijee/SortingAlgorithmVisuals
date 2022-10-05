from ast import Delete
from logging import root
from tkinter import *
from tkinter import ttk
import random
import tkinter.messagebox
import time

class Sorting:

    def __init__(self,num_elem = -1,min_num = -1,max_num = -1):
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

    def bubble_sort(self,mode,guiObj):
        #arr = self.arr.copy()
        if mode == True:
            for i in range (self.num_elem):
                for j in range(self.num_elem-(i+1)):
                    if self.arr[j] > self.arr[j+1]:
                        temp = self.arr[j]
                        self.arr[j] = self.arr[j+1]
                        self.arr[j+1] = temp
                        guiObj.draw_data()
                        time.sleep(0.2)
                        
        else:
            for i in range (self.num_elem):
                for j in range(self.num_elem-(i+1)):
                    if self.arr[j] < self.arr[j+1]:
                        temp = self.arr[j]
                        self.arr[j] = self.arr[j+1]
                        self.arr[j+1] = temp
                        guiObj.draw_data()
                        time.sleep(0.2)
        #return arr

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
        # check if number of elements in arr is greater than 1
        if len(arr) > 1:
            # dividing array into sub arrays'
            left_arr = arr[:len(arr)//2]
            right_arr = arr[len(arr)//2:]
            # recursion
            self.merge_sort(mode,left_arr)
            self.merge_sort(mode,right_arr)

            i = 0 # left
            j = 0 # right
            k = 0 # new
            # acsending order
            if mode == True:
                # adding the sublists into the new list
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
            # decsending order
            else:
                # adding the sublists into the new list
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

    def quick_sort(self,mode,arr = [],left = -1,right = -1):
        if len(arr) == 0:
            arr = self.arr.copy()
            left = 0
            right = len(arr)-1
        if left < right:
            # recursion
            partition_pos = self.partition(mode,arr,left,right)
            self.quick_sort(mode, arr, left, partition_pos-1)
            self.quick_sort(mode, arr,partition_pos+1,right)
        return arr
    # helper function to quick sort
    def partition(self,mode,arr,left,right):
        i = left           # left incrementer
        j = right-1        # right incrementer
        pivot = arr[right] # piviot will always be the right most element
        # acsending order
        if mode == True:
            while i < j:
                while i < right and arr[i] < pivot: # increment i until we find an element that is bigger than pivot
                    i += 1
                while j > left and arr[j] > pivot:  # increment j until we find a element less than less than pivot
                    j -= 1
                if i < j:   # swap these elements if i and j did not cross yet
                    arr[i], arr[j] = arr[j], arr[i]
            if arr[i] > pivot:  # if our ending position of i is greater than pivot, swap these values
                arr[i], arr[right] = arr[right], arr[i]
        # decsending order
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
        return i

    def heap_sort(self,mode):
        arr = self.arr.copy()
        # first loop iteration will bring largest element to root, heapify
        for i in range((len(arr)-2)//2,-1,-1): # range is the last parent
            self.sift_down(arr,i,len(arr))
        # second loop iteration actually sorts the list
        for j in range(len(arr)-1,0,-1):
            arr[0], arr[j] = arr[j], arr[0]
            self.sift_down(arr,0,j)
        return arr
    #i is the parent index and upper is the bounds of the array that we are to stay within
    def sift_down(self,arr,i,upper):
        while(True):
            left_child = i*2+1
            right_child = i*2+2
            # checking if left and right child are valid index's note: upper can be anything 1-len(arr)
            if max(left_child,right_child) < upper:
                # checking if parent is of a higher value than its children, if so then break
                if arr[i] >= max(arr[left_child],arr[right_child]): break
                # if left child is greater than parent, then swap
                elif arr[left_child] > arr[right_child]:
                    arr[left_child], arr[i] = arr[i], arr[left_child]
                    i = left_child  # must update parent
                # if right child is greater than parent, then swap
                else:
                    arr[right_child], arr[i] = arr[i], arr[right_child]
                    i = right_child # must update parent
            # check left child
            elif left_child < upper:
                # if left child is greater than parent, then swap
                if arr[left_child] > arr[i]:
                    arr[left_child], arr[i] = arr[i], arr[left_child]
                    i = left_child  # must update parent
                # if this statement hits, it means that there is no need to continue
                else: break
            elif right_child < upper:
                # if left child is greater than parent, then swap
                if arr[right_child] > arr[i]:
                    arr[right_child], arr[i] = arr[i], arr[right_child]
                    i = right_child  # must update parent
                # if this statement hits, it means that there is no need to continue
                else: break
            # conditional for no children
            else: break

'''
class GUI:

    def __init__(self, root):
        # base window attributes
        self.master = root
        self.master.title("Sorting Algorithm Visuals")
        self.master.geometry("1100x600")
        self.master.maxsize(1100,600)
        self.master.config(bg="black")

        #frame / base layout
        canvas = Canvas(self.master,width=875,height=400,bg='white')
        canvas.grid(row=0,column=0,padx=10,pady=5)

        UI_frame = Frame(self.master,width=875,height=170,bg="#4f4f4f")
        UI_frame.grid(row=1,column=0,padx=10,pady=5)

        stat_frame = Frame(self.master,width=190,height=400,bg="#8ec284")
        stat_frame.grid(row=0,column=1,pady=5)

        box_frame = Frame(self.master,width=190,height=170,bg="#ad90d1")
        box_frame.grid(row=1,column=1,pady=5)
'''

class GUI:

    def __init__(self, root):
        # variables & functions
        self.algChoice = StringVar()
        self.arrObj = Sorting()
        # base window attributes
        self.master = root
        self.master.title("Sorting Algorithm Visuals")
        self.master.geometry("1100x600")
        self.master.maxsize(1100,600)
        self.master.config(bg="black")

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
        Button(self.UI_frame,text="Execute",command=self.execute,bg='red').grid(row=0,column=3,padx=5,pady=5)

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

    def generate(self):
        # checks if parameters taken from GUI are valid
        try:
            self.arrObj = Sorting(int(self.sizeEntry.get()),int(self.lowerBound.get()),int(self.upperBound.get()))
        except:
            self.input_error()
            return
        self.draw_data()

    def draw_data(self):
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
            self.canvas.create_rectangle(x0,y0,x1,y1,fill="red")
            self.canvas.create_text(x0+2,y0,anchor=SW,text=str(self.arrObj.arr[i]))
        self.master.update_idletasks()

    def execute(self):
        if self.algChoice.get() == 'Bubble Sort':
            print(self.arrObj.bubble_sort(True,self))
        print(self.algChoice.get())
        
    def input_error(self):
        tkinter.messagebox.showinfo("ERROR","Invalid parameters")


if __name__ == '__main__':
    # True = ascending order
    # False = decending order
    myTkRoot = Tk()
    my_gui = GUI(myTkRoot)
    myTkRoot.mainloop()