from requests import request


class LazyRequest(object):

    """
    Request which accumulates settings and send later
    """

    def __init__(self, verb, url):
        self.verb = verb
        self.url = url
        self.data = {}
        self.upload = False

    def send(self):
        """
        send real network request
        """
        if self.upload:
            with open(self.file_name) as fp:
                response = request(
                    self.verb, self.url, data=self.data,
                    files={ self.file_field: fp }
                )
        else:
            response = request(self.verb, self.url, data=self.data)
        print(response.status_code)
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
