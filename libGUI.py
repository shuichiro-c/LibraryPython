#import os
#import PySimpleGUI as sg
#
##  セクション1 - オプションの設定と標準レイアウト
#sg.theme('Dark Blue 3')
#
#layout = [
#    [sg.Text('Youtube Path')],
#    [sg.Text('Path', size=(15, 1)), sg.InputText('')],
#    [sg.Submit(button_text='Submit')]
#]
#
## セクション 2 - ウィンドウの生成
#window = sg.Window('Youtube Path', layout)
#
## セクション 3 - イベントループ
#while True:
#    event, values = window.read()
#
#    if event is None:
#        break
#
#    if event == 'Submit':
#        show_message = "名前：" + values[0] + 'が入力されました。\n'
#        print(show_message)
#
#        # ポップアップ
#        sg.popup(show_message)
#
## セクション 4 - ウィンドウの破棄と終了
#window.close()