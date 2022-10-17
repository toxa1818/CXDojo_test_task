import csv
import os
import re
from pathlib import Path
from bs4 import BeautifulSoup
from django.contrib.auth import get_user_model

BASE_DIR = Path(__file__).resolve().parent.parent
MEDIA_PATH = os.path.join(BASE_DIR, "test_files")
CSV_PATH = os.path.join(BASE_DIR, "test_files", "test_task.csv")
XML_PATH = os.path.join(BASE_DIR, "test_files", "test_task.xml")


def get_info_from_files():
    """getting information from files and checking for validity"""
    csv_info = []
    xml_info = []
    regex = re.compile("^[a-zA-Zа-яА-Я.]+$")
    with open(CSV_PATH, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(' '.join(row).split()) == 3 and bool(regex.search(row[0])):
                csv_info.append({'username': row[0], 'password': row[1], 'date_joined': row[2]})

    with open(XML_PATH, 'r') as file:
        data = file.read()
        bs_data = BeautifulSoup(data, 'xml')
        for user in bs_data.select('users user'):
            user = [user.first_name.text, user.last_name.text]
            if len(' '.join(user).split()) == 2 and bool(regex.search(user[0]) and regex.search(user[1])):
                xml_info.append({'first_name': user[0], 'last_name': user[1]})

    valid_users = []
    for csv_user in csv_info[1:]:
        for xml_user in xml_info:
            if xml_user['last_name'].lower() in csv_user['username'].lower():
                xml_user.update(csv_user)
                valid_users.append(xml_user)
                xml_info.remove(xml_user)

    return valid_users


def update_db():
    for file in os.listdir(MEDIA_PATH):
        file_path = os.path.join(MEDIA_PATH, file)
        if os.path.isfile(file_path):
            os.remove(file_path)
    user = get_user_model()
    user.objects.filter(is_superuser=0).all().delete()
