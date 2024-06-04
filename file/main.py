import pandas as pd
import markdown
import argparse
from markdownify import markdownify as md


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
def generate_html_table_dataset(df,sheet_name):
    html = f'## {sheet_name}\n'
    for _, row in df.iterrows():
        html += '<table style="width:100%;">\n'
        html += '<tr>\n'
        html += '<td>数据集名称</td>\n'
        html += '<td>key</td>\n' 
        html += '<td>value</td>\n' 
        html += '<td>备注</td>\n'
        html += '</tr>\n'
        html += '  <tr>\n'
        html += f"    <td rowspan='6' style='text-align: left; width:10%;'>{row['数据集名称']}</td>\n"
        html += f"    <td style='text-align: left; width:10%;'>任务</td>\n"
        html += f"    <td style='text-align: left; width:20%;white-space: normal;'>{row['任务']}</td>\n"
        html += f"    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>{row['备注']}</td>\n"
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
        html += f"    <td style='text-align: left;'>数量</td>\n"
        html += f"    <td style='text-align: left;white-space: normal;'>{row['数量']}</td>\n"
        html += '  </tr>\n'
        


        html += '  <tr>\n'
        html += f"    <td style='text-align: left;'>链接</td>\n"
        html += f"    <td style='text-align: left;white-space: normal;'>{row['链接']}</td>\n"
        html += '  </tr>\n'
        html += '</table>\n\n'

    return html

def process(file_path,sheet_name,name,link):
    # 读取指定工作表
    
    df_sheet1 = pd.read_excel(file_path, sheet_name=sheet_name)

    df_sheet1[name] = df_sheet1.apply(lambda row: f"<a href='{row[link]}'>{row[name]}</a>", axis=1)
    df_sheet1.drop(columns=[link], inplace=True)
    html_table = generate_html_table_dataset(df_sheet1,sheet_name) 
   
    return html_table


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--file_path', type=str, default = '大模型数据集-类别.xlsx')
    parser.add_argument('--sheet_name', type=str, default='智能表1')
    parser.add_argument('--one_sheet', type=bool, default=False)
    parser.add_argument('--filename', type=str, default='大模型数据集.md')
    parser.add_argument('--name', type=str, default='数据集名称')
    parser.add_argument('--link', type=str, default='源链接')
    args = parser.parse_args()
    file_path = args.file_path
    excel_data = pd.ExcelFile(file_path)
    sheet_names = excel_data.sheet_names
    print(sheet_names)
    sheet_name = args.sheet_name
    filename = args.filename
    name = args.name  
    link = args.link
    all_html_table = ''

    if args.one_sheet:
        all_html_table += process(file_path,sheet_name,filename,name,link)
    else:
        for sheet_name in sheet_names:
            all_html_table += process(file_path,sheet_name,name,link)

    with open(filename, 'w', encoding='utf-8') as file:
        file.write(all_html_table)     

    print("file has been created.")
