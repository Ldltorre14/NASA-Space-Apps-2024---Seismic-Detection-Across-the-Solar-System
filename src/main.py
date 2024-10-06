import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import constants.consts as cs
import utils.cleaning_utils
import utils.normalize
import utils.visualize
from utils.preprocessing import preprocessDataFrame

#Load the first dat
df = pd.read_csv(cs.LUNAR_TRAINING_DATA_DIRECTORY + "/xa.s12.00.mhz.1970-01-19HR00_evid00002.csv")
processed_df = preprocessDataFrame(df)


#utils.visualize.visualizeDf(df)
#utils.visualize.visualizeDf(processed_df)
utils.visualize.visualizeVelocityOverTime(df)
utils.visualize.visualizeRollingCorrelationTimeVelocity(df)

utils.visualize.visualizeVelocityOverTime(processed_df)
utils.visualize.visualizeRollingCorrelationTimeVelocity(processed_df)