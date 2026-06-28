from datetime import datetime


def main() -> None:
    print(datetime.now().astimezone().isoformat(timespec="seconds"))


if __name__ == "__main__":
    main()
