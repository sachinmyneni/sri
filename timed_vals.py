from datetime import datetime, timedelta
from time import sleep
import random



def gen_random_val() -> float:
    # Dummy function
    """Function to generate dummy values from the "sensor"

    In your program you replace this with the function that
    returns the real value from the sensor.
    """
    return random.random()

def get_condition() -> bool:
    # Dummy function
    """ Function to generate the "condition" which we need to check whether
    the value from the sensor needs to be accumulated or not.
    Currently this generates a random true/false. 
    
    Note that unlike the example you
    showed me on the paper this true/false condition can switch back
    and forth in a single day. In your example the true condition persisted
    over more than 24hrs... We can make that happen too but this is a more
    general example..

    In your program you replace this with the function that returns the conditon
    """
    return random.choice([True,False])


def get_filename(check_time=None) -> str:
    # Return the YearMonthDate of today if time > 6AM/check_time
    # else return YearMonthDate of yesterday
    check_time = check_time or '06:00:00'
    if datetime.now().strftime("%H:%M:%S") < check_time:
        return (datetime.now() - timedelta(days = 1)).strftime("%Y%m%d")
    else:
        return datetime.now().strftime("%Y%m%d")



if __name__ == '__main__':
    myval = {}  # a dictionary of 'date':cumulative_val
    random.seed(42)

    while True:
        sleep(random.randint(1,5))
        file_key = get_filename()
        if get_condition():
            if file_key in myval:
                myval[file_key] += gen_random_val()
            else:
                myval[file_key] = gen_random_val()
        
        print(myval)





