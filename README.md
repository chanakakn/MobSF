# MobSF
![image](https://user-images.githubusercontent.com/129164792/232051017-ffdef1be-9387-47ed-9268-73f1c37800f5.png)

 Mobile SecurityFramework

 Licence: GPL 3

 Available on GitHub: https://github.com/MobSF/Mobile-Security-Framework-MobSF

 Online analyzer: https://mobsf.live/

![image](https://user-images.githubusercontent.com/129164792/232052032-18e20628-e4ce-419b-a1f6-c0d402236842.png)


Step 1:

sudo docker run -it --rm -e MOBSF_API_KEY=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx -p 8000:8000 opensecurity/mobile-security-framework-mobsf:latest

Step 2:

python MOBSF_CICD.py 'app-qa1.1.apk' 'http://192.168.0.30:8000' xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx upload

Step 3:

python MOBSF_CICD.py 'app-qa1.1.apk' 'http://192.168.0.30:8000' xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx scan

Step 4:

python MOBSF_CICD.py 'aapp-qa1.1.apk' 'http://192.168.0.30:8000' xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx json
python MOBSF_CICD.py 'app-qa1.1.apk' 'http://192.168.0.30:8000' xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx pdf

Step 5:

python MOBSF_CICD.py 'app-qa1.1.apk' 'http://192.168.0.30:8000' xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx delete 
