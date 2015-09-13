# -*- coding: utf-8 -*-
from psychopy import visual, core, event, gui, data, misc
import numpy, os, random, time, csv

try:
    #　画面の準備（灰色の画面、マウスはallowGUI=Falseで表示されないようにしている）
    myWin = visual.Window (fullscr=True, monitor= 'Default', allowGUI=False, units='norm', color= (0,0,0))
    # 文字（漢字)のリスト
    kanjiList = [u'赤',u'黄',u'青',u'赤',u'黄',u'青',u'赤',u'黄',u'青']
    # 色のリスト(visual.TextStimのcolorにいれる)
    colorList = [(1,-1,-1),(1,-1,-1),(1,-1,-1),(1,1,-1),(1,1,-1),(1,1,-1),(-1,-1,1),(-1,-1,1),(-1,-1,1)]
    # 正答の反応(色のリストに対応したキーボードの反応)
    correctReslist = ['1','1','1','2','2','2','3','3','3']
    # 一致条件と不一致条件について(1=一致、2=不一致)
    congruentList = [1,2,2,2,1,2,2,2,1]
    # ランダムに提示するためのリスト
    randomList = range(9)
    # 教示をだす。
    instText = visual.TextStim(myWin,text = u'今から、色のついた文字がでてきます。\n文字の意味ではなく、文字の色に基づいてボタン押しをしてください。\n\n文字が赤色なら、キーボードの１を押してください。\n文字が黄色なら、キーボードの２を押してください。\n文字が青色なら、キーボードの３を押してください。\n\nこの教示が読めたら、「スペース」キーを押して課題を始めてください',pos=(0,0),color = (-1,-1,-1),height=0.1)
    instText.draw()
    myWin.flip()
    #　参加者がspaceキーを押すまで画面を出したまま待つ。
    keyList = event.waitKeys(keyList=['space'])

    #反応時間の計測のための設定
    stopwatch = core.Clock()

    # 内側のforループを2回繰り返すためのfor文
    for m in range(2):
        # randomListをシャッフルする。
        numpy.random.shuffle(randomList)
        # 内側のfor文（range(9)で0~8のリストを作成し、前から順番でiにいれる）
        for i in range(9):
            #　kanjiListのrandomList[i]番目（kanjiList[randomList[i]]）を、
            # colorListのrandomList[i]番目の色(colorList[randomList[i]])で提示する。
            myText = visual.TextStim(myWin,text = kanjiList[randomList[i]],pos=(0,0),color = colorList[randomList[i]],height=0.2)
            myText.draw()
            myWin.flip()

            ##### 参加者の反応測定開始
            # 前回の刺激提示の影響を消去する
            event.clearEvents()
            #ストッウォッチをリセット
            stopwatch.reset()
            # 参加者の反応をリセット
            Responded = False
            #ストップウォッチをリセットしてからstopwatch.getTime()で
            #測定した時間が1秒を超えるまで以下の処理を実行
            while stopwatch.getTime() < 1:
                # もしこれまでに反応がないようなら、event.waitKeysで反応を抜き出す。
                # Responded内には反応と反応時間が入る
                if not Responded:
                    Responded = event.getKeys(keyList=['1','2','3'],timeStamped=stopwatch)
            # もし1秒たっても反応がないなら、no responseと反応時間なしで処理する
            if not Responded:
                Responded = [('no respose', 0)]
            #### 参加者の反応測定終了

            # 正解、不正解のフィードバックと中視点提示
            if Responded[0][0] == 'no respose':
                # fbTextに、フィードバックする文字をいれる
                fbText = visual.TextStim(myWin,text = u'無反応',pos=(0,-0.3),color = (-1,-1,-1),height=0.2)
                # rtTextに、フィードバックする反応時間(Responded[0][0])をいれる
                rtText = visual.TextStim(myWin,text = str(Responded[0][1])+u'秒',pos=(0,-0.5),color = (-1,-1,-1),height=0.2)
            elif Responded[0][0]== correctReslist[randomList[i]]:
                # fbTextに、フィードバックする文字をいれる
                fbText = visual.TextStim(myWin,text = u'正解',pos=(0,-0.3),color = (-1,-1,-1),height=0.2)
                # rtTextに、フィードバックする反応時間(Responded[0][0])をいれる
                rtText = visual.TextStim(myWin,text = str(Responded[0][1])+u'秒',pos=(0,-0.5),color = (-1,-1,-1),height=0.2)
            else:
                # fbTextに、フィードバックする文字をいれる
                fbText = visual.TextStim(myWin,text = u'不正解',pos=(0,-0.3),color = (-1,-1,-1),height=0.2)
                # rtTextに、フィードバックする反応時間(Responded[0][0])をいれる
                rtText = visual.TextStim(myWin,text = str(Responded[0][1])+u'秒',pos=(0,-0.5),color = (-1,-1,-1),height=0.2)
            #上記で設定したフィードバックと反応時間の書き込み
            fbText.draw()
            rtText.draw()
            # 中視点の準備
            myText = visual.TextStim(myWin,text = '+',pos=(0,0),color = (-1,-1,-1),height=0.2)
            myText.draw()
            #　画面表示
            myWin.flip()
            core.wait(2)
except TypeError, e:
    print e