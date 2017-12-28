from bs4 import BeautifulSoup
import requests



def extract_albany_db():
    #create soup object with page contents
    address = 'http://mods.rna.albany.edu'
    page = requests.get(address + '/mods/modifications/search')
    soup = BeautifulSoup(page.content, 'html.parser')

    #get parameter names
    child_page = requests.get(address + soup.select("table tr td a")[0].attrs['href'])
    child_soup = BeautifulSoup(child_page.content, 'html.parser')
    parameter_names = [parameter.get_text()[:len(parameter.get_text()) - 1]
                       for parameter in child_soup.select('div dl dt')]

    #create modification dictionary
    dict = {}

    #fill dictionary with data from mods.rna.albany.edu subpages
    for child in soup.select("table tr td a"):
        mod = {}
        print(child.attrs['href'])
        child_page = requests.get(address + child.attrs['href'])
        child_soup = BeautifulSoup(child_page.content, 'html.parser')
        value_names = [value.get_text() for value in child_soup.select('div dl dd')]
        for key, value in zip(parameter_names, value_names):
            mod[key] = value
        dict[value_names[0]] = mod

    return dict