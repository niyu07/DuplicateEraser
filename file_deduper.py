import re
import os
import shutil

def collect_files_with_pattern(folder_path):
    # ホームディレクトリを展開して正しいパスに変換
    folder_path = os.path.expanduser(folder_path)

    # 正規表現で「(数字).拡張子」の形式を検出
    pattern = re.compile(r"\(\d+\)\.\w+$")
    collected_files = []

    # フォルダ内の全ファイルをスキャン
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path) and pattern.search(filename):
            collected_files.append(file_path)

    return collected_files

# 使用例
folder_path = "~/Downloads/"  # ホームディレクトリが含まれているパス
collected_files = collect_files_with_pattern(folder_path)

# 作成したいディレクトリ名
dir_name = "DuplicateFiles" 

# 作成するディレクトリのパスを指定
make_dir_path = os.path.expanduser(os.path.join("~/Downloads/", dir_name))

# 作成しようとしているディレクトリが存在するかどうかを判定する
if not os.path.isdir(make_dir_path):
    # ディレクトリが存在しない場合のみ作成する
    os.makedirs(make_dir_path)
    print(f"'{dir_name}' を作成しました。")
else:
    print(f"'{dir_name}' は既に存在しています。")

# 結果を表示
if collected_files:
    print("収集したファイル:")
    for file in collected_files:
        # 移動先のパスを作成
        target_path = os.path.join(make_dir_path, os.path.basename(file))
        
        # ファイルを移動
        shutil.move(file, target_path)
        print(f"'{file}' を '{target_path}' に移動しました。")
else:
    print("該当するファイルは見つかりませんでした。")
