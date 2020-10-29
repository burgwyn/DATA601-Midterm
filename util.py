## import path for saving response
import os.path

## import requests for HTTP requests
import requests

## import json to saving API response
import json

## import pandas for data analysis
import pandas as pd

def generate_prediction_data(features, df):
    prediction_data = []

    percentiles = [5,25,50,75,90,95,99]

    for p in percentiles:
        prediction_data.append(generate_prediction_features(features, df, p))

    return prediction_data

def generate_prediction_features(features, df, percentile):
    prediction_features = []
    for f in features:
        if f == 'Ward':
            prediction_features.append(2)
        elif f == 'Police District':
            prediction_features.append(19)
        else:
            prediction_features.append(df[f].quantile(percentile / 100))
    return prediction_features
