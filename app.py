# 1. Library imports
import uvicorn
from fastapi import FastAPI
from House import House
import pickle
# 2. Create the app object
app = FastAPI()
pickle_in = open("model.sav","rb")
classifier=pickle.load(pickle_in)
# import nest_asyncio
# nest_asyncio.apply()

# # 3. Index route, opens automatically on http://127.0.0.1:8000
# @app.get('/')
# async def index():
#     return {'message': 'Hello, World'}

# # 4. Route with a single parameter, returns the parameter within a message
# #    Located at: http://127.0.0.1:8000/AnyNameHere

# @app.get('/{name}')
# async def get_name(name: str):
#     return {'Welcome To Krish Youtube Channel': f'{name}'}

# # 3. Expose the prediction functionality, make a prediction from the passed
# #     JSON data and return the predicted Bank Note with the confidence

#from datetime import date
@app.post('/')
def predict_house_price(data:House):
    year=data.date.year
    month=data.date.month
    day=data.date.day
    print(data)
    bedrooms = data.bedrooms
    bathrooms = data.bathrooms
    sqft_living =data.sqft_living
    sqft_lot =data.sqft_lot
    floors =data.floors
    waterfront =data.waterfront
    view =data.view
    condition =data.condition
    grade =data.grade
    sqft_above =data.sqft_above
    sqft_basement =data.sqft_basement
    yr_built =data.yr_built
    yr_renovated= data.yr_renovated
    zipcode =data.zipcode
    lat =data.lat
    long =data.long
    sqft_living15 =data.sqft_living15
    sqft_lot15 =data.sqft_lot15
    prediction = classifier.predict([
        year,month,day,  bedrooms,
         bathrooms,
        sqft_living,
        sqft_lot,
        floors,
        waterfront,
        view,
        condition,
        grade,
        sqft_above,
        sqft_basement,
        yr_built,
        yr_renovated,
        zipcode,
        lat,
        long,
        sqft_living15,
        sqft_lot15
        ])

    return {
        'prediction': prediction
    }

# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app)
    
#uvicorn app:app --reload
