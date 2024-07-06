def automate_backup_process():
    # automating backup processs with retries
    max_retries = 3
    retry_count = 0
    backup_sucessful = False
    perform_backup = True
    check_service_status = True
    
    while retry_count < max_retries and not backup_sucessful:
        try:
            print("Attempting backup...")
            perform_backup()
            backup_sucessful = True
            print("Backup completed successfully.")
        except Exception as e:
            retry_count += 1
            print(f"backup failed. retry {retry_count}/{max_retries}.Error: {e}")
    if not backup_sucessful:
        print("Backup after maximum retries. please check the system.")
        
def perform_backup():
    import random
    if random.choice([True , False]):
        raise Exception("Simulated backup error.")
def processs_logs():
    logs= [
        "2024-07-05 12:00:00 INFO Service started",
        "2024-07-05 12:01:00 Error Failed to connect to to database",
        "2024-07-05 12:02:00  WARN High memory usage detected",
        "2024-07-05 12:03:00 INFO Service running smootly"
    ]
    error_logs = []
    
    for log in logs:
        if "ERROR" in log:
            error_logs.append(log)
            
    print("Error Logs:")
    for error in error_logs:
        print(error)
      
def deploy_feature_toggles():
    features = {
        "feature_a": True,
        "feature_b": False,
        "feature_c": True
        
    }
    for feature, is_enabled in feature.items():
        if is_enabled:
            print(f"{feature} is enabled and will be deployed.")
        else:
            print(f"{feature} is disabled and will not be deployed.")
            
def main():
    print("checking service status:")
                        
        