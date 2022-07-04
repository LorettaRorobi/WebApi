# import modules
import uvicorn
from app.NigeriaSolarEstimator import app

# main driver app
if __name__ == '__main__':
    uvicorn.run(app)