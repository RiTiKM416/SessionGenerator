![ZeroTwo](https://github.com/RiTiKM416/assets/blob/main/tanjiro.jpg)

# 🔐 Telethon StringSession Generator

A simple and secure Python script to generate a reusable Telegram `StringSession` using [Telethon](https://github.com/LonamiWebs/Telethon). This session can be used to deploy a userbot on any VPS.

♞ Use responsibly. This script logs in to your Telegram account and generates a session string that grants full access. Keep it private. ♞



**Cool Thing about SessionGenerator**

✯ Logs into your Telegram account using `api_id`, `api_hash`, and OTP.
✯ Handles **2FA (Two-Step Verification)** if enabled.

✯ Generates a **string-based session** (suitable for environment variables).

✯ Sends the session string to your **Saved Messages** as plain text.

✯ Fully **terminal-based**, no GUI or command-line arguments.

✯ **VPS-friendly**: ideal for deploying userbots and automation.


---

# **✩ Some Requirements ✩**

✯ Python 3.7+
✯ Telethon

Install dependencies with:
<pre> 
pip install telethon </pre>

# **✪ How To Use Use ✪**
  
  
**1. Clone the repository or download the script**
<pre>git clone https://github.com/RiTiKM416/SessionGenerator.git
cd telethon-session-generator</pre>
  
  
**2. Run The Script**
<pre>python SessionGenerator.py</pre>
  
  
**3. Follow the Prompts.**
▸ Enter your `API_ID` and `API_HASH` 〈 Get then from [Telegram](https://my.telegram.org/apps) 〉

▸ Enter your Phone Number with country code. 

▸ Enter The OTP (Received on telegram)

▸ Enter 2FA Password if enabled. 
  
  
**4. After Successfully logged in.** 

The Scriptt Will be generated. `StringSession`.  
The Session can be found in your saved messages. 
  
  
# 📄 License  

 This project is licensed under the [MIT License.](https://github.com/RiTiKM416/SessionGenerator/blob/main/LICENSE)


# 🤝 Disclaimer
This project is for educational and personal use only. The author is not responsible for any misuse, account bans, or damages caused by improper use. Always follow Telegram's [Terms of Service.](https://telegram.org/tos)

# 👨‍💻 Author  
Made with ❤️ using [Telethon](https://github.com/LonamiWebs/Telethon)

GitHub: [@RiTiKM416](https://github.com/RiTiKM416)
