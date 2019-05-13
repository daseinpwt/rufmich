import importlib
from flask import Flask
from flask import request as fl_request
from callme.request import CMRequest, InvalidJsonError, InvalidRequestError
from callme.response import CMResponse
from callme.error import CMError
import sys

app = Flask(__name__)
@app.route("/callme", methods=['POST'])
def callme():
    try:
        request = CMRequest(fl_request)
    except InvalidJsonError:
        return CMResponse(error={'code': -32700, 'message': 'Parse error'}, id=None)
    except InvalidRequestError:
        return CMResponse(error={'code': -32600, 'message': 'Invalid Request'}, id=None)

    try:
        result = request.process()
    except (ModuleNotFoundError, AttributeError):
        return CMResponse(error={'code': -32601, 'message': 'Method not found'}, id=None)
    except TypeError:
        return CMResponse(error={'code': -32602, 'message': 'Invalid params'}, id=None)
    except CMError as error:
        return CMResponse(error=error.to_dict(), id=None)
    except:
        return CMResponse(error={'code': -32603, 'message': 'Internal error'}, id=None)

    return CMResponse(result=result, id=None)

class CMServer():
    def load(self, path):
        sys.path.insert(0, path)
        return self
    
    def run(self, **kw):
        app.run(**kw)
