import hashlib
import string

class URLShortener:
    def __init__(self):
        self.url_dict = {}
        self.id_counter = 0

    def encode_id(self, id):
        # Base 62 encoding with digits, lowercase, and uppercase letters
        chars = string.digits + string.ascii_lowercase + string.ascii_uppercase
        encoded = []
        while id:
            id, remainder = divmod(id, 62)
            encoded.append(chars[remainder])
        return ''.join(reversed(encoded))

    def shorten(self, url):
        # Generate the MD5 hash of the URL
        hash = hashlib.md5(url.encode()).hexdigest()
        # Take the first 8 characters of the hash as the ID
        id = int(hash[:8], 16)
        # Encode the ID using base 62 encoding to generate the shortened URL
        short_url = self.encode_id(id)
        # Store the mapping in a dictionary
        self.url_dict[short_url] = url
        self.id_counter += 1
        return short_url

    def expand(self, short_url):
        # Look up the original URL from the dictionary
        return self.url_dict.get(short_url, None)

# Create a URLShortener instance
url_shortener = URLShortener()

# Prompt the user to enter a long URL
long_url = input('Enter a long URL to shorten: ')

# Shorten the URL
short_url = url_shortener.shorten(long_url)

# Print the shortened URL
print('The Short URL is:', short_url)

#https://youtu.be/VuG7ge_8I2Y