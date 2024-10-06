from sklearn.preprocessing import StandardScaler, MinMaxScaler, MaxAbsScaler

#Function for normalizing the speed, so the range goes from 0 to 1 instead of a bigger range
def normalizeVelocity(data):
    print("Normalizing Velocity...")
    scaler = MinMaxScaler()
    data['velocity(m/s)'] = scaler.fit_transform(data[['velocity(m/s)']])
    
    return data 


