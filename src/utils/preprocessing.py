from utils.normalize import normalizeVelocity
from utils.cleaning_utils import deleteDuplicateValues, deleteMissingValues
import pandas as pd

def preprocessDataFrame(df):
    print("Converting Time to DateTime...")
    df['time_abs(%Y-%m-%dT%H:%M:%S.%f)'] = pd.to_datetime(df['time_abs(%Y-%m-%dT%H:%M:%S.%f)'])

    df = deleteMissingValues(df)
    df = deleteDuplicateValues(df)
    df  = normalizeVelocity(df)

    return df