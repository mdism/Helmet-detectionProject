import csv

def append_to_csv(filename, row_data):
  """Appends a new row to a CSV file.

  Args:
    filename: The name of the CSV file.
    row_data: A list of values to be appended as a new row.
  """

  with open(filename, 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(row_data)

# Example usage:
filename = 'my_data.csv'
new_row = ['new_value1', 'new_value2', 'new_value3']

append_to_csv(filename, new_row)