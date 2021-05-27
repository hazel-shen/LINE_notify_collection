# Ansible Collection - hazel_shen.line_notify

Documentation for the collection.

ansible-galaxy collection install hazel_shen.line_notify  --ignore-certs

## LINE Notify API Document

[LINE Notify API Document](https://notify-bot.line.me/doc/en/)

## How to use this collection

Download collection from [Ansible Galaxy](https://galaxy.ansible.com/hazel_shen/line_notify) 
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

![line_notify_tree](https://raw.githubusercontent.com/hazel-shen/Image_Repo/main/line_notify_tree.jpg)

Please put these code into `requirements.yml`:
```
---
collections:
- hazel_shen.line_notify
```

Ansible Tower will download collection automatically when you execute the playbook with collection requirement.

## Use case - Notify someone when things go wrong :'(

![Ansible Tower Workflow](https://raw.githubusercontent.com/hazel-shen/Image_Repo/main/line_notify_use_case.jpg)

## How to develop