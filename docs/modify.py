import os
import re

# 定义函数来处理每个 Markdown 文件
def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    new_lines = []
    for line in lines:
        line = line.replace("\\\\", "\\\\\\\\")  # 替换反斜杠
        # 使用正则表达式查找包含 $$ 的行，并确保 $$ 单独成行
        if '$$' in line:
            # 分割出 $$ 前后的部分，并插入换行符
            parts = re.split(r'(\$\$)', line.strip())
            # 保证 $$ 成为独立一行
            for part in parts:
                if part:
                    new_lines.append(part + '\n')
        else:
            new_lines.append(line)

    # 将处理后的内容写回文件
    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)

# 定义递归遍历目录的函数
def process_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                print(f'Processing {file_path}...')
                process_file(file_path)

# 调用处理函数
if __name__ == '__main__':
    process_directory('/Users/yaodongyu/Coding/Learning/Preisthe/docs')  # 从当前目录开始
    # process_file('/Users/yaodongyu/Coding/Learning/Preisthe/docs/Physics/lecture03.md')