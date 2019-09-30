from ptest.assertion import assert_equals, assert_true
from ptest.decorator import TestClass, Test

from config import BASE_ENDPOINT, SERVICES_PATH
from library import common_utils, http_util
from resources.schemas import services_schemas
from resources.data import data


@TestClass(run_mode='singleline')
class ServicesCURDTest:
    testcase_data = {}

    @Test()
    def test_001_create_service(self):
        url = common_utils.build_resource_endpoint(BASE_ENDPOINT, SERVICES_PATH)
        payload = common_utils.create_services_payload(data.SINGLE_USER_WORKFLOW_SERVICES[0])
        response = http_util.post(url, request_json=payload, headers=common_utils.get_basic_headers())
        assert_equals(response.status_code, 201)
        response_json = response.json()
        assert_true(common_utils.validate_schema(response_json, services_schemas.services_success_schema))
        assert_equals(response_json["name"], data.SINGLE_USER_WORKFLOW_SERVICES[0])
        self.testcase_data[response_json["name"]] = response_json["id"]

    @Test()
    def test_002_get_service(self):
        url = common_utils.build_resource_endpoint(BASE_ENDPOINT, SERVICES_PATH,
                                                   resource=str(self.testcase_data[data.SINGLE_USER_WORKFLOW_SERVICES[0]]))
        response = http_util.get(url, headers=common_utils.get_basic_headers())
        assert_equals(response.status_code, 200)
        response_json = response.json()
        assert_true(common_utils.validate_schema(response_json, services_schemas.services_success_schema))
        assert_equals(response_json["name"], data.SINGLE_USER_WORKFLOW_SERVICES[0])
        assert_equals(response_json["id"], self.testcase_data[data.SINGLE_USER_WORKFLOW_SERVICES[0]])

    @Test()
    def test_003_update_service(self):
        url = common_utils.build_resource_endpoint(BASE_ENDPOINT, SERVICES_PATH,
                                                   resource=str(self.testcase_data[data.SINGLE_USER_WORKFLOW_SERVICES[0]]))
        payload = common_utils.create_services_payload("updated service name")
        response = http_util.patch(url, request_json=payload, headers=common_utils.get_basic_headers())
        assert_equals(response.status_code, 200)
        response_json = response.json()
        assert_true(common_utils.validate_schema(response_json, services_schemas.services_success_schema))
        assert_equals(response_json["id"], self.testcase_data[data.SINGLE_USER_WORKFLOW_SERVICES[0]])
        assert_equals(response_json["name"], "updated service name", "Updated name did't match")

        # updating the data back to original to maintain state
        payload = common_utils.create_services_payload(data.SINGLE_USER_WORKFLOW_SERVICES[0])
        get_response = http_util.patch(url, request_json=payload, headers=common_utils.get_basic_headers())
        self.testcase_data[get_response.json()["name"]] = response_json["id"]


    @Test()
    def test_004_delete_service(self):
        url = common_utils.build_resource_endpoint(BASE_ENDPOINT, SERVICES_PATH,
                                                   resource=str(self.testcase_data[data.SINGLE_USER_WORKFLOW_SERVICES[0]]))
        response = http_util.delete(url, headers=common_utils.get_basic_headers())
        assert_equals(response.status_code, 200)
        response_json = response.json()
        assert_true(common_utils.validate_schema(response_json, services_schemas.services_success_schema))
        assert_equals(response_json["name"], data.SINGLE_USER_WORKFLOW_SERVICES[0])
        assert_equals(response_json["id"], self.testcase_data[data.SINGLE_USER_WORKFLOW_SERVICES[0]])
        get_response = http_util.get(url, headers=common_utils.get_basic_headers())
        assert_equals(get_response.status_code, 404)





