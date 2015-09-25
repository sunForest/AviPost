Feature: /users

    Background:

        Given Tom, Jerry, Spike are users
        And Tom is logged in

    Scenario: GET

        When GET "/users/"
        Then request will success for 200
        And return 3 items
        And has structure
        """
        {
            "$schema": "http://json-schema.org/draft-04/schema#",
            "id": "http://jsonschema.net",
            "type": "array",
            "items": {
                "id": "http://jsonschema.net/0",
                "type": "object",
                "properties": {
                    "username": {
                        "id": "http://jsonschema.net/0/username",
                        "type": "string"
                    },
                    "email": {
                        "id": "http://jsonschema.net/0/email",
                        "type": "string"
                    },
                    "id": {
                        "id": "http://jsonschema.net/0/id",
                        "type": "integer"
                    }
                },
                "required": [
                    "username",
                    "email",
                    "id"
                ]
            },
            "required": [
              "0"
            ]
        }
        """