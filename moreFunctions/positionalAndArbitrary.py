###Arbitrary parameters need to be last

def assignSeat(seat, passenger, *requests):
    """assign seat and requests to passengers"""
    print("\nAssign seat number " + str(seat) + " and the following requests to " + str(passenger.title()))
    for request in requests:
        print('- ' + request)

assignSeat(13,'Brent','window seat','breakfast','comfort+')