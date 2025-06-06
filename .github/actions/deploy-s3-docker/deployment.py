import os
from pathlib import Path
import boto3
from botocore.config import Config


def run():
    bucket = os.environ["INPUT_BUCKET"]
    bucket_region = os.environ["INPUT_REGION"]
    dist_folder = os.environ["INPUT_DIST-FOLDER"]

    configuration = Config(region_name=bucket_region)

    s3_client = boto3.client("s3", config=configuration)

    for root, subdirs, files in os.walk(dist_folder):
        for file in files:
            s3_client.upload_file(os.path.join(root, file), bucket, file)

    website_url = f"http://{bucket}.s3-website-{bucket_region}.amazonaws.com"
    Path(os.environ["GITHUB_OUTPUT"]).write_text(
        f"website-url={website_url}", newline="\n"
    )


if __name__ == "__main__":
    run()
