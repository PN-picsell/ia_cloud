import boto3

def detect_text(photo, bucket):

    client=boto3.client('rekognition')

    response=client.detect_text(Image={'S3Object':{'Bucket':bucket,'Name':photo}})
                        
    textDetections=response['TextDetections']
    print ('Detected text\n----------')
    for text in textDetections:
            print ('Detected text:' + text['DetectedText'])
            print ('Confidence: ' + "{:.2f}".format(text['Confidence']) + "%")
            print ('Id: {}'.format(text['Id']))
            if 'ParentId' in text:
                print ('Parent Id: {}'.format(text['ParentId']))
            print ('Type:' + text['Type'])
            print()
    return text['DetectedText']

def awsRekognition(url):

    bucket='s3.eu-west-1.amazonaws.com'
    photo=url
    text=detect_text(photo,bucket)
    return text


if __name__ == "__main__":
    main('https://i.ibb.co/XbNhmFK/hello-world.png')