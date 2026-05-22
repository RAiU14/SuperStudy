#necessary imports
import pandas

# dynamic path input
path = input("Enter excel file path : ").strip("'\"")

# reading the excel file data from the given path
data = pandas.read_excel(path)

# printing column names in the excel file
print("Below are your column names : ")

# prints the column names and puts it in a list
print(data.columns.tolist())

# dynamic input for coulmn name, its case sensitive
column_name = input("Enter the exact column name [case sensitive] : ")

# final print of all the data in the given column name
print(data[column_name].tolist())