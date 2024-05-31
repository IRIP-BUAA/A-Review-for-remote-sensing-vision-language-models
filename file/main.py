import pandas as pd
import markdown
from markdownify import markdownify as md

# 读取Excel文件
file_path = '遥感大模型论文汇总.xlsx'
excel_data = pd.ExcelFile(file_path)
sheet_names = excel_data.sheet_names
print(sheet_names)
def generate_html_table_1(df):
    html = ''
    for _, row in df.iterrows():
        html += '<table style="width:100%;">\n'
        html += '<tr>\n'
        html += '<td>Paper</td>\n'
        html += '<td>key</td>\n' 
        html += '<td>value</td>\n' 
        html += '<td>Short Summary</td>\n'
        html += '</tr>\n'
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
def generate_html_table_2(df):
    html = ''
    for _, row in df.iterrows():
        html += '<table style="width:100%;">\n'
        html += '<tr>\n'
        html += '<td>Paper</td>\n'
        html += '<td>key</td>\n' 
        html += '<td>value</td>\n' 
        html += '<td>Short Summary</td>\n'
        html += '</tr>\n'
        html += '  <tr>\n'
        html += f"    <td rowspan='11' style='text-align: left; width:30%;'>{row['Paper']}</td>\n"
        html += f"    <td style='text-align: left; width:10%;'>Published in</td>\n"
        html += f"    <td style='text-align: left; width:20%;'>{row['Published in']}</td>\n"
        html += f"    <td rowspan='11' style='text-align: left; width:40%;word-wrap: break-word;'>{row['Short Summary']}</td>\n"
        html += '  </tr>\n'
        
        html += '  <tr>\n'
        html += f"    <td style='text-align: left;'>Type</td>\n"
        html += f"    <td style='text-align: left;'>{row['Type']}</td>\n"
        html += '  </tr>\n'
        
        html += '  <tr>\n'
        html += f"    <td style='text-align: left;'>Code/Project</td>\n"
        html += f"    <td style='text-align: left;'>{row['Code/Project']}</td>\n"
        html += '  </tr>\n'
        
        html += '  <tr>\n'
        html += f"    <td style='text-align: left;'>备注</td>\n"
        html += f"    <td style='text-align: left;'>{row['备注']}</td>\n"
        html += '  </tr>\n'
        
        html += '  <tr>\n'
        html += f"    <td style='text-align: left;'>数据类型</td>\n"
        html += f"    <td style='text-align: left;'>{row['数据类型']}</td>\n"
        html += '  </tr>\n'

        html += '  <tr>\n'
        html += f"    <td style='text-align: left;'>Backbone</td>\n"
        html += f"    <td style='text-align: left;'>{row['Backbone']}</td>\n"
        html += '  </tr>\n'
        
        html += '  <tr>\n'
        html += f"    <td style='text-align: left;'>Backbone 1</td>\n"
        html += f"    <td style='text-align: left;'>{row['Backbone 1']}</td>\n"
        html += '  </tr>\n'
        
        html += '  <tr>\n'
        html += f"    <td style='text-align: left;'>下游任务</td>\n"
        html += f"    <td style='text-align: left;'>{row['下游任务']}</td>\n"
        html += '  </tr>\n'
        
        html += '  <tr>\n'
        html += f"    <td style='text-align: left;'>下游任务 1</td>\n"
        html += f"    <td style='text-align: left;'>{row['下游任务 1']}</td>\n"
        html += '  </tr>\n'

        html += '  <tr>\n'
        html += f"    <td style='text-align: left;'>Survey Inclusion</td>\n"
        html += f"    <td style='text-align: left;'>{row['Survey Inclusion']}</td>\n"
        html += '  </tr>\n'

        html += '  <tr>\n'
        html += f"    <td style='text-align: left;'>other</td>\n"
        html += f"    <td style='text-align: left;'>{row['other']}</td>\n"
        html += '  </tr>\n'
        html += '</table>'
    return html
def generate_html_table_dataset(df):
    html = ''
    for _, row in df.iterrows():
        html += '<table style="width:100%;">\n'
        html += '<tr>\n'
        html += '<td>数据集名称</td>\n'
        html += '<td>key</td>\n' 
        html += '<td>value</td>\n' 
        html += '<td>备注</td>\n'
        html += '</tr>\n'
        html += '  <tr>\n'
        html += f"    <td rowspan='9' style='text-align: left; width:10%;'>{row['数据集名称']}</td>\n"
        html += f"    <td style='text-align: left; width:10%;'>任务</td>\n"
        html += f"    <td style='text-align: left; width:20%;white-space: normal;'>{row['任务']}</td>\n"
        html += f"    <td rowspan='9' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>{row['备注']}</td>\n"
        html += '  </tr>\n'
        
        html += '  <tr>\n'
        html += f"    <td style='text-align: left;'>语言</td>\n"
        html += f"    <td style='text-align: left;white-space: normal;'>{row['语言']}</td>\n"
        html += '  </tr>\n'
        
        html += '  <tr>\n'
        html += f"    <td style='text-align: left;'>发布时间/Project</td>\n"
        html += f"    <td style='text-align: left;white-space: normal;'>{row['发布时间']}</td>\n"
        html += '  </tr>\n'
        
        html += '  <tr>\n'
        html += f"    <td style='text-align: left;'>模态</td>\n"
        html += f"    <td style='text-align: left;white-space: normal;'>{row['模态']}</td>\n"
        html += '  </tr>\n'
        
        html += '  <tr>\n'
        html += f"    <td style='text-align: left;'>训练阶段</td>\n"
        html += f"    <td style='text-align: left;white-space: normal;'>{row['训练阶段']}</td>\n"
        html += '  </tr>\n'

        html += '  <tr>\n'
        html += f"    <td style='text-align: left;'>规模</td>\n"
        html += f"    <td style='text-align: left;white-space: normal;'>{row['规模']}</td>\n"
        html += '  </tr>\n'
        
        html += '  <tr>\n'
        html += f"    <td style='text-align: left;'>数量</td>\n"
        html += f"    <td style='text-align: left;white-space: normal;'>{row['数量']}</td>\n"
        html += '  </tr>\n'
        
        html += '  <tr>\n'
        html += f"    <td style='text-align: left;'>涉及领域</td>\n"
        html += f"    <td style='text-align: left;white-space: normal;'>{row['涉及领域']}</td>\n"
        html += '  </tr>\n'

        html += '  <tr>\n'
        html += f"    <td style='text-align: left;'>链接</td>\n"
        html += f"    <td style='text-align: left;white-space: normal;'>{row['链接']}</td>\n"
        html += '  </tr>\n'
        html += '</table>'

    return html
def process_1(sheet_name='智能表1',filename='遥感大模型论文汇总-智能表1.md'):
    # 读取指定工作表
    df_sheet1 = pd.read_excel(file_path, sheet_name=sheet_name)


    df_sheet1['Paper'] = df_sheet1.apply(lambda row: f"<a href='{row['Link']}'>{row['Paper']}</a>", axis=1)


    df_sheet1.drop(columns=['Link'], inplace=True)
    html_table = generate_html_table_1(df_sheet1) 
    
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(html_table)
# html_file = '遥感大模型论文汇总.md'
# sheet_name='智能表2'
        
# process_1(sheet_name,html_file)

def process_2(sheet_name='智能表2',filename='遥感大模型论文汇总-智能表2.md'):
    # 读取指定工作表
    df_sheet1 = pd.read_excel(file_path, sheet_name=sheet_name)


    df_sheet1['Paper'] = df_sheet1.apply(lambda row: f"<a href='{row['Link']}'>{row['Paper']}</a>", axis=1)


    df_sheet1.drop(columns=['Link'], inplace=True)
    html_table = generate_html_table_2(df_sheet1) 
    
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(html_table)     
def process_3(sheet_name='智能表1',filename='大模型数据集.md'):
    # 读取指定工作表
    file_path = '大模型数据集.xlsx'
    df_sheet1 = pd.read_excel(file_path, sheet_name=sheet_name)

    df_sheet1['数据集名称'] = df_sheet1.apply(lambda row: f"<a href='{row['源链接']}'>{row['数据集名称']}</a>", axis=1)


    df_sheet1.drop(columns=['源链接'], inplace=True)
    html_table = generate_html_table_dataset(df_sheet1) 
    
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(html_table)     


        
process_1()
print("file has been created.")
