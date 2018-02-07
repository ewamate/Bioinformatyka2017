from bs4 import BeautifulSoup
import requests


def extract_albany_db():
    """
    Go through every subpage of http://mods.rna.albany.edu and save information from tables into one dictionary.
    @return: dictionary with all RNA modifications from http://mods.rna.albany.edu
    """

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

        #get soup object for subpage
        child_page = requests.get(address + child.attrs['href'])
        child_soup = BeautifulSoup(child_page.content, 'html.parser')

        #get parameter names
        value_names = [value.get_text() for value in child_soup.select('div dl dd')]
        value_names[3] = str(value_names[3]) + " " + str(value_names[4])
        value_names = value_names[:3] + value_names[4:]

        #add parameters and values to dictionary
        for key, value in zip(parameter_names, value_names):
            mod[key] = value
        dict[value_names[1]] = mod

    return dict


def extract_modomics_db():
    """
    Go through every subpage of http://modomics.genesilico.pl and save information from tables into one dictionary.
    @return: dictionary with all RNA modifications from http://modomics.genesilico.pl
    """

    #create soup object with page contents
    address = 'http://modomics.genesilico.pl'
    page = requests.get(address + '/modifications/')
    soup = BeautifulSoup(page.content, 'html.parser')

    #create modification dictionary
    dict = {}

    #fill dictionary with data from mods.rna.albany.edu subpages
    for child in soup.select("table tbody tr td a"):
        mod = {}

        #get soup object for subpage
        child_page = requests.get(address + child.attrs['href'])
        child_soup = BeautifulSoup(child_page.content, 'html.parser')

        #get parameter names
        tables = [s.select('tbody tr td') for s in child_soup.find_all("table", id="modification_details")]
        tables = tables[0] + tables[1]
        parameter_value_pairs = [parameter.get_text() for parameter in tables]
        parameter_value_pairs = parameter_value_pairs[:len(parameter_value_pairs) - 2]

        #add parameters and values to dictionary
        for key, value in zip(parameter_value_pairs[::2], parameter_value_pairs[1::2]):
            mod[key] = value
        dict[parameter_value_pairs[3]] = mod

    return dict