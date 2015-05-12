Feature: /postcards

    Scenario: GET
        Given server has 5 postcards
        When GET "/postcards/"
        Then request will success(200)
        And return 5 items
        And is like
            """
            [{
                "message" : "Hello",
                "cover": "http://world.com/0.png",
                "sender": "someone"
            }]
            """

    Scenario: POST
        Given server has 3 postcards
        When POST "/postcards/" with params {"message":"Hello with image"} and file "test_image.jpg"
        Then request will success(201)

