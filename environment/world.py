class WorldGM:
    """自由な行動を受け止めて結果を処理するゲームマスター（世界エンジン）"""
    
    # 英語の行動タイプを日本語に変換する辞書
    ACTION_MAP = {
        "broadcast": "拡散・配信",
        "work": "仕事・作業",
        "help": "手助け・協力",
        "speak": "会話",
        "move": "移動",
        "trade": "取引",
        "steal": "窃盗・スリ",
        "arrest": "逮捕・連行",
        "news": "ニュース発表",
        "crime": "犯罪行動",
        "attack": "攻撃",
        "search": "調査・捜索"
    }

    def __init__(self):
        self.turn = 0
        self.news_board = [] # 街のニュース・話題
        self.public_logs = []

    def update_world(self, agent_name: str, action: dict):
        action_type = action.get("action_type", "speak")
        target = action.get("target", "周囲")
        thought = action.get("thought", "")
        detail = action.get("detail", "")

        # 英語の行動名を日本語に変換（辞書にない未知の単語はそのまま表示）
        action_jp = self.ACTION_MAP.get(action_type.lower(), action_type)

        log_entry = {
            "turn": self.turn,
            "agent": agent_name,
            "action_type": action_jp,
            "target": target,
            "thought": thought,
            "detail": detail
        }
        self.public_logs.append(log_entry)

        # 街の話題・ニュースに影響を与える行動の検知
        if action_type.lower() in ["broadcast", "news", "crime", "steal", "arrest"]:
            news_item = f"【Turn {self.turn} ニュース】{agent_name}が「{target}」に対して {action_jp} 行動: 『{detail}』"
            self.news_board.append(news_item)

        # コンソール表示（日本語化）
        print(f"👤 [{agent_name}] ({action_jp} -> {target})")
        print(f"   🧠 思考: {thought}")
        print(f"   💬 行動: {detail}")
        print("-" * 60)

    def get_world_state(self) -> dict:
        return {
            "turn": self.turn,
            "recent_news": self.news_board[-3:] if self.news_board else ["街は穏やかです。"],
            "recent_actions": [f"{l['agent']}: {l['detail']}" for l in self.public_logs[-5:]]
        }