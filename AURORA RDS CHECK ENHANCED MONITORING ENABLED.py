import boto3
def check_enhancedmonitoring_enabled(dbinstance):
    try:
        eclient = boto3.client('rds')
        rds_instances = eclient.describe_db_instances(DBInstanceIdentifier=dbinstance)
        if rds_instances['DBInstances'][0]['MonitoringInterval'] == 0:
            return False
            sys.exit(1)
            print('The instance you selected doesn''t have Enhanced Monitoring activated.')
        else:
            return True

check_enhancedmonitoring_enabled(dbinstance='dbinstance')