# Pankkiautomaatti-Simulaatio (KT6OHJ)

## Projektin kuvaus

Tämä projekti oli osa Ohjelmointi 1 kurssin toteutusta, jossa keskityin vielä itse  modernin Flask API -sovelluksen kehittämiseen ja integrointiin CI/CD-pipelineen. Projektissa käytettiin versiohallintaan GitHubia ja tavoitteena oli simuloida pankkiautomaatin perustoimintoja skaalautuvassa ja automatisoidussa ympäristössä. Toteutuksessa huomioitiin ohjelmistokehityksen parhaat käytännöt sekä työkalut, joita hyödynnetään myös ammattimaisessa ohjelmistokehityksessä.

## Projektin kohokohdat

### Flask API:n kehitys
- Sovellus toteutettiin käyttäen Flask-kehystä, joka on moderni ja kevyt ratkaisu API-kehitykseen.
- Flaskin avulla luotiin tehokas ja helposti ylläpidettävä palvelu pankkiautomaattitoiminnoille, kuten tilitapahtumien simulointiin.

### CI/CD-pipeline
- GitHub Actions -pipeline automatisoi koodin rakentamisen ja testauksen jokaisen päivityksen yhteydessä.
- Pipeline varmistaa, että koodi on jatkuvasti toimivaa ja testattua, mikä minimoi tuotantoympäristössä esiintyvät ongelmat.

### AWS Elastic Beanstalk
- Projekti sisälsi AWS Elastic Beanstalk -ympäristön konfiguroinnin Python-sovelluksen isännöimiseksi.
- Vaikka tekniset rajoitteet estivät loppuunsaattamisen, projektissa opittiin monipuolisesti AWS:n ympäristönhallinnan perusteista ja käytännöistä.

## Oppimiskokemukset

- **Flask ja API-kehitys:** Projektin aikana kehittyivät API-kehitykseen liittyvät taidot, mukaan lukien REST-rajapintojen suunnittelu ja toteutus.
- **CI/CD-käytännöt:** Pipelinien rakentaminen GitHub Actionsilla tarjosi käytännön kokemusta automaation hyödyntämisestä ohjelmistokehityksessä.
- **Pilvipalvelut:** AWS Elastic Beanstalk -ympäristön hallinta opetti pilvipalveluiden käytön perusteita ja niiden konfigurointia tuotantoympäristöjä varten.



### Miksi tämä projekti on merkityksellinen?
Tämä projekti kuvastaa käytännön kokemusta ohjelmistokehityksen eri osa-alueilta, joita voidaan hyödyntää monipuolisesti kehittämisen ja teknologian taustatehtävissä, kuten testausautomaation harjoittelupaikoissa. Flaskin kaltaisen modernin kehitysalustan käyttö, CI/CD-pipelinen rakentaminen sekä AWS:n ympäristöjen hallinta osoittavat kykyä omaksua uusia teknologioita ja ratkaista ongelmia joustavasti.




## Käyttöohjeet

## Ohjelman Suorittaminen

Seuraa näitä ohjeita käynnistääksesi pankkiautomaattisimulaation:

### 1. Esivaatimukset
- Varmista, että järjestelmääsi on asennettu GCC (GNU Compiler Collection).
- Pythonin tulee olla asennettuna testiskriptien suorittamiseksi.

### 2. Käännä ja Suorita Ohjelma
1. Avaa terminaali ja siirry hakemistoon, jossa `main.c` sijaitsee.
2. Käännä ohjelma komennolla:
   ```bash
   gcc main.c -o ohjelma.exe

