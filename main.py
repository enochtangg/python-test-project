import sentry_sdk

def main():
    import sys

    # Prints current Python version
    print("Current version of Python is ", sys.version)
    sentry_sdk.init(
        dsn="https://08ac10d6145043dfaf26145be59ab85f@o1317830.ingest.sentry.io/6571063",

        # Set traces_sample_rate to 1.0 to capture 100%
        # of transactions for performance monitoring.
        # We recommend adjusting this value in production.
        traces_sample_rate=1.0
    )
    division_by_zero = 1 / 0

if __name__ == "__main__":
    main()