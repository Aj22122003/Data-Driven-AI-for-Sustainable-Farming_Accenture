import pandas as pd
import joblib

def fertilizer_prediction(temperature, humidity, moisture, soil_type, crop_type, N, K, P):
    soil_types = ['Black', 'Clayey', 'Loamy', 'Red', 'Sandy']
    crop_types = ['Barley',
                    'Bengal Gram',
                    'Cotton',
                    'Ground Nuts',
                    'Maize',
                    'Millets',
                    'Oil seeds',
                    'Paddy',
                    'Pulses',
                    'Red Gram',
                    'Sugarcane',
                    'Tobacco',
                    'Wheat']
    fertilizer_names = ['10-26-26', '14-35-14', '17-17-17', '20-20', '28-28', 'DAP', 'Urea']
    features = {
        'Temparature':[temperature],
        'Moisture':[moisture],
        'Humidity ':[humidity],
        'Soil Type': [soil_types.index(soil_type)],
        'Crop Type': [crop_types.index(crop_type)],
        'Nitrogen':[N],
        'Potassium':[K], 
        'Phosphorous':[P]
    }

    df = pd.DataFrame(features)
    model = joblib.load('bagging_classifier_model.pkl')
    predictions = model.predict(df)
    return fertilizer_names[predictions[0]]


def yield_prediction(Temp,Precipitation,SOM,AWC,Land_Area,VPD):

    features = {
        'Temp': [Temp],
        'Precipitation': [Precipitation],
        'SOM': [SOM],
        'AWC': [AWC],
        'Land Area': [Land_Area],
        'VPD': [VPD]
    }

    # Convert the features dictionary to a DataFrame
    df = pd.DataFrame(features)

    # Load the model
    model = joblib.load('linear_regression_yields_1.pkl')

    # Make predictions using the model
    predictions = model.predict(df)
    return predictions[0]
#fertilizer_prediction(20.87974371,82.00274423,38,'Sandy','Maize',37,0,0)    Example call

#yield_prediction(20.09499032,58.19599999,1.246915053,0.148337743,436036.48,10.49023064)    Example c
