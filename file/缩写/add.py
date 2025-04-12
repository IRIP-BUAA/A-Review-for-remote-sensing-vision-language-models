import re
import json
import difflib

# 1. 加载映射数据（mapping.json）
# JSON 格式示例（key 为缩写，value 为论文全名）：
# {
#    "SMLFR": "Generative ConvNet Foundation Model With Sparse Modeling and Low-Frequency Reconstruction for Remote Sensing Image Interpretation",
#    "XXX": "Another Paper Title"
# }
with open('result.json', 'r', encoding='utf8') as f:
    mapping = json.load(f)

# 反转映射：构造字典 {论文全名: 缩写}，方便后续根据论文全名查找缩写
mapping_inverted = {paper_title: abbr for abbr, paper_title in mapping.items()}

# 用于记录 md 文件中找到的论文全名（匹配到的论文按照 mapping 中的原论文名记录）
found_papers = set()

# 2. 处理 md 文件（data.md），假设每行格式为：
# | 第一列 | [论文全名](链接) | 第三列 | 第四列 |
with open('/Users/bytedance/Documents/work/A-Survey-on-Remote-Sensing-Foundation-Models-From-Vision-to-Multimodality/README copy.md', 'r', encoding='utf8') as f:
    md_lines = f.readlines()

new_md_lines = []

# 正则表达式说明：
# - ^\|\s* 匹配行首的 | 及可能的空格
# - (.*?)\s*\| 匹配第一列（例如原来的 "-"）
# - \s*\[([^\]]+)\]\(([^)]+)\)\s*\| 匹配第二列：[论文全名](链接)，提取论文全名和链接
# - 后续 (.*?)\s*\| 匹配第三列和第四列数据（假设有四列）  
pattern = re.compile(
    r'^\|\s*(.*?)\s*\|\s*\[([^\]]+)\]\(([^)]+)\)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|'
)

for line in md_lines:
    m = pattern.match(line)
    if m:
        first_col = m.group(1)  # 原始第一列内容（通常为 "-"）
        md_paper_name = m.group(2)  # md 中提取的论文全名（可能缺少标点）
        link = m.group(3)        # 链接
        col3 = m.group(4)
        col4 = m.group(5)

        # 使用 difflib 进行模糊匹配
        # 从 mapping_inverted 的所有论文全名中寻找与 md_paper_name 相似度最高的匹配项
        matches = difflib.get_close_matches(md_paper_name, mapping_inverted.keys(), n=1, cutoff=0.8)
        if matches:
            best_match = matches[0]
            new_first = mapping_inverted[best_match]
            # 将匹配到的映射论文原名记录下来
            found_papers.add(best_match)
        else:
            new_first = first_col

        # 重构该行（保持其它列及链接不变）
        new_line = f"| {new_first} | [{md_paper_name}]({link}) | {col3} | {col4} |\n"
        new_md_lines.append(new_line)
    else:
        # 非表格行保持原样输出
        new_md_lines.append(line)

# 写入更新后的 md 文件
with open('data_updated.md', 'w', encoding='utf8') as f:
    f.writelines(new_md_lines)

# 3. 记录 mapping 中存在但 md 中没有出现的论文（按 mapping 原始论文全名）
unmatched = {abbr: paper_title for abbr, paper_title in mapping.items() if paper_title not in found_papers}

# 保存未匹配的数据到 unmatched.json
with open('unmatched.json', 'w', encoding='utf8') as f:
    json.dump(unmatched, f, ensure_ascii=False, indent=2)

print("处理完成：已生成 'data_updated.md' 和 'unmatched.json'。")
