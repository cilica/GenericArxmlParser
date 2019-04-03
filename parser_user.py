from logging import root
import parser_autosar43

ECUEXTRACT_FILE = 'C:\\TODO\\path_to_ecuextract.arxml'


def main():
  print "======================================="
  print "========== Ecu Extract E2E ============"
  print "======================================="
  rootObject = parser_autosar43.parse(ECUEXTRACT_FILE,True)
  printE2EStuff(rootObject)



def printE2EStuff(rootObjectVariant):
   #xpath: /AUTOSAR/AR_PACKAGES/AR_PACKAGE[5]/ELEMENTS/DATA_TRANSFORMATION_SET/TRANSFORMATION_TECHNOLOGYS/TRANSFORMATION_TECHNOLOGY[2]/TRANSFORMATION_DESCRIPTIONS/END_TO_END_TRANSFORMATION_DESCRIPTION/MAX_DELTA_COUNTER
   for package in rootObjectVariant.AR_PACKAGES.AR_PACKAGE:
      if (package.ELEMENTS is not None) and (package.ELEMENTS.DATA_TRANSFORMATION_SET is not None):
         if type(package.ELEMENTS.DATA_TRANSFORMATION_SET) is list:
            for dataSet in package.ELEMENTS.DATA_TRANSFORMATION_SET:
               if dataSet.TRANSFORMATION_TECHNOLOGYS is not None:
                  for transfTechn in dataSet.TRANSFORMATION_TECHNOLOGYS.TRANSFORMATION_TECHNOLOGY:
                     print transfTechn.SHORT_NAME.valueOf_
                     if transfTechn.TRANSFORMATION_DESCRIPTIONS is not None and transfTechn.TRANSFORMATION_DESCRIPTIONS.END_TO_END_TRANSFORMATION_DESCRIPTION is not None:
                        for descr in transfTechn.TRANSFORMATION_DESCRIPTIONS.END_TO_END_TRANSFORMATION_DESCRIPTION:
                           if (descr.MAX_DELTA_COUNTER is not None):
                              print "   has MAX-DELTA-COUNTER: " + descr.MAX_DELTA_COUNTER.valueOf_
                           if (descr.PROFILE_NAME is not None):                         
                              print "   has PROFILE-NAME: " + descr.PROFILE_NAME.valueOf_


if __name__== "__main__":
  main()
