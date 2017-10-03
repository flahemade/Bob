# coding: utf8

import json
import codecs

class messageBuilder:
    """
    Message handler
    """

    def __init__(self):
        """
        Not needed by now
        """
        return None
        
    def buildAnswer(self,message):
        """
        build an answer according to message
        :param message: Message received
        """
        data=self.parseKnowledge("knowledge.json")
        answer=self.compareKnowledge(data,message)
        return answer
    
    def parseKnowledge(self,file):
        """
        open and load a knowledgeFile
        :param file: File containing knowledge base
        """
        with codecs.open('knowledge.json',"r","utf-8") as file:
            data = json.load(file)
        return data

    def compareKnowledge(self,data,message):
        """
        compare message received to knowledge base
        :param data: Knowledge file loaded
        :param message: Message received
        """
        answer=''
        for i in data:
            if i.lower()==message.decode('utf-8').lower():
                answer=str(data[i]).decode('utf-8')
        return answer