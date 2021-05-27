# Ansible Collection - hazel_shen.line_notify

Documentation for the collection.

ansible-galaxy collection install hazel_shen.line_notify  --ignore-certs

## LINE Notify API Document

[LINE Notify API Document](https://notify-bot.line.me/doc/en/)

## How to use this collection

```
# Download Ansible collection
ansible-galaxy collection install hazel_shen.line_notify
```
The following is example playbook:
```
---
- hosts: localhost
  collections:
  - hazel_shen.line_notify
  
  tasks:
  - name: line notify
    line_notify:
      access_token: "{{ access_token }}"
      message_content: "{{ message_content }}"
```
## How to use on Ansible Tower 

Your project tree should be like this:
.
├── collections
│   └── requirements.yml
└── line_notify_playbook.yml

Please put these code into `requirements.yml`:
```
---
collections:
- hazel_shen.line_notify
```

## How to develop