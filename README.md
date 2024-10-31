# active_power_prediction_api
API to predict active power
In order to run:
1) Create a .win_env using: python3 -m venv .win_env in cmd
2) Activate this environment using .win_env\Scripts\activate
3) Install requirements using: pip install -r requirements.txt
4) Go to folder: /active_power_prediction_api/app.py
5) Run python app.py

You will see in cmd tha flask has been started! This is great
Now go to POSTMAN to send a request like this:

{
  "apparent_power": 230.0,
  "current": 20.0,
  "power_factor": 0.95
}

In url complete the localhost: http://127.0.0.1:8080/predict
