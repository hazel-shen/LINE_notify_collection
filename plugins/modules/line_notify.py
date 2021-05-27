#!/usr/bin/python
from ansible.module_utils.basic import *
import requests, json

LINE_NOTIFY_SERVER_URI = "https://notify-api.line.me/api/notify"

def main():
    module = AnsibleModule(
        argument_spec={
            'access_token': {'required': True},
            'message': {'required': True},
        }
    )
    response = send_notify(module.params['access_token'], module.params['message'])
    module.exit_json(changed=False, meta=json.loads(response.text))
   
def send_notify(access_token, message_content):
    headers = {"Authorization": "Bearer " + access_token}
    message_content = format_message(message_content)
    return requests.post(LINE_NOTIFY_SERVER_URI, headers=headers, params=message_content)
    
    
def format_message(message_content):
    message = {'message': message_content}
    return message

if __name__ == "__main__":
      main()