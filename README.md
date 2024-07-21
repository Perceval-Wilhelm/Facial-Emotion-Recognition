# Facial Expression Recognition Application

This project is a web application for real-time facial expression recognition using different machine learning models. The application is built using Streamlit and deployed using Docker.

## Project Structure

```

Facial-Expression-Recognition
│
├── Application
│   ├── app.py
│   ├── haarcascade_frontalface_default.xml
│   ├── Dockerfile
│   ├── requirements.txt
│   └── docker-compose.yml (optional)
│
├── Code
│   ├── CNN_from_scratch_method
│   │   ├── CNN_from_scratch.ipynb
│   │   └── model
│   │       ├── best_face_model.json
│   │       └── best_model.h5
│   │
│   ├── DeepFace_method
│   │   └── DeepFace.ipynb
│   │
│   ├── Demo_CNN_method
│   │   └── CNN_demo_real_time.py
│   │
│   ├── Demo_DeepFace_method
│   │   └── DeepFace_demo_real_time.py
│   │
│   └── SVM_method
│       ├── model
│       │   └── svm_emotion_model.joblib
│       └── SVM.ipynb
│
├── Dataset
└── Reports

```

## Features

- Real-time facial expression recognition using CNN, DeepFace, and SVM models.
- Visualization of detected faces with bounding boxes and predicted emotions.
- User-friendly interface built with Streamlit.
- Dockerized for easy deployment.

## Getting Started

### Prerequisites

- Python 3.8.19
- Docker
- Docker Compose (optional)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/Facial-Expression-Recognition.git
   cd Facial-Expression-Recognition/Application
   ```

2. Ensure you have a `requirements.txt` file in the `Application` directory with the dependencies listed above.

   ```bash
   pip install -r requirements.txt
   ```

### Usage

#### 1. Running the Application Locally

You can run the application locally using Streamlit.

```bash
streamlit run app.py
```

Open your web browser and navigate to `http://localhost:8501` to see the application.

#### 2. Running the Docker Container

If you prefer to use Docker, you can pull and run the Docker image directly from Docker Hub.

2.1. **Pulling the Docker Image**

   To pull the Docker image from Docker Hub, use the following command:
   
   ```bash
   docker pull percevalwilhelm/emotion-detection-app
   ```

2.2. **Running the Docker Container**

   Run the Docker container using:
   
   ```bash
   docker run -p 8501:8501 percevalwilhelm/emotion-detection-app
   ```

   You can now access the application in your web browser at `http://localhost:8501`.

#### 3. Using Docker

3.1. **Build the Docker Image:**

   ```bash
   docker build -t emotion-detection-app .
   ```

3.2. **Run the Docker Container:**

   ```bash
   docker run -p 8501:8501 emotion-detection-app
   ```

3.3. Open your web browser and navigate to `http://localhost:8501` to access the application.

#### 4. Using Docker Compose (Optional)

4.1. Create a `docker-compose.yml` file in the `Application` directory with the following content:

   ```yaml
   version: '3'
   services:
     app:
       build: .
       ports:
         - "8501:8501"
   ```

4.2. **Run Docker Compose:**

   ```bash
   docker-compose up
   ```

4.3. Open your web browser and navigate to `http://localhost:8501` to access the application.

### File Details

#### `app.py`

The main application script for Streamlit. It includes functions to load models, process images, predict emotions, and display results.

#### `Dockerfile`

Defines the Docker image configuration for the application.

#### `requirements.txt`

Lists all the Python dependencies required for the application.

#### `docker-compose.yml` (Optional)

Defines the Docker Compose configuration for the application.

### Model Files

- **CNN Model:**
  - `Code/CNN_from_scratch_method/model/best_face_model.json`
  - `Code/CNN_from_scratch_method/model/best_model.h5`

- **SVM Model:**
  - `Code/SVM_method/model/svm_emotion_model.joblib`

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Special thanks to the contributors of the DeepFace and Streamlit libraries.
- Thanks to all the open-source contributors and the community for their support.

Great! Since you've already pushed your Docker image to Docker Hub, you can update your `README.md` to reflect this, including instructions on how to pull and run the image. Here is the updated `README.md`:

```markdown
# Emotion Detection Application

This application detects emotions from images using different machine learning models (CNN, DeepFace, SVM). The application is built using Streamlit for the web interface and Docker for containerization.

## Project Structure

```
/Facial-Expression-Recognition
|---Application
|    |---app.py
|    |---haarcascade_frontalface_default.xml
|---Code
|    |---CNN_from_scratch_method
|    |    |---CNN_from_scratch.ipynb
|    |    |     |---model
|    |    |     |    |---best_face_model.json
|    |    |     |    |---best_model.h5
|    |---DeepFace_method
|    |    |---DeepFace.ipynb
|    |---Demo_CNN_method
|    |    |---CNN_demo_real_time.py
|    |---Demo_DeepFace_method
|    |    |---DeepFace_demo_real_time.py
|    |---SVM_method
|    |    |---model
|    |    |    |---svm_emotion_model.joblib
|    |    |---SVM.ipynb
```

## Requirements

- Python 3.8.19
- Docker

## Setup Instructions

### 1. Install Dependencies

First, ensure you have all the necessary dependencies installed. You can install them using the provided `requirements.txt` file.

```bash
pip install -r requirements.txt
```

### 2. Running the Application Locally

You can run the application locally using Streamlit.

```bash
streamlit run app.py
```

Open your web browser and navigate to `http://localhost:8501` to see the application.

### 3. Running the Docker Container

If you prefer to use Docker, you can pull and run the Docker image directly from Docker Hub.

#### 3.1 Pulling the Docker Image

To pull the Docker image from Docker Hub, use the following command:

```bash
docker pull percevalwilhelm/emotion-detection-app
```

#### 3.2 Running the Docker Container

Run the Docker container using:

```bash
docker run -p 8501:8501 percevalwilhelm/emotion-detection-app
```

You can now access the application in your web browser at `http://localhost:8501`.

### 4. Deploying the Docker Container

You can deploy the Docker container to various cloud providers. Below are the steps for some common platforms:

#### 4.1 Deploy to AWS ECS

1. **Create an ECS Cluster**:
   - Go to the ECS dashboard and create a new cluster.

2. **Create a Task Definition**:
   - Define a new task using the Docker image `percevalwilhelm/emotion-detection-app`.

3. **Run the Task**:
   - Create a service to run the task on your ECS cluster.

4. **Setup Networking**:
   - Ensure your ECS service has access to the internet.
   - Configure security groups and load balancers as necessary.

#### 4.2 Deploy to Google Kubernetes Engine (GKE)

1. **Create a GKE Cluster**:
   - Use the GCP Console to create a new Kubernetes cluster.

2. **Create a Deployment**:
   - Define a Kubernetes deployment using your Docker image.
   
   ```yaml
   apiVersion: apps/v1
   kind: Deployment
   metadata:
     name: emotion-detection-app
   spec:
     replicas: 1
     selector:
       matchLabels:
         app: emotion-detection-app
     template:
       metadata:
         labels:
           app: emotion-detection-app
       spec:
         containers:
         - name: emotion-detection-app
           image: percevalwilhelm/emotion-detection-app:latest
           ports:
           - containerPort: 8501
   ```

3. **Create a Service**:
   - Expose the deployment using a LoadBalancer service.
   
   ```yaml
   apiVersion: v1
   kind: Service
   metadata:
     name: emotion-detection-app-service
   spec:
     type: LoadBalancer
     ports:
     - port: 80
       targetPort: 8501
     selector:
       app: emotion-detection-app
   ```

4. **Deploy to GKE**:
   - Apply the deployment and service using `kubectl`.

   ```bash
   kubectl apply -f deployment.yaml
   kubectl apply -f service.yaml
   ```

#### 4.3 Deploy to Azure Kubernetes Service (AKS)

1. **Create an AKS Cluster**:
   - Use the Azure portal to create a new Kubernetes cluster.

2. **Follow Similar Steps as GKE**:
   - Define a deployment and service similar to the GKE steps.

### 5. Monitoring and Scaling

After deployment, monitor your application to ensure it is running smoothly. You can scale your deployment by increasing the number of replicas or adjusting your cloud provider's scaling options.

### 6. Setup CI/CD (Optional)

For continuous integration and deployment, set up a CI/CD pipeline using tools like GitHub Actions, Jenkins, or GitLab CI. This will automate building and pushing your Docker image and deploying your application to the cloud.

## Conclusion

These steps should help you successfully deploy and manage your Dockerized emotion detection application. If you encounter any issues, feel free to refer to the documentation or seek help from the community.
```

This `README.md` file provides detailed instructions for setting up, running, and deploying your application using Docker. If you have any specific modifications or additional information you would like to include, let me know!
