# coding: utf8

import json
import codecs

class knowledgeBuilder:
    
    def __init__(self):
        """
        Not needed by now
        """
        return None
        
    def addEntry(self,message,file,answer):
        """
        Add an entry to knowledge base
        :param message: Message received
        :param file: File to add
        :param answer: Answer to associate
        """
        entry = {message.decode('utf_8'):answer.decode('utf_8')}
        
        with codecs.open('knowledge.json','r+','utf_8') as file:
            data = json.load(file)
            
        data.update(entry)
        print data
        
        with codecs.open('knowledge.json','r+','utf_8') as file:
            json.dump(data,file)
            
        return True