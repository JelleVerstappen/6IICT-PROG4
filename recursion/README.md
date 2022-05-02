## General
This README contains info for exercises 2.3 and 2.4. 

### 2.3 - Recursive rectangles
It is possible to see recursion in action visually. For this we will be using pygame. Complete the `recursive_draw` function in `Opdracht 2.3 Recursive Rectangles`. It will be used in the `main` function (which is already completed) to draw progressively smaller rectangles on the screen. The scale and position of the rectangles should change as follows:
* `scale`: each rectangle should be 80% of the width and height of the previous rectangle.
* `position`: The starting point (top left) of each rectangle should be increased. The `x-co` should increase by 10% the width (goes right), the `y-co` with 10% the height (goes down).

The function should stop drawing rectangles once their width or height is equal to or lower than `10 pixels`.

The resulting figure should look something like below.

<p align="center">
  <img src="images/figure_recursive_rectangles.png" width="400" height="200"/>
</p>


`Tip`: The `recursive_draw` function should not return anything outside the function. For this reason only the base case needs a return statement.

### 2.4 - Fractals
A fractal is a geometrical figure, where each part has the same statistical character as the whole. In layman's terms, they are useful in modelling structures in which similar patterns recur at progressively smaller scales (see snowflake for an example).

<p align="center">
  <img src="images/snowflake_rectangle.png" width="200" height="200"/>
</p>

Fractals are best programmed recursively. For this we will be using pygame. Complete the `recursive_fractal` function in `Opdracht 2.4 Fractals`. It will be used in the `main` function (which is already completed) to draw fractals with a certain "depth". Depending on the depth used in `main` the fractal will expand. Below figures show the resulting fractal when `recursive_fractal` is called with a respective depth of 1, 2 and 3.

The function should stop drawing fractals once the depth reaches `0`.

```
fractal_depth = 1
recursive_fractal(0, 0, width, height, fractal_depth, screen)
# ------------------
fractal_depth = 2
recursive_fractal(0, 0, width, height, fractal_depth, screen)
# ------------------
fractal_depth = 3
recursive_fractal(0, 0, width, height, fractal_depth, screen)
```

<p float="center" align="center">
  <img src="images/fractal_1.png" width="200" />
  <img src="images/fractal_2.png" width="200" /> 
  <img src="images/fractal_3.png" width="200" />
</p>

`Opdracht 2.4 Fractals` already contains a `draw_shape` function (is completed). Calling it will draw the above `H-shape` at a certain x- and y-co, with a certain width and height, on the screen.

```
draw_shape(x,y,width,height, screen)
```

`Tip`: The `recusive_fractal` function should not return anything outside the function. For this reason only the base case should use a return statement. Think about how many fractals each depth of recursion should have. Is there a pattern?