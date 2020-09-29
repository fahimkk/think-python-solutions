import datetime

def print_day(date):
    print(date.strftime('%A'))

dt = datetime.date(1994,9,27)
#print_day(dt)

def age_next_bday(bday):
    tdy = datetime.datetime.now()
    print(f'Age: {tdy.year-bday.year}')
    next_bday = datetime.datetime(tdy.year+1, bday.month, bday.day) 
    print(f'Time remaining for next Bday: {next_bday-tdy}')

bday = datetime.date(1898,3,21)
#age_next_bday(bday)


def double_day(bday1, bday2):
    tday = datetime.date.today()
    age1 = (tday-bday1).days
    age2 = (tday-bday2).days
    if age1 < age2:
        age1,age2=age2,age1
    i=0
    while age1+i != 2*(age2+i):
        i+=1
    return tday+datetime.timedelta(age1+i)

def n_times_day(bday1, bday2,n):
    tday = datetime.date.today()
    age1 = (tday-bday1).days
    age2 = (tday-bday2).days
    if age1 < age2:
        age1,age2=age2,age1

    i=0
    while age1+i != n*(age2+i):
        i+=1
    return tday+datetime.timedelta(age1+i)


print(double_day(dt, bday))
print('----')
print(n_times_day(dt,bday,1.5))