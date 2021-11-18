import json


def my_json():
    with open('/Users/sbhattacharjee/IdeaProjects/LightningTalks-PythonDebugger/python_debug_json.txt') as f:
        return json.load(f)


def team_json():
    with open('/Users/sbhattacharjee/IdeaProjects/LightningTalks-PythonDebugger/de_team_json.txt') as f:
        return json.load(f)
