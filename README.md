# Public Transport Shortest Path Finder

This repository contains Python code for a public transport shortest path finder using Dijkstra's algorithm. Given a network of stations and their connections, this program calculates the shortest path and distance between two selected stations using weighted edges that represent the travel time between stations.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Usage](#usage)
- [Installation](#installation)
- [Example](#example)
- [Contributing](#contributing)
- [License](#license)

## Introduction
This code provides a `Graph` class that represents a network of stations and connections in a public transport system. It uses Dijkstra's algorithm to find the shortest path and distance between two selected stations. Additionally, it employs the Levenshtein distance algorithm to handle slight discrepancies in station name input.

## Features
- **Graph Representation:** The code provides a `Graph` class to represent the network of stations and their connections. Stations are vertices, and connections between stations are edges with associated weights (travel times).
- **Dijkstra's Algorithm:** The `Graph` class implements Dijkstra's algorithm to calculate the shortest path and distance between two selected stations.
- **Levenshtein Distance:** A helper function is included to find the most similar station name in case of minor input discrepancies.

## Usage
1. Clone or download the repository.
2. Run the Python script in your preferred environment.
3. Enter the names of the starting and ending stations.

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/public-transport-shortest-path.git
   ```
2. Navigate to the project directory:
   ```sh
   cd public-transport-shortest-path
   ```
3. Run the Python script:
   ```sh
   python shortest_path_finder.py
   ```

## Example
```python
# Input: Enter the first station
start_vertex = input("Enter the first station: ")

# Correct any minor input discrepancies using Levenshtein distance
start_vertex = find_most_similar_string(start_vertex, vertex_names)

# Input: Enter the last station
end_vertex = input("Enter the last station: ")

# Correct any minor input discrepancies using Levenshtein distance
end_vertex = find_most_similar_string(end_vertex, vertex_names)

# Find and print the shortest path
path = g.shortest_path(start_vertex, end_vertex)
print("Shortest path:", " -> ".join(path))
```

## Contributing
Contributions are welcome! Please create a pull request for any enhancements or fixes.

## License
This project is licensed under the [MIT License](LICENSE).

---

*Note: This README provides an overview of the code functionality and usage. For detailed implementation, please refer to the source code in `shortest_path_finder.py`.*
