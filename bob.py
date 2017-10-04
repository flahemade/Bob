# coding: utf8

import sys
import irclib
import ircbot
from messageBuilder import MessageBuilder
from knowledgeBuilder import KnowledgeBuilder

class Bob(ircbot.SingleServerIRCBot):
    """Insufflate life to Bob"""
    waitingForAnswer=''
        
    def __init__(self, server, port):
        """Connect to the server and inits the 'waitingForAnswer'
        
        :param server: Address of the server
        :param port: The port to connect on (default 6667)
        
        """
        ircbot.SingleServerIRCBot.__init__(self, [(server,int(port))], "Bob", "Bah bob..")
        global waitingForAnswer
        waitingForAnswer = ''

    def on_welcome(self, serv, ev):
        """Define what to say on connecting
        
        :param serv: Provided by ircbot
        :param ev: Provided by ircbot
        
        """
        serv.join("#Bob")
        serv.privmsg("#Bob","Bob est dans la place.")

    def on_pubmsg(self, serv, ev):
        """Define what to do when a user tells something
        
        :param serv: Provided by ircbot
        :param ev: Provided by ircbot
        
        """
        canal = ev.target()
        message = ev.arguments()[0]
        bob = message.lower().split('bob')
        global waitingForAnswer
        if len(waitingForAnswer)==0 :
            mb=MessageBuilder()
            answer=mb.build_answer(message)
            if answer != '':
                   serv.privmsg("#Bob",answer)
            else:
                serv.privmsg("#Bob","Et on répond quoi à ça ?")
                waitingForAnswer=message
        else:
            kb=KnowledgeBuilder()
            insert=kb.add_entry(waitingForAnswer,"knowledge.json",message)
            if insert:
                serv.privmsg("#Bob","Ok, cimer.")
            waitingForAnswer = ''
    
    def on_join(self, serv, ev):
        """Define what to do when a user joins
        
        :param serv: Provided by ircbot
        :param ev: Provided by ircbot
        
        """
        source=ev.source()
        person=source.split('!')
        if person[0] != 'Bob':
            serv.privmsg("#Bob","Salut "+person[0]+" :)")
        
if __name__ == "__main__":
    """Main method expecting arg1 & arg2 from CLI
        
        :param arg1: Server address
        :param arg2: Server port
    
    """
    Bob(sys.argv[1], sys.argv[2]).start()
