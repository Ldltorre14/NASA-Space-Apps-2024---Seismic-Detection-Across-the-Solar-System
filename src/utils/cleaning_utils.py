import pandas as pd
import constants.consts as cs



#Function for deleting rows with missing values
def deleteMissingValues(data):
    return data.dropna()


def deleteDuplicateValues(data):
    return data.drop_duplicates()



