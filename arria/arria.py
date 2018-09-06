#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 10:46:11 2018

@author: phil
"""

import requests
import pandas as pd


def arria(access_token, user_id, message_data):
    headers = {
        'Content-Type': 'application/json;charset=UTF-8',
    }
    params = {
        'access_token': 'Bearer ',
    }
    payload = {
        'recipient': {
            'id': user_id,
        },
        'message': message_data,
    }
        
    url = 'https://graph.facebook.com/v2.6/me/messages'
    response = requests.post(url, 
                             headers=headers, 
                             params=params,
                             data=json.dumps(payload)
                             )
    
    response.raise_for_status()
    return response.json() 


'''
{
  "data": [
    {
      "id": "Primary",
      "type": "2d",
      "dataSet": [
        ["State", "Premier", "Party", "Terms", "StateLandArea", "StatePop2010", "StatePop2016", "Capital", "CapitalPop2010", "CapitalPop2016"],
        ["New South Wales", "Mike Baird", "Liberal", "1", "800,641", "7,238,800", "7,618,200", "Sydney", "4,183,471", "4,526,479"],
        ["Victoria",  "Daniel Andrews", "ALP",  "1", "227,416",  "5,547,500", "5,938,100",  "Melbourne",  "3,953,939", "4,353,514"],
        ["Queensland", "Annastacia Palaszczuk", "ALP", "1", "1,730,647", "4,516,400", "4,779,400", "Brisbane", "2,019,074", "2,209,453"],
        ["Western Australia", "Colin Barnett", "Liberal", "2", "2,529,875", "2,296,400", "2,591,600", "Perth", "1,723,218", "1,958,912"],
        ["South Australia", "Jay Weatherill", "ALP", "2", "983,482", "1,644,600", "1,698,600", "Adelaide", "1,225,668", "1,288,681"],
        ["Tasmania", "Will Hodgman", "Liberal", "1", "68,401", "507,600", "516,600", "Hobart", "203,446", "209,254"],
        ["the Australian Capital Territory", "Andrew Barr", "ALP", "1", "2,358", "358,900", "390,800", "Canberra", "398,430", "424,666"],
        ["the Northern Territory", "Michael Gunner", "ALP", "1", "1,349,129", "229,700", "244,600", "Darwin", "112,987", "123,396"]
      ]
    }
  ],
  "options": {
    "nullValueBehaviour": "SHOW_IDENTIFIER"
  }
}
'''



if __name__ == '__main__':
    df = pd.read_excel("../data.xlsx", sheetname='Actual vs RSBPL')[:-1]
    
