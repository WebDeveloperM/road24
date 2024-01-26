import random

import requests
import json
import uuid

from django.conf import settings

from users.models import SmsCode


def send_code(phone, sender="4546"):
    phone = phone.replace("+", "")
    phone = phone.replace("(", "")
    phone = phone.replace(")", "")
    phone = phone.replace("-", "")
    phone = int(phone)
    print(settings.ESKIZ_TOKEN, '------------------------')
    dispatch_id = str(uuid.uuid4()).split('-')[0]
    token = settings.ESKIZ_TOKEN

    rand_list = random.sample(range(1, 10), 4)
    rand_str = ''.join(map(str, rand_list))

    try:
        url = "https://notify.eskiz.uz/api/message/sms/send"
        payload = json.dumps(         
            {
            'mobile_phone': phone,
            "from": sender,
            "message": f"Tasdiqlash kodi: {rand_str}",
            "callback_url": "http://road24.uz"
        })
        headers = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        SmsCode.objects.create(dispatch_id=dispatch_id, code=rand_str)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

    return {"message_status": response.json(), "phone": phone, "dispatch_id": dispatch_id}