# import mechanize
# browser = mechanize.Browser()
# browser.set_handle_robots(False)
# cookies = mechanize.CookieJar()
# browser.set_cookiejar(cookies)
# browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.517.41 Safari/534.7')]
# browser.set_handle_refresh(False)

# url = 'https://studentscorner.vardhaman.org/student_corner_index.php'
# browser.open(url)
# browser.select_form(nr = 0)       #This is login-password form -> nr = number = 0
# browser.form['rollno'] = '20881A05B1'
# browser.form['wak'] = '#NN5A'
# response = browser.submit()
# print(response.read())
# attendance_url = 'https://studentscorner.vardhaman.org/student_attendance.php'

import mechanize
from bs4 import BeautifulSoup

# Create a mechanize browser object
browser = mechanize.Browser()
browser.set_handle_robots(False)
cookies = mechanize.CookieJar()
browser.set_cookiejar(cookies)
browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.517.41 Safari/534.7')]
browser.set_handle_refresh(False)

# Login
login_url = 'https://studentscorner.vardhaman.org/student_corner_index.php'
browser.open(login_url)
browser.select_form(nr=0)
browser.form['rollno'] = '20881A05B1'
browser.form['wak'] = '#NN5A'
response = browser.submit()

# Continue to attendance URL
attendance_url = 'https://studentscorner.vardhaman.org/student_attendance.php'
response = browser.open(attendance_url)
# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response, 'html.parser')
# Find the fifth table
table = soup.find('font')
print(table.text)
















# import requests
# from bs4 import BeautifulSoup

# # URL of the webpage to scrape attendance from
# attendance_url = 'https://studentscorner.vardhaman.org/student_attendance.php'

# # Credentials for authentication
# username = "20881A05B1"
# password = "#NN5A"
# login_data = {
#             'rollno': '20881A05B1',
#             'wak': '#NN5A',
#         }

# # Authenticate and get a session cookie
# login_url = 'https://studentscorner.vardhaman.org/student_corner_index.php'
# with requests.Session() as s:
#     r=s.post(login_url,data=login_data)
#     print(r.text)

# session = requests.Session()
# # Fetch the login page to obtain any necessary cookies or CSRF tokens
# login_page = session.get(login_url)
# soup = BeautifulSoup(login_page.content, 'html.parser')

# # Find the login form
# login_form = soup.find('form')

# if login_form:
#     # Extract the relevant input fields and their values
#     rollno_input = login_form.find('input', {'type':'text','class': 'login-field', 'id': 'username', 'name': 'rollno','placeholder':'Rollno'})
#     wak_input = login_form.find('input', {'type':'password','class': 'login-field', 'id': 'login-pass','placeholder':'password'})

#     if rollno_input and wak_input:
#         # Prepare the login data
#         login_data = {
#             'username': username,
#             'login-pass': password
#         }

#         # Perform the login
#         response = session.post(login_url, data=login_data)

#         if response.status_code == 200:
#             # Authentication successful, proceed to fetch attendance data
#             response = session.get(attendance_url)

#             if response.status_code == 200:
#                 # Parse the HTML content using BeautifulSoup
#                 soup = BeautifulSoup(response.content, 'html.parser')

#                 # Find the attendance table based on its class name or other identifier
#                 attendance_table = soup.find_all('font')
#                 print(attendance_table)

#                 if attendance_table:
#                     # Find the attendance percentage
#                     attendance_row = attendance_table[4].find_parent('tr')
#                     attendance_percentage = attendance_row.find_all('th')[1].text.strip()

#                     # Print or process the attendance percentage
#                     print('Attendance Percentage:', attendance_percentage)
#                 else:
#                     print('Attendance table not found.')
#             else:
#                 print(f'Failed to fetch attendance. Status code: {response.status_code}')
#         else:
#             print(f'Authentication failed. Status code: {response.status_code}')
