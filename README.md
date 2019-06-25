## Veanfi Heat Plugin
This plugin is made to request certificate from Venafi Platform or Cloud and save it to the
Heat resource.

### Installation
1. Install vcert and venafi-openstack-heat-plugin pip packages on openstack instance:
```bash
pip install vcert venafi-openstack-heat-plugin
``` 
2. Create directory /usr/lib/heat
```bash
mkdir -p /usr/lib/heat
```
3. link installed plugin into /usr/lib/heat
```bash
ln -s $(python -m site --user-site)/venafi-openstack-heat-plugin /usr/lib/heat/
``` 
4. restart heat engine:
```bash
sudo systemctl restart devstack@h-eng
```

### Usage

You can find example yml resource in [test_certificate.yml](venafi/resources/tests/fixtures/test_certificate.yml)  
We recommend to export credentials as variables and add them as hidden parameters to the stack.

Venafi Platform example:
If you want to use trust bundle you have to encode it into base64 string:
```bash
cat /opt/venafi/bundle.pem |base64 --wrap=10000
```

```bash
openstack stack create -t venafi/resources/tests/fixtures/test_certificate.yml \
--parameter common_name="tpp-usuu1.venafi.example.com" \
--parameter sans="IP:192.168.1.1","DNS:www.venafi.example.com","DNS:m.venafi.example.com","email:test@venafi.com","IP Address:192.168.2.2" \
--parameter tpp_user=admin \
--parameter tpp_password=${passsword} \
--parameter venafi_url=https://venafi.example.com/vedsdk \
--parameter zone=devops\\default \
--parameter trust_bundle=LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tCk1JSURmVENDQW1XZ0F3SUJBZ0lRVW1ZR0tqdzdmazI1Ylg3K29KZDIyakFOQmdrcWhraUc5dzBCQVFzRkFEQkYKTVNjd0pRWURWUVFMRXg1V1pXNWhabWtnVDNCbGNtRjBhVzl1WVd3Z1EyVnlkR2xtYVdOaGRHVXhHakFZQmdOVgpCQU1URVdoaExYUndjREV1YzNGc2FHRXVZMjl0TUI0WERURTVNRFl4TnpJeE1UVXhPRm9YRFRJd01EWXhOakl4Ck1UVXhPRm93UlRFbk1DVUdBMVVFQ3hNZVZtVnVZV1pwSUU5d1pYSmhkR2x2Ym1Gc0lFTmxjblJwWm1sallYUmwKTVJvd0dBWURWUVFERXhGb1lTMTBjSEF4TG5OeGJHaGhMbU52YlRDQ0FTSXdEUVlKS29aSWh2Y05BUUVCQlFBRApnZ0VQQURDQ0FRb0NnZ0VCQUxTYW5RQ0JFUEtXaG1KYzZ0T1Fod1oweExqN25xbm1KWGwrUjF0am9XN3RKUk5kCjljTzRyQzI0RjNFdFNOdnlmRldtSjBidUxEcWNmbkdKR2tWazFkOWtVZWI0elJKbXU0RlBOa1VzdjRRUkRoSGUKc2FydEowZU8wN2Rpek5nMXU4SG0rek5DcGk3TFZQRDhHRGJHeVN0WTVRblE1ZGU0ZllBMnpaV2NQNldRUjU4VApJblE0Q1NtejhiV01iRXdtQTgxdGlNVVR3YWMwTEFuL0hhYjVjOUVhaDlwc0NqSmMydFJiUjhpbmRRQWVmMmEzCkl3VEE1VUpzSHdpRjBGSHFRY2RDSG56NCtEdUVnVUlaaWZCcUNxSkhWdG53S0xya0YzZTNWZDdLemJBQXkzNlcKd2N0ZUhsdFk5UGlFUlRBSnp5WHRBNklscm5XT1lqNlRzNkVCYWJVQ0F3RUFBYU5wTUdjd0hRWURWUjBPQkJZRQpGRmxVc29uYVpwd25RTE9iTTFFNUYwdzNYamQrTUFrR0ExVWRFd1FDTUFBd0hBWURWUjBSQkJVd0U0SVJhR0V0CmRIQndNUzV6Y1d4b1lTNWpiMjB3SFFZRFZSMGxCQll3RkFZSUt3WUJCUVVIQXdFR0NDc0dBUVVGQndNQ01BMEcKQ1NxR1NJYjNEUUVCQ3dVQUE0SUJBUUJYTnorMEJ1YzFlL2o2bnJoUHlRb0g2RDM3N0ptUmplMjBDQW5TSDlwNwpWMW5FeHlOMS83dGtXL0JTOEJtSlF4Ty84dWhBVXNVQ3FWalpleVZVRnN5czc4VE5YeEVQQncrT3lLMlJLVWJDCmJsYTFPa1dTWkxVb1A3WThoTysyWU80R1BnU25ndDhXMWR3dHdjQ1gvMFZEaFNDUEoxU2N0RXUwMHlkSlZpMWEKYkhqb1I5VG0xYXNyeG53Z0ttcGpxQlpsbWxaUDBvZDZyMTRFVFlIZjJKelFxa24rTjY4UHN5Mm1VZlo0ZDBpRQptajdnU0RwUlpvNlk2NHd0WlBoZU9mWlZCaEg3SjhxRUdRcjk5dW5kc0FvSVlla2NVSkd1RjhBRStFZUVuQllWCmNKQWZtYUE2Zmx0R0puVnZlTUpod29xRDVBNzNrcWpzRlNFeUNvZ3VncTRCCi0tLS0tRU5EIENFUlRJRklDQVRFLS0tLS0K \
venafi-tests-stack-usuu1
```

Venafi Cloud example:
```bash
openstack stack create -t venafi/resources/tests/fixtures/test_certificate.yml \
--parameter common_name="cloud-ag1ya.example.com" \
--parameter sans="DNS:www.venafi.example.com","DNS:m.venafi.example.com" \
--parameter api_key=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx \
--parameter zone=Default
```

### ASCIINEMA video:
[![asciicast](https://asciinema.org/a/l3WfHpViFBhyINI3wY0mEyZkC.svg)](https://asciinema.org/a/l3WfHpViFBhyINI3wY0mEyZkC)
Also see examples in [Makefile](Makefile)
