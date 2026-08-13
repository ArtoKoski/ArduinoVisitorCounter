Toteutin tiimikaverin kanssa Arduino projektin. Teimme kävijämäärälaskurin joka toimii molempiin suuntiin. Kävijän saapuessa lisätään kävijämäärään +1 ja poistuessa vähennetään -1. Laskurille on olemassa sivusto joka päivittyy reaaliaikaisesti.

Laitteisto lähtee toimimaan, kun laittaa Arduinoon virrat. Sivusto toimii kun ottaa Putty:llä tai vastaavalla ohjelmalla yhteyden WEB-serveriin ja suorittaa kansiossa var/www/html/Foxtrot aktivoidussa venv-tilassa komennon python counter.py (löytyy Code kohdasta nimellä server.py)
