# SortingAlgorithmVisuals
## Description:
This program is made for learning purposes on 6 sorting algorithms through dynamic visuals on a fully functioning GUI.

## Functionality:
- Ability to generate a random array of integers through the options of *array size(integer), lower bound(integer), upper bound(integer)*
- Functioning *pause, play, foward, and backward* during execution
- *Execution speed* slider that is functional before and during execution for dynamic speed changes
- *Algorithm drop down menu* can choose from the options: *Insertion Sort, Selection Sort, Bubble Sort, Quick Sort, Merge Sort, and Heap Sort*
- *Comparison counter* that allows user to see the amount of sorting comparisons during its runtime

## Class Structure:
All within the main.py file there has been two defined classes, the *Sorting* class and the *GUI* class
### Sorting:
This class houses the constructor for the creation of a randomly generated array that is used for the visual. Parameters are from the defined text boxes in the GUI class that allow user enter the *array size, lower bound, and upper bound*.
```python
def __init__(self,num_elem = -1,min_num = -1,max_num = -1):
        self.num_elem = num_elem
        self.min_num = min_num
        self.max_num = max_num
        self.arr = []
    
        for _ in range(self.num_elem):
            self.arr.append(random.randint(self.min_num,self.max_num))
```
All other functions include the sorting algorithms outlined in *Functionality*.
*Note:* whenever the user generates a new array, the *Sorting object* is destroyed and a new object is created.
### GUI:
This class houses all the operations to be done in the GUI. The constructor of this class includes the creation of the GUI window and their assigned variables,data members to house the house the user input from the GUI: ```self.algChoice = StringVar()```(*algorithm choice*) & ```self.mode = StringVar()```(*descending or ascending*),creation of a empty *Sorting* object: ```self.arrObj = Sorting()```,the initialization of flags: ```self.abort = False```,```self.pp = False```, & ```self.done = IntVar()```, data members: ```self.index = 0```(index counter for *frame_play* function) & ```self.numCompare = 0```(var to hold number of comparisons at a given frame of the sort) *note: all data member functionality explanations will be further outlined in the design choice tab*

## Design Choice:
The current design choice for the animation of a selected sorting algorithm has gone through three changes with the third implementation being the current one employed.
- the first design choice was

