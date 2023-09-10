# ArubaInstantCertUpdate
Code to update Aruba IAP with a new cert when renewal happens.  I use this to deploy letsencrypt certificates.


Note:
When you create the certificate file you want to upload, Aruba's user guid says it must contain the following objects in this order top to bottom. 
Certificate
Intermediate Certificates
Root certificate (CA cert)
Private Key
