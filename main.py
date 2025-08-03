import asyncio
from GuardRails.input_guardrail import input_guardrail_func
from GuardRails.output_guardrail import output_guardrail_func

def main():
    print("Hello from open-ai-agents!")
    # asyncio.run(input_guardrail_func())
    # asyncio.run()
    output_guardrail_func()


if __name__ == "__main__":
    main()
