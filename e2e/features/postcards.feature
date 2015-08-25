Feature: /postcards

    Scenario: GET
        Given server has 5 postcards
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
        Given server has 3 postcards
        When POST "/postcards/"
        And with file "test_image.jpg" as cover
        And with data 
            """
            {
                "message": "Hello with image"
            } 
            """
        Then request will success for 201
