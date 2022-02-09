import csv
import requests


def Evale_shop(url):
    response = requests.get(url)
    allData = []
    if response.status_code == 200:
        contents = response.json()
        file = "evaly.csv"
        with open(file, 'w') as file:
            csvfile = csv.writer(file)
            for content in contents['data']:
                data = []
                if content['shop_name'] == 'বই বাজার':
                    content['shop_name'] = 'Book bazar'
                    data.append(content['shop_name'])
                    
                else:
                    data.append(content['shop_name'])
                data.append(content['contact_number'])
                data.append(content['owner_name'])
                data.append(content['owner_number'])
                allData.append(data)
                csvfile.writerows(allData)

    else:
        print('{} connection fail'.format(response.status_code))


def Employees_info(url):
    allData = []
    response = requests.get(url)
    if response.status_code == 200:
        contents = response.json()

        filename = "employees.csv"
        with open(filename, 'w') as file:
            csvfile = csv.writer(file)
            for employees in contents['data']:
                data = []
                data.append(employees['employee_name'])
                data.append(employees['employee_salary'])
                data.append(employees['employee_age'])
                allData.append(data)
                csvfile.writerows(allData)

    else:
        print('{} connection fail'.format(response.status_code))


urls = ['https://api.evaly.com.bd/core/custom/shops/?page=1&limit=7',
        'http://dummy.restapiexample.com/api/v1/employees']

Evale_shop(urls[0])
Employees_info(urls[1])
