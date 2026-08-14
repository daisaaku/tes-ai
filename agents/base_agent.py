import json
import urllib.request
import urllib.error

class BaseAgent:
    def __init__(self, name: str, system_prompt: str, model: str = 'qwen2.5:3b', ollama_url: str = 'http://localhost:11434'):
        self.name = name
        self.system_prompt = system_prompt
        self.model = model
        self.ollama_url = ollama_url
        self.history = []

    def think_and_action(self, input_data: dict) -> dict:
        """相手や世界のデータを受け取り、自由思考してJSON形式で回答を返す"""
        user_input_str = json.dumps(input_data, ensure_ascii=False)
        self.history.append({'role': 'user', 'content': user_input_str})

        messages = [{'role': 'system', 'content': self.system_prompt}] + self.history

        payload = {
            "model": self.model,
            "messages": messages,
            "format": "json",
            "stream": False
        }

        try:
            req = urllib.request.Request(
                f"{self.ollama_url}/api/chat",
                data=json.dumps(payload).encode('utf-8'),
                headers={'Content-Type': 'application/json'}
            )
            with urllib.request.urlopen(req, timeout=30) as response:
                result = json.loads(response.read().decode('utf-8'))
                content = result['message']['content']
        except Exception as e:
            # Ollama未起動時や通信エラー時のフォールバック処理（ローカル開発用）
            content = json.dumps({
                "thought": f"（通信エラーまたはテスト環境のため自律思考モード稼働中: {e}）",
                "action_type": "speak",
                "target": "周囲の人々",
                "detail": f"こんにちは、{self.name}です。街の様子を見ています。"
            }, ensure_ascii=False)

        self.history.append({'role': 'assistant', 'content': content})

        try:
            return json.loads(content)
        except json.JSONDecodeError:
            return {
                "thought": "（思考のパース失敗）",
                "action_type": "speak",
                "target": "全員",
                "detail": content
            }
