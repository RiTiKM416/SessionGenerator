#!/usr/bin/env python3
# Telethon StringSession Generator Script
# Logs in to Telegram, creates a StringSession, and sends it to Saved Messages.

from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from telethon.errors import SessionPasswordNeededError
from telethon.errors.rpcerrorlist import (
    PhoneNumberInvalidError, PhoneCodeInvalidError, PhoneCodeExpiredError,
    ApiIdInvalidError
)
import sys

def main():
    try:
        # Prompt user for API ID, API Hash, and phone number
        api_id = input('Enter your Telegram API ID: ').strip()
        api_hash = input('Enter your Telegram API Hash: ').strip()
        phone = input('Enter your phone number (e.g. +123456789): ').strip()

        # Create a Telethon client with an in-memory StringSession
        client = TelegramClient(StringSession(), api_id, api_hash)

        print('Connecting to Telegram...')
        client.connect()

        # If not already authorized, perform the login
        if not client.is_user_authorized():
            try:
                # Send the OTP code to the phone
                client.send_code_request(phone)
                print('OTP code sent to your Telegram app or SMS.')
            except PhoneNumberInvalidError:
                print('Error: The phone number is invalid. Please check the format.')
                sys.exit(1)

            # Prompt user to enter the received code
            code = input('Enter the code you received: ').strip()
            try:
                # Attempt to sign in with the received code
                client.sign_in(phone=phone, code=code)
            except SessionPasswordNeededError:
                # 2FA is enabled: prompt for the password
                pw = input('Two-step verification is enabled. Enter your 2FA password: ')
                client.sign_in(password=pw)
            except PhoneCodeInvalidError:
                print('Error: The code you entered is invalid.')
                sys.exit(1)
            except PhoneCodeExpiredError:
                print('Error: The code has expired. Please rerun the script to get a new code.')
                sys.exit(1)

        # At this point, we should be logged in
        print('Logged in successfully!')

        # Generate the string session (export the authorization key)
        session_string = client.session.save()
        print('StringSession created. (Keep this string secure!)')

        # Send the session string to "Saved Messages" (chat with yourself)
        try:
            client.send_message('me', session_string)
            print('Session string has been sent to your Saved Messages.')
        except Exception as e:
            print(f'Warning: Failed to send session string via Telegram: {e}')

    except ApiIdInvalidError:
        print('Error: The API ID or API Hash is invalid.')
        sys.exit(1)
    except PhoneNumberInvalidError:
        print('Error: The phone number is invalid. Please check the format.')
        sys.exit(1)
    except Exception as e:
        print(f'An unexpected error occurred: {e}')
        sys.exit(1)
    finally:
        # Disconnect the client if it's still connected
        if 'client' in locals() and client.is_connected():
            client.disconnect()

if __name__ == '__main__':
    main()
