WebDAV Server ![](https://travis-ci.com/rremizov/ansible-webdav-server.svg?branch=master)
=============

Setup and configure Nginx as a WebDAV server.

Features
--------

- Configure multiple virtual hosts.
- Use an existing SSL certificate or get one from [Let's Encrypt](https://letsencrypt.org/).
- Restrict access with Basic Auth.
- Configure allowlist to allow access from certain networks only.
- Configure [Rate Limiting](https://www.nginx.com/blog/rate-limiting-nginx/).

Requirements
------------

- Debian or Ubuntu.

Role Variables
--------------

**[defaults/main.yml](defaults/main.yml)**

Example
-------

```yaml
    webdav_server_hosts:
      - domain: www.example0.com
        root: /mnt/volume
        limit_request_rate: 1r/s
        limit_request_burst: 10
        limit_request_delay: nodelay
        client_max_body_size: 128m
        autoindex_enabled: yes
        basic_auth:
          - username: user0
            password: password0
            state: present
          - username: user1
            password: password1
            state: absent
        cidr_allowlist:
          - 1.2.3.4/32
          - 1.2.4.0/24
        state: enabled
      - domain: www.example1.com
        state: disabled
```
