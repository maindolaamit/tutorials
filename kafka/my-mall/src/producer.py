import time

import pandas as pd
from random import random, randint
from kafka import KafkaConsumer, KafkaProducer


class UserLocationProducer():
    MALL_GPS_LOC = (28.457523, 77.026344)
    LATTITUDE = 28.457523
    LONGITUDE = 77.026344
    # approximate radius of earth in km
    R = 6371.0087714150598

    @staticmethod
    def add_tuple(loc1, loc2):
        """
        Method to add two locations (lattitude, longitude)
        :param loc1:
        :param loc2:
        :return:
        """
        return loc1[0] + loc2[0], loc1[1] + loc2[1]

    @staticmethod
    def sub_tuple(loc1, loc2):
        """
        Method to substract two locations (lattitude, longitude)
        :param loc1:
        :param loc2:
        :return:
        """
        return loc1[0] - loc2[0], loc1[1] - loc2[1]

    @staticmethod
    def calculate_distance(loc1, loc2):
        """
        Function to return distance between two co-ordinates in KM
        :param loc1:
        :param loc2:
        :return:
        """
        from math import sin, cos, sqrt, atan2, radians

        # Convert into radian
        lat1 = radians(loc1[0])
        lon1 = radians(loc1[1])
        lat2 = radians(loc2[0])
        lon2 = radians(loc2[1])
        # Take difference
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        # Calculate the
        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))

        return round(UserLocationProducer.R * c, 2)

    def get_current_location(self, gps_loc):
        """
        Get the current location randomly by add/sub delta to current location
        :param gps_loc:
        :return:
        """
        loc1 = self.MALL_GPS_LOC
        loc2 = gps_loc
        if randint(0, 1) == 1:
            return loc1[0] + loc2[0], loc1[1] + loc2[1]
        else:
            return loc1[0] - loc2[0], loc1[1] - loc2[1]

    def generate_data(self):
        """
        Main method to generate GPS data for the customers
        """
        df = pd.read_csv('customers.csv')
        df.columns = [col.lower() for col in df.columns]
        for index, row in df.head(10).iterrows():
            # Generate random delta
            gps_loc = (random() * random() * 0.1, random() * random() * 0.1)
            # Add or remove delta
            current_loc = self.get_current_location(gps_loc)
            distance = self.calculate_distance(self.MALL_GPS_LOC, current_loc)
            print(f"Customer Id : {row['customerid']} | Location : {current_loc} | Distance : {distance} KM")
            # Push the location to Kafka Topic
            producer = KafkaProducer(bootstrap_servers='localhost:9092', acks=1)
            producer.send(topic='send-locations', key=row['customerid'], value=current_loc)
            time.sleep(10)

    def __init__(self):
        self.generate_data()
