import json

from utils.api import Google_maps
from utils.checking import Checking
import allure

# Create, change and delete new location
@allure.epic("Test create location")
class Test_create_location():

    @allure.description("create, update ad delete location")
    def test_create_new_location(self):

        print("Post method")
        result_post = Google_maps.create_new_location()
        check_post = result_post.json()
        place_id = check_post.get("place_id")
        # token = json.loads(result_post.text) #  for list of token fields
        # print(list(token))

        Checking.check_status_code(result_post, 200)
        Checking.check_json_token(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])
        Checking.check_json_value(result_post, "status", "OK")

        print("Get post method")
        result_get = Google_maps.get_new_location(place_id)

        Checking.check_status_code(result_get, 200)

        print("Put method")
        result_put = Google_maps.put_new_location(place_id)

        Checking.check_status_code(result_put, 200)
        Checking.check_json_token(result_put, ["msg"])

        print("Get put method")
        result_get = Google_maps.get_new_location(place_id)

        Checking.check_status_code(result_get, 200)

        print("Delete method")
        result_delete = Google_maps.delete_new_location(place_id)

        Checking.check_status_code(result_delete, 200)

        print("Get delete method")
        result_get = Google_maps.get_new_location(place_id)

        Checking.check_status_code(result_get, 404)


