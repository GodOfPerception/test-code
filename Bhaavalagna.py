"""Astrology has one lagna called Bhav Lagna.
Its calculated like this

5.2 Bhaava Lagna Bhaava lagna is at the position of Sun at the time of sunrise. It moves at the rate of one rasi per 2 hours. In the rest of this book, bhava lagna will be denoted by BL. 10 
If sunrise takes place at 6:00 am and Sun is at 6s 4°47' then, horalagna is at 6s 4°47' at 6:00 am, at 6s 19°47' at 7:00 am, at 7s 4°47' at 8:00 am, 8s 4°47' at 10:00 am and so on. Bhavalagna moves at the rate of 1° per 4 minutes (i.e., 15° per hour). 

The following method may be used for computing bhavalagna. 
(1) Find the time of sunrise and sun's longitude at sunrise. 
(2) Find the difference between the birthtime (or the event time) and the sunrise time found in (1) above. Convert the difference into minutes. The result is the advancement of bhavalagna since sunrise, in degrees.
 (3) Add Sun's longitude at sunrise (in degrees) to the above number. Expunge multiples of 360° and reduce the number to the range 0°–360°
 
 
 #code"""
import json

data = {
    'day': 'Friday',
    'sunrise': '6:37:00',
    'sunlongitude': '24°17',
    'sunset': '18:30:16',
    'moonrise': '15:49:27',
    'moonset': '2:55:31',
    'vedic_sunrise': '5:7:21',
    'vedic_sunset': '18:26:9'
}

jdatai = json.dumps(data)
jdataii = json.loads(jdatai)

sunrise_str = jdataii["sunrise"]
sunrise_components = sunrise_str.split(':')
sunrise_h = int(sunrise_components[0])
sunrise_m = int(sunrise_components[1])
sunrise_s = int(sunrise_components[2])
total_sunrise = sunrise_h * 3600 + sunrise_m * 60 + sunrise_s
sun_longitude = jdataii["sunlongitude"]
sun_longitude_angle = int(sun_longitude.split('°')[0])
sun_longitude_degree= int(sun_longitude.split('°')[1])

time_str = input("Enter Time of birth in format of hour:min AM/PM: ")
time_components = time_str.split(':')
time_h = int(time_components[0])
time_m = int(time_components[1].split()[0])
time_ampm = time_components[1].split()[1]
if time_ampm == "PM":
    time_h = time_h + 12 if time_h < 12 else time_h
if time_ampm == "AM" and time_h == 12:
    time_h = 0
time_s = 0
total_seci = time_h * 3600 + time_m * 60 + time_s

if total_seci > total_sunrise:
    elapsed_second = (total_seci - total_sunrise)
else:
    elapsed_second = (total_sunrise - total_seci)

elapsed_minutes = (elapsed_second // 60)/2
sun_longitude_sunrise=270+sun_longitude_angle+elapsed_minutes
s=sun_longitude_sunrise-360

print("HL is",int(s%30),"°",sun_longitude_degree,"in")
degree_ranges = {
    0: 'Aries',
    1: 'Taurus',
    2: 'Gemini',
    3: 'Cancer',
    4: 'Leo',
    5: 'Virgo',
    6: 'Libra',
    7: 'Scorpio',
    8: 'Sagittarius',
    9: 'Capricorns',
    10: 'Aquarius',
    11: 'Pieces'
}
sign = sun_longitude_sunrise//30
if sign>11:
    sign=sign//2

print(degree_ranges[sign])
