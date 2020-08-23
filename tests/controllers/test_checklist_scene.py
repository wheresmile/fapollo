# -*- coding: utf-8 -*-
import json
from pprint import pprint

from tests.fixtures.checklist_scene import scene_2, scene_home_checklist


def test_checklist_scenes_all(auth):

    response = auth.get("/api/v1/checklist_scene/all")
    assert response.status_code == 200
    res_json = json.loads(response.get_data(as_text=True))
    # pprint(res_json)
    assert res_json["data"]["last_id"] == 2
    assert res_json["data"]["has_more"] == 0
    scenes = res_json["data"]["scenes"]
    assert len(scenes) == 2
    for scene in scenes:
        assert scene.get("id") is not None
        assert scene.get("description") is not None


def test_checklists_of_scene(auth):
    response = auth.get("/api/v1/checklist_scene/checklists?scene_id={}".format(scene_home_checklist.id))
    assert response.status_code == 200
    res_json = json.loads(response.get_data(as_text=True))
    # pprint(res_json)
    assert type(res_json["data"]) is list
    assert len(res_json["data"]) == 3
