# Weaviate Image Search Engine

Weaviate is a vector database that allows you to create and query embeddings with pre-trained deep learning models. It integrates with ResNet-50 to vectorize images, making it possible to build an image similarity search engine with relative ease.

## Installation and Setup

1. Run docker compose file:

To run Weaviate locally, use their Docker Compose config that supports the image module.

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
