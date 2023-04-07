import json
from flask import Flask, request


app = Flask(__name__)

@app.route('/')
def home():
    return 'hello, world~~~~'

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/walker', methods=['POST'])
def walker():
    r = request.json
    print(json.dumps(r, indent=4))
    print("------")
    
    action_id = r['user_action']['id']
    print(action_id)

    callback = {
        "callback_type": "views.open",
        "new_view": {
            "view_id": "builder_test",
            "header": {
                "title": "This is a view title",
                "subtitle": "Add a subtitle if needed",
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
                    "image_url": "https://swit.express/assets/images/lib/emoji/apple-64/1f609.png",
                    "alt": "Header button icon"
                    },
                    "static_action": {
                    "action_type": "open_link",
                    "link_url": "https://swit.express"
                    }
                }
                ]
            },
            "body": {
                "elements": [
                {
                    "type": "button",
                    "label": "Button 1",
                    "action_id": "eb5c968b-f4fb-4abe-8605-5b8ad6fe908a",
                    "style": "primary_filled"
                }
                ]
            }
        }
    }
    return callback

# 터미널 실행 명령 flask -A walker run --port=5000
# ngrok 경로 C:\Users\USER\Downloads\ngrok-v3-stable-windows-amd64>