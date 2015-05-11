# Use it like:

``` bash 
behave -D base_url=http:127.0.0.1:3000 -D manager=avipost/manage.py e2e/features/ 
```

# Dependencies

The e2e tests use **behave** to do cucumber-like BDD test, and depend on these libraries:

## Library dependencies

* sure: for expressive assertion and error report
* requests: for http requests (for human)
* inflection: for parse plurals
* json-schema-generator: for generate json schema based on example data
* jsonschema: use this though json_schema_generator provides validator, since it has detailed error report

## Command line dependencies

* django: for manage database
* autofixture: with django, for load fixtures
