## import pandas for data analysis
import pandas as pd

def print_summary_statistics(key, dataframe):
    print('{}: max {:f} mean {:f} min {:f}'.format(key, dataframe[key].max(), dataframe[key].mean(), dataframe[key].min()))

def generate_prediction_data(features, dataframe, percentiles = [5, 25, 50, 75, 90, 95, 99]):
    prediction_data = []

    for p in percentiles:
        prediction_data.append(generate_prediction_features(features, dataframe, p))

    return prediction_data

def generate_prediction_features(features, dataframe, percentile):
    prediction_features = []
    for f in features:
        if f == 'Ward':
            prediction_features.append(2)
        elif f == 'Police District':
            prediction_features.append(19)
        else:
            prediction_features.append(dataframe[f].quantile(percentile / 100))
    return prediction_features
