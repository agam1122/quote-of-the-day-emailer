# quote-of-the-day-emailer

This project sends a random quote from a file (`quotes.txt`) via email every Wednesday. The script checks the current day of the week, and if it's Wednesday, it reads a random quote from the file and sends it to a specified email address.

## Features

- Reads quotes from a text file
- Selects a random quote each Wednesday
- Sends the selected quote via email


## Prerequisites

- Python 3.x
- An email account (preferably Gmail)
- App-specific password for your email account (if using Gmail, you need to set up 2-step verification and create an app password)


## Installation

1. Clone the repository or download the script.

   ```
   git clone https://github.com/your-username/quote-of-the-day-emailer.git
   cd quote-of-the-day-emailer
   ```
2. Ensure you have a file named quotes.txt in the same directory as the script.

3. Install the required Python libraries if not already installed.
   ```
    pip install smtplib
   ```

   
##Configuration

 -  Replace YOUR_EMAIL_ID and YOUR_APP_PASSWORD in the script with your actual email ID and app-specific password.
 -  Optionally, you can change the recipient email address (to_addrs) to the desired recipient.

##Troubleshooting

  - SMTP Authentication Error: Ensure you are using the correct app-specific password for your email account.
  - File Not Found Error: Make sure the quotes.txt file is in the same directory as the script and contains quotes.





   
