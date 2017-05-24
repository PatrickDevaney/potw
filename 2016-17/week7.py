import http.client

# Initialize connection, make request, get response
connection = http.client.HTTPConnection("potw.quinnftw.com")
connection.request("GET", "/problem/s3cret")
response = connection.getresponse()

# Translate the HTTP version into the usual format
responseString = "HTTP/" + str(response.version)[0] + "." + str(response.version)[1]
# Now add on status and reason
responseString += " " + str(response.status) + " " + str(response.reason)
# Output the HTTP response
print(responseString)
# Get and output the headers
headers = response.getheaders()
for header in headers:
    print(header[0] + ": " + header[1])
