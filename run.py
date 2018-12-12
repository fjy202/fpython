import sys
import traceback
def run(text):
    try:
        return eval(text)
    except:
        try:
            exec(text)
        except Exception as e:
            sys.stderr.write(traceback.print_exception(*sys.exc_info()))
