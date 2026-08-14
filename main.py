from agents.free_agent import FreeAgent
from environment.world import WorldGM

def run_simulation():
    print("==================================================")
    print(" 🚀 TES-AI: 完全自由社会シミュレーション 起動")
    print("==================================================\n")

    # 1. 自由な意思を持つ多様なエージェントたち
    agents = [
        FreeAgent(
            name="アリス",
            role="人気インフルエンサー",
            personality="目立ちたがり屋でフォロワー第一主義。自分の発言で街を動かしたい。",
            initial_status={"money": 1200000, "health": 100, "location": "駅前広場"}
        ),
        FreeAgent(
            name="マスター",
            role="喫茶店マスター",
            personality="噂好きで情報通。客同士の会話を聞いて楽しんでいる。",
            initial_status={"money": 500000, "health": 100, "location": "喫茶店"}
        ),
        FreeAgent(
            name="田中",
            role="一般人",
            personality="パッパラ商事で働いてる普通のサラリーマン。仕事以外家に出ない引きこもり。思ったことをすぐSNSに投稿する。",
            initial_status={"money": 40000, "health": 100, "location": "家"}
        ),
        FreeAgent(
            name="ボブ",
            role="一般人",
            personality="自由奔放で人懐っこい。新しいことを試すのが好きで、常に新しいアイデアを持っている。",
            initial_status={"money": 60000, "health": 100, "location": "公園"}
        ),
        FreeAgent(
            name="チャーリー",
            role="一般人",
            personality="好奇心旺盛で冒険好き。新しい場所や人との出会いを求めている。",
            initial_status={"money": 80000, "health": 100, "location": "大都会"}
        ),
        FreeAgent(
            name="デイビッド",
            role="ニュースキャスター",
            personality="冷静沈着で計画的。リスクを避ける傾向があり、慎重に行動する。",
            initial_status={"money": 150000, "health": 100, "location": "放送局"}
        ),
    ]

    gm = WorldGM()
    max_turns = 3

    for turn in range(1, max_turns + 1):
        gm.turn = turn
        print(f"==================== TURN {turn} ====================")
        
        # 全エージェントが現在の世界状況を見て自由に行動を決める
        for agent in agents:
            world_state = gm.get_world_state()
            action = agent.act(world_state)
            gm.update_world(agent.name, action)

    print("\n==================================================")
    print(" 🏁 シミュレーション終了")
    print("==================================================")

if __name__ == "__main__":
    run_simulation()
