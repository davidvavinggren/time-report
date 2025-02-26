import yagmail

def mail(month):
    '''
    Function used to email employer with time report for the month.
    '''
    sender = '' # enter sender email
    reciever = '' # enter reciever email
    app_password = '' # enter google app password if gmail is used
    subject = 'Time report {} [David Vävinggren]'.format(month)
    body = "Hello!\n\nTime report for {} created by davvabot is attached to this email.\n\nBest regards,\n\ndavvabot".format(month)
    attachment = ''.format(month.lower()) # enter path to file attached
    
    try:
        with yagmail.SMTP(sender, app_password) as yag:
            yag.send(reciever, subject, body, attachment)
            print('\nEmail sent successfully.')
    except:
        return False
    return