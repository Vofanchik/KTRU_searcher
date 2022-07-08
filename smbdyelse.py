import requests
from bs4 import BeautifulSoup
from pprint import pprint

# data = {'id': '6231',
#         'table_name': 'med_products',
#         'fancybox': 'true'}
#
# headers = {'Accept': '*/*',
# 'Accept-Encoding': 'gzip, deflate, br',
# 'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
# 'Connection': 'keep-alive',
# 'Cookie': '_ym_uid=163205177663442347; _ym_d=1632051776; uid=3230190944360843000; _ym_isad=2; _ym_visorc=w; sputnik_session=1644580559537|1',
# 'DNT': '1',
# 'Host': 'roszdravnadzor.gov.ru',
# 'If-Modified-Since': 'Fri, 11 Feb 2022 12:27:17 GMT',
# 'Referer': 'https://roszdravnadzor.gov.ru/',
# 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
# 'sec-ch-ua-mobile': '?0',
# 'sec-ch-ua-platform': "Windows",
# 'Sec-Fetch-Dest': 'empty',
# 'Sec-Fetch-Mode': 'cors',
# 'Sec-Fetch-Site': 'same-origin',
# 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36',
# 'X-Requested-With': 'XMLHttpRequest'}
#
# res = requests.post('https://roszdravnadzor.gov.ru/services/misearch', headers=headers, data=data)
# print(res.text)
class NkmiSearcher:
    def ros_zdrav_list_search(self, name_search):
        data = {
        'draw': '4',
        'order[0][column]': '0',
        'order[0][dir]': 'asc',
        'start': '0',
        'length': '25',
        'search[regex]': 'false',
        'prev_total': '5',
        'q_mi_label_application': f'{name_search}',
        }

        headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Content-Length': '4171',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'DNT': '1',
        'Host': 'roszdravnadzor.gov.ru',
        'Origin': 'https://roszdravnadzor.gov.ru',
        'Referer': 'https://roszdravnadzor.gov.ru/',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': "Windows",
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
        }

        res = requests.post('https://roszdravnadzor.gov.ru/ajax/services/misearch', headers=headers, data=data)
        res_ls = res.json()['data']
        res_ls_main_all = []
        for all in res_ls:
            res_ls_main = {}
            res_ls_main['id'] = all['col1']['label'].replace('o', '')
            # res_ls_main['name']
            res_ls_main_all.append(res_ls_main)

        return res_ls

o = NkmiSearcher()
pprint(o.ros_zdrav_list_search('перчатки'))


# for all in res.json()['data']:
#     # print(all)
#     print(all['col1']['label'].replace('o', ''))
#
#
# headers = {'Accept': '*/*',
#              'Accept-Encoding': 'gzip, deflate, br',
#              'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
#              'Connection': 'keep-alive',
#              'DNT': '1',
#              'Host': 'zakupki.gov.ru',
#              'Referer': 'https://zakupki.gov.ru/epz/ktru/search/results.html',
#              'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
#              'sec-ch-ua-mobile': '?0',
#              'sec-ch-ua-platform': "Windows",
#              'Sec-Fetch-Dest': 'empty',
#              'Sec-Fetch-Mode': 'cors',
#              'Sec-Fetch-Site': 'same-origin',
#              'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36',
#              'X-Requested-With': 'XMLHttpRequest'}
#
# data = {'searchString': '122570',
#          'ktruClassifierId': '296',
#          'source': 'M',
#          'recordsPerPage': '_500',
#          'search': 'true',
#          'medicalProduct': 'false'}
#
# res = requests.post('https://zakupki.gov.ru/epz/ktru/ktruClassifiers/items.html', headers=headers, data=data)
#
# soup = BeautifulSoup(res.text, 'html.parser')
#
# name = soup.find(class_="ktruClassifiersItems")
#
# print(name.get_text().replace('\n', '')[7:])


# headers = {
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,'
#               'application/signed-exchange;v=b3;q=0.9',
#     'Accept-Encoding': 'gzip, deflate, br',
#     'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
#     'Connection': 'keep-alive',
#     'Cookie': '_ym_uid=1630900769777928721; _ym_d=1630900769; '
#               'contractCsvSettingsId=9feab4cb-ade1-4b6f-84ba-19b7b87faacd; _ym_isad=2; contentFilter=; _ym_visorc=b',
#     'DNT': '1',
#     'Host': 'zakupki.gov.ru',
#     'Referer': 'https://zakupki.gov.ru/epz/ktru/search/results.html',
#     'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': 'Windows',
#     'Sec-Fetch-Dest': 'document',
#     'Sec-Fetch-Mode': 'navigate',
#     'Sec-Fetch-Site': 'same-origin',
#     'Sec-Fetch-User': '?1',
#     'Upgrade-Insecure-Requests': '1',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
#                   'Chrome/98.0.4758.82 Safari/537.36'}
#
# data = {'searchString': 'перчатки',
#         'morphology': 'on',
#         'search-filter': 'Наименованию позиции',
#         'active': 'on',
#         'ktruCharselectedTemplateItem': '0',
#         'sortBy': 'ITEM_NAME',
#         'pageNumber': '1',
#         'sortDirection': 'false',
#         'recordsPerPage': '_10',
#         'showLotsInfoHidden': 'false',
#         'rubricatorIdSelected': '369'}
#
# res = requests.post('https://zakupki.gov.ru/epz/ktru/ktruClassifiers/items.html', headers=headers, data=data)
# # soup = BeautifulSoup(res.text, 'html.parser')
# pprint(res.text)
# # print(soup.find_all(class_ = 'ktruClassifiersItems'))
#
# # for all in soup.find_all(class_ = 'ktruClassifiersItems'):
# #     print(all.text)
