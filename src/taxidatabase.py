#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 19:30:55 2022

@author: Nuno Santos

Taxi Booking System
"""

import sqlite3
from sqlite3 import Error

# functions to manage our database:
def create_connection(db_file):
    conn = None

    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    
    return conn

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

#This code creates passengers
def create_passenger(conn, passenger):
    sql = ''' INSERT INTO passengers(
                                    title,
                                    firstName,
                                    lastName,
                                    email,
                                    mobNumber,
                                    password,
                                    postcode,
                                    address,
                                    town,
                                    county,
                                    paymentMethod)
              VALUES(?,?,?,?,?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, passenger)
    conn.commit()
    return cur.lastrowid

#This code creates drivers
def create_driver(conn, driver):
    sql = ''' INSERT INTO drivers(
                                    title,
                                    firstName,
                                    lastName,
                                    email,
                                    mobNumber,
                                    password,
                                    regNum)
              VALUES(?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, driver)
    conn.commit()
    return cur.lastrowid

#This code creates bookings
def create_booking(conn, booking):
    sql = ''' INSERT INTO bookings(
                                    driverid,
                                    passengerid,
                                    dateBooked,
                                    startTime,
                                    startAddress,
                                    endTime,
                                    destinationAddress,
                                    paymentMethod)
              VALUES(?,?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, booking)
    conn.commit()
    return cur.lastrowid

#This code creates tables as long as they don't exist
def create_tables(conn):
    
    sql_create_drivers_table = """ CREATE TABLE IF NOT EXISTS drivers (
                                        id integer PRIMARY KEY,
                                        title text NOT NULL,
                                        firstName text NOT NULL,
                                        lastName text NOT NULL,
                                        email text NOT NULL,
                                        mobNumber text UNIQUE,
                                        password text NOT NULL,
                                        regNum text NOT NULL
                                    ); """
    
    sql_create_passengers_table = """ CREATE TABLE IF NOT EXISTS passengers (
                                        id integer PRIMARY KEY,
                                        title text NOT NULL,
                                        firstName text NOT NULL,
                                        lastName text NOT NULL,
                                        email text UNIQUE NOT NULL,
                                        mobNumber text NOT NULL
                                        password text NOT NULL,
                                        postcode text NOT NULL,
                                        address text NOT NULL,
                                        town text NOT NULL,
                                        county text NOT NULL,
                                        paymentMethod text NOT NULL
                                    ); """

    sql_create_bookings_table = """ CREATE TABLE IF NOT EXISTS bookings (
                                    id integer PRIMARY KEY,
                                    driverid integer NOT NULL,
                                    passengerid integer NOT NULL,
                                    dateBooked text NOT NULL,
                                    startTime text NOT NULL,
                                    endTime text NOT NULL,
                                    startAddress text NOT NULL,
                                    destinationAddress text NOT NULL,
                                    paymentMethod text NOT NULL,
                                    FOREIGN KEY (driverid) REFERENCES drivers (id),
                                    FOREIGN KEY (passengerid) REFERENCES passengers (id)
                                ); """
    
    # create passengers table
    create_table(conn, sql_create_passengers_table)
    # create drivers table
    create_table(conn, sql_create_drivers_table)
    # # create bookings table
    create_table(conn, sql_create_bookings_table)
    
#This code is to allow passengers to log in
def login_passenger(conn, user):
    sql = ''' SELECT * FROM passengers WHERE email=? AND password=?'''
    cur = conn.cursor()
    cur.execute(sql, user)
    first = cur.fetchall()[0] 
    return first

#This code is to allow driver to log in
def login_driver(conn, user):
    sql = ''' SELECT * FROM drivers WHERE email=? AND password=?'''
    cur = conn.cursor()
    cur.execute(sql, user)
    first = cur.fetchall()[0] 
    return first

#This code fetches all drivers
def get_drivers(conn):
    sql = ''' SELECT * FROM drivers'''
    cur = conn.cursor()
    cur.execute(sql)
    return cur.fetchall()

#This code fetches all drivers
def get_passengers(conn):
    sql = ''' SELECT * FROM passengers'''
    cur = conn.cursor()
    cur.execute(sql)
    return cur.fetchall()

#This code fetches all bookings
def get_bookings(conn):
    sql = ''' SELECT * FROM bookings'''
    cur = conn.cursor()
    cur.execute(sql)
    return cur.fetchall()

#This code deletes bookings
def delete_booking(conn, id):
    sql = 'DELETE FROM bookings WHERE id=?'
    cur = conn.cursor()
    cur.execute(sql, (id,))
    conn.commit()


