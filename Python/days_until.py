from datetime import datetime
def days_until(date_str):
    future_date = datetime.strptime(date_str, '%Y-%m-%d')
    return (future_date - datetime.now()).days
