# import modules
import json
import numpy as np
import pandas as pd
from fastapi import FastAPI, Request
from app.solar_irradiation import Get_Radiation

# instantiate fastapi
app = FastAPI()
                                             
@app.get("/")
async def Solar_Estimator(request:Request):
        """
            Get inputs from users and return estimated solar radiation. 
        """
        raw_data = await request.json()

        results = Get_Radiation(raw_data)
        
        return results