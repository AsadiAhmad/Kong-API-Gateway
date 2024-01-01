# Kong-API-Gateway
 a simple project that shows how to use kong API Gateway service.
## Step 1: Docker
download Docker and install it on your system.
## Step 2: Kong

### Pull the Docker image  

```bash  
docker pull kong/kong-gateway:2.7.0.0-alpine
```  


### Step1: Create a Docker network

```bash
docker network create kong-net
```  

### Step2: Start and prepare Postgres DB

```bash  
docker run -d --name kong-database --network=kong-net -e “POSTGRES_USER=kong” -e “POSTGRES_DB=kong” -e “POSTGRES_PASSWORD=kong” -p 5432:5432 postgres:9.6
```   

```bash
docker run --rm --network=kong-net -e “KONG_DATABASE=postgres” -e “KONG_PG_HOST=kong-database” -e “KONG_PG_PASSWORD=kong” kong:latest kong migrations bootstrap
```   

### Step3: Start kong

```bash 
docker run -d --name kong --network=kong-net -e “KONG_DATABASE=postgres” -e “KONG_PG_HOST=kong-database” -e “KONG_PG_PASSWORD=kong” -e “KONG_PROXY_ACCESS_LOG=/dev/stdout” -e “KONG_ADMIN_ACCESS_LOG=/dev/stdout” -e “KONG_PROXY_ERROR_LOG=/dev/stderr” -e “KONG_ADMIN_ERROR_LOG=/dev/stderr” -e “KONG_ADMIN_LISTEN=0.0.0.0:8001, 0.0.0.0:8444 ssl” -p 8000:8000 -p 8443:8443 -p 8001:8001 -p 8444:8444 -p 8002:8002 kong:latest
```    
## Step 3: Create a service
In this step, you can use one of the services that I have built (myservice1.py or myservice2.py). Run one of these services locally on your PC.  
here is the code of myservice1.py:
```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hi, I'm service 1"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=5000)

```
When you type ```bash http://yourip:5000/``` into your browser's address bar and hit enter, you will see that the service is running successfully.  
![Local Image](/images/IP-restriction/service-runnig.jpg)
## Step 4:
