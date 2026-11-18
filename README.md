# Student-CI-Project

A small Python project used to demonstrate Continuous Integration with Jenkins and GitHub webhooks (CMSC 426, In-Class Activity 3).

## Structure

```
Student-CI-Project/
  app.py             application source code
  tests/
    __init__.py
    test_app.py      automated unit tests
  build.bat          Windows batch build script used by Jenkins
  Jenkinsfile        optional declarative pipeline
  README.md
```

## Requirements

- Python 3.8 or newer (no third-party packages needed)
- Git

## Run the application

```
python app.py
```

Expected output:

```
Application started
2 + 3 = 5
5 - 2 = 3
4 * 3 = 12
```

## Run the tests

```
python -m unittest discover -s tests -t .
```

A successful run ends with `OK`. Any failing test returns a non-zero exit code, which makes the Jenkins build fail.

## Jenkins setup

1. Create a Freestyle project named `Student-CI-Project`.
2. Under Source Code Management choose Git and enter this repository URL.
3. Under Build Triggers tick `GitHub hook trigger for GITScm polling`.
4. Add the build step `Execute Windows batch command` with the content `build.bat`.
5. In GitHub open Settings, Webhooks, Add webhook:
   - Payload URL: `https://<your-ngrok-address>/github-webhook/`
   - Content type: `application/json`
   - Event: Just the push event
6. Push a commit and confirm a new build starts in Jenkins.

To use the pipeline instead, create a Pipeline job with `Pipeline script from SCM` and script path `Jenkinsfile`.

## Failure experiment

Change an expected value in `tests/test_app.py`, push, and confirm Jenkins marks the build as failed. Restore the original value and push again to confirm the build passes.

____

Change to test webhook