# coding: utf8

import sys
import irclib
import ircbot
from messageBuilder import messageBuilder
from knowledgeBuilder import knowledgeBuilder

class Bob(ircbot.SingleServerIRCBot):
    """
        Insufflating live to Bob
    """
    waitingForAnswer=''
        
    def __init__(self,server,port):
        """
        Connects to the server and inits the 'waitingForAnswer'
        :param server: Address of the server
        :param port: The port to connect on (default 6667)
        """
        ircbot.SingleServerIRCBot.__init__(self, [(server,int(port))],"Bob","Bah bob..")
        global waitingForAnswer
        waitingForAnswer=''

    def on_welcome(self, serv, ev):
        """
        Defines what to say on connecting
        :param serv: Provided by ircbot
        :param ev: Provided by ircbot
        """
        serv.join("#Bob")
        serv.privmsg("#Bob","Bob est dans la place.")

    def on_pubmsg(self, serv, ev):
        """
        Defines what to do when a user tells something
        :param serv: Provided by ircbot
        :param ev: Provided by ircbot
        """
        global waitingForAnswer
        canal = ev.target()
        message=ev.arguments()[0]
        if len(waitingForAnswer)==0 :
            mb=messageBuilder()
            answer=mb.buildAnswer(message)
            if answer!='':
                serv.privmsg("#Bob",answer)
            else:
                serv.privmsg("#Bob","Et on répond quoi à ça ?")
                waitingForAnswer=message
        else:
            kb=knowledgeBuilder()
            insert=kb.addEntry(waitingForAnswer,"knowledge.json",message)
            if(insert):
                serv.privmsg("#Bob","Ok, cimer.")
            waitingForAnswer=''
    
    def on_join(self, serv, ev):
        """
        Defines what to do when a user joins
        :param serv: Provided by ircbot
        :param ev: Provided by ircbot
        """
        source=ev.source()
        person=source.split('!')
        if(person!='Bob'):
            serv.privmsg("#Bob","Salut "+person[0]+" :)")
        

if __name__ == "__main__":
    """
        Main method expecting arg1 & arg2 from CLI
        :param arg1: Server address
        :param arg2: Server port
        """
    Bob(sys.argv[1],sys.argv[2]).start()
