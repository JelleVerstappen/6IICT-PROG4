## Challenge

`finance.py` contains a mistake. When running the implementation (found in `main.py`) this prints:

```
************hobby************* 
Initial deposit            500 
Initial deposit           1000 
Initial deposit           1500 
                          -100 
                          -200 
Brussel                   -300
Maasmechelen              -150
Doctor's visit cat        -400
Special feed for cat       -50
To Travel Expenses, 20    -500
From Travel Expenses,      500
Parijs                    -800
Doctor's visit dog        -200
Total: 200.0

*******Travel Expenses********
Initial deposit            500
Initial deposit           1000
Initial deposit           1500
                          -100
                          -200
Brussel                   -300
Maasmechelen              -150
Doctor's visit cat        -400
Special feed for cat       -50
To Travel Expenses, 20    -500
From Travel Expenses,      500
Parijs                    -800
Doctor's visit dog        -200
Total: 250.0

***********animals************
Initial deposit            500
Initial deposit           1000
Initial deposit           1500
                          -100
                          -200
Brussel                   -300
Maasmechelen              -150
Doctor's visit cat        -400
Special feed for cat       -50
To Travel Expenses, 20    -500
From Travel Expenses,      500
Parijs                    -800
Doctor's visit dog        -200
Total: 350.0
```

This is wrong. The correct print is:
```
************hobby************* 
Initial deposit            500
                          -100
                          -200
Total: 200.0

*******Travel Expenses********
Initial deposit           1000
Brussel                   -300
Maasmechelen              -150
From Travel Expenses,      500
Parijs                    -800
Total: 250.0

***********animals************
Initial deposit           1500
Doctor's visit cat        -400
Special feed for cat       -50
To Travel Expenses, 20    -500
Doctor's visit dog        -200
Total: 350.
```

The challenge is as follows:
* Find what part of the program causes this problem.
* Find out why the current code is causing this problem.
* Give a solution to the problem.

You can use all the files in this folder. As a hint, only one mistake was made in the current code.
