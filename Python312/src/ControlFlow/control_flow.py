# control flow statements in automation
def check_service_status():
    # checking the status of multiple services in a cloud environment
    services = {
        "auth_service": "running",
        "database_service":"stopped",
        "payment_sevices": "running",
        "logging_service": "maintenance"
    }
    
    for service, status in services.item():
        if status == "running":
            print(f"(service) is operational.")
        elif status == "stopped":
            print(f"(service) is currently stopped.")
        elif status == "maintenance":
            print(f"(service) is under maintenance")
        else:
            print(f"(service) has an unknown status: {status}")
            
            
            