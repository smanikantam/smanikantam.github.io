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