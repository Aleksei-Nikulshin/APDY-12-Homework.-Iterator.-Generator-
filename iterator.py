
import json
import wikipediaapi


class CountriesWiki:

    def __init__(self, path, start):
        self.file = open(path, encoding='utf-8')
        self.json = json.load(self.file)
        self.start = start - 1
        self.wiki = wikipediaapi.Wikipedia('en')

    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1

        if self.start == len(self.json):
            raise StopIteration

        country = self.json[self.start]['name']['official']
        country_page = self.wiki.page(country)
        country_link = country_page.fullurl

        return country, country_link


if __name__ == '__main__':
    output_file = open('countries_links.txt', 'w', encoding='utf-8')

    try:
        for country, url in CountriesWiki('countries.json', 1):
            print(f'country = {country}')
            output_file.write(str(country) +"  " + str(url) + '\n')
    except Exception as e:
        print(e)

    output_file.close()