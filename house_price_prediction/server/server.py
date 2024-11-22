from flask import Flask, request, jsonify
import utils


app = Flask(__name__)

@app.route("/get_city_names", methods=["GET"])
def get_city_name():
    response = jsonify(
        {
            'cities': utils.get_city_names()
            }
        )
    response.headers.add("Access-Control-Allow-Origin", "*")
    
    return response

@app.route("/get_estimated_price", methods=["GET", "POST"])
def get_estimated_price():
    n_bedrooms = int(request.form["n_bedrooms"])
    n_bathrooms = int(request.form["n_bathrooms"])
    sqft_living = int(request.form["sqft_living"])
    sqft_lot = int(request.form["sqft_lot"])
    floors = int(request.form["floors"])
    yrs_since_last_renovation = int(request.form["yrs_since_last_renovation"])
    basement = request.form["basement"]
    city = request.form["city"]
    
    response = jsonify(
        {
            "estimated_price": utils.predict_home_price(n_bedrooms, n_bathrooms, sqft_living, sqft_lot, floors, yrs_since_last_renovation, basement, city)
            }
        )
    response.headers.add("Access-Control-Allow-Origin", "*")
    
    return response


if __name__ == "__main__":
    print("Starting Python Flask Server For House Price Prediction")
    utils.load_saved_artifacts()
    app.run()


