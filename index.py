from datetime import datetime, date, timedelta
from parseHTML import parseHTML

startDate = date(2013, 4, 13)
endDate = datetime.now().date()
while startDate < endDate:
    startDate += timedelta(days=1)
    parseHTML(startDate.isoformat(), 'data')