import pandas as pd
import markdown
from markdownify import markdownify as md

# 读取Excel文件
file_path = '遥感大模型论文汇总.xlsx'
excel_data = pd.ExcelFile(file_path)
sheet_names = excel_data.sheet_names
print(sheet_names)

# 读取指定工作表
df_sheet1 = pd.read_excel(file_path, sheet_name='智能表2')

# 将第一列paper变为超链接，链接的内容是同一行中Link列的内容
df_sheet1['Paper'] = df_sheet1.apply(lambda row: f"<a href='{row['Link']}'>{row['Paper']}</a>", axis=1)

# 删除Link列，因为已经将其内容整合到paper列中
df_sheet1.drop(columns=['Link'], inplace=True)

# 定义转换为HTML格式的函数
def generate_html_table(df):
    html = '<table style="width:100%;">\n'
    html += '<tr>\n'
    html += '<td>Paper</td>\n'
    html += '<td>key</td>\n' 
    html += '<td>value</td>\n' 
    html += '<td>Short Summary</td>\n'
    html += '</tr>\n'
    for _, row in df.iterrows():
        html += '  <tr>\n'
        html += f"    <td rowspan='9' style='text-align: left; width:30%;'>{row['Paper']}</td>\n"
        html += f"    <td style='text-align: left; width:10%;'>Tag</td>\n"
        html += f"    <td style='text-align: left; width:20%;'>{row['Tag']}</td>\n"
        html += f"    <td rowspan='9' style='text-align: left; width:40%;word-wrap: break-word;'>{row['Short Summary']}</td>\n"
        html += '  </tr>\n'
        
        html += '  <tr>\n'
        html += f"    <td style='text-align: left;'>Visual Encoder</td>\n"
        html += f"    <td style='text-align: left;'>{row['Visual Encoder']}</td>\n"
        html += '  </tr>\n'
        
        html += '  <tr>\n'
        html += f"    <td style='text-align: left;'>Text Encoder</td>\n"
        html += f"    <td style='text-align: left;'>{row['Text Encoder']}</td>\n"
        html += '  </tr>\n'
        
        html += '  <tr>\n'
        html += f"    <td style='text-align: left;'>Model Details</td>\n"
        html += f"    <td style='text-align: left;'>{row['Model Details']}</td>\n"
        html += '  </tr>\n'
        
        html += '  <tr>\n'
        html += f"    <td style='text-align: left;'>Task</td>\n"
        html += f"    <td style='text-align: left;'>{row['Task']}</td>\n"
        html += '  </tr>\n'

        html += '  <tr>\n'
        html += f"    <td style='text-align: left;'>Code/Project</td>\n"
        html += f"    <td style='text-align: left;'>{row['Code/Project']}</td>\n"
        html += '  </tr>\n'
        
        html += '  <tr>\n'
        html += f"    <td style='text-align: left;'>Survey Inclusion</td>\n"
        html += f"    <td style='text-align: left;'>{row['Survey Inclusion']}</td>\n"
        html += '  </tr>\n'
        
        html += '  <tr>\n'
        html += f"    <td style='text-align: left;'>备注</td>\n"
        html += f"    <td style='text-align: left;'>{row['备注']}</td>\n"
        html += '  </tr>\n'
        
        html += '  <tr>\n'
        html += f"    <td style='text-align: left;'>Published in</td>\n"
        html += f"    <td style='text-align: left;'>{row['Published in']}</td>\n"
        html += '  </tr>\n'

       
    html += '</table>'
    return html

# 生成HTML格式表格
html_table = generate_html_table(df_sheet1)

# 写入HTML文件
html_file = '遥感大模型论文汇总.html'
with open(html_file, 'w', encoding='utf-8') as file:
    file.write(html_table)

print("HTML file has been created.")
