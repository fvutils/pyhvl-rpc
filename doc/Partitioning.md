
- hvl-rpc implements 
    - API definition decorators
    - Endpoint base API, including 
    
- Specializations implement
    - Implementation for `import` APIs
        - These implement the bridge from method calls to appropriate back-end action
    - Endpoint implementation
        - These do things such as message passing
	    - Responsible for implementing `export`-API call bridges
	    
In short, hvlrpc mostly functions as a user-level facade and delegates much
of the transport implementation (moving data, calling methods) to the 
environment-specific implementations

This means that an endpoint implementation primarily needs to be provided
opportunities to wrap implementations that are then used by other parts
of the system.
    - Create an API-import implementation
    - Notified when an API-export implementation is registered with an endpoint
        - Should 
    
Endpoint must signal something of its capabilities
    - Are call-ins supported? If not, then registering export implementations is a problem
    - Are call-outs supported? If not, then there shouldn't be any imports registered
    - Are call-out tasks supported? If not, should flag
    - Must flag if variadic arguments are not supported



        