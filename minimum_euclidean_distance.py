# Öklid Mesafesini Hesaplayan Fonksiyon
def euclideanDistance(point1, point2):
    return ((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2) ** 0.5

# Noktaların Tanımlanması
points = [(1, 2), (4, 6), (5, 8), (3, 4), (7, 1)]

# Mesafelerin Hesaplanması
distances = []

for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append((distance, points[i], points[j]))

# Minimum Mesafenin Bulunması
min_distance = min(distances, key=lambda x: x[0])

# Sonucu Yazdırma
print(f"Minimum Öklid mesafesi: {min_distance[0]:.2f} \nNoktalar: {min_distance[1]} ve {min_distance[2]}")
