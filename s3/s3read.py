import boto3

s3 = boto3.client('s3')
response = s3.list_buckets()

print("The raw response is: ")
print(response)

print("\nThe items in response are")
for things in response:
    print(things)

print("\nThe buckets in the [Bucket] response item were: ")
for bucket in response['Buckets']:
    print(bucket["Name"])