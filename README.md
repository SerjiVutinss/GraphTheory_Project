## Graph Theory Project
A Python program to execute regular expressions on strings using Thompson's Construction

### Overview
* Currently works with any alphabet containing single character elements, e.g. (0,1,2) but not (0,10,20); (a,b,c) but not (a,ab,bc), etc
* Charting feature is still experimental and results are unpredictable due to random nature of chart drawing.

### Prerequisites - **matplotlib** and **networkx** for charting

[Instructions at matplotlib.org](https://matplotlib.org/users/installing.html)

    python -m pip install -U pip
    python -m pip install -U matplotlib

### Installation and Running

1. Clone this repository
2. Install matplotlib as described above
3. Move into repository directory and then run:    

```python
      python app.py
```

### Usage

On execution, the menu is displayed giving users a number of options and toggles.  While at the main menu, 'q' is used to quit the application.

This repo contains a sample file of infixes and a sample file of strings (infixes.txt & strings.txt).  The results of these matches are stored in the results.csv file.

#### Options

The plotting of graphs and writing results to a CSV file can be toggled on or off and these are both off by default.

Enabling the 'Toggle write to CSV file for result set' option, the user will be prompted for the output file path which can not be left empty.  Once set, the output file name will not change until 'Write To CSV' is explicitly disabled and re-enabled by the user. 

1. Manually enter an infix and a string to match against it
    * Infix can not be an empty
    * String can be an empty string
    
2. Manually enter the filename of a file of infixes and a file of strings to match - neither file name can be left empty

3. Run test suite of strings and infixes - match harcoded lists of infixes and strings

### Sample Charts

A selection of images of charted NFAs using the program.  

It should be noted that the Initial state of the 'solution NFA' (or overall NFA) is coloured orange, while the Accept state is coloured green.  The Initial state should have an in-degree of zero, while the Accept state should have an out-degree of zero.

Due to the random nature of the chart layouts, easily readable charts are not always generated.  This is a feature which could be expanded on and improved on in future.

![a.b.c*](https://github.com/SerjiVutinss/GraphTheory_Project/blob/master/GraphTheory_Project/img/img_ab_c_star.png)

##### *Chart above shows the NFA for the reg-ex: *a.b.c***

![a.(b.b)*.c](https://github.com/SerjiVutinss/GraphTheory_Project/blob/master/GraphTheory_Project/img/img_a_bb_star_c_star.png)

##### *Chart above shows the NFA for the reg-ex: *a.(b.b)*.c**

![(a.b.c.(b|d))*](https://github.com/SerjiVutinss/GraphTheory_Project/blob/master/GraphTheory_Project/img/img_abc_and_b_or_d_star.png)

##### *Chart above shows the NFA for the reg-ex: *(a.b.c.(b|d))***
