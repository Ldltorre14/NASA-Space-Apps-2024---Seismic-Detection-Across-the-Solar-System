import pandas as pd
import constants.consts as cs


#Load the first dat
df = pd.read_csv(cs.LUNAR_TRAINING_DATA_DIRECTORY + "/xa.s12.00.mhz.1970-01-19HR00_evid00002.csv")

print(df.head)