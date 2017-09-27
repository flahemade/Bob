# coding: utf8

import sys
import irclib
import ircbot
from messageBuilder import messageBuilder
from knowledgeBuilder import knowledgeBuilder

class Bob(ircbot.SingleServerIRCBot):
    
    waitingForAnswer=''
        
    def __init__(self,server,port):
        ircbot.SingleServerIRCBot.__init__(self, [(server,int(port))],"Bob","Bah bob..")
        global waitingForAnswer
        waitingForAnswer=''

    def on_welcome(self, serv, ev):
        serv.join("#Bob")
        serv.privmsg("#Bob","Bob est dans la place.")

    def on_pubmsg(self, serv, ev):
        global waitingForAnswer
        canal = ev.target()
        message=ev.arguments()[0]
        if len(waitingForAnswer)==0 :
            mb=messageBuilder()
            answer=mb(message)
            if answer!='':
                serv.privmsg("#Bob",answer)
            else:
                serv.privmsg("#Bob","Et on répond quoi à ça ?")
                waitingForAnswer=message
        else:
            kb=knowledgeBuilder()
            insert=kb(waitingForAnswer,"knowledge.json",message)
            if(insert):
                serv.privmsg("#Bob","Ok, cimer.")
            waitingForAnswer=''
    
    def on_join(self, serv, ev):
        source=ev.source()
        person=source.split('!')
        serv.privmsg("#Bob","Salut "+person[0]+" :)")
        

if __name__ == "__main__":
    Bob(sys.argv[1],sys.argv[2]).start()
