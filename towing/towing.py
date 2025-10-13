import csv
from pathlib import Path


# combine the paths
BASE_DIR = Path(__file__).parent
data_path = BASE_DIR / "towing.csv"

def get_data(file_path: str) -> None:

    """
    Helper function to access the csv data and print each row

    Input: 
        file_path: The path to the csv file saved as a string

    Output:
        Each row of the csv file
    
    """
    file_path = Path(file_path) 
    with open(file_path, 'r', newline='') as f:
        return list(csv.reader(f))


def top_days(n):
    """
    Returns the top days that vehicles were towed.

    Inputs:
        n (int): Number of days to return.

    Output:
        A list of tuples where the first item is a date and the second item
        the number of vehicles towed on that date.

        There should only be 'n' elements, ordered by vehicles towed on the day.

        For example:
            [
              ("06/15/2022", 82),
              ("05/01/2022", 51),
              ("05/11/2022", 39),
            ]
    """
    data = get_data(data_path)
    data = data[1:] #get rid of header
    N = n

    # create empty dictionary
    date_count = {}

    # create a dictionary entry for every date 
    # and a count for how many cars got towed on that date
    for d in data:
        date_value = d[0]
        if date_value in date_count:
            date_count[date_value] += 1
        else:
            date_count[date_value] = 1

    # sort dates according to count
    sorted_dates = sorted(date_count.items(), key=lambda item: item[1], reverse=True) 

    #for i, j tuple in sorted_dates:
    #for i, j in sorted_dates[:N]:
    #    return((i, j))
    return sorted_dates[:N]

        


def day_summary():
    """
    Return a list of all days in chronological order, along with the
     number of cars towed for each day.

    Output:
        A list of tuples where the first item is a date and the second item the
         number of vehicles towed on that date.

        For example:
            [
              ("07/01/2022", 5),
              ("07/02/2022", 30),
              ... # truncated
              ("09/29/2022", 76),
            ]
    """
    data = get_data(data_path)
    data = data[1:] #get rid of header

    # create empty dictionary
    date_count_full = {}

    # create a dictionary entry for every date 
    # and a count for how many cars got towed on that date
    for d in data:
        date_value = d[0]
        if date_value in date_count_full:
            date_count_full[date_value] += 1
        else:
            date_count_full[date_value] = 1

    # sort dates chronologically
    sorted_dates = sorted(date_count_full.items()) 

    return sorted_dates
