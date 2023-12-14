import json


class DierenasielRepository:
    __filename = "doc/dierenasiel_kortrijk.json"
    # __filename = "doc/dierenasiel_brugge.json"

    @staticmethod
    def __read_local_json_file(bestandsnaam):
        fo = open(bestandsnaam, encoding="utf8")
        response_json = fo.read()
        fo.close()
        return json.loads(response_json)
