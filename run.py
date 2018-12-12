import sys
import traceback
import os
class ModuleNotFoundError(BaseException):
    pass
def runpython(text):
    try:
        return eval(text)
    except:
        try:
            exec(text)
        except BaseException as e:
            sys.stderr.write(traceback.print_exception(*sys.exc_info()))
def runmodule(module=sys.argv[1],arguments=sys.argv[2:]):
    runfile(findmodule(module),args=arguments)
def findmodule(module):
    #在sys.argv就为下面查找该模块。
    for path in sys.path:
        for ext in ("py","pyw"):
            if module+"."+ext in os.listdir(path):
                return path+"/"+module+"."+ext
    raise ModuleNotFoundError("Module not found:"+module)
def runfile(file,args=[]):
    argv=sys.argv
    sys.argv=[file]+args
    return runpython(open(file).read()))
