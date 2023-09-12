from utils.http_methods import Http_methods

#methods for testing google maps api

base_url = "https://rahulshettyacademy.com"
key_parameter = "?key=qaclick123"

class Google_maps():
    @staticmethod
    def create_new_location():
        json_for_new_location = {
        "location": {
        "lat": -38.383494,
        "lng": 33.427362
        }, "accuracy": 50,
        "name": "Frontline house",
        "phone_number": "(+91) 983 893 3937",
        "address": "29, side layout, cohen 09",
        "types": [
        "shoe park",
        "shop"
        ],
        "website": "http://google.com",
        "language": "French-IN"
        }
        post_resource = "/maps/api/place/add/json"
        post_url = base_url + post_resource + key_parameter
        print(post_url)
        result_post = Http_methods.post(post_url, json_for_new_location)
        print(result_post.text)
        return result_post

    @staticmethod
    def get_new_location(place_id):
        get_resource = "/maps/api/place/get/json"
        get_url = base_url + get_resource + key_parameter + "&place_id=" + place_id
        print(get_url)
        result_get = Http_methods.get(get_url)
        print(result_get.text)
        return result_get

    @staticmethod
    def put_new_location(place_id):
        put_resource = "/maps/api/place/update/json"
        put_url = base_url + put_resource + key_parameter
        print(put_url)
        json_for_update_new_location = {
        "place_id":place_id,
        "address":"100 Lenina street, RU",
        "key":"qaclick123"
        }
        result_put = Http_methods.put(put_url, json_for_update_new_location)
        print(result_put.text)
        return result_put

    @staticmethod
    def delete_new_location(place_id):
        delete_resource = "/maps/api/place/delete/json"
        delete_url = base_url + delete_resource + key_parameter
        print(delete_url)
        json_for_delete_new_location = {
        "place_id":place_id
        }
        result_delete = Http_methods.delete(delete_url, json_for_delete_new_location)
        print(result_delete.text)
        return result_delete