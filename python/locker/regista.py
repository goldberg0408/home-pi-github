import sys
from sdk.api.sender_id import SenderID 
from sdk.exceptions import CoolsmsException

##  @brief This sample code demonstrate how to verify sender number through CoolSMS Rest API 
if __name__ == "__main__":

    # set api key, api secret
    api_key = "NCS76REGORDXIHMI"
    api_secret = "XSCPKTB0CVFBVWBMHV1QNLM7IG2KL2XB"

    # handle_key is mandatory.
    handle_key = "SID5A1CEB4A78EB1"

    cool = SenderID(api_key, api_secret)

    try:
        response = cool.verify(handle_key)
        if response == None:
            print("Register Success")

    except CoolsmsException as e:
        print("Error Code : %s" % e.code)
        print("Error Message : %s" % e.msg)

    sys.exit()
