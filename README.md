# Xss-Scanner

This project focuses on developing a XSS automated scanner but with 100 % accuracy as it will check if the alert pop has appeared in the browser or not.

A quick workflow :
  First it will grab the spider file then it will extract the get urls and store it in one file then it will also sort the urls if they are similar and store them in get_updated.txt in a folder named similar to the targeted website automatically.
  Then it will pick the urls from that file and will start testing by grabbing payloads from XSS payload file all 9(MAX) Urls will get tested simultaneously.

There are few path changes you have to do:

Main.py file:
  change the file_path parameter to the location where the spider.txt file is located
  
multithreading_testing.py file:
  Change the path for the geckodriver.exe
  Change the path for the XSS payload file 
  
  
Note: For mac users you have to configure the capabilties for the geckodriver
Note: You have to rename teh spider in such a way that for example the website is https://www.google.com then the name of the spider file will be https-www_google_com.txt.
  
 
