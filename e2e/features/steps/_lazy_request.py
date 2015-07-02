from requests import request


TEST_TOKEN = 'CAAGhrMP3FZBgBAGemH67ru5s9lk1ajnVshgujfl2JBgAzBozFFFiUwMULCZAzQ3S2y2oMd1kvmvAs9Rb8zEzwdsxmKKyDVa0DPlHnv3FD0363BOL2llilQVDZBhLZBJqgoNI5PsqjDPVC4oeL7uMPoZAvNLlQYZBOQwpKSxZCKLoizJYZC2BRD0xu1oLCd3z2YUjcKbgWyYWGKBQ11DJHm0ZCYOvSyiJ6eVUZD'


class LazyRequest(object):

    """
    Request which accumulates settings and send later
    """

    def __init__(self, verb, url):
        self.get_token_url = "http://127.0.0.1:8000/users/register-by-token/facebook"
        self.verb = verb
        self.url = url
        self.data = {}
        self.upload = False
        self.token = None

    def get_token(self, access_token=TEST_TOKEN):
        params = {'access_token': access_token}
        res = request('GET', self.get_token_url, params=params)
        resAsJson = res.json()
        self.token = resAsJson['access_token']

    def send(self):
        """
        send real network request
        """
        headers = {}
        if self.token:
            headers['Authorization'] = 'Bearer ' + self.token

        if self.upload:
            with open(self.file_name) as fp:
                response = request(
                    self.verb, self.url, data=self.data,
                    files={ self.file_field: fp }, headers=headers
                )
        else:
            response = request(self.verb, self.url, data=self.data, headers=headers)
        return response
    

    def add_file(self, file_name, file_field):
        """ add file to be uploaded

        :file_name: file to be uploaded
        :file_field: as what field

        """
        self.upload = True
        self.file_name = file_name
        self.file_field = file_field

    def add_data(self, data):
        """ add data body (json)

        :data: json to be sent as data body

        """
        self.data = data
