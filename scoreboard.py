from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()  # Turtleクラスを継承して初期化
        self.color("white")  # 色を白に設定
        self.penup()  # ペンを上げる（描画しない）
        self.hideturtle()  # タートル（カーソル）を非表示にする
        self.l_score = 0  # 左側の得点
        self.r_score = 0  # 右側の得点
        self.update_scoreboard()  # 初期得点表示を更新

    def update_scoreboard(self):
        self.clear()  # 前回描画した内容を消去
        self.goto(-100, 200)  # 左側の得点位置に移動
        self.write(self.l_score, align="center", font=("Courier", 80 , "normal"))  # 左の得点を表示
        self.goto(100, 200)  # 右側の得点位置に移動
        self.write(self.r_score, align="center", font=("Courier", 80 , "normal"))  # 右の得点を表示

    def l_point(self):
        self.l_score += 1  # 左の得点を1加算
        self.update_scoreboard()  # 得点表示を更新

    def r_point(self):
        self.r_score += 1  # 右の得点を1加算
        self.update_scoreboard()  # 得点表示を更新
