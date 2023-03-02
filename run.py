from booking.booking import Booking
import time

with Booking(teardown = False) as bot:
    bot.land_first_page()
    print('Exiting...')