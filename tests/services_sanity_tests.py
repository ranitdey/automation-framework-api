from ptest.assertion import assert_equals, assert_true
from ptest.decorator import TestClass, Test
from library import http_util
from library import common_utils
from config import BASE_ENDPOINT, SERVICES_PATH
from resources.schemas import services_schemas
from resources.data import data


@TestClass(run_mode='singleline')
class ServicesSanityTests:
    testcase_data = {}

    @Test()
    def test_001_get_all_services_sanity(self):
        url = common_utils.build_resource_endpoint(BASE_ENDPOINT, SERVICES_PATH)
        response = http_util.get(url, headers=common_utils.get_basic_headers())
        assert_equals(response.status_code, 200)
        assert_true(common_utils.validate_schema(response.json(), services_schemas.services_get_all_schema))

    @Test()
    def test_002_get_all_services_pagination(self):
        url = common_utils.build_resource_endpoint(BASE_ENDPOINT, SERVICES_PATH)
        response = http_util.get(url, headers=common_utils.get_basic_headers())
        assert_equals(response.status_code, 200)
        assert_true(common_utils.validate_schema(response.json(), services_schemas.services_get_all_schema))
        limit = response.json()["limit"]
        url = common_utils.build_resource_endpoint(BASE_ENDPOINT, SERVICES_PATH) + "?$skip=" + str(limit)
        paginated_response = http_util.get(url, headers=common_utils.get_basic_headers())
        assert_equals(response.status_code, 200)
        assert_true(common_utils.validate_schema(response.json(), services_schemas.services_get_all_schema))
        assert_equals(paginated_response.json()["skip"], limit)

    @Test(data_provider=data.TEST_SERVICES)
    def test_003_create_services_error(self, service):
        url = common_utils.build_resource_endpoint(BASE_ENDPOINT, SERVICES_PATH)
        error_payload = {"error_name": service}
        response = http_util.post(url, request_json=error_payload, headers=common_utils.get_basic_headers())
        response_json = response.json()
        assert_equals(response.status_code, 400)
        assert_true(common_utils.validate_schema(response_json, services_schemas.services_error_schema))

    @Test(data_provider=data.TEST_SERVICES)
    def test_004_create_services_success(self, service):
        url = common_utils.build_resource_endpoint(BASE_ENDPOINT, SERVICES_PATH)
        response = http_util.post(url, request_json=common_utils.create_services_payload(service),
                                  headers=common_utils.get_basic_headers())
        response_json = response.json()
        assert_equals(response.status_code, 201)
        assert_true(common_utils.validate_schema(response_json, services_schemas.services_success_schema))
        assert_equals(response_json["name"], service, "Service name did't match")
        self.testcase_data[service] = str(response_json["id"])

    @Test(data_provider=data.TEST_SERVICES, depends_on="test_005_create_services_success")
    def test_005_get_services_success(self, service):
        url = common_utils.build_resource_endpoint(BASE_ENDPOINT, SERVICES_PATH, self.testcase_data[service])
        response = http_util.get(url, headers=common_utils.get_basic_headers())
        response_json = response.json()
        assert_equals(response.status_code, 200)
        assert_true(common_utils.validate_schema(response_json, services_schemas.services_success_schema))
        assert_equals(str(response_json["id"]), self.testcase_data[service])
        assert_equals(service, response_json["name"])

    @Test(data_provider=data.TEST_SERVICES, depends_on="test_006_get_services_success")
    def test_006_delete_services_success(self, service):
        url = common_utils.build_resource_endpoint(BASE_ENDPOINT, SERVICES_PATH, self.testcase_data[service])
        response = http_util.delete(url, headers=common_utils.get_basic_headers())
        response_json = response.json()
        assert_equals(response.status_code, 200)
        assert_true(common_utils.validate_schema(response_json, services_schemas.services_success_schema))
        assert_equals(str(response_json["id"]), self.testcase_data[service])
        assert_equals(service, response_json["name"])

    @Test(data_provider=data.TEST_SERVICES, depends_on="test_006_delete_services_success")
    def test_007_delete_services_error(self, service):
        url = common_utils.build_resource_endpoint(BASE_ENDPOINT, SERVICES_PATH, self.testcase_data[service])
        response = http_util.delete(url, headers=common_utils.get_basic_headers())
        response_json = response.json()
        assert_equals(response.status_code, 404)
        assert_true(common_utils.validate_schema(response_json, services_schemas.services_error_schema))

    @Test(data_provider=data.TEST_SERVICES, depends_on="test_006_delete_services_success")
    def test_008_get_services_error(self, service):
        url = common_utils.build_resource_endpoint(BASE_ENDPOINT, SERVICES_PATH, self.testcase_data[service])
        response = http_util.get(url, headers=common_utils.get_basic_headers())
        response_json = response.json()
        assert_equals(response.status_code, 404)
        assert_true(common_utils.validate_schema(response_json, services_schemas.services_error_schema))





















