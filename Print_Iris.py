# Zichong Meng
# January 16 2025

#imports
import pandas as pd

#read and print iris csv
def read_print_iris(file_path):
    try:
        # read iris with pandas
        data = pd.read_csv(file_path)
        # print each row
        for index, row in data.iterrows():
            print(f"Row #{index}")
            print(row)
            print()
    except FileNotFoundError:
        print(f"No Iris file found at {file_path}.")
    except Exception as e:
        print(f"{e} occured in the process.")

if __name__ == "__main__":
    read_print_iris('data/Iris.csv')
