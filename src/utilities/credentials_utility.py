import os


class CredentialsUtility:

    @staticmethod
    def get_wc_api_keys():
        wc_key = os.environ.get("WC_KEY")
        wc_secret = os.environ.get("WC_SECRET")
        print(wc_key, wc_secret)

        if not wc_key or not wc_secret:
            raise Exception("The API credentials 'WC_KEY' and 'WC_SECRET' must be set in env variables.")
        else:
            return {"wc_key": wc_key, "wc_secret": wc_secret}