##################################################################
import nexmo
from twilio.rest import Client
##################################################################
account_sid = 'AC730d2142614ea4d8220278bb5bd247fd'
auth_token = 'fdd8833312fe3d2ebc9eb7142c3cb771'
##################################################################
# account_sid = 'ACf896cacf87342b00d224a999be391e7e'
# auth_token = 'c26c67fbb8193ebb4cec3a8364469a4a'
client = Client(account_sid, auth_token)
client_1 = nexmo.Client(key='a442ba3b', secret='2allzGX4QBsVF05Q')
##################################################################




def sms(msg):
	message = client.messages \
	                .create(
	                     body=str(msg),
	                     from_='+15093977702',
	                     # from_='+15017122661',
	                     to='+917639147936'
	                 )

	print(message.sid)


def sms_1(msg,phn):
	client_1.send_message({
	    'from': 'Nexmo',
	    'to': '91'+str(phn),
	    'text': str(msg),
	})



def call(phn):
	call = client.calls.create(
	                        twiml='<Response><Say>Alert!, You have a request</Say></Response>',
	                        to='+91'+str(phn),
	                        from_='+15093977702'
	                    )

	print(call.sid)


# sms("Vanakam daee")
# call(76391479)
# sms("vana dura",7092600127)
###############################################################################################

