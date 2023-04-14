# MobSF
![image](https://user-images.githubusercontent.com/129164792/232051017-ffdef1be-9387-47ed-9268-73f1c37800f5.png)


Step 1:

sudo docker run -it --rm -e MOBSF_API_KEY=4b869c0b5fef83e8d7205f0fe68d50e1a7a59bbce5c3d7da157d2c3fd8cce8fc -p 8000:8000 opensecurity/mobile-security-framework-mobsf:latest

Step 2:

python MOBSF_CICD.py 'app-qa1.1.apk' 'http://192.168.0.30:8000' 4b869c0b5fef83e8d7205f0fe68d50e1a7a59bbce5c3d7da157d2c3fd8cce8fc upload

Step 3:

python MOBSF_CICD.py 'app-qa1.1.apk' 'http://192.168.0.30:8000' 4b869c0b5fef83e8d7205f0fe68d50e1a7a59bbce5c3d7da157d2c3fd8cce8fc scan

Step 4:

python MOBSF_CICD.py 'aapp-qa1.1.apk' 'http://192.168.0.30:8000' 4b869c0b5fef83e8d7205f0fe68d50e1a7a59bbce5c3d7da157d2c3fd8cce8fc json
python MOBSF_CICD.py 'app-qa1.1.apk' 'http://192.168.0.30:8000' 4b869c0b5fef83e8d7205f0fe68d50e1a7a59bbce5c3d7da157d2c3fd8cce8fc pdf

Step 5:

python MOBSF_CICD.py 'app-qa1.1.apk' 'http://192.168.0.30:8000' 4b869c0b5fef83e8d7205f0fe68d50e1a7a59bbce5c3d7da157d2c3fd8cce8fc delete 
