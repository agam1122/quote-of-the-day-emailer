import smtplib
import datetime as dt
import random

my_email = "YOUR_EMAIL"
my_password = "APP_PASSWORD_CREATED_WITH_YOUR_EMAIL"
receivers_email = "RECEIVERS_EMAIL"

# Get the current date and time
now = dt.datetime.now()
# Get the current weekday (Monday is 0 and Sunday is 6)
weekday = now.weekday()

try:
    # Check if today is Wednesday (2 represents Wednesday)
    if weekday == 2:
        # Open the file containing quotes and read all lines into a list
        with open("quotes.txt") as quote_file:
            all_quotes = quote_file.readlines()
            # Select a random quote from the list
            quote = random.choice(all_quotes)
            # print(all_quotes)
            # print(quote)

        # Set up the connection to the Gmail SMTP server
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            # Secure the connection using TLS (Transport Layer Security)
            connection.starttls()  # tls --> transport layer security
            # Log in to the email account
            connection.login(user=my_email, password=my_password)
            # Send an email with the selected quote
            connection.sendmail(from_addr=my_email, to_addrs=receivers_email,
                                msg=f"Subject: Quote of the day\n\n{quote}")

# except smtplib.SMTPException:
#     print("Error occured.")

except Exception as e:
    # Print any exception that occurs
    print(e)
