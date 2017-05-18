#!/usr/bin/python2.7
# -*- coding: utf8 -*-

import pyowm



#city=input('What city?: ')
city = 'Tomsk'
owm = pyowm.OWM('b4593b1e61dc9e134ca7aceea1b80b2c')
#owm_ru=OWM(language='ru')


observation = owm.weather_at_place(city)
w = observation.get_weather()
temp=w.get_temperature('celsius')['temp']

print('In city {0} now temperature: {1} cel'.format(city,temp))
print('Also in this city ' + w.get_detailed_status())
#print ('In city ' + 'temp' )

