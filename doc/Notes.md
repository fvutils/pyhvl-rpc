
Two types of endpoints on an API:
- available static APIs (collection of static functions 
- Object constructors
  - Object has a presence on each side (?)
  
  
- Endpoint capabilities
  - Inbound only
  - Outbound only
  - Bi-directional
  
- Must be flexible with 
  
- Endpoints are hierarchical
  - SystemVerilog simulation
    - VIP1
    - VIP2
  - Core0
  - Core1
  
# Outbound Calling
ep.get_api(Api).Method()
Api.Method(args) ->
  - Finds a top-level endpoint that supports the API 
  
- Endpoint represents:
  - Entire environment providing static/global methods
  - Static instance within an environment (eg VIP)
  - Creator of objects within another environment
  
- Leverage notion of default endpoint
  - Create object using default endpoint

 
Class.ctor() -> obj

