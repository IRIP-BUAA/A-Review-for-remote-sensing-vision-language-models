import json

# 1. 加载 JSON 数据（假设文件名为 mapping.json）
with open('/Users/bytedance/Documents/work/A-Survey-on-Remote-Sensing-Foundation-Models-From-Vision-to-Multimodality/file/缩写/unmatched.json', 'r', encoding='utf8') as f:
    mapping = json.load(f)

# 2. 读取 md 文件的全部内容（假设文件名为 data.md）
with open('/Users/bytedance/Documents/work/A-Survey-on-Remote-Sensing-Foundation-Models-From-Vision-to-Multimodality/README.md', 'r', encoding='utf8') as f:
    md_content = f.read()

# 如果需要不区分大小写，先将 md 内容转为统一格式
# md_content = md_content.lower()

# 3. 遍历 JSON 数据中每个 key，若在 md 文件中能找到该 key，则删除该数据
# 注意：这里使用字典解析构造新字典
new_mapping = {key: value for key, value in mapping.items() if key not in md_content}

# 如果需要不区分大小写，可以这样做：
# new_mapping = {key: value for key, value in mapping.items() if key.lower() not in md_content.lower()}

# 4. 将剩下的数据保存到新的 JSON 文件（例如 new_mapping.json）
with open('new_unmapping.json', 'w', encoding='utf8') as f:
    json.dump(new_mapping, f, ensure_ascii=False, indent=2)

print("处理完成：已生成 'new_mapping.json'。")
