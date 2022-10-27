# CSC 474 – Homework 4

## Firewalls

Assumptions:

- The *DMZ mail gateway* and the *DMZ mail server* are the same machine/have the same IP address.
- All servers run on the default port/the port assumed in this list (e.g. 25 for SMTP, see Piazza).
- The clients in the *Internal Protected Network* are configured to use the gateways (otherwise they will not be able to use SMTP to outside servers etc.).
- The provided rules are supposed to only apply to the *Workstations* in the *Internal Protected Network*. If the *Application and Database Servers* should also have those rights, all but the last rule in the internal firewall need to be duplicated and `10.0.2.0/24` replaced with `10.0.1.0/24` in the new set. If all clients in the *Internal Protected Network* are supposed to have access, including ones not mentioned in the graphic, replace `10.0.2.0/24` with `*`.
- Web requests from clients from the *Internal Protected Network* to the *Web Server* in the *Internal DMZ Network* still need to go through the *Web Proxy*.
- The provided servers in the *Internal DMZ Network* are the only present server that need to be accessible through SSH.

### External Firewall

| Action | Src IP    | Src Port | Dest IP   | Dest Port | Protocol | Flags | Comment                                                |
| ------ | --------- | -------- | --------- | --------- | -------- | ----- | ------------------------------------------------------ |
| allow  | \*        | \*       | 10.0.0.11 | 25        | SMTP     |       | SMTP outside access of Email server incoming (Rule 1)  |
| allow  | 10.0.0.11 | 25       | \*        | \*        | SMTP     |       | SMTP outside access of Email server outgoing (Rule 1)  |
| allow  | 10.0.0.11 | \*       | \*        | 25        | SMTP     |       | Proxy SMTP outgoing (Rule 1)                           |
| allow  | \*        | 25       | 10.0.0.11 | \*        | SMTP     |       | Proxy SMTP incoming (Rule 1)                           |
| allow  | \*        | \*       | 10.0.0.11 | 993       | IMAPS    |       | IMAPS outside access of Email server incoming (Rule 3) |
| allow  | 10.0.0.11 | 993      | \*        | \*        | IMAPS    | ACK   | IMAPS outside access of Email server outgoing (Rule 3) |
| allow  | 10.0.0.13 | \*       | \*        | 80        | HTTP     |       | Proxy HTTP outgoing (Rule 4)                           |
| allow  | \*        | 80       | 10.0.0.13 | \*        | HTTP     |       | Proxy HTTP incoming (Rule 4)                           |
| allow  | 10.0.0.13 | \*       | \*        | 443       | HTTPS    |       | Proxy HTTPS outgoing (Rule 4)                          |
| allow  | \*        | 443      | 10.0.0.13 | \*        | HTTPS    | ACK   | Proxy HTTPS incoming (Rule 4)                          |
| allow  | \*        | \*       | 10.0.0.10 | 80        | HTTP     |       | HTTP outside access of web server incoming (Rule 5)    |
| allow  | 10.0.0.10 | 80       | \*        | \*        | HTTP     |       | HTTP outside access of web server outgoing (Rule 5)    |
| allow  | \*        | \*       | 10.0.0.10 | 443       | HTTPS    |       | HTTPS outside access of web server incoming (Rule 5)   |
| allow  | 10.0.0.10 | 443      | \*        | \*        | HTTPS    | ACK   | HTTPS outside access of web server outgoing (Rule 5)   |
| allow  | 10.0.0.12 | \*       | \*        | 53        | DNS      |       | Proxy DNS server outgoing (Rule 6)                     |
| allow  | \*        | 53       | 10.0.0.12 | \*        | DNS      |       | Proxy DNS server incoming (Rule 6)                     |
| allow  | \*        | \*       | 10.0.0.12 | 53        | DNS      |       | Outside access of DNS server incoming (Rule 7)         |
| allow  | 10.0.0.12 | 53       | \*        | \*        | DNS      |       | Outside access of DNS server outgoing (Rule 7)         |
| deny   | \*        | \*       | \*        | \*        | \*       |       | Deny everything not covered above                      |


### Internal Firewall

| Action | Src IP      | Src Port | Dest IP     | Dest Port | Protocol | Flags | Comment                               |
| ------ | ----------- | -------- | ----------- | --------- | -------- | ----- | ------------------------------------- |
| allow  | 10.0.2.0/24 | \*       | 10.0.0.11   | 25        | SMTP     |       | SMTP incoming (Rule 1)                |
| allow  | 10.0.0.11   | 25       | 10.0.2.0/24 | \*        | SMTP     |       | SMTP outgoing (Rule 1)                |
| allow  | 10.0.2.0/24 | \*       | 10.0.0.11   | 143       | IMAP     |       | IMAP incoming (Rule 2)                |
| allow  | 10.0.0.11   | 143      | 10.0.2.0/24 | \*        | IMAP     |       | IMAP outgoing (Rule 2)                |
| allow  | 10.0.2.0/24 | \*       | 10.0.0.11   | 993       | IMAPS    |       | IMAPS incoming (Rule 2)               |
| allow  | 10.0.0.11   | 993      | 10.0.2.0/24 | \*        | IMAPS    | ACK   | IMAPS outgoing (Rule 2)               |
| allow  | 10.0.2.0/24 | \*       | 10.0.0.13   | 80        | HTTP     |       | HTTP incoming (Rule 4)                |
| allow  | 10.0.0.13   | 80       | 10.0.2.0/24 | \*        | HTTP     |       | HTTP outgoing (Rule 4)                |
| allow  | 10.0.2.0/24 | \*       | 10.0.0.13   | 443       | HTTPS    |       | HTTPS incoming (Rule 4)               |
| allow  | 10.0.0.13   | 443      | 10.0.2.0/24 | \*        | HTTPS    | ACK   | HTTPS outgoing (Rule 4)               |
| allow  | 10.0.2.0/24 | \*       | 10.0.0.12   | 25        | DNS      |       | DNS incoming (Rule 6)                 |
| allow  | 10.0.0.12   | 25       | 10.0.2.0/24 | \*        | DNS      |       | DNS outgoing (Rule 6)                 |
| allow  | 10.0.2.0/24 | \*       | 10.0.0.10   | 22        | SSH      |       | SSH incoming to Web Server (Rule 8)   |
| allow  | 10.0.0.10   | 22       | 10.0.2.0/24 | \*        | SSH      |       | SSH outgoing to Web Server (Rule 8)   |
| allow  | 10.0.2.0/24 | \*       | 10.0.0.11   | 22        | SSH      |       | SSH incoming to Email Server (Rule 8) |
| allow  | 10.0.0.11   | 22       | 10.0.2.0/24 | \*        | SSH      |       | SSH outgoing to Email Server (Rule 8) |
| allow  | 10.0.2.0/24 | \*       | 10.0.0.12   | 22        | SSH      |       | SSH incoming to DNS Server (Rule 8)   |
| allow  | 10.0.0.12   | 22       | 10.0.2.0/24 | \*        | SSH      |       | SSH outgoing to DNS Server (Rule 8)   |
| allow  | 10.0.2.0/24 | \*       | 10.0.0.13   | 22        | SSH      |       | SSH incoming to Web Proxy (Rule 8)    |
| allow  | 10.0.0.13   | 22       | 10.0.2.0/24 | \*        | SSH      |       | SSH outgoing to Web Proxy (Rule 8)    |
| deny   | \*          | \*       | \*          | \*        | \*       |       | Deny everything not covered above     |

## Routing

### 2.a BGP hijack

*subprefix* is more dangerous.

Because most routers will prefer more specific routes (longest-prefix matching). This means that if an attacker knows the exact address of their target, they can generate a BGP advertisement which will be more specific than anything else and will therefore be accepted by any AS/device within an AS. This means, the attacker gets *all* traffic for that IP address.

### 2.b BGP filtering rules

For peers it might be difficult because the other party's customers might change frequently and keeping the filtering rules up-to-date might not be feasible.

Customers will always get all the announcements from their provider, so filtering them isn't really possible because it is impossible to know whether or not the route is legitimate or not.

So the only role that can use filtering is providers because they can contractually fix which prefix the customer gets and throw away anything from outside that prefix. The customer would probably also not want to route other routes because the extra traffic costs them money. The only exception would be if the customer is a comparatively small provider that has changing customers with their prefixes. At this point, the same argument as with peers applies.

### 2.c BGPsec

- Cryptography necessary for certificate checking is computationally expensive, so this adds an extra load on routers.
- If only some of the routers/ASs support this, the gained security is very small.