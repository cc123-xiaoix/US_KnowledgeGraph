"""
  @author Jay Liu
  @create_time 2021/10/26 18:27
  @email 1299870737@qq.com
"""

import mwclient
import csv
import time
import re 

# ！！！不要直接用！！！参数改成你自己的
# 第一个参数是IP地址，path参数是wiki的文件夹名，看看/var/www/html/下面wiki名字是啥
#site = mwclient.Site("47.117.143.163/", scheme='http', path='mediawiki/')

# 如果是本地安装的mediawiki的话，用下面这行
site = mwclient.Site("localhost:8080/", scheme='http', path='mediawiki/')

# 在wiki上创建Bot用户，更改到Bot用户组下面
site.login("Jzc1986914548@Bot", "qsrfe9u6mhvut7e2qoi051dn2n38ngrq")

if __name__ == '__main__':
    origin_list = []
    # year_list = [2021]#,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021]
    # for year in year_list:
    #   # with open(f'./NIH_{year}/data_{year}.csv', 'r', encoding='utf-8') as csv_file:
    #   with open(f'C:/数据/NIH_{year}/data_{year}_PM.csv', 'r', encoding='utf-8', errors='ignore') as csv_file:
    #       csv_reader = csv.reader(csv_file)
    #       origin_header = next(csv_reader)
    #       for row in csv_reader:
    #           origin_list.append(row)
    with open(f'C:/数据/科研论文.csv', 'r', encoding='utf-8') as csv_file:  
      csv_reader = csv.reader(csv_file)
      origin_header = next(csv_reader)
      for row in csv_reader:
          origin_list.append(row)
    for item in origin_list:
        #page = site.pages['期刊论文/{}'.format(item[13])]
        title_len = len('期刊论文/{}'.format(item[13]).encode('utf-8'))
        if title_len <= 255:
            #page = site.pages['期刊论文/{}'.format(item[13]).replace("[", "").replace("]", "")]
            page_title = re.sub(r'[^a-zA-Z0-9]', ' ', item[13]) 
            page = site.pages['期刊论文/{}'.format(page_title)]
        else:
            continue
        template1 = '{{div|row}}\n' \
                    '{{div|col-md-9}}\n' 
        template2 = f'{{科研论文简介\n' \
                    f'|PubTitle={item[13]}\n' \
                    f'|PMID={item[11]}\n' \
                    f'|Affiliation={item[0]}\n' \
                    f'|Country={item[2]}\n}}'
        template3 = '==知识图谱==\n' 
        template4 = f'{{#network:\n' \
                    f'| options=\n' \
                      f'{{\n"autoResize": true,\n' \
                      f'"nodes": {{\n' \
                      f'"color": "#f8f8f8",\n' \
                      f'"shape": "box",\n' \
                      f'"borderWidth": 1,\n' \
                      f'"font": {{ "color": "#1b599b", "size": 17 }}\n' \
                      f'}}\n' \
                    f'}}\n' \
                    f'}}'
        template5 = '==期刊论文编码==\n'
        template6 = f'{{编码\n' \
                    f'|Code=PMID\n' \
                    f'|Code_value={item[11]}\n}}'
        template7 = f'{{编码\n' \
                    f'|Code=PMCID\n' \
                    f'|Code_value={item[10]}\n}}'
        template8 = f'{{编码\n' \
                    f'|Code=ISSN\n' \
                    f'|Code_value={item[3]}\n}}'
        template9 = '==期刊论文发表==\n'
        template10 = f'{{编码\n' \
                    f'|Code=Language\n' \
                    f'|Code_value={item[8]}\n}}'
        template11 = f'{{编码\n' \
                    f'|Code=PageNumber\n' \
                    f'|Code_value={item[9]}\n}}'
        template12 = f'{{编码\n' \
                    f'|Code=Country\n' \
                    f'|Code_value={item[2]}\n}}'
        template13 = f'{{编码\n' \
                    f'|Code=PubYear\n' \
                    f'|Code_value={item[14]}\n}}'
        template14 = f'{{编码\n' \
                    f'|Code=PubDate\n' \
                    f'|Code_value={item[12]}\n}}'
        template15 = '==期刊==\n'
        template16 = f'{{编码\n' \
                    f'|Code=JournalTitle\n' \
                    f'|Code_value={item[5]}\n}}'
        template17 = f'{{编码\n' \
                    f'|Code=JournalIssue\n' \
                    f'|Code_value={item[4]}\n}}'
        template18 = f'{{编码\n' \
                    f'|Code=JournalVolume\n' \
                    f'|Code_value={item[7]}\n}}'            
        template19 = f'{{科研论文期刊附加\n' \
                    f'|附加文本={item[6]}\n}}' 
        template20 = '{{div ' \
                    'end}}\n\n' 

        template21 = '{{div|col-md-3 sidebar-sticky|padding: 10px 30px}}\n' 
        template22 = f'{{科研论文基本信息\n' \
                    f'|PubTitle={item[13]}\n' \
                    f'|Country={item[2]}\n' \
                    f'|PubDate={item[12]}\n' \
                    f'|PubYear={item[14]}\n' \
                    f'|Language={item[8]}\n' \
                    f'|JournalTitle={item[5]}\n' \
                    f'|JounalTitleAbbr={item[6]}\n' \
                    f'|JournalIssue={item[4]}\n' \
                    f'|JournalVolume={item[7]}\n' \
                    f'|PageNumber={item[9]}\n' \
                    f'|PMID={item[11]}\n' \
                    f'|PMCID={item[10]}\n' \
                    f'|ISSN={item[3]}\n' \
                    f'|Author={item[1]}\n}}'
        template23 = '{{div ' \
                    'end}}\n' \
                    '{{div ' \
                    'end}}\n' \
                    '{{院士页面样式'\
                    '}}'
        #template7 = '[[Category:科研人员]]'
        template2 = '{' + template2 + '}\n'
        template4 = '{' + template4 + '}\n'
        template6 = '{' + template6 + '}\n'
        template7 = '{' + template7 + '}\n'
        template8 = '{' + template8 + '}\n'
        template10 = '{' + template10 + '}\n'
        template11 = '{' + template11 + '}\n'
        template12 = '{' + template12 + '}\n'
        template13 = '{' + template13 + '}\n'
        template14 = '{' + template14 + '}\n'
        template16 = '{' + template16 + '}\n'
        template17 = '{' + template17 + '}\n'
        template18 = '{' + template18 + '}\n'
        template19 = '{' + template19 + '}\n'
        template22 = '{' + template22 + '}\n'
        page.edit(template1+template2+template3+template4+template5+template6+template7+template8+template9+template10+template11+template12+template13+template14+template15+template16+template17+template18+template19+template20+template21+template22+template23)

        print('已添加{}科研论文数据'.format(page_title))
        # 这里可以调整循环的间歇时间
        #time.sleep(1)
