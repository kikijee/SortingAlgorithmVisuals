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
This class houses all the operations to be done in the GUI
#### Constructor:
The constructor of this class includes the creation of the GUI window and their assigned variables,data members to house the house the user input from the GUI: ```self.algChoice = StringVar()```(*algorithm choice*) & ```self.mode = StringVar()```(*descending or ascending*),creation of a empty *Sorting* object: ```self.arrObj = Sorting()```,the initialization of flags: ```self.abort = False```,```self.pp = False```, & ```self.done = IntVar()```, data members: ```self.index = 0```(index counter for *frame_play* function) & ```self.numCompare = 0```(var to hold number of comparisons at a given frame of the sort) *note: all data member functionality explanations will be further outlined in the design choice tab*
#### generate():
The generate function is to create a new *sorting* object by using the ```.get()``` method on the tkinter text box objects and pass them to the parameters of the *sorting* constructor, if there is invalid parameters, there is a error window that pops up explaining the invalid input. If there is no error, the *draw_data* function is then called.
```python
def generate(self):
        # checks if parameters taken from GUI are valid
        try:
            self.arrObj = Sorting(int(self.sizeEntry.get()),int(self.lowerBound.get()),int(self.upperBound.get()))
        except:
            self.input_error()
            return
        self.draw_data(['red' for x in range(len(self.arrObj.arr))])
        self.execButton.config(state=NORMAL)
```
#### draw_data(colorArr):
The *draw_data* function is to draw the array on the canvas of the GUI through rectangles whose height corresponds to that intergers value. To do this ww first normilize the data of ```self.arrObj.arr``` by taking the max element of that array and creating a new array that holds the decimal value (percentage of the max height) at a given index. the passed in *colorArr* contains strings that specify the color of a rectagle at a given index.
```python
max_elem = max(self.arrObj.arr)
normalized_data = [i / max_elem for i in self.arrObj.arr]
```
This normalized data is then used in a for loop to draw the rectangles.
```python
for i,x in enumerate(normalized_data):
        #top left of rectangle
        x0 = i * x_width + offset + spacing
        y0 = c_height - x * 380            
        #bottom right of rectangle
        x1 = (i+1) * x_width + offset
        y1 = c_height
        self.canvas.create_rectangle(x0,y0,x1,y1,fill=colorArr[i])
        self.canvas.create_text(x0+2,y0,anchor=SW,text=str(self.arrObj.arr[i]))
```
#### execute():
The *execute* function checks what sorting algorithm to call through the ```self.arrObj``` object, once we find out which algorithm, it also checks whether the user wants the algorithm to sort in ascending or descending order, the function corresponding to the algorithm is then called, along with the function *frame_play* after. example:
```python
 if self.algChoice.get() == 'Bubble Sort':
            if self.mode.get() == 'Ascending':
                self.arrObj.bubble_sort(True,self,self.execSpeed.get())
                self.frame_play()
            else:
                self.arrObj.bubble_sort(False,self,self.execSpeed.get())
                self.frame_play()
```
#### frame_play():
The *frame_play* function is the function responsible for the on screen animations.
## How to run:
- There is a executable file ```main.exe``` included
- to run on terminal with main.py ```python3 .\main.py```

