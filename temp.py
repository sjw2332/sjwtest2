import requests
from bs4 import BeautifulSoup

def callTempData():
    uri = '''
            https://search.naver.com/search.naver?sm=tab_sug.top&where=nexearch&query=%EB%82%A0%EC%94%A8&oquery=%EB%82%A0%EC%94%A8&tqi=hRttdsprvxZssn79WD8ssssstU8-001581&acq=%EB%82%A0%EC%94%A8&acr=1&qdt=0
        '''
    response = requests.get(uri)
    temphtml = response.text

    soup = BeautifulSoup(temphtml, 'html.parser')

    today = soup.select_one('.todaytemp')
    tempdic = dict(temp = today.text)
    print(tempdic)
    return tempdic
