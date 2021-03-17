
- hvl-rpc implements 
    - API definition decorators
    - Endpoint base API, including 
    
- Specializations implement
    - Implementation for `import` APIs
        - These implement the bridge from method calls to appropriate back-end action
    - Endpoint implementation
        - These do things such as message passing
	    - Responsible for implementing `export`-API call bridges

        