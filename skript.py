# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 09:47:56 2022

@author: sklad_2
"""

# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re

selection = re.compile(r'(\+7|8){1}\s*\(?(\d{3})\)?(\s*|-*)*(\d{3})(\s*|-*)*(\d{2})(\s*|-*)*'
                     r'(\d{2})(\s*\(*(доб.)(\s)*(\d+))?\)*')

with open("phonebook_raw.csv", encoding='utf8') as f:
    rows = csv.reader(f, delimiter=',')
    contacts_list = list(rows)


def check_name(last_name, first_name, list_items):
    for item in list_items:
        if item[0] == last_name and item[1] == first_name:
            return list_items.index(item)


def pretty_phone(phone, pattern):
    return re.sub(selection, r'+7(\2)\4-\6-\8\11\10\12', phone)


def contacts():
    new_contacts = [contacts_list[0]]
    contacts_list.pop(0)
    for contact in contacts_list:
        full_name = ' '.join(contact[0:3])
        listfull_name = full_name.split(' ')
        checked_name = check_name(listfull_name[0], listfull_name[1], new_contacts)
        pretty_number = pretty_phone(contact[5], selection)
        new_contact = [listfull_name[0],
                       listfull_name[1],
                       listfull_name[2],
                       contact[3],
                       contact[4],
                       pretty_number,
                       contact[6]]
        if checked_name is None:
            new_contacts.append(new_contact)
        else:
            i = 0
            while i < len(new_contacts[checked_name]):
                if new_contacts[checked_name][i] == '':
                    new_contacts[checked_name][i] = new_contact[i]
                i += 1
    return new_contacts


with open("phonebook.csv", "w", encoding='utf8', newline='') as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(contacts())