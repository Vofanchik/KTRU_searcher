import requests
from bs4 import BeautifulSoup
from pprint import pprint





class NkmiSearcher:
    def ros_zdrav_list_search(self, name_search, quantity_search=3):
        data = {
        'draw': '4',
        'order[0][column]': '0',
        'order[0][dir]': 'asc',
        'start': '0',
        'length': f'{quantity_search}',
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
        recs_total = res.json()['recordsTotal']
        res_ls_main_all = []
        res_ls_main_all.append(recs_total)
        for all in res_ls:
            res_ls_main = {}
            res_ls_main['id'] = all['col1']['label'].replace('o', '')
            res_ls_main['name_short'] = all['col5']['label'].replace('\r', '').replace('\n', ' ')
            if 'title' in all['col5']:
                res_ls_main['name_full'] = all['col5']['title']
            res_ls_main['ru'] = all['col2']['label']
            res_ls_main['owner'] = all['col9']['label']
            if 'label' in all['col15']:
                res_ls_main['nkmi'] = all['col15']['label']
            res_ls_main_all.append(res_ls_main)
            if 'title' in all['col10']:
                res_ls_main['prod_adress'] = all['col10']['title']
            else:
                res_ls_main['prod_adress'] = all['col10']['label']

        return res_ls_main_all

    def search_rzn_item(self, id):
        try:
            data = {'id': f'{id}',
                    'table_name': 'med_products',
                    'fancybox': 'true'}

            headers = {'Accept': '*/*',
                       'Accept-Encoding': 'gzip, deflate, br',
                       'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
                       'Connection': 'keep-alive',
                       'Cookie': '_ym_uid=163205177663442347; _ym_d=1632051776; uid=3230190944360843000; _ym_isad=2; _ym_visorc=w; sputnik_session=1644580559537|1',
                       'DNT': '1',
                       'Host': 'roszdravnadzor.gov.ru',
                       'If-Modified-Since': 'Fri, 11 Feb 2022 12:27:17 GMT',
                       'Referer': 'https://roszdravnadzor.gov.ru/',
                       'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
                       'sec-ch-ua-mobile': '?0',
                       'sec-ch-ua-platform': "Windows",
                       'Sec-Fetch-Dest': 'empty',
                       'Sec-Fetch-Mode': 'cors',
                       'Sec-Fetch-Site': 'same-origin',
                       'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36',
                       'X-Requested-With': 'XMLHttpRequest'}

            res = requests.post('https://roszdravnadzor.gov.ru/services/misearch', headers=headers, data=data)

            soup = BeautifulSoup(res.text, 'html.parser')
            unparsed = soup.find(string="Модели медицинского изделия").parent.next_sibling.next_sibling.find_all('td')
            table_nkmi = []
            for items in unparsed:
                table_nkmi.append(items.text.replace('\xa0', ''))

            lst1 = [i for i in table_nkmi[::2]]
            lst2 = [i for i in table_nkmi[1::2]]
            # dic = {x: y for x,y in zip(lst1, lst2)}
            ls_con = list(zip(lst1, lst2))

            return ls_con
            # TODO: добавить загрузку excel как у о64333
        except:
            return None

    def search_ktru_by_nkmi(self, name_search):
        try:
            headers = {'Accept': '*/*',
                       'Accept-Encoding': 'gzip, deflate, br',
                       'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
                       'Connection': 'keep-alive',
                       'DNT': '1',
                       'Host': 'zakupki.gov.ru',
                       'Referer': 'https://zakupki.gov.ru/epz/ktru/search/results.html',
                       'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
                       'sec-ch-ua-mobile': '?0',
                       'sec-ch-ua-platform': "Windows",
                       'Sec-Fetch-Dest': 'empty',
                       'Sec-Fetch-Mode': 'cors',
                       'Sec-Fetch-Site': 'same-origin',
                       'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36',
                       'X-Requested-With': 'XMLHttpRequest'}

            data = {'searchString': f'{name_search}',
                    'ktruClassifierId': '296',
                    'source': 'M',
                    'recordsPerPage': '_500',
                    'search': 'true',
                    'medicalProduct': 'false'}

            res = requests.post('https://zakupki.gov.ru/epz/ktru/ktruClassifiers/items.html', headers=headers, data=data)

            soup = BeautifulSoup(res.text, 'html.parser')

            name = soup.find(class_="ktruClassifiersItems").get_text().replace('\n', '')[7:].strip()

            return name

        except:
            return None

    def search_ktrus(self, ktru, quantity_items=5):
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
                              'Chrome/51.0.2704.103 Safari/537.36 '
            }
            payloads_ = {f'searchString': ktru,
                         'recordsPerPage': f'_{quantity_items}',
                         'morphology': 'on',
                         'search-filter': 'Наименованию позиции',
                         'active': 'on',
                         'sortBy': 'ITEM_CODE',
                         'sortDirection': 'true',
                         'showLotsInfoHidden': 'false',
                         'rubricatorIdSelected': '369'
                         }
            response = requests.get(
                f"https://zakupki.gov.ru/epz/ktru/search/results.html",
                params=payloads_, headers=headers)

            soup = BeautifulSoup(response.text, 'html.parser')

            ktrus = soup.find_all(class_='registry-entry__header-mid__number')
            ktrus = [i.get_text().replace('\n', '').strip() for i in ktrus]
            ktrus = ktrus[::2]

            ref_ktrus = soup.find_all(class_='registry-entry__header-mid__number')
            ref_ktrus = ['https://zakupki.gov.ru' + i.a.get('href') for i in ref_ktrus]
            ref_ktrus = ref_ktrus[::2]

            name_ktrus = soup.find_all(class_='d-flex registry-entry__header-mid__h4 align-items-center w-space-inherit text-break hyphenate')
            name_ktrus = [i.get_text().replace('\n', '').strip() for i in name_ktrus]

            searched_ktrus = list(zip(ktrus, name_ktrus, ref_ktrus))

            return searched_ktrus
        except:
            return None

# o = NkmiSearcher()
# pprint(o.search_ktrus('Фартук для защиты от излучения'))






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
# data = {'searchString': 'Фартук для защиты от излучения',
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
# print(soup.find_all(class_ = 'ktruClassifiersItems'))

# for all in soup.find_all(class_ = 'ktruClassifiersItems'):
#     print(all.text)
