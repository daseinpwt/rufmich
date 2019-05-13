from callme.server import CMServer

server = CMServer()
server.load('/Users/wentaopan/Projects/test/methods')
server.run(port=8080)