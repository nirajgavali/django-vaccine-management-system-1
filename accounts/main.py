import pandas as pd
import datetime
import smtplib
import os
os.chdir(r"C:\Users\Sam\Dropbox\My PC (DESKTOP-7141SDP)\Desktop\vaccine management system\accounts")
# os.mkdir("testing") 

# authentication details
GMAIL_ID = 'samarth.mailme@gmail.com'
GMAIL_PSWD = 'happyperson'


def sendEmail(to, sub, msg):
    print(f"Email to {to} sent with subject: {sub} and message {msg}" )
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(GMAIL_ID, GMAIL_PSWD)
    s.sendmail(GMAIL_ID, to, f"Subject: {sub}\n\n{msg}")
    print("mail sent")
    s.quit()
# sendEmail('samarth.mailme@gmail.com', 'hello sam bhaii', 'How r u??')   

if __name__ == "__main__":
    
    df = pd.read_excel("data.xlsx")
    
    today = datetime.datetime.now().strftime("%d-%m")
    yearNow = datetime.datetime.now().strftime("%Y")
    
    writeInd = []

    for index, item in df.iterrows():

        # print(index, item['Vaccine_Date'])
        bday = item['Vaccine_Date'].strftime("%d-%m")
        print(bday) 
        
        if(today == bday) and yearNow not in str(item['Year']):
            
            sendEmail(item['Email'], f"Vaccine Remider for {item['Name']}", f"Reminder for Rotavirus vaccine to be taken by your ward {item['Name']}, Today") 
            writeInd.append(index)

    # print(writeInd)
    for i in writeInd:
        yr = df.loc[i, 'Year']
        df.loc[i, 'Year'] = str(yr) + ', ' + str(yearNow)
        # print(df.loc[i, 'Year'])

    print(df) 
    df.to_excel('data.xlsx', index=False) 
    # os.remove('testing')