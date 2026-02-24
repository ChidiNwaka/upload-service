import os

class Config:
    ENV = os.getenv("ENV", "dev")
    PORT = int(os.getenv("PORT", "5000"))

    DATABASE_URL = os.getenv("DATABASE_URL", "")

    AWS_REGION = os.getenv("AWS_REGION", "us-west-2")
    S3_BUCKET = os.getenv("S3_BUCKET", "")

