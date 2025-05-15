import fitz
import base64
import json

def lambda_handler(event, context):
    data = json.loads(event['body'])
    file_encoded = data['file']
    file_extension = data['extension']
    file_bytes = base64.b64decode(file_encoded)
    

    # Open PDF from bytes
    doc = fitz.open(stream=pdf_bytes, filetype="pdf")
    text = "".join([page.get_text() for page in doc])


    return {
        'statusCode': 200,
        'body': f'Received text: {text}'
    }