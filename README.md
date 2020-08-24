# spot-chart pulls swedish spot prices from Tibber to create a chart
When running spot-charts.py it pulls spot prices from Tibber and uses template.htm as a design template and insert the table with prices for today/tomorrow at the "placeholders" \<today\>/\<tomorrow\> and pushes the result to the file spotprices.htm.

#Installation
1. Install pyTibber (pip3 install pyTibber)
2. highcharts.js file from https://www.highcharts.com/
3. Rename or copy settings.py.example to settings.py and enter your API token from developer.tibber.com
4. Run the spot-chart.py manually or in some automated way. I'm using cron to run it once every hour.
5. Make the spotprices.htm togehter with the highcharts.js accessable through some kind of webserver.

#Known issues
Does not handle transition between summer and winter time. ':00:00+02:00' needs to be changed to ':00:00+01:00' for winter time.
