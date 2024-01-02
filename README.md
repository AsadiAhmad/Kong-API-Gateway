<!DOCTYPE html>
<html>

<body>

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
When you type ``` http://yourip:5000/``` into your browser's address bar and hit enter, you will see that the service is running successfully.
  
  
<img src="images/IP-restriction/service-runnig.JPG" width="400">

*your service is running on port 5000 on your local IP*
## Step 4: Primary settings
### Step4-1: Adding your service in Kong
 type ``` http://yourip:8002/``` into your browser's address bar and hit enter, you will see the Kong Manager OSS on your browser.  
 click on Gateway Services on the menu.
 add your service information and hit save button.  
 
 #### image of creating service should be added 
 
 ### Step4-2: Adding your route in Kong
 
 ### Step4-1: Adding your consumer in Kong
 
 
## Step 5:Installing plugins
In this section, we guide you through the installation and usage of ten distinct plugins in Kong, providing step-by-step instructions for each
### Step 5-1: IP restriction plugin
in this step you should go to Plugins section and enable IP Restriction plugin.

<img src="images/IP-restriction/1.JPG" width="400"> 

Please configure your plugin settings as shown in the image below.  

<img src="images/IP-restriction/2.JPG" width="400">


<img src="images/IP-restriction/3.JPG" width="400">


<img src="images/IP-restriction/4.JPG" width="400">
*Adjust the settings according to your preferences.*  
then click on install button.  
Upon entering ``` http://yourip:8000/yourservicename``` into your browser's address bar and pressing enter, you will observe that access to the service is restricted for your IP. 

<img src="images/IP-restriction/5.JPG" width="400">

*your service page* 
### Step 5-2: Basic authentication plugin
in this step you should go to Plugins section and enable Basic Authentication plugin.

<img src="images/Basic-authentication/1.JPG" width="400"> 

Please configure your plugin settings as shown in the image below.  

<img src="images/Basic-authentication/2.JPG" width="400">


<img src="images/Basic-authentication/3.JPG" width="400">

then click on install button.  
Once you've activated the plugin, proceed to create a new consumer (as previously explained).

<img src="images/Basic-authentication/4.JPG" width="400"> 

Subsequently, click on your designated consumer and navigate to the credentials section. You will notice the addition of the Basic Authentication section for your consumer. Click on ``` New Basic Auth Credential```.

<img src="images/Basic-authentication/5.JPG" width="400">  

set a username and password for your consumer then click on create button.

<img src="images/Basic-authentication/6.JPG" width="400">

Upon entering ``` http://yourip:8000/yourservicename``` into your browser's address bar and pressing enter, you will observe that you need Username and password for accessing to your service.

<img src="images/Basic-authentication/7.JPG" width="400">

Upon entering the accurate username and password, you will gain access to your service content.

<img src="images/Basic-authentication/8.JPG" width="400">

### Step 5-3: Request termination plugin
Firstly, you should create your second consumer(as previously explained).
then you should go to Plugins section and enable Request termination plugin. 

<img src="images/Request-termination/3.JPG" width="400">


<img src="images/Request-termination/4.JPG" width="400">

Please configure your plugin settings as shown in the image below.

<img src="images/Request-termination/5.JPG" width="400">


<img src="images/Request-termination/6.JPG" width="400">


<img src="images/Request-termination/7.JPG" width="400">

then click on install button. 
Subsequently, click on your designated consumer and navigate to the credentials section. You will notice the addition of the Basic Authentication section for your consumer. Click on ``` New Basic Auth Credential```.

<img src="images/Request-termination/8.JPG" width="400">


<img src="images/Request-termination/9.JPG" width="400">

set a username and password for your consumer then click on create button.

<img src="images/Request-termination/10.JPG" width="400">

When you correctly input your username and password, you'll sign in. However, a message will be displayed, indicating that your request has been terminated.

<img src="images/Request-termination/11.JPG" width="400">


<img src="images/Request-termination/12.JPG" width="400">

### Step 5-4: Proxy caching plugin
In the first step you should go to Plugins section and enable Proxy caching plugin.

<img src="images/Proxy-caching/1.JPG" width="400">


<img src="images/Proxy-caching/2.JPG" width="400">

Please configure your plugin settings as shown in the image below.  

<img src="images/Proxy-caching/3.JPG" width="400">


<img src="images/Proxy-caching/4.JPG" width="400">


<img src="images/Proxy-caching/5.JPG" width="400">


<img src="images/Proxy-caching/6.JPG" width="400">

Now, using Thunder Client, or any other preferred service such as Postman, send a GET request to ``` http://yourip:8000/yourservicename```. With the plugin disabled, you should observe that everything is functioning correctly, but there is no evidence of caching, as depicted in the image below.

<img src="images/Proxy-caching/7.JPG" width="400">

Now enable your proxy caching plugin from Kong manager.

<img src="images/Proxy-caching/7.JPG" width="400">

Upon sending another GET request, you'll notice that the headers now include ``` x-cache-key``` and  ```x-cache-status``` .  

<img src="images/Proxy-caching/9.JPG" width="400">

### Step 5-5: Response rate limiting plugin
In the first step you should go to Plugins section and enable Response rate limiting plugin.

<img src="images/Response-rate-limiting/1.JPG" width="400">


<img src="images/Response-rate-limiting/2.JPG" width="400">

Please configure your plugin settings as shown in the image below.

<img src="images/Response-rate-limiting/3.JPG" width="400">


<img src="images/Response-rate-limiting/4.JPG" width="400">


<img src="images/Response-rate-limiting/5.JPG" width="400">


<img src="images/Response-rate-limiting/6.JPG" width="400">


<img src="images/Response-rate-limiting/7.JPG" width="400">

Now, using Thunder Client, or any other preferred service such as Postman, send a GET request to ``` http://yourip:8000/yourservicename```.You'll notice that the headers now include ```x-ratelimit-limit-first-limit-seconds``` and```x-ratelimit-remaining-first-limit-seconds```. 

<img src="images/Response-rate-limiting/9.JPG" width="400">

### Step 5-6: Rate limiting plugin
In the first step you should go to Plugins section and enable Response Rate limiting plugin.

<img src="images/Rate-Limiter/1.JPG" width="400"> 

Please configure your plugin settings as shown in the image below.
<img src="images/Rate-Limiter/2.JPG" width="400"> 


<img src="images/Rate-Limiter/3.JPG" width="400"> 


<img src="images/Rate-Limiter/4.JPG" width="400"> 


<img src="images/Rate-Limiter/5.JPG" width="400">


<img src="images/Rate-Limiter/6.JPG" width="400">

When you enter ``` http://yourip:8000/yourservicename``` in your browser's address bar and hit enter, attempting to exceed the rate limit will result in an error.

<img src="images/Rate-Limiter/8.JPG" width="400">  

### Step 5-7: Bot detection plugin
In the first step you should go to Plugins section and enable Bot Detection plugin.

<img src="images/Bot-Detection/1.JPG" width="400">

Please configure your plugin settings as shown in the image below.

<img src="images/Bot-Detection/2.JPG" width="400">


<img src="images/Bot-Detection/3.JPG" width="400">

When an attempt is made to access our service through Google Chrome, the system promptly identifies the user as a bot. Consequently, upon opening Google Chrome and entering ```http://yourip:8000/yourservicename``` into the browser's address bar, an error message explicitly stating "Forbidden" is displayed. This proactive measure plays a crucial role in recognizing and restraining potential automated bot activities.

<img src="images/Bot-Detection/5.JPG" width="400">


### Step 5-8: Request size limiting plugin
In the first step you should go to Plugins section and enable Request size limiting plugin.

<img src="images/Request-Size-Limiting/1.JPG" width="400">

Please configure your plugin settings as shown in the image below.

<img src="images/Request-Size-Limiting/2.JPG" width="400">


<img src="images/Request-Size-Limiting/3.JPG" width="400">

Use Thunder Client, Postman, or your preferred service to send a GET request to ```http://yourip:8000/yourservicename```, ensuring that it remains within the size-limiting restrictions. Upon doing so, you will receive a standard response.

<img src="images/Request-Size-Limiting/4.JPG" width="400">

Conversely, if you surpass the size-limiting restrictions in your request, the response will notify you that your request exceeds the size-limiting range.

<img src="images/Request-Size-Limiting/5.JPG" width="400">


### Step 5-9: Key auth restriction plugin
### Step 5-10: ACL plugin

</body>
</html>