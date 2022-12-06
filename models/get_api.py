import requests

url = "http://swopenAPI.seoul.go.kr/api/subway/7552464455797673363444686f556a/json/realtimeStationArrival/0/5/"


def request_api(station):
    return requests.get(url + station).json()


def data_filter(request, direction):
    direction_dict = {"right": "외선", "left": "내선"}
    state_dict = {0: "진입", 1: "도착", 2: "출발", 3: "전역 출발", 4: "전역 진입", 5: "전역 도착", 99: "이동 중"}
    response = {"subways": []}

    for item in request["realtimeArrivalList"]:
        data_dict = {}

        if item["updnLine"] == direction_dict[direction]:
            data_dict["finalStation"] = item["bstatnNm"] + "행"
            data_dict["test"] = item["trainLineNm"].split(" ")[2]

            minute = int(item["barvlDt"]) // 60
            second = int(item["barvlDt"]) % 60
            data_dict["goalTime"] = str(minute) + "분 " + str(second) + "초"

            data_dict["state"] = state_dict[int(item["arvlCd"])]
            data_dict["lastest_station"] = item["arvlMsg3"]

            response["subways"].append(data_dict)

    return response
