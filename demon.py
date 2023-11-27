import requests
import random

class Demon():
  def __init__(self):
    """
    This sets up the hard-coded API url to an instance variable
    args: none
    return: none
    """
    self.api_url = "https://anime-facts-rest-api.herokuapp.com/api/v1/demon_slayer"

  def get(self):
    """
    This reads the API as a json and sets the data to an instance variable
    args: none
    return: none
    """
    results = requests.get(self.api_url)
    self.data = results.json()

  def __str__(self):
    """
    This returns a statement using API data as a string, except when the data cannot 
    be accessed due to a network issue it returns "Network Error"
    args: none
    return: (str) a string that is printed in the terminal when the class is printed in main()
    """
    try:
      return "\n'Demon Slayer' Anime Fact: " + self.data['data'][random.randrange(0, 10)]['fact']
    except:
      return "Network Error"

