from flask import Flask, request
import json
app = Flask(__name__)

@app.route("/")
def home():
    return "Flask home Test"

@app.route('/devel', methods=['POST'])
def devel():
    r = request.json
    print(json.dumps(r, indent=4))
    action_id = r['user_action']['id']
    print(action_id)

    this_ch_id = r['context']['channel_id']
    #print(this_ch_id)
    
    if action_id == 'btn_submit':

        cur = r['current_view']
        cur['header']['title'] = "업데이트 된 타이틀"
        cur['header']['subtitle'] = "업데이트 된 서브 타이틀"

        callback = {
            "callback_type": "views.update",
            "new_view": cur
        }

    else:

        callback = {
            "callback_type": "views.open",
            "new_view": {
                "view_id": "builder_test",
                "header": {
                    "title": "회식 선택",
                    "subtitle": "메뉴와 회식일정을 정해주세요.",
                    "context_menu": [
                        {
                            "label": "Menu item 1",
                            "action_id": "2fc5573a-c439-4131-9c82-6ed78c1f1758"
                        },
                        {
                            "label": "Menu item 2",
                            "action_id": "340d4ae1-0cb2-42c7-8880-4b5c2aed0f2d"
                        },
                        {
                            "label": "Menu item 3",
                            "action_id": "449fec68-ad54-4ee8-aa29-1c56957868c7"
                        }
                    ],
                    "buttons": [
                        {
                            "type": "button",
                            "icon": {
                                "type": "image",
                                "image_url": "https://swit.io/assets/images/lib/emoji/apple-64/1f609.png",
                                "alt": "Header button icon"
                            },
                            "static_action": {
                                "action_type": "open_link",
                                "link_url": "https://swit.io"
                            }
                        }
                    ]
                },
                "body": {
                    "elements": [
                        {
                            "type": "select",
                            "placeholder": "Select an item",
                            "multiselect": True,
                            "trigger_on_input": True,
                            "options": [
                                {
                                    "label": "곱창",
                                    "action_id": "eb5c968b-f4fb-4abe-8605-db83d6fd908a"
                                },
                                {
                                    "label": "닭내장",
                                    "action_id": "8992c582-7b37-4df5-be65-fb46d22f4839",
                                    "static_action": {
                                        "action_type": "open_link",
                                        "link_url": "https://swit.io"
                                    }
                                }
                            ]
                        },
                        {
                            "type": "datepicker",
                            "placeholder": "YYYY-MM-DD",
                            "action_id": "a60389c6-2517-4388-8f56-da1aaf9c7b28"
                        },
                        {
                            "type": "divider"
                        },
                        {
                            "type": "text_input",
                            "action_id": "435cd98a-1c04-409e-9230-d654ba44b0ca",
                            "placeholder": "기타 먹고 싶은거 입력해주세요.",
                            "trigger_on_input": False
                        },
                        {
                            "type": "button",
                            "label": "Close",
                            "style": "secondary",
                            "static_action": {
                                "action_type": "close_view"
                            }
                        },
                        {
                            "type": "button",
                            "label": "제출",
                            "action_id": "btn_submit",
                            "style": "primary"
                        }
                    ]
                }
            }

        }

    return callback