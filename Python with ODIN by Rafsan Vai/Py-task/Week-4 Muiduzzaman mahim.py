import csv
import requests

def evaly(url):
    response = requests.get(url)
    recieved_data = []
    if response.status_code == 200:
        contents = response.json()
        evaly_data_file = "evaly_data_file.csv"
        with open(evaly_data_file, 'w') as evaly_data_file:
            csvfile = csv.writer(evaly_data_file)
            for content in contents['data']:
                data = []
                if content['shop_name'] == 'বই বাজার':
                    content['shop_name'] = 'Book bazar'
                    data.append(content['store_name'])
                else:
                    data.append(content['store_name'])
                data.append(content['contact'])
                data.append(content['store_owner_name'])
                data.append(content['store_owner_number'])
                recieved_data.append(data)
                csvfile.writerows(recieved_data)

    else:
        print('{} Error'.format(response.status_code))


def employee(url):
    recieved_data = []
    response = requests.get(url)
    if response.status_code == 200:
        contents = response.json()

        filename = "evaly_employee_file.csv"
        with open(filename, 'w') as evaly_data_file:
            csvfile = csv.writer(evaly_data_file)
            for employees in contents['data']:
                data = []
                data.append(employees['Name'])
                data.append(employees['Salary'])
                data.append(employees['Age'])
                recieved_data.append(data)
                csvfile.writerows(recieved_data)

    else:
        print('{} Error'.format(response.status_code))


urls = ['https://api.evaly.com.bd/core/custom/shops/?page=1&limit=7',
        'http://dummy.restapiexample.com/api/v1/employees']

evaly(urls[0])
employee(urls[1])
