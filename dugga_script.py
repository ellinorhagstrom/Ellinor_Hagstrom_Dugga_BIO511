import csv
import pandas as pd
import matplotlib.pyplot as plt


def part1():
    """First adds all absolute values to the sum variable and prints it
    Second it will create a list of cubes from all negative numbers in number list
    Third it will print the first duplicate number in the list (- and + are treated the same)"""
    numbers = [15, -5, -12, 7, 10, -7, 3, -10, 4]

    # a)
    sum = 0
    for n in numbers:
        if (
            abs(n) >= 10
        ):  # If the absolute value of the number is larger than or equal to 10 --> The if block will run
            sum += abs(n)  # Add all absolute values to variable "sum"
    print(sum)

    # b)
    cubes_list = []
    for n in numbers:
        if n < 0:  # If the number is lower than 0 --> if block will run
            cube = n**3  # Takes n to the power of 3
            cubes_list.append(cube)  # Appends the list with the cube

    print(cubes_list)

    # c)
    unique_list = []
    for n in numbers:
        if (
            abs(n) in unique_list
        ):  # Takes the absolute value of n and checks if it is already in the list
            print(
                f"{n} is the first duplicate"
            )  # If n already is in list --> Print the number and say that its the first duplicate
            break  # When the first duplicate is found --> go out of if block
        unique_list.append(n)  # Appends the list with n

    else:  # Prints only wheen the loop has ended, therefore it will only print if the if-block does not hit break. Thus the else will not be run if the loop is stopped by break
        print("No duplicates")


part1()


def part2():
    """Creates a histogram of the fpkm_log2 column in the file brca_head500_genes.csv"""
    # 2.1)
    df = pd.read_csv(
        "brca_head500_genes.csv", sep=","
    )  # Reads the file into a pandas dataframe

    # 2.2.1 & 2.2.2 & 2.2.3)
    plt.hist(
        data=df, x="fpkm_log2"
    )  # Creates a histogram with df as data and fpkm_log2 as x
    plt.title("Distribution of gene expression")  # Creates title
    plt.xlabel("Expression")  # Creates x label
    plt.ylabel("Number of genes")  # Creates y label
    plt.savefig("fpkm_distribution.png")  # Saves firgure as a png
    plt.show()  # Shows the figure


part2()
