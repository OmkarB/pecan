import wolframalpha
import bs4
import requests
import api_key



# Parse the suggested url given by xml
def parseExamplePage(url):
    website = requests.get(url)

    soup = bs4.BeautifulSoup(website.text, "html.parser")

    # find all suggested actions
    actions = soup.findAll("div", { "class" : "ex-caption" })

    # find all suggested examples
    examples = soup.findAll("span", { "class" : "content"})
    #
    # for action in actions:
    #     print(action.text)
    #
    # for example in examples:
    #     print(example.text)


def main(query):
    # get the Wolfram API
    app_id = api_key.wolfram_key
    # Connect to Wolfram
    client = wolframalpha.Client(app_id)

    res = client.query(query)

    # When query is broad
    if len(res.pods) == 0:
        suggested_url = res.tree.find('examplepage').get('url')
        parseExamplePage(suggested_url)
    #
    # else:
    #     for pod in res.pods:
    #         #print(pod.title)
    #         print(pod.text)


