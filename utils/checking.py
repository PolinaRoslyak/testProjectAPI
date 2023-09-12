# Methods for checking http responses
import json
class Checking():

    @staticmethod
    def check_status_code(result, code):
        assert code == result.status_code
        print("Status code is " + str(result.status_code))

    @staticmethod
    def check_json_token(result, expected_value):
        token = json.loads(result.text)
        assert list(token) == expected_value
        print("all values are in token")

    @staticmethod
    def check_json_value(result, field_name, expected_value):
        check_info = result.json().get(field_name)
        assert expected_value == check_info
        print(field_name + " is correct")

    @staticmethod
    def check_json_search_word_in_value(result, field_name, searched_word):
        check_info = result.json().get(field_name)
        if searched_word in check_info:
            print(searched_word + " is in value")
        else:
            print(searched_word + " is not in value")

