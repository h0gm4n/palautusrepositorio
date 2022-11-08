import toml
from urllib import request
from project import Project


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        print(content)

        data = toml.loads(content)

        nimi = data["tool"]["poetry"]["name"]

        kuvaus = data["tool"]["poetry"]["description"]

        riippuvuudet = []
        for i in data["tool"]["poetry"]["dependencies"]:
            riippuvuudet.append(i)

        dev_riippuvuudet = []
        for k in data["tool"]["poetry"]["dev-dependencies"]:
            dev_riippuvuudet.append(k)

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(nimi, kuvaus, riippuvuudet, dev_riippuvuudet)
