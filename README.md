# Google_NDB_Emulator

Here is a YouTube video about this project https://youtu.be/4_zZzEzeuKE

This allows you to test your Google NDB code locally in a development environment rather than working with your actual database. 
It lets you work with the Google Cloud Datastore emulator to test your Google NDB code.

Running the example program:

  note: when referring to the terminal it should be your command line terminal. Don’t use PowerShell. For info on how to run the command line on Visual Studio Code go here https://docs.google.com/document/d/1bbWogGdQ48rMJFB9Wxvtt7XWw5SUfP07BVl6cHk69hk/edit?usp=sharing

  Step 1: Download NDBEmulator folder or the main.py, the requirements.txt, and the app.yaml individually and open it whatever editor you use.

  Step 2: Install google cloud SDK if you haven't already done so https://cloud.google.com/sdk/docs/install

  Step3: After navigating to the NDBEmulator folder in your terminal run:  gcloud components install cloud-datastore-emulator
  (if you want more on datastore-emulator go to https://cloud.google.com/datastore/docs/tools/datastore-emulator)

  Step 4: in your terminal run: 
    pip install datastore-viewer

  Step 5: in your terminal run: 
    pip install -r requirements.txt

  Step 6: in your terminal run: 
    gcloud beta emulators datastore start --data-dir=. --project test --host-port "127.0.0.1:8001"

  Step 7: Open a new terminal but leave the emulator terminal running. This can be done in visual studio code by clicking the plus sign on choosing Terminal and New Terminal.

  Step8: Make sure you are still navigated to the NDBEmulator folder in your terminal.

  Step 9: in your new terminal run:
    For mac:
      export FLASK_APP=main 
      (press return)
      export FLASK_ENV=development
      (press return)
      flask run
    For PC:
      set FLASK_APP=main
      (press return)
      set FLASK_ENV=development
      (press return)
      flask run

     Alternatively, you can run:
     python3 main.py

     or just

     python main.py

    For info on how to run Flask from the command line on Visual Studio Code go here https://docs.google.com/document/d/1bbWogGdQ48rMJFB9Wxvtt7XWw5SUfP07BVl6cHk69hk/edit?usp=sharing

   Step 10: in your browser go to http://127.0.0.1:5000
   (you'll see the main page)

   Step 11: go to http://127.0.0.1:5000/test
   (you'll see what has been added to the local database)

   step12: Open a 3rd terminal. Make sure you are still navigated to the NDBEmulator folder in your new terminal.

   step 13: in your new terminal run:
    For Mac:
      export DATASTORE_EMULATOR_HOST=localhost:8001 && datastore-viewer
    For PC:
      set DATASTORE_EMULATOR_HOST=localhost:8001 && datastore-viewer

   Step 14: in your browser go to http://127.0.0.1:8082/

   Step 15: in the search box in the upper left-hand corner type:
        test

    Step16:
       hit refresh and it should show you the data saved in your local development database
       
 Adding the necessary code to your existing Flask Google NDB project:
 
   note: when referring to the terminal it should be your command line terminal. Don’t use PowerShell.

  Step 1: To your existing code add:  
        import mock
        from flask import Flask
        from google.cloud import ndb
        import google.auth.credentials
        import os
        
        os.environ["DATASTORE_DATASET"] = "test"
        os.environ["DATASTORE_EMULATOR_HOST"] = "127.0.0.1:8001"
        os.environ["DATASTORE_EMULATOR_HOST_PATH"] = "127.0.0.1:8001/datastore"
        os.environ["DATASTORE_HOST"] = "http://127.0.0.1:8001"
        os.environ["DATASTORE_PROJECT_ID"] = "test"
        
        credentials = mock.Mock(spec=google.auth.credentials.Credentials)
        
 step 1.5 Anywhere you want to test the database add:
          client = ndb.Client(project="test", credentials=credentials)
          with client.context():
        
  Step 2: Install google cloud SDK if you haven't already done so https://cloud.google.com/sdk/docs/install

  Step3: After navigating to your project folder in your terminal run:  gcloud components install cloud-datastore-emulator
  (if you want more on datastore-emulator go to https://cloud.google.com/datastore/docs/tools/datastore-emulator)

  Step 4: in your terminal run: 
    pip install datastore-viewer

  Step 5: add the requirements.txt info to your current requirements.txt and in your terminal run: 
    pip install -r requirements.txt

  Step 6: in your terminal run: 
    gcloud beta emulators datastore start --data-dir=. --project test --host-port "127.0.0.1:8001"

  Step 7: Open a new terminal but leave the emulator terminal running. This can be done in visual studio code by clicking the plus sign on choosing Terminal and New Terminal.

  Step8: Make sure you are still navigated to the NDBEmulator folder in your terminal.

  Step 9: in your new terminal run:
    For mac:
      export FLASK_APP=main 
      (press return)
      export FLASK_ENV=development
      (press return)
      flask run
    For PC:
      set FLASK_APP=main
      (press return)
      set FLASK_ENV=development
      (press return)
      flask run

     Alternatively, you can run:
        python3 main.py

     or just

        python main.py

    For info on how to run Flask from the command line on Visual Studio Code go here https://docs.google.com/document/d/1bbWogGdQ48rMJFB9Wxvtt7XWw5SUfP07BVl6cHk69hk/edit?usp=sharing


   Step 10: in your browser go to http://127.0.0.1:5000
   (you'll see the main page)

   Step 11: go to http://127.0.0.1:5000/test
   (you'll see what has been added to the local database)

   step12: Open a 3rd terminal. Make sure you are still navigated to the NDBEmulator folder in your new terminal.

   step 13: in your new terminal run:
    For Mac:
      export DATASTORE_EMULATOR_HOST=localhost:8001 && datastore-viewer
    For PC:
      set DATASTORE_EMULATOR_HOST=localhost:8001 && datastore-viewer

   Step 14: in your browser go to http://127.0.0.1:8082/

   Step 15: in the search box in the upper left-hand corner type:
        test

    Step16:
       hit refresh and it should show you the data saved in your local development database

	

![image](https://user-images.githubusercontent.com/61996426/127399471-c1a54238-2d28-4ecb-83bd-f656e971df93.png)
