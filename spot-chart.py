import datetime
import tibber
import json
import settings
tibber_connection = tibber.Tibber(settings.access_token)
tibber_connection.sync_update_info()
#print(tibber_connection.name)
home = tibber_connection.get_homes()[0]
#home.sync_update_info()
#print(home.address1)

home.sync_update_price_info()
print(home.current_price_info)
print(home.price_total)
#print(home.current_price_total)
#test = []
count = 0
prices = json.loads(str(home.price_total).replace("'", '"'))
tibber_connection.sync_close_connection()
#Generate variables for dates
date_today = datetime.date.today()
one_day = datetime.timedelta(days=1)
date_tomorrow = date_today + one_day

today_series = ""
tomorrow_series = ""
while count < 24:
    s = "0" + str(count)
    hour = s[-2:]
    datetime_today = str(date_today)+"T"+hour+':00:00+02:00'
    datetime_tomorrow = str(date_tomorrow) + "T" + hour + ':00:00+02:00'
    #print(prices[date])
    if count == 0:
        today_series = str(prices[datetime_today])

        #try to see if data for tomorrow exists.
        try:
            tomorrow_series = str(prices[datetime_tomorrow])
        except:
            tomorrow_series = ""
    else:
        today_series = today_series+","+str(prices[datetime_today])
        if tomorrow_series != "":
            tomorrow_series = tomorrow_series + "," + str(prices[datetime_tomorrow])
    count = count + 1


print(today_series)
print(tomorrow_series)
f = open("template.htm")
#outputstring = str(f.read()).replace("<today>", today_series)
outputstring = str(f.read()).replace("<today>", today_series).replace("<tomorrow>",tomorrow_series)
file = open("spotprices.htm", "w")
print(outputstring)
file.writelines(outputstring)
f.close()
file.close()

