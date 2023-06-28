# Weaviate Image Search Engine

Image search engine powered by Vector database and ResNet-50.

## Installation and Setup

1. Run docker compose file:

```sh
docker compose up -d
```

2. Activate the environment:

```sh
pip3 install pipenv && pipenv install && pipenv shell
```

3. Launch Streamlit:

```
streamlit run streamlit_app.py --server.enableCORS false --server.enableXsrfProtection false
```

## Images

Feel free to insert your images in `img` folder and see if the database suggests you similar images.

## Weaviate Schema

This is the schema implemented in Weaviate. You can modify the class name, change the vectorizer or insert more properties.

```python
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
```
