##IN Brute Force Challenge (Python + Socket)

##Overview
This project was created for a web application security challenge.  
The goal was to systematically guess a 3-digit PIN using a Python script, only using the socket library.

##How I Found the Address and Port
- The server executable starts and listens on `127.0.0.1:8888` (confirmed via browser and Wireshark).

##How I Determined What to Send
- Using browser developer tools (Network tab), I saw the form sends a POST request to /verify.
- The request body contains a field called (magicNumber).

##Constraints Encountered
- The server enforces a slowdown after repeated requests.
- To avoid being blocked, I added a 1-second sleep() between each attempt.

##What I Learned
- How raw HTTP POST requests work at the socket level.
- How web servers expect properly formatted HTTP requests.
- How simple brute-force attacks can be effective if no security measures are implemented.

##Security Improvements I Recommend
- Implement account lockout after several failed attempts.
- Add CAPTCHA verification.
- Increase PIN length (ex: 6+ digits or use alphanumeric passwords).
- Increase the delay before they can input again

