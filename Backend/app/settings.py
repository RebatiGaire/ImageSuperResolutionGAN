# Flask settings
DEFAULT_FLASK_SERVER_NAME = '127.0.0.1'
DEFAULT_FLASK_SERVER_PORT = '5000'
DEFAULT_FLASK_DEBUG = '1'

# Flask-Restplus settings
RESTPLUS_SWAGGER_UI_DOC_EXPANSION = 'list'
RESTPLUS_VALIDATE = True
RESTPLUS_MASK_SWAGGER = False
RESTPLUS_ERROR_404_HELP = False

# ISRGAN client settings
DEFAULT_TF_SERVER_NAME = '172.17.0.2'
DEFAULT_TF_SERVER_PORT = 9000

# Multiple models properties
generic_model = {
    'ISRGAN_MODEL_NAME': 'generic_model',
    'ISRGAN_MODEL_SIGNATURE_NAME': 'serving_default',
    'ISRGAN_MODEL_INPUTS_KEY': 'input_2',
}

face_model = {
    'ISRGAN_MODEL_NAME': 'face_model',
    'ISRGAN_MODEL_SIGNATURE_NAME': 'serving_default',
    'ISRGAN_MODEL_INPUTS_KEY': 'input_2',
}

medical_model = {
    'ISRGAN_MODEL_NAME': 'medical_model',
    'ISRGAN_MODEL_SIGNATURE_NAME': 'serving_default',
    'ISRGAN_MODEL_INPUTS_KEY': 'input_2',
}
