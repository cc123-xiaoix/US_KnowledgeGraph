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
    # year_list = [2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021]
    # for year in year_list:
    #   # with open(f'./NIH_{year}/data_{year}.csv', 'r', encoding='utf-8') as csv_file:
    #   with open(f'C:/数据/NIH_{year}/data_{year}_PI.csv', 'r', encoding='utf-8') as csv_file:
    #       csv_reader = csv.reader(csv_file)
    #       origin_header = next(csv_reader)
    #       for row in csv_reader:
    #           origin_list.append(row)
    with open(f'C:/数据/科研人员.csv', 'r', encoding='utf-8') as csv_file:  
      csv_reader = csv.reader(csv_file)
      origin_header = next(csv_reader)
      for row in csv_reader:
          origin_list.append(row)
    for item in origin_list:
        #page = site.pages['NIH科研人员/{}'.format(item[2])]
        title_len = len('科研人员/{}'.format(item[2]).encode('utf-8'))
        if title_len <= 255:
            #page = site.pages['期刊论文/{}'.format(item[13]).replace("[", "").replace("]", "")]
            page_title = re.sub(r'[^a-zA-Z0-9]', ' ', item[2]) 
            page = site.pages['科研人员/{}'.format(page_title)]
        else:
            continue
        template1 = '{{div|row}}\n' \
                    '{{div|col-md-9}}\n' 
        template2 = f'{{科研人员个人简介\n' \
                    f'|ADMINISTERINGIC={item[0]}\n' \
                    f'|PIIDS={item[1]}\n' \
                    f'|PINAMEs={item[2]}\n}}' 
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
        template5 = '==科研人员编码==\n'
        template6 = f'{{编码\n' \
                    f'|Code=PIIDS\n' \
                    f'|Code_value={item[1]}\n}}'
        template7 = '{{div ' \
                    'end}}\n\n' 
        
        
        template8 = '{{div|col-md-3 sidebar-sticky|padding: 10px 30px}}\n' 
        template9 = f'{{科研人员基本信息\n' \
                    f'|ADMINISTERINGIC={item[0]}\n' \
                    f'|PIIDS={item[1]}\n' \
                    f'|PINAMEs={item[2]}\n}}'
        template10 = '{{div ' \
                    'end}}\n' \
                    '{{div ' \
                    'end}}\n' \
                    '{{院士页面样式'\
                    '}}'
        #template7 = '[[Category:科研人员]]'
        template2 = '{' + template2 + '}\n'
        template4 = '{' + template4 + '}\n'
        template6 = '{' + template6 + '}\n'
        template9 = '{' + template9 + '}\n'
        page.edit(template1+template2+template3+template4+template5+template6+template7+template8+template9+template10)

        print('已添加{}科研人员数据'.format(item[2]))
        # 这里可以调整循环的间歇时间
        #time.sleep(1)
