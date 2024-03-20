"""
Gmail Authentication Update:

1. Deprecated Feature:
   - Gmail no longer supports app passwords. This feature is now deprecated.

2. Recommended Alternative:
   - The suggested alternative for authentication is using OAuth 2.0.

3. Implementation Attempt:
   - A project was created in Google Cloud Platform.
   - Gmail API was enabled.
   - Credentials were created.
   - OAuth consent screen was configured.
   - OAuth client ID was created.
   - Attempted to obtain OAuth 2.0 tokens using OAuth.

4. Access Issue:
   - The Python Email Sender Script is currently facing an access block.
   - The specific error encountered is 'Error 403: access_denied'.
   - This is due to the script not having completed Google's verification process.
   - As a result, the app is in testing mode and only accessible by developer-approved testers.

5. Error Details:
   - Email Account: payerornie@gmail.com
   - Script Name: Python Email Sender Script
   - Status: Incomplete Google verification process
   - Accessibility: Limited to developer-approved testers
   - Recommended Action: 
     a) For users: Contact the developer if you believe you should have access.
     b) For developers: Review the error details to address the verification process.
"""

from email.message import EmailMessage
from secure import password # Assumes 'password' is defined in a separate secure module
import ssl
import smtplib

# Initialize email credentials and recipient details
email_sender = 'payerornie@gmail.com'
email_password = password
email_reciever = 'ornpayer@gmail.com' # Alternative email address for testing

subject = "Test email"
body = """
Python script for email sender.
"""

# Create an email message instance
em = EmailMessage()
em["From"] = email_sender
em["To"] = email_reciever
em["Subject"] = subject
em.set_content(body)


# Create a secure SSL context
context = ssl.create_default_context()

# Send the email using SMTP over SSL
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        """
        Establishes a secure SMTP connection and sends an email.

        Uses the SMTP_SSL class for a secure connection over SSL. Logs in to the sender's email account using the provided credentials and sends an email to the specified recipient.

        @returns None
        """ 
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_reciever, em.as_string())
