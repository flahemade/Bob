# coding: utf8

import json
import codecs

class knowledgeBuilder:
    
    def __init__(self):
        return None
        
    def __call__(self,message,file,answer):
        
        entry = {message.decode('utf-8'):answer.decode('utf8')+"\n"}
        
        with codecs.open('knowledge.json','r+','utf8') as file:
            data = json.load(file)
            
        data.update(entry)
        
        with codecs.open('knowledge.json','r+','utf8') as file:
            json.dump(data,file)
            
        return True