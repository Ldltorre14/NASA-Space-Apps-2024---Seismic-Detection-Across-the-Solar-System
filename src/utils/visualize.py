import pandas as pd
import matplotlib.pyplot as plt
import constants.consts as cs


df = pd.read_csv(cs.MARS_TRAINING_DATA_DIRECTORY + "/XB.ELYSE.02.BHV.2022-01-02HR04_evid0006.csv")

print(df.head())