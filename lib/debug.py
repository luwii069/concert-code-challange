#!/usr/bin/env python3
import ipdb

from classes.many_to_many import Band
from classes.many_to_many import Concert
from classes.many_to_many import Venue


# Create instances of Band
band1 = Band("The Beatles", "Liverpool")
band2 = Band("Led Zeppelin", "London")

# Create instances of Venue
venue1 = Venue("Madison Square Garden", "New York City")
venue2 = Venue("Wembley Stadium", "London")

# Create instances of Concert
concert1 = Concert("2024-07-15", band1, venue1)
concert2 = Concert("2024-08-20", band2, venue2)

# Test methods of Band class
print("Band Name:", band1.name)  # Output: The Beatles
print("Band Hometown:", band1.hometown)  # Output: Liverpool
print("Concerts by Band:", band1.concerts())  # Output: [concert1]
print("Venues for Band:", band1.venues())  # Output: [venue1]
print("Introduction for Band:", band1.all_introductions())  # Output: ["Hello New York City!!!!! We are The Beatles and we're from Liverpool"]

# Test methods of Venue class
print("Venue Name:", venue1.name)  # Output: Madison Square Garden
print("Venue City:", venue1.city)  # Output: New York City
print("Concerts at Venue:", venue1.concerts())  # Output: [concert1]
print("Bands at Venue:", venue1.bands())  # Output: [band1]

# Test methods of Concert class
print("Concert Date:", concert1.date)  # Output: 2024-07-15
print("Concert Band:", concert1.band)  # Output: Band object for The Beatles
print("Concert Venue:", concert1.venue)  # Output: Venue object for Madison Square Garden
print("Hometown Show:", concert1.hometown_show())  # Output: True
print("Introduction:", concert1.introduction())  # Output: "Hello New York City!!!!! We are The Beatles and we're from Liverpool"

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")

    ipdb.set_trace()
