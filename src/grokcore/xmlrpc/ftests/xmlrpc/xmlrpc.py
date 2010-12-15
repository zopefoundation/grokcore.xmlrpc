"""
  >>> getRootFolder()["Manfred"] = Mammoth()

  >>> from zope.app.wsgi.testlayer import XMLRPCServerProxy
  >>> server = XMLRPCServerProxy("http://localhost/")

  >>> server.Manfred.stomp()
  'Manfred stomped.'
  >>> server.Manfred.dance()
  "Manfred doesn't like to dance."

Let's also check whether we can use XML-RPC with subobjects we
traverse to::

  >>> server.Manfred.baby.pounce()
  'baby pounced.'
  
"""
import grokcore.component as grok
import grokcore.xmlrpc
from grokcore.content import Model


class Mammoth(Model):
    def traverse(self, name):
        if name == 'baby':
            return MammothBaby()

class MammothBaby(Model):
    pass

class MammothRPC(grokcore.xmlrpc.XMLRPC):
    grok.context(Mammoth)
    
    def stomp(self):
        return '%s stomped.' % self.context.__name__

    def dance(self):
        return '%s doesn\'t like to dance.' % self.context.__name__

class BabyRPC(grokcore.xmlrpc.XMLRPC):
    grok.context(MammothBaby)

    def pounce(self):
        return '%s pounced.' % self.context.__name__

