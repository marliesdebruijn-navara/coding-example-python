# coding-example-python

Example of some code I made in advent of code 2024 - day 6.

During advent of code, I worked in a jupyter notebook. This repository is the part for day 6.
The examples and input are in their own folders, as I had at least one for each day.

The file day6A.py contains the solution for part 1.
The question is: There is a guard, you have a map, how many distinct positions will the guard visit before leaving the mapped area?

- If there is something directly in front of you, turn right 90 degrees.
- Otherwise, take a step forward.

The file day6B.py contains the solution for part 2 (and part 1).
Here, we want to know in how many spots on the map we could add an obstacle, such that the guard is stuck in a loop.

For the solution in 6A, I kept moving one step at a time.
For solution in 6B, I have updated this, such that longer stretches are moved in one go (until the guard has to turn, leaves the map, or is stuck in a loop).