# venmo_web_scrape

Python webscraper for the Venmo API. The other ones I found online are not updated for the newest api.

Relatively simple webscraper, taking two arguements of epoch times (GMT) for start and end of analysis, returning all elements from the venmo API and writing them to a csv file.

I wouldn't advise running this sequentially for pulling all of the data, it will take a long time. Parallelize it for better performance.

Returns date and time, username for ID1, username for ID2, message, and transaction direction.

To use: replace TIME1 and TIME2 for start and end times. The code goes 1000 seconds over time 2, for sake of full coverage.
