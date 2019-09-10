# A-search-algorithm

## What is it?
A* Search algorithm is one of the best and popular technique used in path-finding and graph traversals.

## Why A* Search Algorithm?
Informally speaking, A* Search algorithms, unlike other traversal techniques, it has “brains”. What it means is that it is really a smart algorithm which separates it from the other conventional algorithms. This fact is cleared in detail in below sections.
And it is also worth mentioning that many games and web-based maps use this algorithm to find the shortest path very efficiently (approximation).

If you wish to know more, I recommend you to check out https://www.geeksforgeeks.org/a-search-algorithm/ , or any other page

## Setup
To run this project, you will just need a program that can read python, you can also use
https://www.onlinegdb.com/online_python_compiler

## How to use it?
First, you need to define a map with length (x) and height (y), the map will be generated automatically.
Then, manually define the point where you start, your goal and the blocks that you cannot visit.

## Details
You cannot travel diagonally next to a blocked up coordinate (if the blocked path is in the way).
The code uses map to save the info of every point in the map, and uses mapXY to searh the index of a point that is being calculated.

***You will find the map I use for the code in this project***
