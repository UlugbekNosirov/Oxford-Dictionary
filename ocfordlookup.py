import requests

app_id = "91e97b05"
app_key = "e963525216b62c26b09724c7ed4e434a"
language = "en-gb"


def getDefinition(word_id):
    url = "https://od-api.oxforddictionaries.com:443/api/v2/entries/" + language + "/" + word_id.lower()
    r = requests.get(url, headers={"app_id": app_id, "app_key": app_key})
    if 'error' in r.json():
        return False
    sences = r.json()['results'][0]['lexicalEntries'][0]['entries'][0]['senses']
    output = {}
    definition = []
    for sence in sences:
        definition.append(f"👉 {sence['definitions'][0]}")
    output['definitions'] = "\n".join(definition)
    if r.json()['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0]['audioFile']:
        output['audio'] = r.json()['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0]['audioFile']
    return output


