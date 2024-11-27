from twilio.rest import Client

account_sid = 'ACfba06a8dcc929dc41deca23bd11210b2'
auth_token = '608048f6a209ad6a558daefc6246f587'
client = Client(account_sid, auth_token)
def sendSms():
    message = client.messages.create(
        from_='+12077090042',
        body='Alert !!! HUMAN DETECTED',
        to='+918777014564'
    )
