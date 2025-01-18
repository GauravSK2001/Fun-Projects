def add_time(start, duration,today=0):
    Days=['monday','tuesday','wednesday','thursday','friday','saturday','sunday']

    post=start.split(' ')[1] #am/pm

    post_parity= 0 if post=='AM' else 1


    Current_time_hr =int((start.split(' ')[0]).split(':')[0]) #hours
    Current_time_min=int((start.split(' ')[0]).split(':')[1]) #minutes
    if post_parity==1:
        Current_time_hr+=12

    
    duration_hr =int(duration.split(':')[0])
    duration_min=int(duration.split(':')[1])


    Added_time_hrs=duration_hr+Current_time_hr+(Current_time_min+duration_min)//60
    Added_time_min=(Current_time_min+duration_min)%60
    days_passed=Added_time_hrs//24
    end_time_hrs=Added_time_hrs%12

    EndPoint='AM' if (Added_time_hrs//12)%2 == 0 else 'PM'
    print(f'days_passed:{days_passed}')
    
    if end_time_hrs==0:
            end_time_hrs+=12

    if today==0:
        if  days_passed==0:
            return (f'{end_time_hrs}:{Added_time_min:02} {EndPoint}')
        elif days_passed==1:
            return (f'{end_time_hrs}:{Added_time_min:02} {EndPoint} (next day)')
        else:
            return (f'{end_time_hrs}:{Added_time_min:02} {EndPoint} ({days_passed} days later)')
    
    else :
        Added_day=Days[(Days.index(today.lower())+days_passed)%7]
        Added_day=Added_day[0].upper()+Added_day[1:]
        if days_passed==0:
            return (f'{end_time_hrs}:{Added_time_min:02} {EndPoint}, {Added_day}')
        elif days_passed==1:
            return (f'{end_time_hrs}:{Added_time_min:02} {EndPoint}, {Added_day} (next day)')
        else:
            return (f'{end_time_hrs}:{Added_time_min:02} {EndPoint}, {Added_day[0].upper()+Added_day[1:]} ({days_passed} days later)')

