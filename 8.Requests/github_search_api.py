import requests
import json


def search_items(finding):
    search_git = requests.get("https://api.github.com/search/repositories?q=" + finding)
    json_txt = json.loads(search_git.text)
    
    if json_txt['total_count'] > 30:
        print("Total results:", json_txt['total_count'], "exceeded max results of 30.")
    else:
        print("Total results:", json_txt['total_count'])
    return json_txt

user_input = input("Search from github: ")
print("Searching for: " + user_input)
search_results = search_items(user_input)

for index, pages in enumerate(search_results['items'], start=1):
    
    print(
        index, "\nDescription: ", pages['description'], "\nClone page: ", pages['clone_url'], "\n"
    )