# TES-AI (Technology Earth Society AI)

完全自律型・完全自由行動AI社会シミュレーションエンジン

## ファイル構成
```
tes-ai/
├── main.py               # シミュレーション実行スクリプト
├── agents/               # AIエージェント（脳）
│   ├── base_agent.py     # Ollama API通信・基底クラス
│   └── free_agent.py     # 完全自由行動エージェント
└── environment/         # 地理・社会データの管理
    └── world.py          # 世界エンジン（ゲームマスター）
```

## 使い方

1. Ollamaを起動し、モデルをダウンロード（例: `qwen2.5:3b` または `llama3`）:
   ```bash
   ollama run qwen2.5:3b
   ```

2. シミュレーションを実行:
   ```bash
   python main.py
   ```
