import datetime

# 現在時刻を取得
now = datetime.datetime.now()
timestamp_str = now.strftime("%Y/%m/%d %H:%M:%S")
# "[----/--/-- 00:00:00]"

# ビルド情報ファイルを作成
with open('build_info.py', 'w') as f:
    f.write(f'__BUILD_TIMESTAMP__ = "{timestamp_str}"\n')
    #f.write(f'__APP_VERSION__ = "1.0.0"\n')

#print(f"ビルド情報ファイルを生成しました: build_info.py, タイムスタンプ: {timestamp_str}")