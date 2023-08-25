import heapq
import Levenshtein

class Graph:
    # (same as before)
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        self.vertices[vertex] = []

    def add_edge(self, vertex1, vertex2, weight):
        self.vertices[vertex1].append((vertex2, weight))
        self.vertices[vertex2].append((vertex1, weight))

    def dijkstra(self, start_vertex):
        distances = {vertex: float('inf') for vertex in self.vertices}
        distances[start_vertex] = 0

        priority_queue = [(0, start_vertex)]

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)

            if current_distance > distances[current_vertex]:
                continue

            for neighbor, weight in self.vertices[current_vertex]:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances
    def shortest_path(self, start_vertex, end_vertex):
        distances = {vertex: float('inf') for vertex in self.vertices}
        distances[start_vertex] = 0

        priority_queue = [(0, start_vertex)]
        previous_vertices = {}

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)

            if current_distance > distances[current_vertex]:
                continue

            for neighbor, weight in self.vertices[current_vertex]:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))
                    previous_vertices[neighbor] = current_vertex

        shortest_path = []
        current = end_vertex
        while current in previous_vertices:
            shortest_path.insert(0, current)
            current = previous_vertices[current]
        shortest_path.insert(0, start_vertex)

        return shortest_path
def find_most_similar_string(target_string, string_array):
    most_similar_string = None
    min_distance = float('inf')

    for string in string_array:
        distance = Levenshtein.distance(target_string, string)
        if distance < min_distance:
            min_distance = distance
            most_similar_string = string

    return most_similar_string
vertex_names = [
    "Noida Sector 62~B",
    "Botanical Garden~B",
    "Yamuna Bank~B",
    "Rajiv Chowk~BY",
    "Vaishali~B",
    "Moti Nagar~B",
    "Janak Puri West~BO",
    "Dwarka Sector 21~B",
    "Huda City Center~Y",
    "Saket~Y",
    "Vishwavidyalaya~Y",
    "Chandni Chowk~Y",
    "New Delhi~YO",
    "AIIMS~Y",
    "Shivaji Stadium~O",
    "DDS Campus~O",
    "IGI Airport~O",
    "Rajouri Garden~BP",
    "Netaji Subhash Place~PR",
    "Punjabi Bagh West~P"
]
# Create a graph and add vertices and edges
g = Graph()
# (add vertices and edges)
# Adding vertices
g.add_vertex("Noida Sector 62~B")
g.add_vertex("Botanical Garden~B")
g.add_vertex("Yamuna Bank~B")
g.add_vertex("Rajiv Chowk~BY")
g.add_vertex("Vaishali~B")
g.add_vertex("Moti Nagar~B")
g.add_vertex("Janak Puri West~BO")
g.add_vertex("Dwarka Sector 21~B")
g.add_vertex("Huda City Center~Y")
g.add_vertex("Saket~Y")
g.add_vertex("Vishwavidyalaya~Y")
g.add_vertex("Chandni Chowk~Y")
g.add_vertex("New Delhi~YO")
g.add_vertex("AIIMS~Y")
g.add_vertex("Shivaji Stadium~O")
g.add_vertex("DDS Campus~O")
g.add_vertex("IGI Airport~O")
g.add_vertex("Rajouri Garden~BP")
g.add_vertex("Netaji Subhash Place~PR")
g.add_vertex("Punjabi Bagh West~P")

# Adding edges
g.add_edge("Noida Sector 62~B", "Botanical Garden~B", 8)
g.add_edge("Botanical Garden~B", "Yamuna Bank~B", 10)
g.add_edge("Yamuna Bank~B", "Vaishali~B", 8)
g.add_edge("Yamuna Bank~B", "Rajiv Chowk~BY", 6)
g.add_edge("Rajiv Chowk~BY", "Moti Nagar~B", 9)
g.add_edge("Moti Nagar~B", "Janak Puri West~BO", 7)
g.add_edge("Janak Puri West~BO", "Dwarka Sector 21~B", 6)
g.add_edge("Huda City Center~Y", "Saket~Y", 15)
g.add_edge("Saket~Y", "AIIMS~Y", 6)
g.add_edge("AIIMS~Y", "Rajiv Chowk~BY", 7)
g.add_edge("Rajiv Chowk~BY", "New Delhi~YO", 1)
g.add_edge("New Delhi~YO", "Chandni Chowk~Y", 2)
g.add_edge("Chandni Chowk~Y", "Vishwavidyalaya~Y", 5)
g.add_edge("New Delhi~YO", "Shivaji Stadium~O", 2)
g.add_edge("Shivaji Stadium~O", "DDS Campus~O", 7)
g.add_edge("DDS Campus~O", "IGI Airport~O", 8)
g.add_edge("Moti Nagar~B", "Rajouri Garden~BP", 2)
g.add_edge("Punjabi Bagh West~P", "Rajouri Garden~BP", 2)
g.add_edge("Punjabi Bagh West~P", "Netaji Subhash Place~PR", 3)
# Find the shortest path
start_vertex = input("enter the first station: ")
start_vertex = find_most_similar_string(start_vertex,vertex_names)
end_vertex = input("enter the last station: ")
end_vertex = find_most_similar_string(end_vertex,vertex_names)
path = g.shortest_path(start_vertex, end_vertex)

shortest_distances = g.dijkstra(start_vertex)

print("Shortest distances from vertex", start_vertex)
for vertex, distance in shortest_distances.items():
    print(f"To vertex {vertex}: Distance = {distance}")
print(f"\n\n\nShortest path from {start_vertex} to {end_vertex}:")
print(" -> ".join(path))