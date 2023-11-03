# Scrapyscrape

`Scrapyscrape` is an advanced web crawling and web scraping project designed to extract information on products from various websites for data analysis purposes. This project is built using the Scrapy framework and integrates various AWS services and Apache Airflow for orchestration.

## Table of Contents

- [Introduction](#introduction)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [AWS Deployment](#aws-deployment)
- [Airflow Orchestration](#airflow-orchestration)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This web crawler is designed to run quarterly to collect up-to-date information about products across different platforms. It is scheduled and orchestrated using Apache Airflow and hosted on AWS infrastructure, utilizing services such as EC2 and ECR for storing and running the Dockerized application.

## Technologies Used

- **Scrapy**: An open-source and collaborative web crawling framework for Python used to extract the data from the websites.
- **Docker**: Used to containerize the Scrapy application for consistent deployment and scalability.
- **Amazon Web Services (AWS)**:
  - **ECR (Elastic Container Registry)**: Used to store Docker images of the Scrapy application.
  - **EC2 (Elastic Compute Cloud)**: Used to run the Docker container on a virtual server in the AWS cloud.
- **Apache Airflow**: Used to orchestrate the workflow of the crawling process, including scheduling and monitoring the crawler runs.
- **Python**: The primary programming language used for developing the project.
- **Git**: Used for version control and source code management.

## Installation

Before you can run the scraper, ensure you have Docker and Python installed on your system. Then, clone the repository:

```sh
git clone https://github.com/quinlayen/scrapyscrape.git
cd scrapyscrape
```
## Usage

To use the scrapyscrape application, you need to first build the Docker image from the Dockerfile provided in the repository. Run the following command:
```sh
docker build -t scrapyscrape .
```
Once the image is built, you can run it with Docker:

```sh
docker run scrapyscrape
```
## AWS Deployment

The Docker image for the scraper can be pushed to AWS ECR with the following commands:

```sh
$(aws ecr get-login --no-include-email --region your-region)
docker tag scrapyscrape:latest your-ecr-repository-url/scrapyscrape:latest
docker push your-ecr-repository-url/scrapyscrape:latest
```

To run the scraper on AWS EC2:

    Pull the Docker image from ECR.
    Deploy an EC2 instance.
    Run the Docker container on the EC2 instance.

Refer to AWS documentation for detailed steps on ECR and EC2 setup.

## Airflow Orchestration

To orchestrate the scraper with Apache Airflow:

    Set up Apache Airflow on an EC2 instance or use the managed Apache Airflow service on AWS.
    Create a DAG for the scraping process.
    Schedule the DAG to run quarterly.
    Monitor the DAG's performance and logs through the Airflow web interface.

## Contributing

We welcome contributions to the scrapyscrape project. If you would like to contribute, please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
