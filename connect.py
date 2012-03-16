import uno
from com.sun.star.connection import NoConnectException

pipe = 'ooo_pipe'
localContext = uno.getComponentContext()
resolver = localContext.ServiceManager.createInstanceWithContext("com.sun.star.bridge.UnoUrlResolver", localContext)
context = resolver.resolve("uno:pipe,name=%s;urp;StarOffice.ComponentContext" % pipe)

