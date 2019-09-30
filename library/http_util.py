import requests
import json
from ptest.plogger import preporter


def get(url, headers={}):
    preporter.info("GET URL: " + url)
    return requests.get(url, headers=headers)


def post(url, request_json, headers={}):
    preporter.info("POST URL: " + url)
    preporter.info("Request JSON: " + json.dumps(request_json))
    return requests.post(url, json=request_json, headers=headers)


def put(url, request_json, headers={}):
    preporter.info("PUT URL: " + url)
    preporter.info("Request JSON: " + json.dumps(request_json))
    return requests.put(url, json=request_json, headers=headers)


def patch(url, request_json, headers={}):
    preporter.info("Patch URL: " + url)
    preporter.info("Request JSON: " + json.dumps(request_json))
    return requests.patch(url, json=request_json, headers=headers)


def delete(url, request_json, headers={}):
    preporter.info("Delete URL: " + url)
    preporter.info("Request JSON: " + json.dumps(request_json))
    return requests.delete(url, headers=headers)

