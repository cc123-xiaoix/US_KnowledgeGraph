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
    #2018年数据分成两份处理，其余年份单独处理
    # year_list = [2010]#,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021]
    # #将CSV文件中单行数据长度的最大限制设置为1GB
    # csv.field_size_limit(100 * 1024 * 1024)
    # for year in year_list:
    #   # with open(f'./NIH_{year}/data_{year}.csv', 'r', encoding='utf-8') as csv_file:
    #     with open(f'C:/数据/NIH_{year}/data_{year}_PRO.csv', 'r', encoding='utf-8') as csv_file:
    #         csv_reader = csv.reader(csv_file)
    #         origin_header = next(csv_reader)
    #         for row in csv_reader:
    #             origin_list.append(row)
    with open(f'C:/数据/科研项目.csv', 'r', encoding='utf-8') as csv_file:  
      csv_reader = csv.reader(csv_file)
      origin_header = next(csv_reader)
      for row in csv_reader:
          origin_list.append(row)
    for item in origin_list:
        #page = site.pages['NIH科研项目/{}'.format(item[11])]
        title_len = len('美国NIH科研项目/{}'.format(item[11]).encode('utf-8'))
        if title_len <= 255:
            #page = site.pages['期刊论文/{}'.format(item[13]).replace("[", "").replace("]", "")]
            page_title = re.sub(r'[^a-zA-Z0-9]', ' ', item[11]) 
            page = site.pages['美国NIH科研项目/{}'.format(page_title)]
        else:
            continue
        template1 = '{{div|row}}\n' \
                    '{{div|col-md-9}}\n' 
        template2 = f'{{科研项目简介\n' \
                    f'|ProjectTitle={item[11]}\n' \
                    f'|AbstractText={item[0]}\n' \
                    f'|ApplicationID={item[1]}\n' \
                    f'|ProjectTerms={item[10]}\n}}'
        template3 = f'{{PHR\n' \
                    f'|评价文本={item[25]}\n}}'
        template4 = '==知识图谱==\n' 
        template5 = f'{{#network:\n' \
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
        template6 = '==科研项目编码==\n'
        template7 = f'{{编码\n' \
                    f'|Code=ApplicationID\n' \
                    f'|Code_value={item[1]}\n}}'
        template8 = f'{{编码\n' \
                    f'|Code=CoreProjectNum\n' \
                    f'|Code_value={item[4]}\n}}'
        template9 = f'{{编码\n' \
                    f'|Code=FullProjectNum\n' \
                    f'|Code_value={item[5]}\n}}'
        template10 = f'{{编码\n' \
                    f'|Code=CFDACode\n' \
                    f'|Code_value={item[21]}\n}}'
        template11 = f'{{编码\n' \
                    f'|Code=FOANumber\n' \
                    f'|Code_value={item[22]}\n}}'
        template12 = f'{{编码\n' \
                    f'|Code=SubProjectID\n' \
                    f'|Code_value={item[17]}\n}}'
        template13 = f'{{编码\n' \
                    f'|Code=FundingMechanism\n' \
                    f'|Code_value={item[6]}\n}}'
        
        template14 = '==科研项目==\n'
        template15 = f'{{编码\n' \
                    f'|Code=ProjectOfficerName\n' \
                    f'|Code_value={item[7]}\n}}'
        template16 = f'{{编码\n' \
                    f'|Code=StudySection\n' \
                    f'|Code_value={item[12]}\n}}'
        template17 = f'{{编码\n' \
                    f'|Code=StudySectionName\n' \
                    f'|Code_value={item[13]}\n}}'
        template18 = f'{{编码\n' \
                    f'|Code=NIHSpendingCats\n' \
                    f'|Code_value={item[18]}\n}}'
        template19 = f'{{编码\n' \
                    f'|Code=ApplicationType\n' \
                    f'|Code_value={item[19]}\n}}'

        template20 = '==科研项目花销==\n'
        template21 = f'{{科研项目花销\n' \
                    f'|名字=Budget\n' \
                    f'|开始时间={item[2]}\n' \
                    f'|结束时间={item[3]}\n}}'
        template22 = f'{{科研项目花销\n' \
                    f'|名字=Project\n' \
                    f'|开始时间={item[8]}\n' \
                    f'|结束时间={item[9]}\n}}'
        template23 = f'{{编码\n' \
                    f'|Code=TotalCost\n' \
                    f'|Code_value={item[15]}\n}}'
        template24 = f'{{编码\n' \
                    f'|Code=TotalCostSubProject\n' \
                    f'|Code_value={item[16]}\n}}'

        template25 = '==资助信息==\n'
        template26 = f'{{编码\n' \
                    f'|Code=AwardNoticeDate\n' \
                    f'|Code_value={item[20]}\n}}'
        template27 = f'{{编码\n' \
                    f'|Code=FundingICs\n' \
                    f'|Code_value={item[23]}\n}}'
        template28 = f'{{编码\n' \
                    f'|Code=ICName\n' \
                    f'|Code_value={item[24]}\n}}'
        template29 = f'{{编码\n' \
                    f'|Code=SupportYear\n' \
                    f'|Code_value={item[14]}\n}}'
        template30 = f'{{编码\n' \
                    f'|Code=Fy\n' \
                    f'|Code_value={item[29]}\n}}'

        template31 = '{{div ' \
                    'end}}\n\n' 
        
        template32 = '{{div|col-md-3 sidebar-sticky|padding: 10px 30px}}\n' 
        template33 = f'{{科研项目基本信息\n' \
                    f'|ApplicationID={item[1]}\n' \
                    f'|BudgetStart={item[2]}\n' \
                    f'|BudgetEnd={item[3]}\n' \
                    f'|CoreProjectNum={item[4]}\n' \
                    f'|FullProjectNum={item[5]}\n' \
                    f'|SubProjectID={item[17]}\n' \
                    f'|NIHSpendingCats={item[18]}\n' \
                    f'|ApplicationType={item[19]}\n' \
                    f'|StudySection={item[12]}\n' \
                    f'|StudySectionName={item[13]}\n' \
                    f'|ProjectOfficerName={item[7]}\n' \
                    f'|ProjectStart={item[8]}\n' \
                    f'|ProjectEnd={item[9]}\n' \
                    f'|ProjectTerms={item[10]}\n' \
                    f'|ProjectTitle={item[11]}\n' \
                    f'|SupportYear={item[14]}\n' \
                    f'|TotalCost={item[15]}\n' \
                    f'|TotalCostSubProject={item[16]}\n' \
                    f'|AwardNoticeDate={item[20]}\n' \
                    f'|CFDACode={item[21]}\n' \
                    f'|FOANumber={item[22]}\n' \
                    f'|FundingICs={item[23]}\n' \
                    f'|ICName={item[24]}\n' \
                    f'|FundingMechanism={item[6]}' \
                    f'|Fy={item[29]}\n' \
                    f'|PHR={item[25]}\n' \
                    f'|OrgName={item[26]}\n' \
                    f'|PINames={item[27]}\n' \
                    f'|PubTitle={item[28]}\n}}'
        template34 = '{{div ' \
                    'end}}\n' \
                    '{{div ' \
                    'end}}\n' \
                    '{{院士页面样式'\
                    '}}'
        #template7 = '[[Category:科研人员]]'
        template2 = '{' + template2 + '}\n'
        template3 = '{' + template3 + '}\n'
        template5 = '{' + template5 + '}\n'
        template7 = '{' + template7 + '}\n'
        template8 = '{' + template8 + '}\n'
        template9 = '{' + template9 + '}\n'
        template10 = '{' + template10 + '}\n'
        template11 = '{' + template11 + '}\n'
        template12 = '{' + template12 + '}\n'
        template13 = '{' + template13 + '}\n'
        template15 = '{' + template15 + '}\n'
        template16 = '{' + template16 + '}\n'
        template17 = '{' + template17 + '}\n'
        template18 = '{' + template18 + '}\n'
        template19 = '{' + template19 + '}\n'
        template21 = '{' + template21 + '}\n'
        template22 = '{' + template22 + '}\n'
        template23 = '{' + template23 + '}\n'
        template24 = '{' + template24 + '}\n'
        template26 = '{' + template26 + '}\n'
        template27 = '{' + template27 + '}\n'
        template28 = '{' + template28 + '}\n'
        template29 = '{' + template29 + '}\n'
        template30 = '{' + template30 + '}\n'
        template33 = '{' + template33 + '}\n'
        page.edit(template1+template2+template3+template4+template5+template6+template7+template8+template9+template10+template11+template12+template13+template14+template15+template16+template17+template18+template19+template20+template21+template22+template23+template24+template25+template26+template27+template28+template29+template30+template31+template32+template33+template34)

        print('已添加{}科研项目数据'.format(item[11]))
        # 这里可以调整循环的间歇时间
        #time.sleep(1)
