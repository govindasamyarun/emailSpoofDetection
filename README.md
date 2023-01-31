# Email Spoof Detection #
=====

An email parser is a software or tool used for data extraction from incoming emails used to automate workflow. Processing sensitive information using email parsers is riskier without implementing proper security controls. Threat actors could use legitimate domain and display name spoofing techniques to trick the parsers into processing fraudulent emails. 

Real-time email header analysis is essential to prevent spoofing attacks. This module will help perform email header analysis. 

# Installation

```bash
$ pip install emailSpoofDetection
```

## Python

```python
from emailSpoofDetection import emailSpoofDetection

header = "email-header"
emailDomain = "test.com"

output = emailSpoofDetection(header, emailDomain)

# { validEmail: True }
# { validEmail: False }

```