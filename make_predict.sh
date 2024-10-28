#!/usr/bin/env bash

PORT=5000
echo "Port: $PORT"

# POST method predict
curl -d '{  
   "CRIM":{
      "0":0.62976
   },
   "ZN":{  
      "0":28
   },
   "INDUS":{  
      "0":10.010
   },
   "CHAS":{  
      "0":0
   },
   "NOX":{  
      "0":0.4390
   },
   "RM":{  
      "0":5.6020
   },
   "AGE":{  
      "0":21.10
   },
   "DIS":{  
      "0":6.575
   },
   "RAD":{  
      "0":2
   },
   "TAX":{  
      "0":296.0
   },
   "PTRATIO":{  
      "0":15.3
   },
   "B":{  
      "0":396.9
   },
   "LSTAT":{  
      "0":4.98
   }
}'\
     -H "Content-Type: application/json" \
     -X POST http://localhost:$PORT/predict