from urllib.request import urlopen
'''
urllib is a standard Python library (meaning you don’t have to install anything extra
to run this example) and contains functions for requesting data across the web, handling
cookies, and even changing metadata such as headers and your user agent. We
will be using urllib extensively throughout the book, so I recommend you read the
Python documentation for the library.
'''
html = urlopen('http://pythonscraping.com/pages/page1.html')
print(html.read())

'''
This command outputs the complete HTML code for page 1 located at URL 
http://pythonscraping.com/pages/page1.html
More accurately, this outputs the HTML file page1.html,
found in the directory <web root>/pages, on the server located at the domain name
http://pythonscraping.com 
'''