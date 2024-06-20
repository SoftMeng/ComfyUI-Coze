import requests
import random
import json

url = "https://api.coze.cn/open_api/v2/chat"
conversation_id = random.randint(32768, 65536)
user = random.randint(32768, 65536)

class ComfyUI_Coze:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text_positive": ("STRING", {"default": "给我个有创意的提示词", "multiline": True}),
                "bot_id": ("STRING", {"default": "需要填写Coze的BotID", "multiline": True}),
                "token": ("STRING", {"default": "需要填写Coze的Token", "multiline": True}),
                "seed": ("INT", {"default": 0}),
                "log_prompt": (["No", "Yes"], {"default":"Yes"}),
            },
        }

    RETURN_TYPES = ('STRING',)
    RETURN_NAMES = ('text_positive',)
    FUNCTION = "cozeApi"
    OUTPUT_NODE = True
    CATEGORY = "ComfyUI_Mexx"

    def cozeApi(self, text_positive, bot_id, token, seed, log_prompt):
        payload = json.dumps({
            "conversation_id": "mexx_" + str(conversation_id),
            "bot_id": bot_id,
            "user": "mexx_" + str(user),
            "query": text_positive,
            "stream": False
        })
        headers = {
            'Authorization': 'Bearer ' + token,
            'Accept': '*/*',
            'Host': 'api.coze.cn',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json'
        }

        r = requests.request("POST", url, headers=headers, data=payload)
        result = r.json()

        if log_prompt == "Yes":
            print(f"resp: {result}")
        messages = result["messages"]
        filtered_messages = [message for message in messages if message.get('type') == 'answer']
        content = filtered_messages[0]["content"]
        return [content]


NODE_CLASS_MAPPINGS = {
    "ComfyUI_Coze": ComfyUI_Coze
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ComfyUI_Coze": "ComfyUI_Coze"
}
