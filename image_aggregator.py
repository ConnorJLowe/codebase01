#----------------------------------------------------------------
#
# Image Aggregator
#
# This is an extension of the "Image Finder" exercise, so you
# will need to have completed that one before beginning this.
#
# In the previous exercise you created a program that found
# and printed the URLs of images in Wikipedia pages.  Here
# you will extend that program so that it produces a whole new
# web page containing just the extracted images without the
# surrounding text.
#
# As per the steps below, you will follow the same process
# for finding images, but instead of printing the URLs
# you will create an HTML file that, when opened in a web
# browser, displays the images found.  The HTML code you
# generate should have a structure like the following:
#
# <!DOCTYPE html>
# <html>
#
#     <head>
#         <title>Aggregated Images</title>
#     </head>
# 
#     <body>
#         <h1>Images from WIKIPEDIA_URL</h1>
#         <img src="IMAGE_URL">
#         ... etc
#     </body>
#
# </html>
#
# Complete the program by replacing the "pass" statements.


#-----
# Import the necessary URL and RE functions
from urllib.request import urlopen
from re import findall

#-----
# Here are some web pages to try, each of which is a Wikipedia
# page, so we can assume they have a fairly consistent structure.
# As well as large images, you will also discover the images for
# small icons, as well as single pixel meta-data images hidden in
# the page.  Uncomment whichever page you want to use.

wiki_url = 'http://en.wikipedia.org/wiki/Jack_Benny'
##wiki_url = 'http://en.wikipedia.org/wiki/QUT'
##wiki_url = 'http://en.wikipedia.org/wiki/Flags'
##wiki_url = 'http://en.wikipedia.org/wiki/Robby_the_Robot'
##wiki_url = 'http://en.wikipedia.org/wiki/Baby_Huey'
##wiki_url = 'http://en.wikipedia.org/wiki/Superman'

#-----
# Step 1. Get a link to the web page from the server, using one
# of the URLs above
web_page = urlopen(wiki_url)

#-----
# Step 2. Extract the web page's content as a character string
html_code = web_page.read().decode("UTF-8")

#----
# Step 3. Close the connection to the web server
web_page.close()

#-----
# Step 4. Extract all of the image URLs in the web document

url_regex = '<img .*src="([^"]+)"'
urls = findall(url_regex, html_code)
print(urls)

#-----
# Step 5. Open the output HTML file for writing
file_name = 'aggregated_images.html'
html_file = open(file_name, 'w')

#-----
# Step 6. Write the first part of the HTML document into the file
# (using an "f-string" which replaces expressions in braces {...}
# with their current value)
html_file.write(f'''<!DOCTYPE html>
<html>

    <!-- This is an automatically generated HTML document -->

    <head>
        <title>Aggregated Images</title>
    </head>

    <body>
    
        <h1>Images from {wiki_url}</h1>
        
        <!-- The following images were extracted from Wikipedia -->
''')

#-----
# Step 7. Write an image tag for each image found in the
# input web page, making sure the URL is a full address
# beginning 'https://en.wikipedia.org'

for url in urls:
    if url.startswith('//upload'):
        url = f"https:{url}"
    elif url.startswith('/static'):
        url = f"https://en.wikipedia.org{url}"
    
#-----
# Step 8. Write the last part of the HTML file
html_file.write('''
    </body>

</html>''')

#-----
# Step 9. Close the output file and tell the user
# where it is
html_file.close()
print('\nDone! See the result in file ' + file_name + '\n')
