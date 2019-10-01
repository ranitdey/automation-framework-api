# Automation framework for API

## About

An automation framework for API's capable of automating scenarios related to user work-flows and CRUD rest behaviours.

## Requires
* Python (version > 3)
* BestBuy API playground (For mocking dummy API's. To setup this API follow this link:- https://github.com/BestBuy/api-playground)
* Virtualenv (If your system do not have virtualenv please set it up using the following command)
```bash
    pip install virtualenv
```


## How to start

Once you have above requirements satisfied and BestBuy API's running, we can start the automation tests. To do so execute following
steps :-

* Clone this repository and go to the root directory.

```bash
    git clone https://github.com/ranit-geek/automation-framework-api.git
    
    cd automation-framework-api/
```

    
* Create and activate virtual environment using python3.

```bash
    virtualenv -p python3 venv
    
    source venv/bin/activate
```

    
    
* Install requirements from requirements.txt  

```bash
    pip install -r requirements.txt
```



* Run the automated tests   

```bash
    ptest3 -t tests
```




* To see test result report check the HTML report path generated after test run in the terminal and append `/index.html` and then open it in browser
.For example it looks like this in my system :  

```bash
    /Users/ranit/documentation/automation-framework-api/test-output/html-report/index.html
   
```
     


## Test cases automated

### Endpoint : `/services`

#### Services CURD Test
   * test_001: Create a service resource and validate the status code, schema and response payload.
   * test_002: Get the service created by its ID and validate the status code, schema and response payload. 
   * test_003: Update the service created by its ID and validate the status code, schema and response payload.
   * test_004: Delete the service created by its ID and validate the status code, schema and response payload.  

#### Services Sanity Tests
   * test_001: Check if get all API call working fine and validate the status code, schema and response payload.
   
   * test_002: Check if pagination is working properly by getting different paginated responses
    and also validate the status code,schema and response payload.
    
   * test_003: Check the case when wrong payload is given for service creation
    and validate the error status code,schema and error response payload. (This test case is running with a data provider
    , which means it will run multiple times depending on the data provided)
    
   * test_004: Check if services are getting created and validate the status code,schema and response payload. (This test case is running with a data provider
    , which means it will run multiple times depending on the data provided)
    
   * test_005: Get the services which got created in `test_004` and validate the status code,schema and response payload. (This test case is running with a data provider
    , which means it will run multiple times depending on the data provided)
    
   * test_006: Delete the services which got created in `test_004` and validate the status code,schema and response payload. (This test case is running with a data provider
    , which means it will run multiple times depending on the data provided)
    
   * test_007: Try to delete services which already got deleted in `test_006`.This should return an error as 
    those resources are no longer available.Also validate the error status code,schema and the error response payload. (This test case is running with a data provider
    , which means it will run multiple times depending on the data provided)
    
   * test_008: Try to get the services which already got created in `test_004`.This should return an error as 
    those resources are no longer available.Also validate the error status code,schema and the error response payload. (This test case is running with a data provider
    , which means it will run multiple times depending on the data provided)
    

