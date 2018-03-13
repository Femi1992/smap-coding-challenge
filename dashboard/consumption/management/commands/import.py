from django.core.management.base import BaseCommand
import csv, sys

from django.conf import settings


import django

from consumption.models import User, Consumption

class Command(BaseCommand):
    help = 'import data'

    def getUserData(self):

        data = csv.reader(open("/Users/femi/PycharmProjects/smap-coding-challenge/data/user_data.csv"), delimiter=",")

        for row in data:
            print("")


    def handle(self, *args, **options):
        print("Implement me!")


if __name__ == "__main__":
    c = Command()
    c.getUserData()