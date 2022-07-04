import json
from datetime import datetime
import numpy as np
import pandas as pd

model_data = {}

def Transform_Input(data):

    # current date and time
    now = datetime.now()

    model_data['month'] = int(now.strftime("%m"))

    try:
        new_distance = Get_Google_Distance(data['source'], data['destination'])
    except Exception:
        return "Something went wrong getting the distance"

    if new_distance is None:
        return "Something went wrong getting the distance"
    else:
        model_data['totalDistance'] = new_distance

        """
        try:
            tonnage = int(data['tonnage'])
        except Exception as e:
            return "tonnage should be in number"

        if tonnage in available_asset_size:
            self.model_data['cargoTonnage'] = tonnage
            self.model_data[f'asset_size_{tonnage}'] = 1
        else:
            return print(f"tonnage should be within {available_asset_size}", 400)
        """

    good_type = 'OTHERS'
    try:
        good_type_data = str(data['goodType']).upper()
        if good_type_data in available_good_type:
            good_type = good_type_data
    except Exception as e:
            pass
            model_data[f'goodType_{good_type}'] = 1

    try:
        truck_type = str(data['truckType']).title()
    except Exception as e:
        return "invalid truck type"

    if truck_type in available_truck_type:
        model_data[f'asset_type_{truck_type}'] = 1
    else:
        return print(f"truck type should be {available_truck_type}")
            

    try:
        state_names = Return_State_Name(data['source'], data['destination'])
        source_state = state_names[0].upper()
    except Exception as e:
        return "invalid source state"

    if source_state in available_source_states:
        model_data[f'source_{source_state}'] = 1
    else:
        return print(f"source state should be in "
                                               f"{available_source_states}")

    try:
        destination_state = state_names[1].upper()
    except Exception as e:
        return "invalid destination state"

    if destination_state in available_destination_states:
        model_data[f'destination_{destination_state}'] = 1
    else:
        return print(f"destination state should be in "
                                                    f"{available_destination_states}")

    model_features = [
                'Temperature', 'CloudOpacity', 'DHI', 'DNI', 'Precipitation', 'Humidity', 'Pressure', 'WindDirection', 'WindSpeed', 'Month', 'Day'
            ]

    model_data_df = pd.DataFrame([model_data], columns = model_features)
    model_data_df.fillna(0, inplace = True)
    model_data_df = list(model_data_df.iloc[0])

    return model_data_df