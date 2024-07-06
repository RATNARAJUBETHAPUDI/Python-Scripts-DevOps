# datatypes usage in devops operations
def string_operations():
    # parsing a URL from a configuration file
    config_url = "https://api.Roboshop.com/v1/resources?query=test"
    
    #Extracting the protocol , domain and path
    protocol = config_url.split("://")[0]
    domain= config_url.split("://")[1].split("/")[0]
    path = config_url.split(domain)[1]
    
    
    print(f"protocol: {protocol}")
    print(f"Domain: {domain}")
    print(f"Path: {path}")
    
    # Formatting the log message
    service_name = "auth_service"
    status = "running"
    log_message = f"[{service_name}] Status: {status.upper()}"
    print(log_message)
    
def integer_operations():
    # Monitoring system resources
    total_memory_mb = 8192  # total memory inm mb
    used_memory_mb = 6144   # used memory in mb
    
    # Calculating free memory percentage
    free_memory_percentage =((total_memory_mb- used_memory_mb / total_memory_mb)) * 100
    print(f"Free Memory: {free_memory_percentage:.2f}%")
    
    # counting the number of requests
    intial_requests = 1200
    new_requests = 300
    total_requests = intial_requests + new_requests
    print("Total Requests:{total_requests}") 
    
def float_operations():
    # calculating CPU usage
    total_cpu_usage = 1000.0 # totalcpu usage in milli sections
    idle_cpu_usage = 200.0 # total cpu usage in millis
    
    # calculating cpu usage percentage
    cpu_usage_percentage =((total_cpu_usage - idle_cpu_usage) / total_cpu_usage) * 100
    print(f"CPU Usage:{cpu_usage_percentage:.2f}%")
    
    #Converting storage size
    file_size_bytes = 10485760
    file_size_mb = file_size_bytes /(1024 * 1024)
    print(f"File size: {file_size_mb:.2f} MB")
    
def boolean_operations():
    # checking service status
    is_service_active = True
    has_recent_errors = False
    
    if is_service_active  and not has_recent_errors:
        print("The service is activr and running smoothly.")
    else:
        print("The service is either down ha recent errors.")
        
    # Adding feature to existing deployment
    is_feature_enabled = False
    if is_feature_enabled:
        print("The new feature is added.") 
    else:
        print("The feature is not enabled.")
        
def main():
 print("string operations:")
 
 print("\nInteger operations:")
 print("\nfloat operations:")
 print("\nBoolean operations:")
 
 if __name__ == "__main__":
     main()