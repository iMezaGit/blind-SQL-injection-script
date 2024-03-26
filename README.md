# blind-SQL-injection-script
This Python3 script automates SQL injections to web application parameters vulnerable to Boolean-based Blind SQL Injections.

This script does not generate the SQL injection, and do not detect the condition tested. It's purpose is to automate the brute force of each character contained in your query, in order to leak to entire string.

> [!IMPORTANT]
> This tool was made for educational purposes, and should not be used on a real target without consent.

---
## Set-up 
In order to use this script, the library `pwntools` (an exploit development toolkit for python) and python's HTTP requests library, are needed. To install both, you can copy the following commands: 

```
python3 -m pip install --upgrade pwntools
python3 -m pip install requests
```
## Use

To use this script you have to adjust certain things within it.

* **Constants**: First change the example values en in the `# Constants` section.This include:
    * Target URL
    * Mandatory Cookies
    * Necessary Headers 

    > [!WARNING]
    > **Do not change** the constant named **ASCII**

* **Injection**: Adjust the SQL injection as needed for each specific case. Note that you'll have to use the format:
 `(... ascii(substring(data_to_leak),{place},1) ...) = {char}`
Otherwise the script will not work, unless you modify it.
* **Condition**: Lastly, change the condition according to your case. For example, a status code or certain string that the SQL injection reveals.

## Example
In the image below, you can see the script being used in the resolution of the **_IMF: 1_** vulnerable machine, from [VulnHub](https://www.vulnhub.com/entry/imf-1,162/).

![Example image](/images/1.png)

As you can see, in this case, I enumerated the **data base name** and the **user name** from a MySQL database. This information was used to dump the data base with the same script.



