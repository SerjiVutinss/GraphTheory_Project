## Graph Theory Project
A Python program to execute regular expressions on strings using Thompson's Construction

### Overview
* Currently works with any alphabet containing single character elements, e.g. (0,1,2) but not (0,10,20); (a,b,c) but not (a,ab,bc), etc
* Charting feature is still experimental and results are unpredictable due to random nature of chart drawing.

### Prerequisites - **matplotlib** and **networkx** for charting

[Instructions at matplotlib.org](https://matplotlib.org/users/installing.html)

    python -m pip install -U pip
    python -m pip install -U matplotlib

### Installation

1. Clone this repository
2. Install matplotlib as described above
3. Move into repository directory and then run:    

```python
      python app.py
```


### Sample Charts

I have included a selection of images of charted NFAs using the program.  It should be noted that the Initial state of the 'solution NFA' is coloured orange, while the Accept state is coloured green.

![a.b.c*](https://github.com/SerjiVutinss/GraphTheory_Project/blob/master/GraphTheory_Project/img/img_ab_c_star.png)

##### *Chart above shows the NFA for the reg-ex: *a.b.c***

![a.(b.b)*.c](https://github.com/SerjiVutinss/GraphTheory_Project/blob/master/GraphTheory_Project/img/img_a_bb_star_c_star.png)

##### *Chart above shows the NFA for the reg-ex: *a.(b.b)*.c**

![(a.b.c.(b|d))*](https://github.com/SerjiVutinss/GraphTheory_Project/blob/master/GraphTheory_Project/img/img_abc_and_b_or_d_star.png)

##### *Chart above shows the NFA for the reg-ex: *(a.b.c.(b|d))***
