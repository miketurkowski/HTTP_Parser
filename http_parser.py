# This parser determines whether an HTTP request is valid and generates an appropriate HTTP result response.  
# It does not use any libraries built for parsing HTTP requests. 
# Traditional string parsing libraries and functionality are approved.  
# The parser must have exactly one command-line argument: The file path to a text file containing exactly one HTTP request.
# Must support the following methods discussed in RFC 2616:  GET, POST, PUT, DELETE, and HEAD.  
# HTTP parser must parse requests in the following way: If the request is valid, it should return a 200 OK response. 
# If the request is not valid, it should return a 400 BAD REQUEST response. 
# If an exception occurs while processing the HTTP request, it should fail gracefully and return a 500 INTERNAL SERVER ERROR response.

# Define a list of HTTP methods
HTTP_methods = ['GET', 'POST', 'PUT', 'HEAD', 'DELETE']

# Define response messages
valid_response = '200 OK'
invalid_response = '400 BAD REQUEST'
exception_response = '500 INTERNAL SERVER ERROR'

# Define the parse_request function to parse the contents of a request file
def parse_request(request_file):
    try:
        # Open the request file in read mode
        with open(request_file, 'r') as file:
            request = file.read()

        # Split the first line of 'request' using space as a separator
        request_line = request.split('\n')[0].split(' ')

        # Store the first element of 'request_line' in a variable 'method'
        method = request_line[0]

        # Check if the method is not in HTTP_methods
        if method not in HTTP_methods:
            return invalid_response

        # Store the second element of 'request_line' in a variable 'resource'
        resource = request_line[1]

        # Store the third element of 'request_line' in a variable 'http_version'
        http_version = request_line[2]

        # Check if 'http_version' is not equal to 'HTTP/1.0' or 'HTTP/1.1'
        if http_version not in ['HTTP/1.0', 'HTTP/1.1']:
            return invalid_response
        
        # Return a valid response if the function execution reaches this point
        return valid_response
    except Exception as e:

        # Return an exception response if an exception is caught
        return exception_response

# Check if the script is being run as the main program      
if __name__ == '__main__':
    import sys

    # Check if the number of command-line arguments is not equal to 2
    if len(sys.argv) != 2:
        
        # print a usage message and exit with a status code of 1 if the number of command line arguments is not equal to 2
        print('Usage: python3 http_parser.py [file_path]')
        sys.exit(1)

    # Store the second command-line argument in a variable 'request_file'
    request_file = sys.argv[1]

    # Call the parse_request function with 'request_file' as an argument and store the result in a variable 'response'
    response = parse_request(request_file)

    # Print 'response'
    print(response)


