import stackless
import random
import sys

class actor():
    def __init__(self):
        self.channel = stackless.channel()
        stackless.tasklet(self.process_messeges)()
    def process_messeges(self):
        while True:
            self.messeges_handling(self.channel.receive())
    def messeges_handling(self,args):
        pass
    
class world(actor):
    def __init__(self):
        actor.__init__(self)
    def messeges_handling(self):
        pass
    
class champion(actor):
    def __init__(self):
        actor.__init__(self)
    def messeges_handling(self,args):
        print(args)
    
class monster_blue(actor):
    def __init__(self):
        actor.__init__(self)
    def messeges_handling(self,args):
        print(args)
    

stackless.run()