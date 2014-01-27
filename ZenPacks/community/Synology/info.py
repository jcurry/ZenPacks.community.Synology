from ZenPacks.community.ConstructionKit.ClassHelper import *

def SynologySystemgetEventClassesVocabulary(context):
    return SimpleVocabulary.fromValues(context.listgetEventClasses())

class SynologySystemInfo(ClassHelper.SynologySystemInfo):
    ''''''

def SynologyHardDiskgetEventClassesVocabulary(context):
    return SimpleVocabulary.fromValues(context.listgetEventClasses())

class SynologyHardDiskInfo(ClassHelper.SynologyHardDiskInfo):
    ''''''

def SynologyLogicalDiskgetEventClassesVocabulary(context):
    return SimpleVocabulary.fromValues(context.listgetEventClasses())

class SynologyLogicalDiskInfo(ClassHelper.SynologyLogicalDiskInfo):
    ''''''


