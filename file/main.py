import pandas as pd

# 读取Excel文件
file_path = '遥感大模型论文汇总.xlsx'
excel_data = pd.ExcelFile(file_path)
sheet_names = excel_data.sheet_names
print(sheet_names)

# 读取指定工作表
df_sheet1 = pd.read_excel(file_path, sheet_name='智能表2')

# 将第一列paper变为超链接，链接的内容是同一行中Link列的内容
df_sheet1['Paper'] = df_sheet1.apply(lambda row: f"[{row['Paper']}]({row['Link']})", axis=1)

# 删除Link列，因为已经将其内容整合到paper列中
df_sheet1.drop(columns=['Link'], inplace=True)

# 转换为Markdown格式
markdown_table = df_sheet1.to_markdown(index=False)

# 写入Markdown文件
md_file = '遥感大模型论文汇总.md'
with open(md_file, 'w', encoding='utf-8') as file:
    file.write(markdown_table)

print("Markdown file has been created.")
