"""Data fetching API"""
import pandas


# ---------------- Reading and Writing Still to learn file ------------------------------------------- #
def read_csv():
    """Reading from still to learn file or new file, here it is the french words file"""
    # Read from still to learn file
    try:
        data = pandas.read_csv("data/still_to_learn_words.csv")
    # Refresh from french words if there is no 'still to learn file' or the file is empty
    except(FileNotFoundError, pandas.errors.EmptyDataError):
        data = pandas.read_csv("data/french_words.csv")
    return data


# writing still to learn words to 'still to learn' file so we can load from that next time
def write_csv():
    """Writing still to learn words to csv file function"""
    data = pandas.DataFrame(still_to_learn_words, columns=[front_heading, back_heading])
    data.to_csv("data/still_to_learn_words.csv", index=False)


# ------------------------------------------- DATA API ENDPOINTS ------------------------------------------- #
new_data = read_csv()
columns = new_data.columns
# Column headings example: English, French
front_heading = columns[0]
back_heading = columns[1]
still_to_learn_words = new_data.to_dict(orient="records")
