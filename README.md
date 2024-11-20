## Predicting house price in boston and deploying a flask app on AWS SAM CLI

### Arrangement of the files

```

├── app.py
├── azure-pipelines.yml
├── Boston_Housing_prediction.egg-info
│   ├── dependency_links.txt
│   ├── PKG-INFO
│   ├── requires.txt
│   ├── SOURCES.txt
│   └── top_level.txt
├── datasets
│   ├── housing.xls
│   └── __init__.py
├── Dockerfile
├── __init__.py
├── Makefile
├── make_predict_azure_app.sh
├── make_predict.sh
├── models
│   └── xgb_housing_model.joblib
├── notebooks
│   ├── __init__.py
│   ├── predict_housing.ipynb
│   └── README.md
├── os
├── README.md
├── requirements.txt
├── setup.py
└── sys

```
### Steps
- Run `make install` - excecute the instructions in the Makefile with the install section
- Run `python3 app.py`- this excecutes the app in a local host.
- In a separate shell run `./make_predict.sh`

- `notebook` contains an XGBoost regressor model that was used to train the data , and the model was saved for future use at `models`.

### Makefile
- It is used to:
    - create a virtual environment,
    - install the dependencies 
    - Perform tests and linting 
    - Build docker images and run them 

### Flask app
- We create a flask instance 
- We have logger that is set to capture messages of level `INFO` and above.
- The input data converted from a json structure to a dataframe.
- It  is then  scaled using a standard scaler.
- We load the xgboost regressor and make predictions 
- Then we convert the results to a jsonfile.
- All this is running in port 5000.
- use `python app.py` to run this script

### Create ssh keys 
- Open your azure, and look for the terminal and type `ssh-keygen -t rsa` , press enter all the way.
- use `cat /file/path/.ssh/id_rsa.pub` ,this generates a code ,so that you may communicate with github.
- Go to github settings and look for `ssh and GPG keys` add the ssh key and give it a name 
- Got to the repository and look for clone with `SSH`.copy that link to azure terminal 
- in azure terminal register the app service as `az webapp up -n housing-price-service`

### AWS SAM CLI 
- Initialize `sam init`
- Custom build it 