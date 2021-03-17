
- User defines all APIs as a Python class with context methods
- API definitions are associated with an endpoint
  - Launcher environments typically register endpoints and bundles as part of startup
  - Connection environments (eg core monitor) may register from Python side
  
- Imports (Python calls HVL)
  - Rely on API implementation being associated with endpoint
  - HVL must associate implementation
  - User obtains API implementation from API class (default) or from endpoint
  
- Export (HVL calls Python)
  - Use API class as default
  - Allow user to change registration