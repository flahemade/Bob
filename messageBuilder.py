# coding: utf8

import json
import codecs

class MessageBuilder:
    """Message handler"""

    def __init__(self):
        """Not needed by now"""
        return None
        
    def build_answer(self,message):
        """Build an answer according to message
        
        :param message: Message received
        
        """
        data = self.parse_knowledge("knowledge.json")
        answer = self.compare_knowledge(data, message)
        return answer
    
    def parse_knowledge(self,file):
        """Open and load a knowledgeFile
        
        :param file: File containing knowledge base
        
        """
        with codecs.open('knowledge.json', "r", "utf-8") as file:
            data = json.load(file)
        return data

    def compare_knowledge(self, data, message):
        """Compare message received to knowledge base
        
        :param data: Knowledge file loaded
        :param message: Message received
        
        """
        answer = ''
        for entry in data:
            if entry.lower() == message.decode('utf-8').lower():
                answer = str(data[entry]).decode('utf-8')
        return answer