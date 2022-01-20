import os,os.path
import MclApi.Error.ErrorOs as mcer


class McPath(object):
    def __init__(self,path):
        if not(os.path.isdir(path)):
            try:
                os.mkdir(path)
            except OSError:
                mcer.MclPathError("Error:Can't make this dir.")



