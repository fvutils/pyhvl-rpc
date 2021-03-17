
# Endpoint API

- Expose list of registered API and Bundle instances registered by peer
  - Should have capability to register default (null/global) instance
- Export list of registered API and Bundle types registered by peer
  - Specifically, we care about APIs and Bundles that have an implementation
    factory registered.
    
# Startup Sequence
- Python has the first opportunity to register
- Environment should wait for first timestep to obtain handles to Python-provided APIs
  - Maybe focus on first use in all cases
  

Two types of APIs on an endpoint:
- available static APIs (collection of static functions 
- Object constructors
  - Object has a presence on each side (?)
  
  
- APIs are uni-directional, with the tasks and functions either
  being import or export wrt Python.

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

