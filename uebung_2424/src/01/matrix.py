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


if __name__ == '__main__':
    m1 = Matrix(array=[[1, 2], [3, 4]])
    print(m1)

    print()

    m2 = Matrix(shape=(4, 3, 4))
    print(m2)

    print()

    m3 = Matrix(shape=(3, 4, 2))
    print(m3)

    # TODO: multiplicative m2 and m3, the result is a matrix with the 24 at each field
