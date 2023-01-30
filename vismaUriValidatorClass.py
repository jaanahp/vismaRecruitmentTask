import re

class UriValidator:
    uri = ""
    scheme = ""
    parameterDict = {}

#UriValidator-class initializer, takes uri (string) as input and sets parameterDict empty
    def __init__ (self, input):
        self.uri = input
        self.parameterDict = {}

    #Method for checking that uri validateUri-method gets as parameter ('i'), meets the requirements
    def validateUri(self, i):
    #'i' (=uri) is split into a list by the characters given in the first argument
        uriSplitList = re.split('[:/?=&]', i)
        #print(uriSplitList) #print for debugging purposes
        #checks that the first item on uriSplitList is the required scheme "visma-identity"
        if uriSplitList[0] == "visma-identity":
            #if sceme is correct, checks that the fourth item on uriSplitList is 'login' and that the 6th item is type string and matches "severa"
            if uriSplitList[3] == "login" and isinstance(uriSplitList[5], str) == True and uriSplitList[5] == "severa":
                    #scheme-attribute of the class and key-value pairs on parameterDict-dictionary are only set, if all the requirements for the uri are met
                    self.scheme = uriSplitList[0]
                    self.parameterDict["path"] = uriSplitList[3]
                    self.parameterDict["source"] = uriSplitList[5]
            #if sceme is correct, checks that the fourth item on uriSplitList is 'sign' and that the sixth item is type string and matches "vismasign"
            elif uriSplitList[3] == "sign" and isinstance(uriSplitList[5], str) == True and uriSplitList[5] == "vismasign":
                    #checks that the 8th item on uriSplitList is type string and that the 7th item matches "documentid"
                    if "documentid" in uriSplitList and isinstance(uriSplitList[7], str) == True and uriSplitList[6] == "documentid":
                        #scheme-attribute of the class and key-value pairs on parameterDict-dictionary are only set, if all the requirements for the uri are met
                        self.scheme = uriSplitList[0]
                        self.parameterDict["path"] = uriSplitList[3]
                        self.parameterDict["source"] = uriSplitList[5]
                        self.parameterDict["documentId"] = uriSplitList[7]
                    else:
                        print("Incorrect URI")
            #if scheme is correct, checks that the fourth item on uriSplitList is 'confirm' and that the sixth item is type string and matches "netvisor"
            elif uriSplitList[3] == "confirm" and isinstance(uriSplitList[5], str) == True and uriSplitList[5] == "netvisor":
                    #checks that the 8th item on uriSplitList consists of only numbers and that the 7th item matches "paymentnumber"
                    if "paymentnumber" in uriSplitList and uriSplitList[7].isdigit() == True and uriSplitList[6] == "paymentnumber":
                        #scheme-attribute of the class and key-value pairs on parameterDict-dictionary are only set, if all the requirements for the uri are met
                        self.scheme = uriSplitList[0]
                        self.parameterDict["path"] = uriSplitList[3]
                        self.parameterDict["source"] = uriSplitList[5]
                        self.parameterDict["paymentNo"] = int(uriSplitList[7])
                    else:
                        print("Incorrect URI")
            else:
                print("Incorrect URI")
        else:
            print("Incorrect URI")

    #Method returns path, source, documentId and paymentNo as key-value pairs 
    def returnValues(self):
            return self.parameterDict
