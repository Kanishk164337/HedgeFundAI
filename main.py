from core.pipeline import HedgeFundPipeline


def main():

    symbol = input("Enter Stock Symbol: ")

    pipeline = HedgeFundPipeline()

    result = pipeline.analyze(symbol)

    print("\n")
    print("=" * 80)
    print(result["report"])
    print("=" * 80)


if __name__ == "__main__":
    main()