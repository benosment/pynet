#! /usr/bin/env python3

from pygeocoder import Geocoder

if __name__ == '__main__':
    #address = '6085 Parkridge Drive, East Petersburg, PA'
    address = '109 Thamesford Way, Cary, NC'
    print(Geocoder.geocode(address)[0].coordinates)
