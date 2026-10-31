import matplotlib.pyplot as plt
import pandas as pd


def _read_manual_values(prompt):
    while True:
        try:
            values = [float(value) for value in input(prompt).split()]
            if not values:
                raise ValueError("Enter at least one value.")
            return values
        except ValueError as error:
            print(f"Invalid data: {error}")


def _select_column(columns, axis_name):
    while True:
        try:
            column_number = int(input(f"Enter the number for the {axis_name} column: "))
            if 1 <= column_number <= len(columns):
                return columns[column_number - 1]
            print(f"Choose a number from 1 to {len(columns)}.")
        except ValueError:
            print("Enter a valid column number.")


def plot_graph():
    print("Welcome to the Graph Plotter!")
    print("Choose a graph type:")
    print("1. Line Graph")
    print("2. Bar Chart")
    print("3. Scatter Plot")

    choice = input("Enter the number of your choice: ").strip()
    if choice not in {"1", "2", "3"}:
        print("Invalid choice. Exiting...")
        return

    print("\nChoose a data input method:")
    print("1. Enter data manually")
    print("2. Load data from a CSV file")
    data_choice = input("Enter the number of your choice: ").strip()

    if data_choice == "1":
        x_values = _read_manual_values("Enter X values separated by spaces: ")
        y_values = _read_manual_values("Enter Y values separated by spaces: ")
        x_label = input("Enter the X-axis label: ").strip() or "X"
        y_label = input("Enter the Y-axis label: ").strip() or "Y"
    elif data_choice == "2":
        file_path = input("Enter the path to the CSV file: ").strip()
        try:
            data = pd.read_csv(file_path)
        except (OSError, UnicodeDecodeError, pd.errors.EmptyDataError, pd.errors.ParserError) as error:
            print(f"Could not load the CSV file: {error}")
            return

        if len(data.columns) < 2:
            print("The CSV file must contain at least two columns.")
            return

        print("\nCSV columns:")
        for index, column in enumerate(data.columns, start=1):
            print(f"{index}. {column}")

        x_column = _select_column(data.columns, "X")
        y_column = _select_column(data.columns, "Y")
        if x_column == y_column:
            print("Choose different columns for the X and Y axes.")
            return

        x_series = data[x_column]
        y_series = pd.to_numeric(data[y_column], errors="coerce")

        if choice != "2":
            x_series = pd.to_numeric(x_series, errors="coerce")

        valid_rows = x_series.notna() & y_series.notna()
        skipped_rows = len(data) - int(valid_rows.sum())
        if skipped_rows:
            print(f"Skipped {skipped_rows} row(s) with missing or unusable values.")
        x_values = x_series[valid_rows].tolist()
        y_values = y_series[valid_rows].tolist()
        if not x_values:
            print("The selected columns do not contain any usable data.")
            return

        x_label = str(x_column)
        y_label = str(y_column)
    else:
        print("Invalid data input choice. Exiting...")
        return

    if len(x_values) != len(y_values):
        print("X and Y must contain the same number of values.")
        return

    title = input("Enter a graph title (leave blank for a default title): ").strip()
    if not title:
        title = {"1": "Line Graph", "2": "Bar Chart", "3": "Scatter Plot"}[choice]

    plt.figure()
    if choice == "1":
        plt.plot(x_values, y_values, marker="o")
    elif choice == "2":
        plt.bar(x_values, y_values)
    else:
        plt.scatter(x_values, y_values)

    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    plot_graph()
