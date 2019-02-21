from datetime import timedelta

def add_gigasecond(moment):
    
    gigasecond = 1_000_000_000
    datetime_plus_gigas = moment + timedelta(seconds=gigasecond)
    
    return datetime_plus_gigas
