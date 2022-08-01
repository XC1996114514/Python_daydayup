
from flask import Flask, render_template
name = 'シャア・アズナブル, Shaa Azunaburu'
Mobile_Suits = [
    {'title': 'MS-06S 夏亚专用扎古2', 'year': '0079'},
    {'title': 'MSM-07S 夏亚专用魔蟹', 'year': '0079'},
    {'title': 'YMS-14A 夏亚专用勇士', 'year': '0079'},
    {'title': 'MS-09S 夏亚专用力克大魔', 'year': '0079'},
    {'title': 'MSN-02 吉翁号', 'year': '0079'},
    {'title': 'YMS-15E 强人 爱欧斯', 'year': '0087'},
    {'title': 'RMS-099 力克迪亚斯', 'year': '0087'},
    {'title': 'MSN-00100 百式', 'year': '0087'},
    {'title': 'MSN-04 沙扎比', 'year': '0093'},
    {'title': 'MSN-04-02 夜莺', 'year': '0093'},
]
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html', name=name, Mobile_Suits=Mobile_Suits)