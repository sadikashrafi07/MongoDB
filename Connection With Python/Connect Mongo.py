#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 19:50:28 2024

@author: angadi mohammad sadiq
"""

import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017')

mydb = client['Employee']

information = mydb.employeeinformation

record = [
    {
        'firstname': 'Angadi',
        'Middlename': 'Mohammad',
        'Lastname': 'Sadiq',
        'Department': 'CSE(AI/ML)'
    },
    {
        'firstname': 'Danish',
        'Middlename': 'Shaikh',
        'Lastname': 'Irfan',
        'Department': 'CSE'
    },
    {
        'firstname': 'Kumar',
        'Middlename': 'Shivraj',
        'Lastname': 'Bhakat',
        'Department': 'Mech'
    }
]


information.insert_many(record)

