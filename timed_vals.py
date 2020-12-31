from datetime import datetime, timedelta

def get_filename(check_time=None) -> str:
    # Return the YearMonthDate of today if time > 6AM/check_time
    # else return YearMonthDate of yesterday
    check_time = check_time or '06:00:00'
    if datetime.now().strftime("%H:%M:%S") < check_time:
        return (datetime.now() - timedelta(days = 1)).strftime("%Y%m%d")
    else:
        return datetime.now().strftime("%Y%m%d")


