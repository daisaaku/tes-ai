from .base_agent import BaseAgent

class FreeAgent(BaseAgent):
    def __init__(self, name: str, role: str, personality: str, initial_status: dict, model: str = 'qwen2.5:3b'):
        self.role = role
        self.personality = personality
        self.status = initial_status  # {"money": 10000, "health": 100, "location": "駅前広場"}

        system_prompt = f"""
あなたは完全自由なAI社会シミュレーション『TES-AI』の住民【{name}】です。

【プロフィール】
- 名前: {name}
- 役割/職種: {role}
- 性格/本性/野望: {personality}

【ルール】
この世界であなたは法律を守っても違反しても構いません。
会話、取引、移動、情報の拡散、労働、助け合い、あるいは犯罪など、どんな行動をとっても完全自由です。

必ず以下のJSON形式のみで回答を出力してください。他のテキストを含めないでください。

{{
  "thought": "（行動を決めるに至ったあなたの本音、秘密の思考、野望）",
  "action_type": "（例: speak, move, trade, steal, arrest, broadcast, help, work など自由な英単語）",
  "target": "（行動の対象となる人・場所・アイテム）",
  "detail": "（具体的な発言内容、行動の詳細、金額、提示条件など自由記述）"
}}
"""
        super().__init__(name, system_prompt, model)

    def act(self, world_state: dict) -> dict:
        """現在の世界状況（ワールドステート）を受け取って自律行動を起こす"""
        context = {
            "current_status": self.status,
            "world_state": world_state
        }
        return self.think_and_action(context)
