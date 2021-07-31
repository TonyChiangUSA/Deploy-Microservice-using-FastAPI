# Deploy-Microservice-using-FastAPI

```
$cd books_update
$gcloud config set run/region asia-southeast1
$gcloud builds submit --tag gcr.io/sue-gcp-learning-env/fast-api
$gcloud run deploy --image gcr.io/sue-gcp-learning-env/fast-api --platform managed
```
