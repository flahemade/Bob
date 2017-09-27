# coding: utf8

import json
import codecs

class messageBuilder:
    def __init__(self):
        return None
        
    def __call__(self,message):
        data=self.parseKnowledge("knowledge.json")
        answer=self.getData(data,message)
        return answer
    
    def parseKnowledge(self,file):
        with codecs.open('knowledge.json',"r","utf8") as file:
            data = json.load(file)
        return data

    def getData(self,data,message):
        answer=''
        for i in data:
            if i[0].decode('utf8').lower()==message.decode('utf8').lower():
                answer=str(data[i]).decode('utf_8')
        return answer