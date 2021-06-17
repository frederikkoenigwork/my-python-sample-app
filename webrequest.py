import requests 
import time




for i in range(1,1000000):

    url = 'http://127.0.0.1:5000/calc/'+str(i)+'/'+str(i)+'' 
    response = requests.get(url)        # To execute get request 
    print(response.status_code)     # To print http response code  
    print(response.text)            # To print formatted JSON response 

    time.sleep(1)