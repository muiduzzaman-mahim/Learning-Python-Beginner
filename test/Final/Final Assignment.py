import requests
import csv

def ID():

    url = "https://www.scaleupinstitute.org.uk/getCompanies.php?offset=0&min_turnover=0&max_turnover=0&min_employees=&max_employees=&min_growth=&max_growth="
    response = requests.get(url)
    data = response.json()

    serial_number  = []

    for idno in data:
        Serail_Number = idno["Serail_Number"]
        serial_number.append(Serail_Number)

    return serial_number

def comp_details(id):
    Details = []
    count = 0
    for comp_id in id:
        url = "https://www.scaleupinstitute.org.uk/getCompany.php?id={}".format(comp_id)
        response = requests.get(url)
        data = response.json()

        for detail in data:
            details = {
            'Name' : detail["name"],
            'Address' : detail["address1"] +' '+detail["address2"]+' '+detail["address3"]+' '+detail["address4"],
            'Phone' : detail["telephone"],
            'Website' : detail["website"]
            }
            Details.append(details)
            return Details

all_data = comp_details(ID()[0:7000])

csv = ['Name', 'Address', 'Phone','Website']

with open("data.csv", 'w') as csvfile:
    writer = csv.DictWriter(csvfile,fieldnames=csv)
    writer.writeheader()
    for data in all_data:
        writer.writerow(data)