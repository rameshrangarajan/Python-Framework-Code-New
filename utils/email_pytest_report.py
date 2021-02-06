"""
 Utility script to send pytest test report email
* Supports both text and html formatted messages
* Supports text, html, image, audio files as an attachment
* To generate html formatted test report, you need to use pytest-html plugin. To install it use command: pip install pytest-html
* To generate pytest_report.html file use following command from the root of repo e.g. py.test --html = pytest_report.html
"""
import smtplib
import os, sys
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
import mimetypes
from email import encoders

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class email_pytest_report:

    def get_test_report_data(report_file_path):
        # To generate pytest_report.html file use following command e.g. py.test --html = report.html
        test_report_file = os.path.abspath(os.path.join(os.path.dirname(__file__), '..',
                                                            report_file_path))  # Change report file name & address here
        # check file exist or not
        if not os.path.exists(test_report_file):
            raise Exception("File '%s' does not exist. Please provide valid file" % test_report_file)

        with open(test_report_file, "r") as in_file:
            testdata = ""
            for line in in_file:
                testdata = testdata + '\n' + line

        return testdata

    def get_attachment(attachment_file_path):
        "Get attachment and attach it to mail"
        attachment_report_file = os.path.abspath(os.path.join(os.path.dirname(__file__), '..',attachment_file_path))  # Change report file name & address here
        # check file exist or not
        if not os.path.exists(attachment_report_file):
            raise Exception("File '%s' does not exist. Please provide valid file" % attachment_report_file)

        # Guess encoding type
        ctype, encoding = mimetypes.guess_type(attachment_report_file)
        if ctype is None or encoding is not None:
            ctype = 'application/octet-stream'  # Use a binary type as guess couldn't made

        maintype, subtype = ctype.split('/', 1)
        if maintype == 'text':
            fp = open(attachment_report_file)
            attachment = MIMEText(fp.read(), subtype)
            fp.close()
        elif maintype == 'image':
            fp = open(attachment_report_file, 'rb')
            attachment = MIMEImage(fp.read(), subtype)
            fp.close()
        elif maintype == 'audio':
            fp = open(attachment_report_file, 'rb')
            attachment = MIMEAudio(fp.read(), subtype)
            fp.close()
        else:
            fp = open(attachment_report_file, 'rb')
            attachment = MIMEBase(maintype, subtype)
            attachment.set_payload(fp.read())
            fp.close()
            # Encode the payload using Base64
            encoders.encode_base64(attachment)
        # Set the filename parameter
        attachment.add_header('Content-Disposition',
                              'attachment',
                              filename=os.path.basename(attachment_report_file))

        return attachment

    def send_test_report_email(_email_server,_receiver_addrs,_sender_addr,report_file_path):

        # Add html formatted email body with report.html content along with an attachment file
        message = MIMEMultipart()
        # add html formatted body message to email
        reportdata = email_pytest_report.get_test_report_data(report_file_path)  # get html formatted test report data from report.html
        html_body= MIMEText(reportdata, "html")
        message.attach(html_body)
        # add attachment to email
        attachment = email_pytest_report.get_attachment(report_file_path)
        message.attach(attachment)

        message['From'] = _sender_addr
        message['To'] = _receiver_addrs
        message['Subject'] = 'Automation test execution report'  # Update email subject here

        # Send Email
        server = smtplib.SMTP(_email_server)
        server.sendmail(message['From'],  message['To'].split(','), message.as_string())
        server.quit()

