import numpy as np


def get_matrix(name):
    while True:
        try:
            rows_count = int(input("Enter the number of rows for matrix {}: ".format(name)))
            cols_count = int(input("Enter the number of columns for matrix {}: ".format(name)))
            if rows_count <= 0 or cols_count <= 0:
                raise ValueError("The number of rows and columns must be positive.")
            break
        except ValueError as error:
            print("Invalid dimensions:", error)

    elements = []
    print("Enter each row of matrix {} as {} numbers separated by spaces:".format(name, cols_count))
    for row_number in range(rows_count):
        while True:
            try:
                row = [float(value) for value in input("Row {}: ".format(row_number + 1)).split()]
                if len(row) != cols_count:
                    raise ValueError("Expected {} values, got {}.".format(cols_count, len(row)))
                elements.append(row)
                break
            except ValueError as error:
                print("Invalid row:", error)

    return np.array(elements, dtype=float)


def matrix_operations(matrix_a, matrix_b, operation):
    if operation in ("add", "sub"):
        if matrix_a.shape != matrix_b.shape:
            raise ValueError("Addition and subtraction require matrices of the same shape.")
        if operation == "add":
            return matrix_a + matrix_b
        return matrix_a - matrix_b

    if operation in ("mul", "dot"):
        if matrix_a.shape[1] != matrix_b.shape[0]:
            raise ValueError(
                "Matrix multiplication requires the columns of matrix A "
                "to match the rows of matrix B."
            )
        if operation == "mul":
            return np.matmul(matrix_a, matrix_b)
        return np.dot(matrix_a, matrix_b)

    if operation == "trans":
        return matrix_a.T

    if operation == "inverse":
        if matrix_a.shape[0] != matrix_a.shape[1]:
            raise ValueError("Only square matrices have an inverse.")
        return np.linalg.inv(matrix_a)

    raise ValueError("Unknown matrix operation: {}".format(operation))


def main():
    operations = {
        "1": ("add", "Addition"),
        "2": ("sub", "Subtraction"),
        "3": ("mul", "Matrix multiplication (mul)"),
        "4": ("dot", "Dot product"),
        "5": ("trans", "Transpose"),
        "6": ("inverse", "Inverse"),
    }

    while True:
        print("\nMatrix Calculator")
        for key, (_, label) in operations.items():
            print("{}. {}".format(key, label))
        print("0. Exit")

        choice = input("Choose an operation: ").strip()
        if choice == "0":
            print("Goodbye!")
            return
        if choice not in operations:
            print("Invalid choice. Select an operation from 0 to 6.")
            continue

        operation, label = operations[choice]
        print("\n{}".format(label))
        matrix_a = get_matrix("A")
        matrix_b = None
        if operation in ("add", "sub", "mul", "dot"):
            matrix_b = get_matrix("B")

        try:
            result = matrix_operations(matrix_a, matrix_b, operation)
        except np.linalg.LinAlgError:
            print("This matrix is singular and does not have an inverse.")
            continue
        except ValueError as error:
            print("Cannot perform operation:", error)
            continue

        print("\nResult:\n{}".format(result))


if __name__ == "__main__":
    main()
