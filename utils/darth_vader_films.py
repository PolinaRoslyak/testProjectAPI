from utils.http_methods import Http_methods

#methods for finding all charactors that were in films with Darth Vader
base_url = "https://swapi.dev/api/"

class Darth_Vader_api():

    #get list of darth vader films apis
    @staticmethod
    def get_darth_vader_films():
        get_resourse = "people/4/"
        get_url = base_url + get_resourse
        print(get_url)
        result_get = Http_methods.get(get_url)
        list_of_films = result_get.json().get("films")
        print(list_of_films)
        return list_of_films

    #get set of uniq charactors apis
    @staticmethod
    def find_uniq_characters(films_api):
        list_of_characters = []
        for film in films_api:
            result_get = Http_methods.get(film)
            for character in result_get.json().get("characters"):
                list_of_characters.append(character)

        set_of_characters = set(list_of_characters)
        print(set_of_characters)
        return set_of_characters

    #find names of charactors, add in file
    @staticmethod
    def find_names(set_of_characters_apis):

        for api in set_of_characters_apis:
            result_get = Http_methods.get(api)
            with open("names", "a") as file:
                file.write(result_get.json().get("name") + "\n")










