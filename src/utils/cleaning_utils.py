import pandas as pd
import constants.consts as cs



#Function for deleting rows with missing values
def deleteMissingValues(data):
    print("Deleting missing values...")
    return data.dropna()


def deleteDuplicateValues(data):
    print("Deleting duplicated values...")
    return data.drop_duplicates()



