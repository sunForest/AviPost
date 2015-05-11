Feature: /postcards

    Scenario: GET
        Given server has 5 postcards
        When GET "/postcards"
        Then request will success(200)
        And return 5 items
        And is like
            """
            [{
                "message" : "Hello",
                "cover": "http://world.com/0.png",
                "sender" :  "me"
            }]
            """
