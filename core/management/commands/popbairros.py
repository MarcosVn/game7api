#  -*- coding: utf-8 -*-
from django.db.utils import IntegrityError
from django.core.management.base import BaseCommand
from datetime import *
from calendar import monthrange
from core.models import *
import csv


class Command(BaseCommand):
    args = '<data_entrada>'

    def handle(self, *args, **options):

        with open('plan/bairros_sjc.csv', 'rb') as csvfile:
            spamreader = csv.reader(csvfile, delimiter='=', quotechar=',')
            for row in spamreader:
                print row

                oCidade=Cidade.objects.get(id=5340)

                oBairro=Bairro()
                oBairro.cidade=oCidade
                oBairro.nome = row[0].split(",")[0]

                oBairro.save()

                print "Salvo o Bairro {bairro}".format(bairro=oBairro.nome)
