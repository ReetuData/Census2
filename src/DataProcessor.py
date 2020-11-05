#!/usr/bin/env python
# coding: utf-8

import csv
import sys
from csv import DictReader
 
class Census_data_processor:

    def __init__(self, inputFilePath, outputFilePath):
        self.inputFilePath = inputFilePath
        self.outputFilePath = outputFilePath

    def tryfloat(_self, val):
        try:
            return float(val)
        except ValueError:
            return 0
        
    def generateOutput(self, dataDictionary):
        with open(self.outputFilePath, 'w') as file:
            writer = csv.writer(file)
            for key, val in sorted(dataDictionary.items()):
                writer.writerow(val)

    def processCensusData(self):
        dataList = []
        with open(self.inputFilePath, 'r') as read_obj:
            csv_dict_reader = DictReader(read_obj)
            for row in csv_dict_reader:
                dataList.append([row['CBSA09'],row['CBSA_T'],row['POP00'],row['POP10'],row['PPCHG']])
            
        areaCountDictionary = {}
        for l in dataList:
            if (l[0] not in areaCountDictionary):
                areaCountDictionary[l[0]] = [l[0], "%s"%l[1], 1, int(l[2]), int(l[3]), float(l[4])]
            else:
                areaCountDictionary[l[0]][2] = areaCountDictionary[l[0]][2] + 1;
                areaCountDictionary[l[0]][3] = areaCountDictionary[l[0]][3] + int(l[2]);
                areaCountDictionary[l[0]][4] = areaCountDictionary[l[0]][4] + int(l[3]);
                areaCountDictionary[l[0]][5] = areaCountDictionary[l[0]][5] + self.tryfloat(l[4]);

        for key, val in areaCountDictionary.items():
            val[5] = round(val[5]/val[2],2)

        self.generateOutput(areaCountDictionary)
        
processor = Census_data_processor(sys.argv[1], sys.argv[2])
processor.processCensusData()