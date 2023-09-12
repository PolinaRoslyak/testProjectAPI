from utils.darth_vader_films import Darth_Vader_api

class Test_find_specific_characters():

    def test_find_specific_characters(self):

        darth_vader_films = Darth_Vader_api()
        set_of_characters = darth_vader_films.find_uniq_characters(darth_vader_films.get_darth_vader_films())
        darth_vader_films.find_names(set_of_characters)


