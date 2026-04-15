class Matrix:
    def __init__(self, *, array=None, shape=None):
        """
        Create a matrix from a list of lists or from a shape.
        Only one option must be used at all times!
        Args:
            array: a 2D-nested list
            shape: a shape tuple (columns, rows, default_value) -> (2, 2, 0) creates a 2x2 matrix filled with zeroes
        """

        if array is not None and shape is not None:
            ValueError(f"You can't init this matrix with an array and a shape tuple at the same time!")

        if array is not None:
            # Initialize from a list of lists
            self.data = array
            self.rows = len(array)
            self.cols = len(array[0]) if self.rows > 0 else 0
        else:
            # Initialize from a shape
            self.rows, self.cols, default = shape
            self.data = [[default for _ in range(self.cols)] for _ in range(self.rows)]

    def __str__(self):
        """
        Return a string representation of the matrix.
        """
        return '\n'.join([' '.join(map(str, row)) for row in self.data])

    def __len__(self):
        return self.cols

    def __matmul__(self, other):
        """
        Multiply the current matrix with another matrix.
        """
        if self.cols != other.rows:
            raise ValueError('Number of columns in first matrix must be equal to number of rows in second matrix')

        result = Matrix(shape=(self.rows, other.cols, 0))

        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(self.cols):
                    result.data[i][j] += self.data[i][k] * other.data[k][j]

        return result

    def __getitem__(self, index):
        """
        Get a row from the matrix.
        """
        if index >= self.rows:
            raise ValueError('Index out of range')
        return self.data[index]

    def __setitem__(self, index, value):
        """
        Set a row in the matrix.
        """
        if index >= self.rows:
            raise ValueError('Index out of range')
        if len(value) != self.cols:
            raise ValueError('Length of value does not match number of columns')
        self.data[index] = value


if __name__ == '__main__':
    m1 = Matrix(array=[[1, 2], [3, 4]])
    print(m1)

    print()

    m2 = Matrix(shape=(4, 3, 4))
    m2[2] = [10, 10, 10]
    print(m2)

    print()

    m3 = Matrix(shape=(3, 4, 2))
    print(m3)

    print()

    print(m2 @ m3)

    print()
    import numpy as np
    a1 = np.full((4, 3), 4) @ np.full((3, 4), 2)
    print(a1)

