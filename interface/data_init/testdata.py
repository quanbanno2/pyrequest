import time
from data_init.mysql_db import DB

future_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time() + 10000))
past_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time() - 10000))
now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

datas = {
    'sign_event': [
        {'id': 1, 'name': '红米Pro发布会', '`limit`': 2000, 'status': 1, 'address': '背景', 'start_time': future_time,
         "create_time": now_time},
        {'id': 2, 'name': '可参加人数为0', '`limit`': 0, 'status': 1, 'address': '背景', 'start_time': future_time,
         "create_time": now_time},
        {'id': 3, 'name': '状态为0', '`limit`': 2000, 'status': 0, 'address': '背景', 'start_time': future_time,
         "create_time": now_time},
        {'id': 4, 'name': '已结束', '`limit`': 2000, 'status': 1, 'address': '背景', 'start_time': past_time,
         "create_time": now_time}
    ],
    'sign_guest': [
        {"id": '1', "realname": "alen", "phone": "12345678", "email": "adsfaf@gmail.com", "sign": 0,
         "create_time": now_time, "event_id": 1},
        {"id": '2', "realname": "has sign", "phone": "12345678", "email": "adsfaf@gmail.com", "sign": 1,
         "create_time": now_time, "event_id": 2},
        {"id": '3', "realname": "tom", "phone": "12345678", "email": "adsfaf@gmail.com", "sign": 0,
         "create_time": now_time, "event_id": 3}
    ]
}


def init_data():
    DB().init_data(datas)
