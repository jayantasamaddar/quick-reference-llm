import json


def jsonify(jsonstring):
    if jsonstring == None:
        return
    return json.dumps(json.loads(jsonstring))


def strip(response):
    first = str(response).find("{")
    try:
        if first < 0:
            raise ValueError(None)
        last = str(response).rindex("}") + 1
        return jsonify(response[first:last])
    except:
        return
