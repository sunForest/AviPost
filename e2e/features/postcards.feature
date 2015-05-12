Feature: /postcards

    Scenario: GET
        Given server has 5 postcards
        When GET "/postcards/"
        Then request will success for 200
        And return 5 items
        And is like
            """
            [{
                "message": "Hello",
                "cover": "http://world.com/0.png",
                "sender": "someone"
            }]
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
