# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 23:20:54 2022

@author: Mykola
"""

import pandas as pd
import psycopg2
from sqlalchemy import create_engine

engine = create_engine('mysql://root:@localhost:3306/rent_app', echo=False)

df = pd.read_csv('Rent_booking.csv', index_col=False, header=0)
print(df)


# df['dt'] = df['t1'] + ' ' + df['t2']
df['booking_date'] = pd.to_datetime(df['booking_date'], format='%d/%m/%Y')


df.to_sql('blog_bookings', con=engine,  if_exists='append', index=False)