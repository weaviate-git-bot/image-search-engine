import os
import weaviate

client = weaviate.Client(
    url = "http://localhost:8080",
)

schemaConfig = {
    'class': 'MyImages',
    'vectorizer': 'img2vec-neural',
    'vectorIndexType': 'hnsw',
    'moduleConfig': {
        'img2vec-neural': {
            'imageFields': [
                'image'
            ]
        }
    },
    'properties': [
        {
            'name': 'image',
            'dataType': ['blob']
        },
        {
            'name': 'text',
            'dataType': ['string']
        }
    ]
}

try:
    client.schema.create_class(schemaConfig)
    print("Schema defined")
except Exception:
    print("Schema already defined, skipping...")