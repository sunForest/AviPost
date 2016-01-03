Feature: /postcards

    Background:

        Given Tom, Jerry are users
        And Tom is logged in


    Scenario: GET
        Given Tom received 5 postcards 
        When GET "/postcards/"
        Then request will success for 200
        And return 5 items
        And has structure
            """
            {
                "$schema": "http://json-schema.org/draft-04/schema#",
                "id": "/",
                "type": "array",
                "items": {
                    "id": "0",
                    "type": "object",
                    "properties": {
                        "message": {
                            "id": "message",
                            "type": "string"
                        },
                        "cover": {
                            "id": "cover",
                            "type": "string"
                        },
                        "sender": {
                            "id": "sender",
                            "type": "string"
                        }
                    },
                    "required": [
                        "message",
                        "cover",
                        "sender"
                    ]
                },
                "required": [
                    "0"
                ]
            }
            """

    Scenario: POST
        Given Jerry received 3 postcards 
        When POST "/postcards/"
        And with file "test_image.jpg" as cover
        And with data 
            """
            {
                "message": "Hello with image",
                "receiver": "<Jerry's id>",
                "longitude": 0,
                "latitude": 0,
                "messenger": 1
            } 
            """
        Then request will success for 201
        Given Jerry is logged in
        When GET "/postcards/"
        Then request will success for 200
        And return 4 items
