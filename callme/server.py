from flask import Flask
from flask import request as fl_request
from .request import CMRequest, InvalidJsonError, InvalidRequestError
from .response import CMResponse
from .error import CMError
import sys
import os
import shutil
import tempfile

app = Flask('callme')
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
    def __init__(self, load_path):
        self.load_path = load_path
    
    def run(self, **kw):
        with tempfile.TemporaryDirectory() as temp_dir:
            work_dir = os.path.join(temp_dir, 'methods')
            shutil.copytree(self.load_path, work_dir)
            sys.path.insert(0, work_dir)
            app.run(**kw)