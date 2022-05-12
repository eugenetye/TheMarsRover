# The Mars Rover

This is a Python program that simulates a mars rover, with a mission to find the safest path to a given destination as some areas are traversable while others may be dangerous due to high radiation exposure.

## Project Specification

The world (mars) is created as a 2D array of cells. The size of the world is N by N, so each column is of size N and each row is of size N as well. 
Each cell represents a possible location to which the rover can move. The rover cannot move to any cell directly unless it is directly to the right 
or below the rover's current location. To illustrate, consider the following world of 4 by 4 cells:

![world](https://user-images.githubusercontent.com/105037989/167957976-f5202417-5594-4af6-a2f1-1e405844ac01.png)


Conditions and requirements:
* Each value refers to an area’s safety. 0 means the area is unsafe (deadly) and 4 means very safe.
* The rover can’t be in a location with 0 safety and must be avoided.
* The start location is always at location (0, 0) and the destination (goal) is always cell (N-1, N-1).
* If all paths from start to destination involve a cell with 0 safety, then abort the mission.
* There can be many safe paths as in the example above and these paths are: 
    * (0, 0) -> (1, 0) -> (1, 1) -> (2, 1) -> (2, 2) -> (3, 2) -> (3, 3)
    * (0, 0) -> (1, 0) -> (1, 1) -> (2, 1) -> (2, 2) -> (2, 3) -> (3, 3)
    * (0, 0) -> (0, 1) -> (1, 1) -> (2, 1) -> (2, 2) -> (3, 2) -> (3, 3)
    * (0, 0) -> (0, 1) -> (1, 1) -> (2, 1) -> (2, 2) -> (2, 3) -> (3, 3)   [Safest Path]
* Each path has a total of safety points, which is the sum of all values in cells of their path. In the above example, the safest path has 11 safety points.
* The rover must follow the safest path.

# Example Output
Using the world matrix in the above example, the output should be:

![output](https://user-images.githubusercontent.com/105037989/167957925-ebd1d2ff-9529-4a66-a34f-11a660fa1e17.png)



