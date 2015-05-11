Feature: /postcards

  Scenario: GET
    Given sunsen has 3 Postcards
    When GET "/postcards?user=sunsen"
    Then request will success(200)
    And return 3 items
    And each item is as
        """
        {
            "type" : "object",
            "properties" : {
                "message" : {"type" : "string"},
                "cover": {"type": "string"},
                "sender" : {"type" : "string"},
            }
        }
        """
