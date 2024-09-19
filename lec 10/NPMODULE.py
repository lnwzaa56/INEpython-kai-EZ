import numpy as np

random_matrix = np.random.randint(1, 11, size=(3, 3))
print("Random 3x3 Matrix:\n", random_matrix)

matrix_sum = np.sum(random_matrix)
print(f"\nsum of all element: {matrix_sum}")

matrix_sum = np.mean(random_matrix)
print(f"\nMean of the matrix: {matrix_sum:2.2f}")

transposed_matrix = np.transpose(random_matrix)
print("\nTransposed Matrix:\n", transposed_matrix)

