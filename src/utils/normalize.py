from sklearn.preprocessing import StandardScaler, MinMaxScaler

#Function for normalizing the speed, so the range goes from 0 to 1 instead of a bigger range
def normalizeVelocity(data):
    scaler = StandardScaler()
    data['velocity(m/s)'] = scaler.fit_transform(data[['velocity(m/s)']])
    
    return data 


