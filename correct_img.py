import os
import re

# 遍历当前目录及其子目录
def update_md_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                update_file(file_path)

# 替换文件中的图片插入方式
def update_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 正则替换 @import 图片格式
    updated_content = re.sub(r'@import\s+"([^"]+)"', r'![\1](\1)', content)

    # 如果有更改，保存文件
    if updated_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        print(f'Updated: {file_path}')

if __name__ == "__main__":
    # 设置你想要检查的目录
    current_directory = os.getcwd()
    update_md_files(current_directory)
    # update_file("/Users/yaodongyu/Coding/Learning/Preisthe/docs/Physics/lecture03.md")